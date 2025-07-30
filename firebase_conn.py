import firebase_admin
from firebase_admin import credentials, db
from unidecode import unidecode

# Inicializar Firebase una sola vez
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://chatbotemp-default-rtdb.firebaseio.com/'
    })

def normalizar(texto):
    return unidecode(texto.lower().strip())

def buscar_empleado_por_nombre(nombre):
    try:
        ref = db.reference("/empleados")
        empleados = ref.get()
    except Exception as e:
        raise Exception(f"Error conectando a Firebase: {e}")

    if not empleados:
        return None

    nombre_normalizado = normalizar(nombre)
    partes = nombre_normalizado.split()

    coincidencias = []

    fuente = empleados.values() if isinstance(empleados, dict) else empleados

    for datos in fuente:
        if not datos:
            continue
        nombre_empleado = normalizar(datos.get("nombre", ""))
        if all(p in nombre_empleado for p in partes):
            coincidencias.append(datos)

    if len(coincidencias) == 1:
        return coincidencias[0]
    elif len(coincidencias) > 1:
        return {"ambiguo": True, "resultados": coincidencias}
    else:
        return None
