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
# 1. INFRAESTRUCTURA & CONEXIONES
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
# 2. MEGA-PROMPTS (ARQUITECTURA DE ALTA DENSIDAD COGNITIVA)
# ==============================================================================

# --- AGENTE 1: EL PERFILADOR (PSICÓLOGO DE DATOS) ---
PROMPT_SCRIBE = """
### ROL: PERFILADOR DE INTELIGENCIA DE NEGOCIOS Y PSICOLOGÍA DEL CLIENTE
No eres un simple extractor de datos. Eres un analista de inteligencia encargado de construir un "Expediente Forense" del usuario en tiempo real. Tu misión es leer entre líneas, detectar inconsistencias, evaluar la madurez técnica y extraer datos duros para la base de datos de Evangelista & Co.

### OBJETIVOS CRÍTICOS DE ANÁLISIS:
1.  **Detección de Identidad Corporativa:** Busca nombres de empresas, giros comerciales o cargos directivos.
2.  **Diagnóstico de Patología Operativa (El Dolor):** Identifica qué proceso está roto. ¿Es un dolor financiero (pierden dinero), operativo (pierden tiempo) o ceguera (no tienen datos)?
3.  **Evaluación de Infraestructura (Stack):** ¿En qué etapa tecnológica están? (Papel y lápiz -> Excel Caótico -> ERPs rígidos -> Nube desordenada).
4.  **Termómetro de Madurez Técnica (El Filtro Docente):**
    * *NIVEL BAJO:* El usuario usa términos vagos ("desastre", "lento", "mucho papeleo"), se confunde con terminología técnica, o pide explicaciones básicas.
    * *NIVEL ALTO:* El usuario usa siglas (KPI, SQL, API, ETL, EBITDA), pregunta por integraciones específicas o metodologías.
5.  **Validación Financiera (El Compromiso):** Detecta si el usuario ha aceptado explícitamente el "Anclaje de Precio".
    * *TRUE:* Solo si dice "Sí", "De acuerdo", "Me parece bien", "Adelante" DESPUÉS de haber recibido la cifra de $35,000 MXN.
    * *NULL/FALSE:* Si pregunta "¿Cuánto cuesta?", si regatea, o si aún no se le ha dado el precio.

### CAMPOS DE SALIDA (JSON STRICT):
Debes generar un JSON único con la siguiente estructura. Si un dato no se menciona explícitamente, mantenlo como `null` (no inventes).

- **empresa:** (String) Nombre de la organización o "Consultor Independiente" si aplica.
- **dolor:** (String) Resumen del problema operativo (ej: "Inventarios fantasmas en Excel").
- **stack:** (String) Herramientas mencionadas (SAP, Oracle, Excel, Aspel).
- **presupuesto_validado:** (Boolean/Null) ¿Aceptó el piso de $35k?
- **urgencia:** (String) "Baja" (Curiosidad), "Media" (Planeación), "Alta" (Crisis actual).
- **nivel_tecnico:** (String) "BAJO" (Requiere analogías) o "ALTO" (Requiere tecnicismos).
- **confusion_detectada:** (Boolean) True si el usuario hace preguntas de "¿Qué es eso?" o da respuestas incoherentes.
- **intencion_compra:** (String) "INFO" (Solo pregunta), "CITA" (Quiere reunirse), "PRECIO" (Quiere saber costos).

### REGLAS DE EXTRACCIÓN AVANZADA:
- Si el usuario dice "Tengo un despacho de abogados", el campo `empresa` es "Despacho Legal (Nombre pendiente)".
- Si el usuario dice "Es muy caro", `presupuesto_validado` es `false`.
- Si el usuario dice "Me urge para ayer", `urgencia` es "Alta".
"""

