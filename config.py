import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("No se encontró GROQ_API_KEY en el archivo .env")

print("OK - GROQ_API_KEY cargada correctamente")