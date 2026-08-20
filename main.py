from fastapi import FastAPI, Request, HTTPException , Depends, Header, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routers import agg_platosdb, mostrar_platos, update_plato, carrito,auth, cloudinary_config, delete_plato
from starlette.middleware.sessions import SessionMiddleware
import os
from db.auth import verificar_api_key

app = FastAPI()

# Incluir routers
app.include_router(agg_platosdb.router)
app.include_router(mostrar_platos.router)
app.include_router(update_plato.router)
app.include_router(carrito.router)
app.include_router(auth.router)
app.include_router(delete_plato.router)



# Archivos estáticos
#app.mount("/static", StaticFiles(directory="static"), name="static")
#app.mount("/static/imagen", StaticFiles(directory="static/imagen"), name="imagen")

# Plantillas
templates = Jinja2Templates(directory="templates")

# Clave secreta para sesiones
SECRET_KEY = os.environ.get("SECRET_KEY", "mi_clave_secreta_cambiar")
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)



@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    try:
        categorias = await mostrar_platos.all_categorias()
    except:
        categorias = []
    return templates.TemplateResponse("index.html", {
        "request": request,
        "categorias": categorias,
        "categoria_actual": "todos",
        "cart_count": 0   # puedes calcularlo si ya tienes la sesión
    })

"""
ADMIN_API_KEY = os.getenv("ADMIN_API_KEY" , "mi_super_key_secreta")
def require_admin_api_key(x_api_key: str = Header(None)):
    if x_api_key is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="API key missing")
    if x_api_key != ADMIN_API_KEY:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid admin API key")
    return True
"""

@app.get("/admin",response_class=HTMLResponse)
async def admin(request : Request ):
    return templates.TemplateResponse("admin.html",{
        "request" : request
    })



"""
@app.get("/", status_code=200, response_class=HTMLResponse)
async def menu(request: Request, categoria: str = "hamburguesa"):
        # Valores falsos para aislar el error
    categorias = ["Pizzas", "Hamburguesas", "Bebidas"]
    platos = []
    categoria_actual = categoria
    cart_count = 0

    # Imprimir tipos para depurar
    print("DEBUG - Tipos:")
    print(f"  categorias: {type(categorias)} -> {categorias}")
    print(f"  platos: {type(platos)} -> {platos}")
    print(f"  categoria_actual: {type(categoria_actual)} -> {categoria_actual}")
    print(f"  cart_count: {type(cart_count)} -> {cart_count}")

    return templates.TemplateResponse(
        "test.html",
        {
            "request": request,
            "categorias": categorias,
            "platos": platos,
            "categoria_actual": categoria_actual,
            "cart_count": cart_count
        }
    )
"""
