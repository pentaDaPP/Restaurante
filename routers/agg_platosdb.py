from fastapi import APIRouter, HTTPException, Depends
from db.models.producto import Product
from db.cliente import db
from db.schemas.plato import plato_schema
from routers.mostrar_platos import all_platos
from db.auth import verificar_api_key

router = APIRouter(prefix="/agg_platos",
                   tags=["agg_platos"],
                   responses={404:{"message":"no encontrado"}})


@router.post("/", status_code=201)
async def agg_plato(product : Product , api_key : str = Depends(verificar_api_key)):
    
    if(type(search_plato(product.name))) == Product:
        raise HTTPException(status_code=404,detail="el plato ya se encuentra")
    else:
   
        product_dict = dict(product)
        del product_dict["id"]

        id = db["platos"].insert_one(product_dict).inserted_id
        
        new_plato = plato_schema(db["platos"].find_one({"_id" : id }))
        
        return Product(**new_plato)

def search_plato(name : str):
    
    try:
        plato = plato_schema(db["platos"].find_one({"name" : name}))
        return Product(**plato)
    except:
        return "no se ha encontrado al usuario"
