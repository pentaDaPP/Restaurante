import os
from fastapi import Header, HTTPException


def verificar_api_key(
    x_api_key: str = Header(...)
):

    api_key_correcta = os.getenv("API_KEY")

    if not api_key_correcta:
        raise HTTPException(
            status_code=500,
            detail="API Key del servidor no configurada"
        )

    if x_api_key != api_key_correcta:
        raise HTTPException(
            status_code=401,
            detail="API Key incorrecta"
        )

    return x_api_key