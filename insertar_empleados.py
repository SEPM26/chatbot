import firebase_admin
from firebase_admin import credentials, db

# Inicializar Firebase (solo si no ha sido inicializado ya)
try:
    firebase_admin.get_app()
except ValueError:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://chatbotemp-default-rtdb.firebaseio.com'
    })

def insertar_empleado(clave_id, nombre, departamento, extension, correo):
    ref = db.reference(f"empleados/{clave_id}")
    ref.set({
        "nombre": nombre,
        "departamento": departamento,
        "extension": extension,
        "correo": correo
    })
    print(f"Empleado '{nombre}' agregado correctamente.")


if __name__ == "__main__":
    insertar_empleado(
        clave_id="maria_fernandez",
        nombre="María Fernández",
        departamento="Recursos Humanos",
        extension="104",
        correo="maria.fernandez@empresa.com"
    )
