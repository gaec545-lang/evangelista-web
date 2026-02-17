from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from groq import Groq
# from dotenv import load_dotenv  <-- COMENTAMOS ESTO PARA EVITAR ERRORES SI NO HAY ARCHIVO
from fastapi.middleware.cors import CORSMiddleware

# Intentamos cargar .env solo si existe (para local), si no, seguimos
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = FastAPI()

# --- SEGURIDAD CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- VERIFICACIÓN DE LLAVE ---
# Leemos la variable DIRECTAMENTE del sistema
api_key_system = os.environ.get("GROQ_API_KEY")

if not api_key_system:
    # Si no hay llave, imprimimos error en los logs pero NO rompemos la app al inicio
    print("CRITICAL: GROQ_API_KEY not found in environment variables")
    # Ponemos un cliente dummy para que la app arranque, pero fallará al chatear
    client = None
else:
    client = Groq(api_key=api_key_system)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"status": "Sistemas de Evangelista & Co. operativos"}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    # Verificación en tiempo de ejecución
    if not client:
        raise HTTPException(status_code=500, detail="Error de Servidor: API Key no configurada en Railway")
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Eres el asistente estratégico de Evangelista & Co. Responde de forma profesional, concisa y orientada a negocios."
                },
                {
                    "role": "user",
                    "content": request.message,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        return {"response": chat_completion.choices[0].message.content}
    except Exception as e:
        print(f"Error interno: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
