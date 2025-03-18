import mysql.connector

def conectarse()->None:
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Contraseña@123',
        database='dgie41'
    )

def crearTabla():
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("CREATE TABLE prueba(id_prueba INT AUTO_INCREMENT PRIMARY KEY, "
        "nombre VARCHAR(100), descripcion TEXT);")
    conexion.commit()
    conexion.close()

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