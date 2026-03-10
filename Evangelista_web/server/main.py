import os
import json
import re
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import AsyncGroq
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from prompts import PROMPT_SCRIBE, PROMPT_STRATEGIST, PROMPT_VOICE

# ==============================================================================
# 1. INFRAESTRUCTURA & CONEXIONES
# ==============================================================================

api_key            = os.getenv("GROQ_API_KEY")
google_creds_json  = os.getenv("GOOGLE_CREDENTIALS")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = AsyncGroq(api_key=api_key) if api_key else None

sheet_db = None
try:
    if google_creds_json:
        creds_dict = json.loads(google_creds_json)
        scope      = ["https://spreadsheets.google.com/feeds",
                      "https://www.googleapis.com/auth/drive"]
        creds      = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client_gs  = gspread.authorize(creds)
        try:
            sheet_db = client_gs.open("DB_Leads_Evangelista").sheet1
            print("--- CONEXIÓN EXITOSA A GOOGLE SHEETS ---")
        except Exception as e:
            print(f"Error hoja: {e}")
except Exception as e:
    print(f"Error Google: {e}")


class ChatRequest(BaseModel):
    message:   str
    history:   list = []
    lead_data: dict = {}


# ==============================================================================
# 2. MOTORES DE INFERENCIA
# Prompts importados desde prompts.py
# ==============================================================================

async def update_lead_memory(current_memory: dict, user_msg: str) -> dict:
    """Agente 1 — Perfilador Forense. Extrae y actualiza el expediente del lead."""
    if not client:
        return current_memory
    try:
        history_str   = json.dumps(current_memory.get("_history_snapshot", []))
        lead_state_str = json.dumps(current_memory)
        system_prompt  = (
            PROMPT_SCRIBE
            .replace("{history}", history_str)
            .replace("{lead_state}", lead_state_str)
        )
        completion = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": f"Mensaje nuevo del prospecto: {user_msg}"}
            ],
            response_format={"type": "json_object"},
            temperature=0.0,
        )
        new_data = json.loads(completion.choices[0].message.content)
        updated  = current_memory.copy()
        for k, v in new_data.items():
            if v is not None:
                updated[k] = v
        return updated
    except Exception as e:
        print(f"Error Scribe: {e}")
        return current_memory


def detect_contact_info(text: str) -> dict:
    """Cazador silencioso: extrae email y teléfono por regex aunque la IA falle."""
    found = {}
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    if email_match:
        found["email_detectado"] = email_match.group(0)
    phone_match = re.search(r'\b\d{10}\b|\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b', text)
    if phone_match:
        found["telefono_detectado"] = phone_match.group(0)
    return found


async def save_to_sheets(memory: dict, manual_tag: str = None) -> None:
    if not sheet_db:
        return
    try:
        contacto = memory.get("contacto", "")
        if isinstance(contacto, dict):
            contacto = str(contacto)
        tag = manual_tag or "CALIFICADO"
        row = [
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            memory.get("empresa", "N/A"),
            f"{memory.get('dolor_declarado', 'N/A')} | {contacto}",
            memory.get("stack_tecnologico", "N/A"),
            "SI" if memory.get("presupuesto_validado") else "NO",
            memory.get("driver_estrategico", "N/A"),
            tag,
            "WEB",
        ]
        sheet_db.append_row(row)
    except Exception as e:
        print(f"Error Sheets: {e}")


async def run_strategist(history: list, user_msg: str, memory: dict) -> dict:
    """Agente 2 — Estratega. Determina la táctica e instrucciones para el Vocero."""
    history_str = json.dumps(history[-6:])          # últimos 6 turnos
    lead_str    = json.dumps(memory)
    system_prompt = (
        PROMPT_STRATEGIST
        .replace("{history}",   history_str)
        .replace("{lead_data}", lead_str)
        .replace("{last_message}", user_msg)
    )
    try:
        comp = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": system_prompt}],
            response_format={"type": "json_object"},
            temperature=0.2,
        )
        return json.loads(comp.choices[0].message.content)
    except Exception as e:
        print(f"Error Strategist: {e}")
        return {
            "tactic": "INVESTIGATE_DEEP",
            "instructions_for_voice": (
                "El sistema tuvo un error interno. Pide disculpas con brevedad "
                "y solicita al prospecto que describa su problema operativo principal."
            ),
        }