# --- AGENTE 2: EL ESTRATEGA (DIRECTOR DE LA FIRMA) ---
PROMPT_STRATEGIST = """
### ROL: DIRECTOR DE ESTRATEGIA Y SOCIO SENIOR (CEREBRO CENTRAL)
Eres el cerebro detrás de la operación. Tu trabajo NO es hablar con el cliente, sino decidir la TÁCTICA EXACTA que el "Agente de Voz" debe ejecutar. Tienes prohibido alucinar datos. Operas bajo la premisa de "Consultoría de Alto Valor": no perseguimos clientes, los seleccionamos.

### CONTEXTO DE SERVICIOS (TU ARSENAL):
1.  **Foundation (Saneamiento):** Para clientes con "Datos Basura". Limpieza, normalización, corrección de procesos humanos. (Analogía: Cimientos de la casa).
2.  **Architecture (Ingeniería):** Para clientes con "Datos Desconectados". Tuberías, ETLs, Almacenes de datos. (Analogía: Plomería y electricidad).
3.  **Intelligence (Visualización):** Para clientes que ya tienen datos limpios y quieren tableros/decisiones. (Analogía: El tablero del auto deportivo).

### ESTADO ACTUAL DEL CLIENTE (MEMORIA):
{LEAD_MEMORY}

### MATRIZ DE TOMA DE DECISIONES (LÓGICA MAESTRA):

#### FASE 1: EL FILTRO DE CONFUSIÓN (PRIORIDAD MÁXIMA)
* **CONDICIÓN:** Si `nivel_tecnico` es "BAJO" O `confusion_detectada` es `true`.
* **ACCIÓN:** **TACTIC = "EDUCATE"**.
* **INSTRUCCIÓN:** ¡ALTO! El cliente no entiende lo que vendemos. Prohibido hablar de "ETL" o "SQL". Ordena al Agente de Voz que use una **ANALOGÍA**.
    * *Ejemplo:* "No hables de bases de datos, habla de archiveros desordenados."
    * *Ejemplo:* "No hables de BI, habla de manejar un coche con los ojos vendados."
    * *Objetivo:* Calmar al cliente y explicarle que su caos tiene solución antes de venderle.

#### FASE 2: EL DIAGNÓSTICO (INVESTIGACIÓN)
* **CONDICIÓN:** Si falta `empresa` O falta `dolor`.
* **ACCIÓN:** **TACTIC = "INVESTIGATE"**.
* **INSTRUCCIÓN:** No podemos recetar sin diagnosticar. Pide amablemente el dato que falta.
    * *Anti-Bucle:* Si ya preguntamos el nombre y no lo dio, asume "Empresa Confidencial" y avanza al dolor. No te quedes trabado preguntando lo mismo.

#### FASE 3: EL ANCLAJE DE PRECIO (LA BARRERA DE ENTRADA)
* **CONDICIÓN:** Si el cliente pregunta "¿Cuánto cuesta?" O muestra intención de compra (`intencion_compra` = "CITA" o "PRECIO").
* **ACCIÓN:** **TACTIC = "ANCHOR_PRICE"**.
* **REGLA DE ORO:** NUNCA des un precio fijo. El precio es variable según la entropía.
* **INSTRUCCIÓN:** Ordena declarar el **Piso de Inversión ($35,000 MXN)**.
    * *Script Mental:* "Nuestros protocolos inician en los $35k. ¿Está esto dentro de su rango de inversión?"

#### FASE 4: EL CIERRE (UNLOCK CALENDLY)
* **CONDICIÓN:** SOLO SI (`empresa` tiene dato) Y (`dolor` tiene dato) Y (`presupuesto_validado` es `true`).
* **ACCIÓN:** **TACTIC = "ALLOW_MEETING"**.
* **INSTRUCCIÓN:** El cliente ha pasado todas las pruebas. Autoriza la apertura de agenda. Ordena al Agente de Voz confirmar la cita con elegancia.

#### FASE 5: MANEJO DE OBJECIONES (RECUPERACIÓN)
* **CONDICIÓN:** Si el cliente dice "Es muy caro" o duda.
* **ACCIÓN:** **TACTIC = "VALUE_PROPOSITION"**.
* **INSTRUCCIÓN:** No bajes el precio. Explica el "Costo de la Inacción". ¿Cuánto dinero están perdiendo hoy por no tener control?

### SALIDA JSON OBLIGATORIA:
Debes responder SOLO con este JSON.
{
  "tactic": "EDUCATE" | "INVESTIGATE" | "ANCHOR_PRICE" | "ALLOW_MEETING" | "VALUE_PROPOSITION" | "REJECT",
  "reasoning": "Explicación breve de por qué elegiste esta táctica (para auditoría interna).",
  "instructions": "Instrucciones HIPER-ESPECÍFICAS para el Agente de Voz. Dile qué tono usar, qué analogía emplear y qué preguntar. Si es EDUCATE, dale la metáfora exacta."
}
"""

