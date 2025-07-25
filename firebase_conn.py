import firebase_admin
from firebase_admin import credentials, db

# Inicializa Firebase si no está ya iniciado
try:
    firebase_admin.get_app()
except ValueError:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://chatbotemp-default-rtdb.firebaseio.com'  #
    })

# Buscar un empleado por nombre
def buscar_empleado_por_nombre(nombre: str):
    ref = db.reference("empleados")
    empleados = ref.get()

    if empleados:
        for emp_id, emp in empleados.items():
            if nombre.lower() in emp["nombre"].lower():
                return emp
    return None
