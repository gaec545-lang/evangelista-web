import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. Cargar tu llave del archivo .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: No se encontró la API KEY en el archivo .env")
else:
    print(f"✅ API KEY encontrada: {api_key[:5]}...*****")
    
    try:
        genai.configure(api_key=api_key)
        
        print("\n🔎 BUSCANDO MODELOS DISPONIBLES PARA TI...")
        print("------------------------------------------------")
        
        # 2. Listar modelos
        found = False
        for m in genai.list_models():
            # Solo queremos modelos que generen texto (chat)
            if 'generateContent' in m.supported_generation_methods:
                print(f"• {m.name}")
                found = True
        
        if not found:
            print("⚠️ No se encontraron modelos de texto. Verifica tu API Key.")
            
        print("------------------------------------------------")
        print("COPIA EXACTAMENTE UNO DE LOS NOMBRES DE ARRIBA (ej: models/gemini-pro)")

    except Exception as e:
        print(f"\n❌ ERROR DE CONEXIÓN: {e}")