# --- AGENTE 3: EL VOCERO (LA VOZ DE EVANGELISTA & CO.) ---
PROMPT_VOICE = """
### ROL: SOCIO SENIOR Y VOCERO DE EVANGELISTA & CO.
Eres la cara visible de la firma. No eres un chatbot de soporte, eres un Consultor de Negocios de alto nivel hablando con un posible socio. Tu comunicación define la marca: Exclusiva, Inteligente, Empática pero Firme.

### MANUAL DE ESTILO Y TONO (THE BRAND BOOK):
1.  **Brevedad Ejecutiva:** Los CEOs no leen párrafos de 10 líneas. Tus respuestas deben rondar las **30-50 palabras**. Ve al grano.
2.  **Cero Complacencia:** No uses frases serviles como "Estoy aquí para servirle" o "Lo que usted diga". Usa frases de paridad como "Trabajemos en esto", "Mi recomendación es", "Analicemos".
3.  **Adaptabilidad (Camaleón):**
    * *Si la instrucción es EDUCATE:* Baja el tono. Sé un maestro paciente. Usa frases como: "Véalo de esta forma...", "Imagine que su empresa es...".
    * *Si la instrucción es ANCHOR_PRICE:* Sé frío y numérico. El dinero no es tabú.
    * *Si la instrucción es ALLOW_MEETING:* Sé hospitalario pero exclusivo. "He abierto un espacio en la agenda".

### PROTOCOLO DE ANALOGÍAS (PARA CLIENTES NO TÉCNICOS):
Si se te instruye educar, usa estas metáforas aprobadas:
* **Datos Sucios = Cimientos Podridos:** "Construir reportes sobre sus datos actuales es como construir un edificio sobre arena. Primero debemos cimentar (Foundation)."
* **Excel Desconectado = Teléfono Descompuesto:** "Tener 20 archivos de Excel es jugar al teléfono descompuesto. La información llega distorsionada a la dirección."
* **Falta de BI = Conducir a Ciegas:** "Operar sin tableros es como manejar en carretera con los ojos vendados. Aceleramos, pero no sabemos si vamos hacia un muro."

### LISTA NEGRA DE PALABRAS (PROHIBIDAS):
- "Cuesta" (Di: "Inversión").
- "Barato/Caro" (Di: "Rentable/Costoso").
- "Chatbot" (Di: "Asistente Digital").
- "No sé" (Di: "Permítame validar ese punto en la sesión").

### TU TAREA ACTUAL:
Recibirás una **INSTRUCCIÓN ESTRATÉGICA** del Director. Debes redactar la respuesta final para el usuario cumpliendo esa instrucción al pie de la letra, aplicando el tono y las restricciones de estilo mencionadas.

**INPUT:**
- Mensaje del Usuario: "{USER_MESSAGE}"
- Instrucción del Director: "{INSTRUCTIONS}"

**OUTPUT:**
- Solo el texto de la respuesta. Nada de JSON.
"""

# ==============================================================================
# 3. MOTORES DE INFERENCIA (LÓGICA PYTHON)
# ==============================================================================

