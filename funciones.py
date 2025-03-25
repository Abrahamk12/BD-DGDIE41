import mysql.connector
#region conexion
def conectarse()->None:
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Contraseña@123',
        database='dgie41'
    )
#endregion
#region creacion Tablas dinamicas
def crear_tabla(nombre_tabla, **columnas):
    try:
        conexion = conectarse()
        cursor = conexion.cursor()
        columnas_sql = ", ".join([f"{columna} {tipo}" for columna, tipo in columnas.items()])
        consulta = f"CREATE TABLE IF NOT EXISTS {nombre_tabla} ({columnas_sql})"
        cursor.execute(consulta)
        print(f"Tabla '{nombre_tabla}' creada exitosamente.")
        conexion.commit()
        cursor.close()
        conexion.close()
    except mysql.connector.Error as error:
        print(f"Error al crear la tabla: {error}")
#endregion

#region creacion
def crearTabla():
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("CREATE TABLE prueba(id_prueba INT AUTO_INCREMENT PRIMARY KEY, "
        "nombre VARCHAR(100), descripcion TEXT);")
    conexion.commit()
    conexion.close()
#endregion

#region obtener Datos
def guardarUsuario(nombre:str, descripcion:str):
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO prueba(nombre, descripcion) VALUES(%s, %s)"),
        (nombre, descripcion)
    conexion.commit()
    conexion.close()

def comprobarUsuario()->list:
    c_us = []
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT nombre FROM prueba")
        c_usuario = cursor.fetchall()
    conexion.close()
    for i in range(len(c_usuario)):
        us = c_usuario.__getitem__(i)
        c_us.append(us.__getitem__(0))
    return c_us

def getUsuario(nombre:str)->str:
    usuario = ""
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT nombre FROM prueba WHERE usuario = " + "'" + nombre + "'")
        usuario = cursor.fetchone()
        us = usuario.__getitem__(0)
    conexion.close()
    return us

def getPassword(nombre:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        password = cursor.execute("SELECT contraseña FROM usuarios WHERE usuario = " + "'" + nombre + "'")
        password = cursor.fetchone()
    conexion.close() 
    for i in range(len(password)):
        pas = password.__getitem__(i)
    return pas
#endregion