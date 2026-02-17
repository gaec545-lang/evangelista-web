import os
import json
import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import AsyncGroq
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# ==============================================================================
# 1. CONFIGURACIÓN
# ==============================================================================

# Cargar credenciales desde Railway
api_key = os.getenv("GROQ_API_KEY")
google_creds_json = os.getenv("GOOGLE_CREDENTIALS")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conexión Groq
if not api_key:
    client = None
    print("CRITICAL: GROQ_API_KEY not found.")
else:
    client = AsyncGroq(api_key=api_key)

# Conexión Google Sheets
sheet_db = None
try:
    if google_creds_json:
        creds_dict = json.loads(google_creds_json)
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client_gs = gspread.authorize(creds)
        # Intentamos conectar
        try:
            sheet_db = client_gs.open("DB_Leads_Evangelista").sheet1
            print("--- CONEXIÓN EXITOSA A GOOGLE SHEETS ---")
        except Exception as e:
            print(f"Error abriendo la hoja (Verifica el nombre exacto): {e}")
    else:
        print("ADVERTENCIA: No hay credenciales de Google configuradas.")
except Exception as e:
    print(f"Error general Google: {e}")

class ChatRequest(BaseModel):
    message: str
    history: list = []
    lead_data: dict = {} # La memoria viaja aquí

# ==============================================================================
# 2. PROMPTS DE NEGOCIO
# ==============================================================================

CONTEXTO_SERVICIOS = """
SERVICIOS:
1. Foundation (Limpieza de datos).
2. Architecture (Ingeniería/ETL).
3. Intelligence (Power BI).
"""

PROMPT_SCRIBE = """
ERES: Analista de datos silencioso.
OBJETIVO: Extraer datos clave del mensaje actual del usuario.

CAMPOS A EXTRAER (Si no se menciona, usa null):
- empresa: Nombre de la organización.
- dolor: Problema operativo (ej: inventarios, excel lento).
- stack: Herramientas (SAP, Excel, Oracle).
- presupuesto_validado: Boolean (true si aceptó el rango de $35k+).
- urgencia: (Baja/Media/Alta).

SALIDA JSON ÚNICA:
{
  "empresa": "...",
  "dolor": "...",
  "stack": "...",
  "presupuesto_validado": true/false/null,
  "urgencia": "..."
}
"""

PROMPT_STRATEGIST = f"""
### ROL: DIRECTOR DE ESTRATEGIA
Tu objetivo es CLASIFICAR al cliente y validar si merece una reunión.

### MEMORIA DEL LEAD:
{{LEAD_MEMORY}}

{CONTEXTO_SERVICIOS}

### REGLAS DE VETTING:
1. Si falta 'empresa' -> Pregunta nombre y giro.
2. Si falta 'dolor' -> Pregunta qué proceso quieren optimizar.
3. Si preguntan precio -> Dales el anclaje ($35k+) y espera validación.
4. SOLO SI tenemos Empresa + Dolor + Presupuesto Validado -> Permite agendar.

### SALIDA JSON:
{{
  "tactic": "INVESTIGATE" | "ANCHOR_PRICE" | "ALLOW_MEETING" | "REJECT",
  "instructions": "Instrucciones para el redactor."
}}
"""

PROMPT_VOICE = """
ERES: Socio Senior de Evangelista & Co.
TONO: Exclusivo, breve, directo. Max 40 palabras.
OBJETIVO: Ejecutar la instrucción estratégica.
"""

# ==============================================================================
# 3. LÓGICA
# ==============================================================================

async def update_lead_memory(current_memory, user_msg):
    """Actualiza la ficha con IA"""
    if not client: return current_memory
    try:
        completion = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": PROMPT_SCRIBE},
                {"role": "user", "content": user_msg}
            ],
            response_format={"type": "json_object"},
            temperature=0
        )
        new_data = json.loads(completion.choices[0].message.content)
        # Actualizamos solo lo nuevo
        updated = current_memory.copy()
        for k, v in new_data.items():
            if v: updated[k] = v
        return updated
    except:
        return current_memory

async def save_to_sheets(memory):
    """Escribe en Google Sheets"""
    if not sheet_db: return
    try:
        row = [
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            memory.get("empresa", "N/A"),
            memory.get("dolor", "N/A"),
            memory.get("stack", "N/A"),
            "SI" if memory.get("presupuesto_validado") else "NO",
            memory.get("urgencia", "N/A"),
            "8.5", 
            "Lead Web"
        ]
        sheet_db.append_row(row)
        print("Lead guardado en Google Sheets")
    except Exception as e:
        print(f"Error escribiendo en Sheets: {e}")

async def run_strategist(history, user_msg, memory):
    prompt = PROMPT_STRATEGIST.replace("{LEAD_MEMORY}", json.dumps(memory))
    msgs = [{"role": "system", "content": prompt}]
    # Contexto breve
    for m in history[-2:]:
        role = "user" if m.get('role') == "user" else "assistant"
        content = m.get('parts', [""])[0]
        msgs.append({"role": role, "content": content})
    msgs.append({"role": "user", "content": user_msg})

    try:
        comp = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=msgs,
            response_format={"type": "json_object"},
            temperature=0.1
        )
        return json.loads(comp.choices[0].message.content)
    except:
        return {"tactic": "INVESTIGATE", "instructions": "Responde cordialmente."}

async def run_voice(user_msg, instructions):
    try:
        comp = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": PROMPT_VOICE},
                {"role": "user", "content": f"User: {user_msg}\nInstrucción: {instructions}"}
            ]
        )
        return comp.choices[0].message.content
    except:
        return "Un momento, validando servidor."

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    if not client: raise HTTPException(status_code=500, detail="API Key Missing")
    try:
        # 1. Actualizar Memoria
        new_memory = await update_lead_memory(request.lead_data, request.message)
        
        # 2. Estrategia
        estrategia = await run_strategist(request.history, request.message, new_memory)
        
        # 3. Guardar si aplica
        silent_audit = {"action": "CONTINUE"}
        if estrategia.get("tactic") == "ALLOW_MEETING":
            silent_audit = {"action": "UNLOCK_CALENDLY"}
            await save_to_sheets(new_memory)

        # 4. Respuesta Voz
        respuesta = await run_voice(request.message, estrategia.get("instructions"))

        return {
            "response": respuesta,
            "silent_audit": silent_audit,
            "updated_lead_data": new_memory # Devolvemos la memoria al frontend
        }
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
