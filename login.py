import mysql.connector
from datetime import datetime

registro = {}
#region conexion
def conectarse()->None:
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Contraseña@123',
        database='dgie41'
    )
#endregion

def inicio(usuario:str)->None:
    now = datetime.now()
    registro[usuario] = {"Fecha y hora de incio de sesion: ":now}