async def run_voice(user_msg: str, tactic: str, instructions: str) -> str:
    """Agente 3 — Vocero. Redacta el mensaje final visible para el cliente."""
    system_prompt = (
        PROMPT_VOICE
        .replace("{tactic}",               tactic)
        .replace("{instructions_for_voice}", instructions)
        .replace("{last_message}",          user_msg)
        .replace("{history}",              "")   # historial ya incluido en contexto del sistema
    )
    try:
        comp = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": system_prompt}],
            temperature=0.6,
        )
        return comp.choices[0].message.content
    except Exception:
        return "Un momento, estamos ajustando los servidores de análisis."


# ==============================================================================
# 3. ENDPOINT PRINCIPAL
# ==============================================================================

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    if not client:
        raise HTTPException(status_code=500, detail="GROQ_API_KEY no configurada.")

    memory_backup = dict(request.lead_data) if request.lead_data else {}

    # — NIVEL 0: CAZADOR SILENCIOSO —
    # Captura email/teléfono por regex ANTES de cualquier llamada a la IA.
    emergency_contact = detect_contact_info(request.message)
    if emergency_contact:
        print(f"CONTACTO DE EMERGENCIA DETECTADO: {emergency_contact}")
        memory_backup.setdefault("contacto", "")
        memory_backup["contacto"] += f" {emergency_contact}"
        await save_to_sheets(memory_backup, manual_tag="CONTACTO_RESCATADO")

    try:
        # 1. PERFILADO — actualiza el expediente del lead
        new_memory = await update_lead_memory(request.lead_data, request.message)

        # 2. ESTRATEGIA — decide la táctica
        estrategia = await run_strategist(request.history, request.message, new_memory)

        # Hard Lock: no desbloquear agenda si el presupuesto no está validado
        if estrategia.get("tactic") == "ALLOW_MEETING":
            if not new_memory.get("presupuesto_validado"):
                estrategia["tactic"] = "ANCHOR_FOUNDATION_FEE"
                estrategia["instructions_for_voice"] = (
                    "El cliente quiere agendar pero NO ha validado $35,000 MXN. "
                    "Ancla el precio del Foundation y haz la pregunta de cierre."
                )

        # 3. AUDITORÍA SILENCIOSA
        silent_audit = {"action": "CONTINUE"}
        if estrategia.get("tactic") == "ALLOW_MEETING":
            silent_audit = {"action": "UNLOCK_CALENDLY"}
            await save_to_sheets(new_memory)

        # 4. VOZ — genera la respuesta final
        respuesta = await run_voice(
            user_msg=request.message,
            tactic=estrategia.get("tactic", "INVESTIGATE_DEEP"),
            instructions=estrategia.get("instructions_for_voice", ""),
        )

        return {
            "response":          respuesta,
            "silent_audit":      silent_audit,
            "updated_lead_data": new_memory,
        }

    except Exception as e:
        print(f"ERROR CRÍTICO: {e}")
        # Protocolo de blindaje: guardar lo que hay y pedir datos de contacto
        try:
            if sheet_db:
                sheet_db.append_row([
                    datetime.now().strftime("%Y-%m-%d %H:%M"),
                    memory_backup.get("empresa", "Error"),
                    f"FALLO SISTEMA | Msg: {request.message}",
                    "N/A", "NO", "CRITICAL", "ERROR", "WEB",
                ])
        except Exception:
            pass

        return {
            "response": (
                "Interrupción técnica momentánea. Para no perder el avance de su "
                "diagnóstico, escriba su correo electrónico y número de teléfono ahora. "
                "Un Socio Senior lo contactará en los próximos 10 minutos."
            ),
            "silent_audit":      {"action": "CONTINUE"},
            "updated_lead_data": memory_backup,
        }
