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
        clave_id="1",
        nombre="Nerise Suriel",
        departamento="Canales y Producto",
        extension="1201",
        correo="nsuriel@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="2",
        nombre="Francisca Pichardo",
        departamento="Canales y Producto",
        extension="1202",
        correo="fpichardo@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="3",
        nombre="Lucila Valentin",
        departamento=" Canales y Producto",
        extension="1203",
        correo="lvalentin@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="4",
        nombre="Luisanna Tactuk",
        departamento=" Operaciones Tarjeta de Credito",
        extension="1204",
        correo="ltactuk@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="5",
        nombre="Florangel Cruz",
        departamento=" Ciclo de Vida de Tarjeta",
        extension="1205",
        correo="fcruz@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="6",
        nombre="Madelane Dominguez",
        departamento=" Negocios",
        extension="1206",
        correo="mdominguez@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="7",
        nombre="Luisa Casanova",
        departamento=" Cobros TC",
        extension="1207",
        correo="lcasanova@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="8",
        nombre="Maria Alcantara",
        departamento="",
        extension="1208",
        correo="malcantara@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="9",
        nombre="Sorilenne Mendez",
        departamento="Canales y Producto",
        extension="1209",
        correo="srodriguez@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="10",
        nombre="Felipe Rodriguez",
        departamento="Negocios",
        extension="1210",
        correo="frodriguez@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="11",
        nombre="Yomaira Roa",
        departamento="Negocios",
        extension="1211",
        correo="yroa@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="12",
        nombre="Yomary Almanzar",
        departamento="Negocios",
        extension="1212",
        correo="yalmanzar@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="13",
        nombre="Jenny Ogando",
        departamento="Canales y Producto",
        extension="1213",
        correo="jogando@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="14",
        nombre="Lissa Ramirez",
        departamento="tarjeta de credito",
        extension="1214",
        correo="lramirez@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="15",
        nombre="Linette Tupete",
        departamento="Canales y Producto",
        extension="1215",
        correo="ltupete@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="16",
        nombre="Jesús García",
        departamento="Ciberseguridad",
        extension="1216",
        correo="jgarcia@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="18",
        nombre="Angel Veloz",
        departamento="Administracion de Cartera",
        extension="1218",
        correo="aveloz@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="19",
        nombre="Suleika Plata",
        departamento="Canales y Producto",
        extension="1219",
        correo="splata@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="20",
        nombre="Ludy",
        departamento="Tarjeta de Credito",
        extension="1220",
        correo="lisenia@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="21",
        nombre="Jessica Brito",
        departamento="Negocios",
        extension="1221",
        correo="jbrito@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="22",
        nombre="Jose Ignacio",
        departamento="Tesoreria",
        extension="1222",
        correo="jrivero@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="23",
        nombre="Edwin Carreras",
        departamento="Cobros",
        extension="1223",
        correo="ecarreras@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="24",
        nombre="Yulimar Vasquez",
        departamento="Cobros",
        extension="1224",
        correo="cobranzas1@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="25",
        nombre="Evelyn Nuñez",
        departamento="Riesgo",
        extension="1225",
        correo="enunez@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="26",
        nombre="Isaac Sierra",
        departamento="",
        extension="1226",
        correo="isierra@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="28",
        nombre="Miguel Mena",
        departamento="Cobros TC",
        extension="1228",
        correo="mimena@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="29",
        nombre="Juana Solano",
        departamento="Recursos Humano",
        extension="1229",
        correo="jsolano@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="30",
        nombre="Yamel Segura",
        departamento="Credito",
        extension="1230",
        correo="ysegura@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="31",
        nombre="Griselda Tavarez",
        departamento="Credito",
        extension="1231",
        correo="gtavarez@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="32",
        nombre="Anngys Leonardo",
        departamento="Credito",
        extension="1232",
        correo="aleonardo@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="33",
        nombre="Jimmy Borbon",
        departamento="Negocios",
        extension="1233",
        correo="jborbon@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="34",
        nombre="Ruth Martin",
        departamento="Canales y Producto",
        extension="1235",
        correo="rmartin@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="35",
        nombre="Massiel Canela",
        departamento="Operaciones",
        extension="1236",
        correo="mcanela@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="37",
        nombre="Denny Castillo",
        departamento="Operaciones",
        extension="1238",
        correo="dcastillo@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="38",
        nombre="Milagros Castillo",
        departamento="Operaciones",
        extension="1239",
        correo="mcastillo@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="40",
        nombre="Denisse Torres",
        departamento="Contabilidad",
        extension="1241",
        correo="dtorres@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="41",
        nombre="Carolina Montaño",
        departamento="Contabilidad",
        extension="1242",
        correo="cmontano@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="42",
        nombre="William Sanchez",
        departamento="Cobros",
        extension="1243",
        correo="wsanchez@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="43",
        nombre="Salvador Oliveros",
        departamento="Tarjeta de Credito",
        extension="1244",
        correo="joliveros@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="44",
        nombre="Marjorie Abreu",
        departamento="Tesoreria",
        extension="1245",
        correo="mabreu@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="45",
        nombre="Yunior Cesar",
        departamento="Auditoria",
        extension="1246",
        correo="ycquezada@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="46",
        nombre="Jose Lozada",
        departamento="Presidencia",
        extension="1247",
        correo="jlozada@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="49",
        nombre="Paola Herrera",
        departamento="Legal",
        extension="1250",
        correo="pherrera@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="50",
        nombre="Jovanna Cabrera",
        departamento="Riesgo",
        extension="1251",
        correo="jcabrera@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="51",
        nombre="Milagros Vasquez",
        departamento="Legal",
        extension="1252",
        correo="mvasquez@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="52",
        nombre="Benjamín Fermín",
        departamento="Tecnologia",
        extension="1253",
        correo="bfermin@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="53",
        nombre="Kelvy Medina",
        departamento="Administracion",
        extension="1254",
        correo="kmedina@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="55",
        nombre="Yariel Peña",
        departamento="Auditoria",
        extension="1256",
        correo="ypena@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="56",
        nombre="Israel Villamizar",
        departamento="Tecnologia",
        extension="1257",
        correo="ivillamizar@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="57",
        nombre="Rafael Peralta",
        departamento="Tarjeta de Credito",
        extension="1258",
        correo="rperalta@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="58",
        nombre="Margarita Sosa",
        departamento="Administracion",
        extension="1259",
        correo="msosa@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="59",
        nombre="Jhoanna Cruz",
        departamento="Cumplimiento",
        extension="1260",
        correo="jcruz@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="61",
        nombre="Nolberto Moreno",
        departamento="Cobros",
        extension="1262",
        correo="cobranzas@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="62",
        nombre="Rafael B Romero",
        departamento="Seguridad",
        extension="1263",
        correo="rromero@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="63",
        nombre="German Carrasco",
        departamento="Tecnologia",
        extension="1264",
        correo="gcarrasco@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="64",
        nombre="Rosanna Henriquez",
        departamento="Riesgo",
        extension="1265",
        correo="rhenriquez@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="65",
        nombre="Ismael Mejia",
        departamento="Negocios",
        extension="1266",
        correo="imejia@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="66",
        nombre="Yanaira Lorenzo",
        departamento="Administracion",
        extension="1267",
        correo="ylorenzo@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="67",
        nombre="Melany Polanco",
        departamento="Tesoreria",
        extension="1268",
        correo="mpolanco@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="68",
        nombre="Diogenes Tejeda",
        departamento="Contabilidad",
        extension="1269",
        correo="dtejeda@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="69",
        nombre="Ana Morrillo",
        departamento="Tarjeta de Credito",
        extension="1270",
        correo="amorillo@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="70",
        nombre="Soribel Rodriguez",
        departamento="Canales y Producto",
        extension="1271",
        correo="srodriguez@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="71",
        nombre="Maria Reyes",
        departamento="Tarjeta de Credito",
        extension="1272",
        correo="mreyes@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="72",
        nombre="Emilio Mendoza",
        departamento="Tesoreria",
        extension="1273",
        correo="emendoza@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="74",
        nombre="Joan Ozuna",
        departamento="Cumplimiento",
        extension="1275",
        correo="jozuna@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="75",
        nombre="Danilo Ramirez",
        departamento="Ciberseguridad",
        extension="1276",
        correo="jramirez@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="76",
        nombre="Maria del Carmen",
        departamento="Administracion de Cartera",
        extension="1277",
        correo="malberto@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="80",
        nombre="Eusebio Carlino",
        departamento="Presidencia",
        extension="1281",
        correo="ecarlino@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="82",
        nombre="YANIEL QUINTANA",
        departamento="Presidencia",
        extension="1283",
        correo="yafermin@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="83",
        nombre="Roseiry Morin",
        departamento="Tarjeta",
        extension="1284",
        correo="rmorin@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="84",
        nombre="Loraine Sepulveda",
        departamento="Auditoria",
        extension="1285",
        correo="lsepulveda@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="85",
        nombre="Oscar Peralta",
        departamento="Credito",
        extension="1286",
        correo="operalta@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="87",
        nombre="Pamela Gonzalez",
        departamento="Riesgo",
        extension="1288",
        correo="pgonzalez@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="88",
        nombre="Elianny Diaz",
        departamento="Recursos Humano",
        extension="1289",
        correo="ediaz@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="89",
        nombre="Melvin Frias",
        departamento="Tecnologia",
        extension="1290",
        correo="mfrias@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="90",
        nombre="Sebastian Peña",
        departamento="Tecnologia",
        extension="1291",
        correo="spena@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="91",
        nombre="Jonathan Geronimo",
        departamento="Legal",
        extension="1292",
        correo="jgeronimo@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="92",
        nombre="Onnis Grullon",
        departamento="Home",
        extension="1295",
        correo="ogrullon@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="93",
        nombre="Cristian Rodríguez",
        departamento="Cobros",
        extension="1296",
        correo="crodriguez@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="94",
        nombre="Wagner Urbino",
        departamento="Home",
        extension="1297",
        correo="wurbino@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="95",
        nombre="Keisy Mendez",
        departamento="Credito",
        extension="1298",
        correo="kmendez@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="96",
        nombre="Pedro Marcel",
        departamento=" Tecnología",
        extension="1299",
        correo="pmarcel@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="100",
        nombre="Ernesto Batista",
        departamento="",
        extension="1304",
        correo="ebatista@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="101",
        nombre="Yoalbys Siri",
        departamento="Operaciones",
        extension="1305",
        correo="yofrias@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="102",
        nombre="Danilcia Mercedes",
        departamento="",
        extension="1306",
        correo="dmercedes@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="103",
        nombre="Escarlet Jimenez",
        departamento="",
        extension="1307",
        correo="ejimenez@bancoatlantico.com.do"
    )

insertar_empleado(
        clave_id="104",
        nombre="Alba Merejildo",
        departamento="Negocio",
        extension="1308",
        correo="amerejildo@bancoatlantico.com.do"
    )