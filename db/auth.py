# db/auth.py
import os
from fastapi import Header, HTTPException
from dotenv import load_dotenv

load_dotenv()

# Obtener la API Key desde variables de entorno
API_KEY = os.getenv("API_KEY", "mi_api_key_secreta_cambiar")

async def verificar_api_key(x_api_key: str = Header(...)):
    """
    Dependencia para verificar la API Key en los headers.
    Se usa en endpoints que requieren autenticación.
    """
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=403,
            detail="API Key inválida. Acceso no autorizado."
        )
    return x_api_key
