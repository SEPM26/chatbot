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
    posibles_nombres = re.findall(r"[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?:\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)+", texto)
    return posibles_nombres[0] if posibles_nombres else ""

@app.get("/", response_class=FileResponse)
def get_index():
    return FileResponse("static/index.html")

@app.post("/api/chat")
def responder(consulta: Consulta):
    mensaje = consulta.mensaje.strip()
    nombre = extraer_nombre(mensaje)

    # Si parece consulta sobre empleado
    if any(p in mensaje.lower() for p in ["extension", "correo", "trabaja", "departamento", "empleado", "id"]) and nombre:
        empleado = buscar_empleado_por_nombre(nombre)
        if empleado:
            mensaje_lower = mensaje.lower()
            if "extension" in mensaje_lower:
                return {"respuesta": f"La extension de {empleado['nombre']} es {empleado['extension']}."}
            elif "correo" in mensaje_lower or "email" in mensaje_lower:
                return {"respuesta": f"El correo de {empleado['nombre']} es {empleado['correo']}."}
            elif "departamento" in mensaje_lower or "trabaja" in mensaje_lower:
                return {"respuesta": f"{empleado['nombre']} trabaja en {empleado['departamento']}."}
            else:
                # Info general
                return {
                    "respuesta": f"{empleado['nombre']} trabaja en {empleado['departamento']}, su extensión es {empleado['extension']} y su correo es {empleado['correo']}."
                }
        else:
            return {"respuesta": f"No tengo información sobre el empleado llamado {nombre}."}

    # Si no es sobre un empleado, responde con IA
    respuesta = responder_con_ia(mensaje)
    return {"respuesta": respuesta}
