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

if not api_key:
    client = None
else:
    client = AsyncGroq(api_key=api_key)

sheet_db = None
try:
    if google_creds_json:
        creds_dict = json.loads(google_creds_json)
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client_gs = gspread.authorize(creds)
        try:
            sheet_db = client_gs.open("DB_Leads_Evangelista").sheet1
            print("--- CONEXIÓN EXITOSA A GOOGLE SHEETS ---")
        except Exception as e:
            print(f"Error hoja: {e}")
except Exception as e:
    print(f"Error Google: {e}")

class ChatRequest(BaseModel):
    message: str
    history: list = []
    lead_data: dict = {}

# ==============================================================================
# 2. PROMPTS DE NEGOCIO (AJUSTADOS - VERSION SOCIO SENIOR)
# ==============================================================================

CONTEXTO_SERVICIOS = """
SERVICIOS:
1. Foundation (Limpieza y saneamiento de datos).
2. Architecture (Ingeniería y conexión de fuentes).
3. Intelligence (Dashboards y KPIs financieros).
"""

PROMPT_SCRIBE = """
ERES: Analista de datos.
OBJETIVO: Extraer datos y detectar validación de precio.

CAMPOS:
- empresa: Nombre.
- dolor: Problema.
- stack: Herramientas.
- presupuesto_validado: BOOLEAN STRICT. Solo es 'true' si el usuario acepta explícitamente el rango "DESDE $35k". Si solo pregunta precio, es null.
- urgencia: Baja/Media/Alta.

SALIDA JSON:
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
Tu objetivo es CLASIFICAR al cliente. No eres un vendedor desesperado, eres un consultor selectivo.

### MEMORIA:
{{LEAD_MEMORY}}

{CONTEXTO_SERVICIOS}

### REGLAS DE ORO (PRECIOS):
1. **PROHIBIDO PRECIO FIJO:** NUNCA permitas que el redactor diga "Cuesta $35,000".
2. **FRASE OBLIGATORIA:** La instrucción de precio SIEMPRE debe ser: "Menciona que la inversión base inicia en los $35,000 MXN, pero escala según la entropía (caos) de sus datos".

### LÓGICA DE TURNOS:
1. Si el usuario saluda -> Pide contexto del problema (No digas "investigaré", di "Para saber si podemos ayudarle...").
2. Si cuenta su dolor -> Explica brevemente la solución y espera a que ÉL pregunte el precio o muestre interés de compra.
3. Si pregunta precio -> Aplica la Regla de Oro (Anclaje DESDE $35k).
4. SOLO SI (Empresa + Dolor + Presupuesto Validado) -> TACTIC: "ALLOW_MEETING".

### SALIDA JSON:
{{
  "tactic": "INVESTIGATE" | "ANCHOR_PRICE" | "ALLOW_MEETING" | "REJECT",
  "instructions": "Instrucciones precisas para el redactor sobre QUÉ decir (no cómo)."
}}
"""

PROMPT_VOICE = """
ERES: Socio Senior de Evangelista & Co.
TONO: Profesional, Empático pero con Autoridad, Conciso (Max 45 palabras).

### DICCIONARIO PROHIBIDO (NUNCA DIGAS):
- "Cuesta $35,000" (Di: "La inversión base es de...")
- "Investigaré" (Suena a robot)
- "Hola Carlos" (Si ya saludaste, ve al grano)
- "Agendo reunión" (Di: "He habilitado un espacio en la agenda...")

### EJEMPLOS DE RESPUESTA:
- *Si pregunta precio:* "Nuestros protocolos Foundation inician en los **$35,000 MXN**. El alcance final depende de la complejidad de su infraestructura actual."
- *Si acepta el precio:* "Excelente. Dado que estamos alineados en la inversión y la urgencia, procedamos a definir la ruta crítica."

OBJETIVO: Redactar la respuesta final al usuario siguiendo las instrucciones del Estratega.
"""

# ==============================================================================
# 3. LÓGICA
# ==============================================================================

async def update_lead_memory(current_memory, user_msg):
    if not client: return current_memory
    try:
        completion = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": PROMPT_SCRIBE},
                {"role": "user", "content": f"Memoria previa: {current_memory}\nMensaje actual: {user_msg}"}
            ],
            response_format={"type": "json_object"},
            temperature=0
        )
        new_data = json.loads(completion.choices[0].message.content)
        updated = current_memory.copy()
        for k, v in new_data.items():
            if v is not None: updated[k] = v
        return updated
    except:
        return current_memory

async def save_to_sheets(memory):
    if not sheet_db: return
    try:
        row = [
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            memory.get("empresa", "N/A"),
            memory.get("dolor", "N/A"),
            memory.get("stack", "N/A"),
            "SI" if memory.get("presupuesto_validado") else "NO",
            memory.get("urgencia", "N/A"),
            "9.0", 
            "Lead Calificado"
        ]
        sheet_db.append_row(row)
    except Exception as e:
        print(f"Error Sheets: {e}")

async def run_strategist(history, user_msg, memory):
    prompt = PROMPT_STRATEGIST.replace("{LEAD_MEMORY}", json.dumps(memory))
    msgs = [{"role": "system", "content": prompt}]
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
            temperature=0
        )
        return json.loads(comp.choices[0].message.content)
    except:
        return {"tactic": "INVESTIGATE", "instructions": "Continua."}

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
        return "Un momento."

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    if not client: raise HTTPException(status_code=500, detail="API Key Missing")
    try:
        # 1. Memoria
        new_memory = await update_lead_memory(request.lead_data, request.message)
        
        # 2. Estrategia
        estrategia = await run_strategist(request.history, request.message, new_memory)
        
        # --- CANDADO DE SEGURIDAD (HARD LOCK) ---
        # Si la IA quiere agendar pero no hay validación explícita de dinero, LA BLOQUEAMOS.
        if estrategia.get("tactic") == "ALLOW_MEETING":
            if not new_memory.get("presupuesto_validado"):
                print("⚠️ VETO: Bloqueando cita por falta de validación financiera.")
                estrategia["tactic"] = "ANCHOR_PRICE"
                estrategia["instructions"] = "El cliente quiere avanzar pero NO ha aceptado explícitamente el precio base de $35,000 MXN. Dales el precio y pide confirmación antes de agendar."

        # 3. Ejecución
        silent_audit = {"action": "CONTINUE"}
        
        # Solo guardamos y mostramos botón si pasó el candado
        if estrategia.get("tactic") == "ALLOW_MEETING":
            silent_audit = {"action": "UNLOCK_CALENDLY"}
            # Verificar si ya guardamos este lead para no duplicar (opcional simple)
            await save_to_sheets(new_memory)

        # 4. Voz
        respuesta = await run_voice(request.message, estrategia.get("instructions"))

        return {
            "response": respuesta,
            "silent_audit": silent_audit,
            "updated_lead_data": new_memory
        }
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
