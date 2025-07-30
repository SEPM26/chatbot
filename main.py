from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from firebase_conn import buscar_empleado_por_nombre
from utils import responder_con_ia
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/static", StaticFiles(directory="static"), name="static")

class Consulta(BaseModel):
    mensaje: str

def extraer_nombre(texto: str) -> str:
    palabras = re.findall(r"[A-ZÁÉÍÓÚÑa-záéíóúñ]+", texto)
    if len(palabras) >= 2:
        return f"{palabras[-2].capitalize()} {palabras[-1].capitalize()}"
    elif len(palabras) == 1:
        return palabras[0].capitalize()
    return ""

@app.get("/", response_class=FileResponse)
def get_index():
    return FileResponse("static/index.html")

@app.post("/api/chat")
def responder(consulta: Consulta):
    mensaje = consulta.mensaje.strip()
    nombre = extraer_nombre(mensaje)
    print(f"🔎 Buscando: {nombre}")

    es_empleado = any(p in mensaje.lower() for p in [
        "correo", "email", "extension", "trabaja", "departamento"
    ])

    if es_empleado and nombre:
        try:
            empleado = buscar_empleado_por_nombre(nombre)
        except Exception as e:
            return {"respuesta": f"❌ Error al buscar en la base de datos: {str(e)}"}

        if isinstance(empleado, dict) and empleado.get("ambiguo"):
            nombres = [emp["nombre"] for emp in empleado["resultados"]]
            return {"respuesta": f"Encontré varios empleados con ese nombre: {', '.join(nombres)}. ¿Podrías ser más específico?"}

        if empleado:
            if "correo" in mensaje.lower() or "email" in mensaje.lower():
                return {"respuesta": f"El correo de {empleado['nombre']} es {empleado['correo']}."}
            elif "extension" in mensaje.lower():
                return {"respuesta": f"La extensión de {empleado['nombre']} es {empleado['extension']}."}
            elif "departamento" in mensaje.lower() or "trabaja" in mensaje.lower():
                return {"respuesta": f"{empleado['nombre']} trabaja en el departamento de {empleado['departamento']}."}
            else:
                return {"respuesta": f"{empleado['nombre']} - {empleado['departamento']}, Ext: {empleado['extension']}, Correo: {empleado['correo']}"}
        else:
            return {"respuesta": f"No encontré información sobre {nombre}."}

    return {"respuesta": responder_con_ia(mensaje)}