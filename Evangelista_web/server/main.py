import os
import json
import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import AsyncGroq
from dotenv import load_dotenv

# 1. INFRAESTRUCTURA
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware # <--- ASEGÚRATE DE IMPORTAR ESTO ARRIBA

app = FastAPI() # <--- ESTA LÍNEA YA DEBERÍA EXISTIR

# --- INICIO DEL PASE VIP (COPIA DESDE AQUÍ) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # El asterisco permite que CUALQUIER sitio entre. 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --- FIN DEL PASE VIP ---

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

class ChatRequest(BaseModel):
    message: str
    history: list

# ==============================================================================
# 2. ARQUITECTURA TRIPARTITA (MODO "APROXIMACIÓN")
# ==============================================================================

# ------------------------------------------------------------------------------
# AGENTE 1: EL ESTRATEGA (CEREBRO DE NEGOCIOS)
# ------------------------------------------------------------------------------
PROMPT_STRATEGIST = """
### ROL: DIRECTOR DE ESTRATEGIA Y PRICING
Tu objetivo es filtrar leads y vender la REUNIÓN, no el servicio final.

### POLÍTICA DE PRECIOS (STRICT MODE)
1.  **PROHIBIDO COTIZAR FINAL:** Nunca des un precio cerrado (ej: "Son $42,000"). No has visto sus datos, sería irresponsable.
2.  **PRECIO PISO (ANCHOR):** Usa siempre la frase "Inversión base desde $35,000 MXN". Esto sirve solo para filtrar a quienes no tienen presupuesto.
3.  **FACTOR DE INCERTIDUMBRE:** Si detectas caos (Excel, manualidad), advierte que el precio final se ajustará, pero NO digas cuánto.

### LÓGICA DE RESPUESTA
1.  **Perfilado:** ¿Es Estudiante? -> REJECT. ¿Es Empresa? -> PROCEED.
2.  **Manejo de Costos:**
    * Si preguntan "¿Cuánto cuesta?": Da el Rango Base ($35k+) y explica que la cotización final requiere ver la complejidad de sus datos en la sesión.
    * Si piden "Architecture": Explica que Foundation es el prerrequisito para poder cotizar Architecture.

### FORMATO JSON
{
  "tactic": "REJECT" | "ANCHOR_PRICE" | "PIVOT_TO_MEETING",
  "reasoning": "Cliente pide precio. Damos el piso para filtrar.",
  "key_talking_points": "Desde $35k. Ajuste por entropía. Necesitamos sesión para cerrar número.",
  "instructions_for_voice": "Di que arrancamos en 35k, pero que el ajuste final depende de qué tan 'sucios' estén sus datos. Vende la sesión."
}
"""

# ------------------------------------------------------------------------------
# AGENTE 2: EL VOCERO (SOCIO SENIOR)
# ------------------------------------------------------------------------------
PROMPT_VOICE = """
### ROL: SOCIO SENIOR (FRONTMAN)
Tu trabajo es manejar la ansiedad del cliente por el precio con elegancia.

### TONO Y ESTILO
* **Profesionalismo Médico:** Un cirujano no cobra sin ver al paciente. Tú tampoco.
* **Frase Clave:** "En consultoría de alto nivel, dar un precio sin diagnóstico es negligencia."
* **Manejo del Precio:** "Nuestros protocolos Foundation inician en los **$35,000 MXN**. Sin embargo, la inversión final depende de la entropía (desorden) de sus datos actuales. Eso lo determinamos con precisión en la sesión, no por chat."

3.  **CIERRE DE VENTA:**
    Si el Estratega indica "PIVOT_TO_MEETING" o "ANCHOR_PRICE", tu frase final debe ser:
    "He autorizado el acceso a mi agenda privada para una valoración preliminar. Encontrará el enlace exclusivo a continuación."
    (NO pongas el link http en el texto, el sistema lo pondrá visualmente).

    
### INPUT
- Instrucciones del Estratega.
- Mensaje del Usuario.
"""

# ------------------------------------------------------------------------------
# AGENTE 3: EL AUDITOR (VETTING GATE)
# ------------------------------------------------------------------------------
PROMPT_AUDITOR = """
ERES: El Algoritmo de Vetting.
OBJETIVO: Desbloquear Calendly si el lead acepta el Rango de Precio.

CRITERIOS UNLOCK:
1.  **Filtro Económico:** El usuario leyó "Desde $35,000" y siguió interesado (preguntó fechas, dijo ok, etc.).
2.  **Fit:** Tiene un problema real.

SALIDA JSON:
{
  "action": "UNLOCK_CALENDLY" | "CONTINUE",
  "score": 0.0-1.0
}
"""

# ==============================================================================
# 3. MOTORES DE INFERENCIA
# ==============================================================================

async def run_strategist(history, user_msg):
    if not client: return None
    
    # Contexto limitado para rapidez
    messages = [{"role": "system", "content": PROMPT_STRATEGIST}]
    for m in history[-4:]: 
        role = "user" if m['role'] == "user" else "assistant"
        messages.append({"role": role, "content": m['parts'][0]})
    messages.append({"role": "user", "content": user_msg})

    try:
        completion = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0,
            response_format={"type": "json_object"},
            max_tokens=500
        )
        return json.loads(completion.choices[0].message.content)
    except Exception as e:
        print(f"Error Estratega: {e}")
        return {
            "tactic": "ANCHOR_PRICE",
            "reasoning": "Fallback",
            "key_talking_points": "Precio base 35k",
            "instructions_for_voice": "Da el precio base y pide reunión."
        }

async def run_voice(user_msg, strategy_json):
    if not client: return "Error de conexión."

    input_prompt = f"""
    MENSAJE USUARIO: "{user_msg}"
    ESTRATEGIA: {strategy_json}
    
    Redacta la respuesta final con elegancia y sobriedad.
    """

    completion = await client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": PROMPT_VOICE},
            {"role": "user", "content": input_prompt}
        ],
        temperature=0.5,
        max_tokens=400
    )
    return completion.choices[0].message.content

async def run_auditor(user_msg, bot_msg):
    if not client: return {"action": "CONTINUE"}

    audit_input = f"User: {user_msg}\nBot: {bot_msg}"

    try:
        completion = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": PROMPT_AUDITOR},
                {"role": "user", "content": audit_input}
            ],
            temperature=0,
            response_format={"type": "json_object"}
        )
        return json.loads(completion.choices[0].message.content)
    except:
        return {"action": "CONTINUE"}

# ==============================================================================
# 4. ENDPOINT
# ==============================================================================

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        # Paso 1: Estrategia
        estrategia = await run_strategist(request.history, request.message)
        
        # Paso 2: Voz
        respuesta = await run_voice(request.message, estrategia)
        
        # Paso 3: Auditoría
        auditoria = await run_auditor(request.message, respuesta)

        return {
            "response": respuesta,
            "silent_audit": auditoria
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            "response": "Estamos ajustando los algoritmos de cotización. Un momento.",
            "silent_audit": {"action": "CONTINUE"}
        }
