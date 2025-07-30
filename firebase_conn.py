import firebase_admin
from firebase_admin import credentials, db
from unidecode import unidecode

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chatbotemp-default-rtdb.firebaseio.com/'
})

def normalizar(texto):
    return unidecode(texto.lower().strip())

def buscar_empleado_por_nombre(nombre):
    ref = db.reference("empleados")
    empleados = ref.get()

    if not empleados:
        return None

    nombre = normalizar(nombre)

    nombre_partes = nombre.split()

    if isinstance(empleados, list):
        datos_iterables = empleados
    elif isinstance(empleados, dict):
        datos_iterables = empleados.values()
    else:
        return None

    for datos in datos_iterables:
        nombre_empleado = normalizar(datos.get("nombre", ""))
        if all(parte in nombre_empleado for parte in nombre_partes):
            return datos

    return None
