from fastapi import APIRouter, HTTPException, Depends ,Form,File,UploadFile
from db.models.producto import Product
from db.cliente import db
from db.schemas.plato import plato_schema
from routers.mostrar_platos import all_platos
from db.auth import verificar_api_key
import os


router = APIRouter(prefix="/agg_platos",
                   tags=["agg_platos"],
                   responses={404:{"message":"no encontrado"}})


@router.post("/", status_code=201)
async def agg_plato(
    nombre: str = Form(...),
    precio: float = Form(...),
    descripcion: str = Form(...),
    categoria: str = Form(...),
    imagen: UploadFile = File(...),
    api_key: str = Depends(verificar_api_key)
):
    
    
    if(type(search_plato(nombre))) == Product:
        raise HTTPException(status_code=404,detail="el plato ya se encuentra")
    else:
        print("1-entro al endpoint")
        
        contenido = await imagen.read()
        print("nombre", imagen.filename)
        print("size", len(contenido))
        print("tipo", imagen.content_type)
        print("2 - imagen leida")
        nombre_archivo= imagen.filename
        ruta_archivo = os.path.join("static/imagen/",nombre_archivo)
        try:
            print("3-antes de guardar archivo")
            with open(ruta_archivo, "wb") as archivo:
                archivo.write(contenido)
            print("4-archivo guardado")
        except Exception as e:
            print("error guardando imagen",str(e))
            raise e
            
        product_dict = {
                    "name" : nombre,
                    "precio" : precio,
                    "descripcion" : descripcion,
                    "categoria": categoria,
                    "imagen" : ruta_archivo
                }
        print("5-antes de mongodb")
        id = db["platos"].insert_one(product_dict).inserted_id
        print("6-mongodb correcto")
        new_plato = plato_schema(db["platos"].find_one({"_id" : id }))
        
        return Product(**new_plato)

def search_plato(name : str):
    
    try:
        plato = plato_schema(db["platos"].find_one({"name" : name}))
        return Product(**plato)
    except:
        return "no se ha encontrado al plato"