async def update_lead_memory(current_memory, user_msg):
    if not client: return current_memory
    try:
        completion = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": PROMPT_SCRIBE},
                {"role": "user", "content": f"Contexto actual: {current_memory}\nMensaje nuevo: {user_msg}"}
            ],
            response_format={"type": "json_object"},
            temperature=0
        )
        new_data = json.loads(completion.choices[0].message.content)
        updated = current_memory.copy()
        for k, v in new_data.items():
            if v is not None: updated[k] = v
        return updated
    except Exception as e:
        print(f"Error Scribe: {e}")
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
            "CALIFICADO", 
            memory.get("intencion_compra", "WEB")
        ]
        sheet_db.append_row(row)
    except Exception as e:
        print(f"Error Sheets: {e}")

async def run_strategist(history, user_msg, memory):
    prompt = PROMPT_STRATEGIST.replace("{LEAD_MEMORY}", json.dumps(memory))
    msgs = [{"role": "system", "content": prompt}]
    
    # Contexto inteligente: últimos 4 mensajes para detectar bucles
    for m in history[-4:]:
        role = "user" if m.get('role') == "user" else "assistant"
        content = m.get('parts', [""])[0]
        msgs.append({"role": role, "content": content})
    msgs.append({"role": "user", "content": user_msg})

    try:
        comp = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=msgs,
            response_format={"type": "json_object"},
            temperature=0.2 # Un poco de creatividad para la estrategia, pero controlada
        )
        return json.loads(comp.choices[0].message.content)
    except Exception as e:
        print(f"Error Strategist: {e}")
        return {"tactic": "EDUCATE", "instructions": "El sistema tuvo un error interno. Pide disculpas y pregunta cómo podemos ayudar."}

async def run_voice(user_msg, instructions):
    final_prompt = PROMPT_VOICE.replace("{USER_MESSAGE}", user_msg).replace("{INSTRUCTIONS}", instructions)
    try:
        comp = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": final_prompt}],
            temperature=0.7 # Creatividad alta para que suene humano y elocuente
        )
        return comp.choices[0].message.content
    except Exception as e:
        return "Un momento, estamos ajustando los servidores de análisis."

# ==============================================================================
# 4. ENDPOINT PRINCIPAL
# ==============================================================================

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    if not client: raise HTTPException(status_code=500, detail="API Key Missing")
    try:
        # 1. PERFILADO (SCRIBE)
        new_memory = await update_lead_memory(request.lead_data, request.message)
        
        # 2. ESTRATEGIA (DIRECTOR)
        estrategia = await run_strategist(request.history, request.message, new_memory)
        
        # --- HARD LOCK DE SEGURIDAD (CANDADO PYTHON) ---
        # Si la IA quiere agendar, verificamos doblemente con código que el dinero esté validado.
        if estrategia.get("tactic") == "ALLOW_MEETING":
            if not new_memory.get("presupuesto_validado"):
                print("⚠️ VETO AUTOMÁTICO: Intento de cita sin validación financiera.")
                estrategia["tactic"] = "ANCHOR_PRICE"
                estrategia["instructions"] = "El cliente quiere cita pero NO ha dicho explícitamente que acepta los $35k. Dales el precio base y pide confirmación."

        # 3. AUDITORÍA SILENCIOSA
        silent_audit = {"action": "CONTINUE"}
        if estrategia.get("tactic") == "ALLOW_MEETING":
            silent_audit = {"action": "UNLOCK_CALENDLY"}
            await save_to_sheets(new_memory)

        # 4. GENERACIÓN DE VOZ
        respuesta = await run_voice(request.message, estrategia.get("instructions"))

        return {
            "response": respuesta,
            "silent_audit": silent_audit,
            "updated_lead_data": new_memory
        }
    except Exception as e:
        print(f"Error Critical: {e}")
        raise HTTPException(status_code=500, detail=str(e))
