import os
import json
import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import AsyncGroq
# Intentamos cargar dotenv solo si estamos en local
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# ==============================================================================
# 1. INFRAESTRUCTURA & SEGURIDAD
# ==============================================================================

# Recuperar la llave del entorno (Railway)
api_key = os.getenv("GROQ_API_KEY")

app = FastAPI()

# Configuración de CORS (El pase VIP para que tu web entre)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cliente Asíncrono (Más rápido para múltiples usuarios)
if not api_key:
    client = None
    print("CRITICAL: GROQ_API_KEY not found.")
else:
    client = AsyncGroq(api_key=api_key)

# Modelo de datos que recibe desde el Javascript
class ChatRequest(BaseModel):
    message: str
    history: list = [] # Historial de la conversación

# ==============================================================================
# 2. LOS CEREBROS (PROMPTS DE NEGOCIO)
# ==============================================================================

# --- AGENTE 1: EL ESTRATEGA (Piensa, no habla) ---
PROMPT_STRATEGIST = """
### ROL: DIRECTOR DE ESTRATEGIA Y PRICING
Tu objetivo es filtrar leads y vender la REUNIÓN, no el servicio final.

### POLÍTICA DE PRECIOS (STRICT MODE)
1.  **PROHIBIDO COTIZAR FINAL:** Nunca des un precio cerrado (ej: "Son $42,000"). No has visto sus datos, sería irresponsable.
2.  **PRECIO PISO (ANCHOR):** Usa siempre la frase "Inversión base desde $35,000 MXN". Esto sirve solo para filtrar a quienes no tienen presupuesto.
3.  **FACTOR DE INCERTIDUMBRE:** Si detectas caos (Excel, manualidad), advierte que el precio final se ajustará, pero NO digas cuánto.

### LÓGICA DE RESPUESTA
1.  **Perfilado:** ¿Es Estudiante? -> REJECT (Sé cortés pero firme). ¿Es Empresa? -> PROCEED.
2.  **Manejo de Costos:**
    * Si preguntan "¿Cuánto cuesta?": Da el Rango Base ($35k+) y explica que la cotización final requiere ver la complejidad de sus datos en la sesión.
    * Si piden "Architecture": Explica que Foundation es el prerrequisito para poder cotizar Architecture.

### FORMATO JSON OBLIGATORIO
Debes responder SOLO un JSON con esta estructura:
{
  "tactic": "REJECT" | "ANCHOR_PRICE" | "PIVOT_TO_MEETING",
  "reasoning": "Breve explicación de por qué elegiste esto.",
  "instructions_for_voice": "Instrucciones precisas para el agente que redactará la respuesta."
}
"""

# --- AGENTE 2: EL VOCERO (Habla con el cliente) ---
PROMPT_VOICE = """
### ROL: SOCIO SENIOR (FRONTMAN) DE EVANGELISTA & CO.
Tu trabajo es responder al cliente basándote estrictamente en la ESTRATEGIA que se te dará.

### TONO Y ESTILO
* **Autoridad Serena:** No usas signos de exclamación excesivos. Eres breve.
* **Profesionalismo Médico:** Un cirujano no cobra sin ver al paciente. Tú tampoco.
* **Frase Clave de Precio (Si se requiere):** "Nuestros protocolos Foundation inician en los **$35,000 MXN**. Sin embargo, la inversión final depende de la entropía (desorden) de sus datos actuales."

### INPUT
Recibirás:
1. Mensaje del Cliente.
2. Instrucción Estratégica (Síguela al pie de la letra).

Tu respuesta debe ser texto plano, listo para enviarse al chat.
"""

# --- AGENTE 3: EL AUDITOR (Decide si abre Calendly) ---
PROMPT_AUDITOR = """
ERES: El Algoritmo de Vetting (Juez Silencioso).
OBJETIVO: Analizar la conversación y decidir si el cliente merece acceso a la agenda del Director.

CRITERIOS PARA 'UNLOCK_CALENDLY':
1.  **Aceptación Económica:** El usuario ya recibió el precio base ($35k) y sigue interesado o pregunta por fechas.
2.  **Dolor Real:** El usuario expresó un problema de negocio real (inventarios, caos, pérdidas).
3.  **No es Estudiante:** Si parece tarea escolar, bloquea.

SALIDA JSON OBLIGATORIA:
{
  "action": "UNLOCK_CALENDLY" | "CONTINUE",
  "reason": "Explicación breve"
}
"""

# ==============================================================================
# 3. MOTORES DE INFERENCIA (Funciones)
# ==============================================================================

async def run_strategist(history, user_msg):
    if not client: return {"tactic": "PIVOT_TO_MEETING", "instructions_for_voice": "Responde genérico por error de sistema."}
    
    # Preparamos los mensajes para el modelo
    messages = [{"role": "system", "content": PROMPT_STRATEGIST}]
    
    # Añadimos contexto (últimos 3 mensajes para no gastar tantos tokens)
    for m in history[-3:]: 
        role = "user" if m.get('role') == "user" else "assistant"
        content = m.get('parts', [""])[0]
        messages.append({"role": role, "content": content})
    
    messages.append({"role": "user", "content": user_msg})

    try:
        completion = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.1, # Muy frío y calculador
            response_format={"type": "json_object"},
            max_tokens=300
        )
        return json.loads(completion.choices[0].message.content)
    except Exception as e:
        print(f"Error Estratega: {e}")
        return {
            "instructions_for_voice": "El cliente pregunta algo. Responde con profesionalismo invitando a una sesión de diagnóstico."
        }

async def run_voice(user_msg, strategy_json):
    if not client: return "Error: Sistema de IA desconectado."

    input_prompt = f"""
    MENSAJE DEL CLIENTE: "{user_msg}"
    
    INSTRUCCIÓN ESTRATÉGICA: {strategy_json.get('instructions_for_voice')}
    
    Redacta la respuesta final:
    """

    try:
        completion = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": PROMPT_VOICE},
                {"role": "user", "content": input_prompt}
            ],
            temperature=0.6, # Un poco más creativo para hablar
            max_tokens=400
        )
        return completion.choices[0].message.content
    except Exception as e:
        return "Disculpe, estamos experimentando alta demanda en nuestros servidores neuronales."

async def run_auditor(user_msg, bot_msg):
    if not client: return {"action": "CONTINUE"}

    audit_input = f"User: {user_msg}\nBot (Tu respuesta): {bot_msg}"

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
# 4. ENDPOINT PRINCIPAL
# ==============================================================================

@app.get("/")
def read_root():
    return {"status": "Sistema Neural Evangelista & Co. [ONLINE]"}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    if not client:
        raise HTTPException(status_code=500, detail="API Key no configurada")
    
    try:
        # PASO 1: El Estratega piensa qué hacer
        print("--- 1. Estratega pensando... ---")
        estrategia = await run_strategist(request.history, request.message)
        print(f"Estrategia decidida: {estrategia.get('tactic')}")
        
        # PASO 2: El Vocero redacta el mensaje
        print("--- 2. Vocero redactando... ---")
        respuesta_texto = await run_voice(request.message, estrategia)
        
        # PASO 3: El Auditor verifica si desbloquea Calendly
        print("--- 3. Auditor evaluando... ---")
        auditoria = await run_auditor(request.message, respuesta_texto)
        print(f"Decisión Auditor: {auditoria.get('action')}")

        return {
            "response": respuesta_texto,
            "silent_audit": auditoria # Esto le dice al JS si muestra el botón de Calendly
        }

    except Exception as e:
        print(f"Error Crítico: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
