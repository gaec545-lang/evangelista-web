from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from groq import Groq
from dotenv import load_dotenv

# --- IMPORTANTE: El módulo de seguridad ---
from fastapi.middleware.cors import CORSMiddleware 

# Cargar variables de entorno
load_dotenv()

# Inicializar la app
app = FastAPI()

# --- CONFIGURACIÓN DE SEGURIDAD (CORS) ---
# Esto es lo que permite que tu página web hable con el servidor
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite acceso desde cualquier lugar (GitHub, localhost, etc.)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, OPTIONS)
    allow_headers=["*"],  # Permite todos los encabezados
)

# Configuración del cliente Groq
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"status": "Sistemas de Evangelista & Co. operativos"}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    if not os.environ.get("GROQ_API_KEY"):
        raise HTTPException(status_code=500, detail="Error de configuración: API Key no encontrada")
    
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
            model="llama3-8b-8192", # O el modelo que prefieras usar
        )
        return {"response": chat_completion.choices[0].message.content}
    except Exception as e:
        print(f"Error interno: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
