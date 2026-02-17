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

api_key = os.getenv("GROQ_API_KEY")

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
    print("CRITICAL: GROQ_API_KEY not found.")
else:
    client = AsyncGroq(api_key=api_key)

class ChatRequest(BaseModel):
    message: str
    history: list = [] 

# ==============================================================================
# 2. CEREBRO CORPORATIVO (KNOWLEDGE BASE)
# ==============================================================================

CONTEXTO_SERVICIOS = """
NUESTROS 3 PILARES DE SERVICIO:
1. **Foundation (Auditoría & Saneamiento):**
   - *Qué es:* Diagnóstico forense de datos. Limpieza de "Basura IN/Basura OUT".
   - *Base:* Normalización de bases de datos y corrección de flujos operativos humanos.
   
2. **Architecture (Ingeniería de Datos):**
   - *Qué es:* Construcción de la tubería digital. Conexión de fuentes (ERPs, Excel, SQL).
   - *Base:* Modelado de datos (Estrella/Copo de Nieve) y ETLs automatizados.

3. **Intelligence (Visualización & Decisión):**
   - *Qué es:* Tableros de Power BI vivos para toma de decisiones.
   - *Base:* KPIs financieros, operativos y proyecciones de rentabilidad.

PREGUNTAS FRECUENTES (FAQ) - RESPUESTAS APROBADAS:
- *Tiempo:* "Los sprints iniciales duran de 4 a 6 semanas."
- *Entregables:* "Acceso a repositorio de datos propio y tableros en Power BI Service."
- *Stack:* "Python, SQL, Power BI y ecosistema Azure/Fabric."
- *Know-How:* NUNCA expliques CÓMO se hace el código, solo QUÉ logra (Rentabilidad, Orden, Claridad).
"""

# ==============================================================================
# 3. AGENTES (PROMPTS DE NEGOCIO)
# ==============================================================================

# --- AGENTE 1: EL ESTRATEGA (Director Comercial) ---
PROMPT_STRATEGIST = f"""
### ROL: DIRECTOR DE ESTRATEGIA
Tu objetivo es CLASIFICAR la intención del cliente y decidir el siguiente paso.

{CONTEXTO_SERVICIOS}

### REGLA DE ORO: EL FILTRO (VETTING FIRST)
NUNCA mandes a agendar cita de inmediato.
Si el usuario pide cita o precio, PRIMERO debes validar su situación.
La IA debe explicar brevemente que es necesario conocerse para ver si aplica.

### LÓGICA DE RESPUESTA
1. **Duda de Servicio:** Si pregunta "¿Qué hacen?", explica los pilares brevemente.
2. **Intención de Compra:** Si pide "Precio" o "Cita" -> TACTIC: 'QUALIFY_FIRST'.
3. **Estudiante/Curioso:** Si no tiene empresa o busca tarea -> TACTIC: 'REJECT'.

### SALIDA JSON:
{{
  "tactic": "EXPLAIN_SERVICES" | "QUALIFY_FIRST" | "REJECT" | "ANSWER_DOUBT",
  "reasoning": "Por qué elegiste esto",
  "instructions_for_voice": "Instrucciones precisas para el redactor."
}}
"""

# --- AGENTE 2: EL VOCERO (La Voz de la Firma) ---
PROMPT_VOICE = """
### ROL: SOCIO SENIOR DE EVANGELISTA & CO.
Eres la cara de la firma. Tu tono es Exclusivo, Directo y Estratégico.

### RESTRICCIONES CRÍTICAS
1. **MÁXIMO 30 PALABRAS para explicar el proceso de selección.**
   - Ejemplo: "En Evangelista & Co. no aceptamos todos los proyectos. Requerimos conocer su infraestructura actual para validar si nuestra metodología aplica a su caso."
2. **NO VENDAS:** Tú no necesitas el dinero, ellos necesitan el orden.
3. **PRECIO:** Si te ordenan dar precio, usa el anclaje: "Proyectos Foundation desde $35,000 MXN, ajustables según entropía."

### INPUT
Recibirás instrucciones estratégicas y el contexto de servicios si es necesario.
Responde al usuario final.
"""

# --- AGENTE 3: EL AUDITOR (Juez de Calendly) ---
PROMPT_AUDITOR = """
ERES: El Algoritmo de Vetting.
OBJETIVO: Decidir si mostramos el botón de Calendly.

CRITERIOS PARA 'UNLOCK_CALENDLY':
1. El usuario YA explicó su problema (Dolor de negocio).
2. El usuario aceptó implícitamente que necesita ayuda profesional.
3. NO desbloquear en el primer mensaje. Debe haber un intercambio previo.

SALIDA JSON:
{
  "action": "UNLOCK_CALENDLY" | "CONTINUE"
}
"""

# ==============================================================================
# 4. MOTORES DE INFERENCIA
# ==============================================================================

async def run_strategist(history, user_msg):
    if not client: return {"tactic": "QUALIFY_FIRST", "instructions_for_voice": "Error de conexión."}
    
    messages = [{"role": "system", "content": PROMPT_STRATEGIST}]
    for m in history[-3:]: 
        role = "user" if m.get('role') == "user" else "assistant"
        content = m.get('parts', [""])[0]
        messages.append({"role": role, "content": content})
    messages.append({"role": "user", "content": user_msg})

    try:
        completion = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.1,
            response_format={"type": "json_object"},
            max_tokens=300
        )
        return json.loads(completion.choices[0].message.content)
    except:
        return {"instructions_for_voice": "Responde con cortesía profesional."}

async def run_voice(user_msg, strategy_json):
    if not client: return "Sistemas en mantenimiento."

    input_prompt = f"""
    CONTEXTO DEL USUARIO: "{user_msg}"
    INSTRUCCIÓN DEL ESTRATEGA: {strategy_json.get('instructions_for_voice')}
    
    Recuerda: Si es momento de filtrar, usa MÁXIMO 30 palabras para explicar que debemos evaluarlos primero.
    """

    try:
        completion = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": PROMPT_VOICE},
                {"role": "user", "content": input_prompt}
            ],
            temperature=0.6,
            max_tokens=400
        )
        return completion.choices[0].message.content
    except:
        return "Disculpe, estamos recalculando proyecciones. Intente de nuevo."

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
# 5. ENDPOINT
# ==============================================================================

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    if not client: raise HTTPException(status_code=500, detail="API Key Missing")
    try:
        # 1. Estrategia
        estrategia = await run_strategist(request.history, request.message)
        # 2. Voz
        respuesta = await run_voice(request.message, estrategia)
        # 3. Auditoría
        auditoria = await run_auditor(request.message, respuesta)

        return {
            "response": respuesta,
            "silent_audit": auditoria
        }
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
