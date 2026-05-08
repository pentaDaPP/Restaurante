from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id : str | None = None
    name : str
    precio : int
    categoria : str
    imagen : str
    descripcion : str
    
