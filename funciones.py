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

#region insertar Datos
def guardarDatos(nombre_tabla, datos, columnas)->None:
    try:
        # Conexión a la base de datos
        conexion = conectarse()
        cursor = conexion.cursor()

        # Construcción de las columnas y valores
        columnas_sql = ", ".join(columnas.keys())
        valores_sql = ", ".join(["%s"] * len(columnas))  # Marcadores de posición para los valores
        consulta = f"INSERT INTO {nombre_tabla} ({columnas_sql}) VALUES ({valores_sql});"
        
        # Ejecución de la consulta
        cursor.execute(consulta, tuple(datos.values()))  # Pasa los valores como una tupla
        
        # Confirmar los cambios en la base de datos
        conexion.commit()

        print("Datos guardados exitosamente.")

        # Cierre de la conexión
        cursor.close()
        conexion.close()

    except mysql.connector.Error as error:
        print(f"Error al guardar los datos: {error}")


def registrarUsuario(nombre_tabla, datos, columnas)->None:
    try:
        # Conexión a la base de datos
        conexion = conectarse()
        cursor = conexion.cursor()

        # Construcción de las columnas y valores
        columnas_sql = ", ".join(columnas.keys())
        valores_sql = ", ".join(["%s"] * len(columnas))  # Marcadores de posición para los valores
        consulta = f"INSERT INTO {nombre_tabla} ({columnas_sql}) VALUES ({valores_sql});"
        
        # Ejecución de la consulta
        cursor.execute(consulta, tuple(datos.values()))  # Pasa los valores como una tupla
        
        # Confirmar los cambios en la base de datos
        conexion.commit()

        print("Datos guardados exitosamente.")

        # Cierre de la conexión
        cursor.close()
        conexion.close()

    except mysql.connector.Error as error:
        print(f"Error al guardar los datos: {error}")
#endregion

#region obtener Datos
def obtenerDatos(nombre_tabla, **columnas)->list:
    try:
        # Conexión a la base de datos
        conexion = conectarse()
        cursor = conexion.cursor()

        # Construcción de la consulta SQL
        columnas_sql = ", ".join(columnas.keys())
        consulta = f"SELECT {columnas_sql} FROM {nombre_tabla};"
        
        # Ejecución de la consulta
        cursor.execute(consulta)
        
        # Obtención de los datos
        datos = cursor.fetchall()  # Recupera todas las filas del resultado
        for fila in datos:
            print(fila)  # Aquí puedes procesar o guardar los datos como desees

        # Cierre de la conexión
        cursor.close()
        conexion.close()
    except mysql.connector.Error as error:
        print(f"Datos no encontrados: {error}")

def obtenerDatosWhere(nombre_tabla, dato, referencia, **columnas)->list:
    try:
        # Conexión a la base de datos
        conexion = conectarse()
        cursor = conexion.cursor()

        # Construcción de la consulta SQL
        columnas_sql = ", ".join(columnas.keys())
        consulta = f"SELECT {columnas_sql} FROM {nombre_tabla} WHERE {referencia} = {dato};"
        
        # Ejecución de la consulta
        cursor.execute(consulta)
        
        # Obtención de los datos
        datos = cursor.fetchall()  # Recupera todas las filas del resultado
        for fila in datos:
            print(fila)  # Aquí puedes procesar o guardar los datos como desees

        # Cierre de la conexión
        cursor.close()
        conexion.close()
    except mysql.connector.Error as error:
        print(f"Datos no encontrados: {error}")

def obtenerUsuarios(nombre_tabla, referencia)->list:
    try:
        # Conexión a la base de datos
        conexion = conectarse()
        cursor = conexion.cursor()

        # Construcción de la consulta SQL
        consulta = f"SELECT {referencia} FROM {nombre_tabla};"
        
        # Ejecución de la consulta
        cursor.execute(consulta)
        
        # Obtención de los datos
        datos = cursor.fetchall()  # Recupera todas las filas del resultado
        for fila in datos:
            print(fila)  # Aquí puedes procesar o guardar los datos como desees

        # Cierre de la conexión
        cursor.close()
        conexion.close()
    except mysql.connector.Error as error:
        print(f"Datos no encontrados: {error}")

def getPassword(nombre_tabla, referencia, dato)->list:
    try:
        # Conexión a la base de datos
        conexion = conectarse()
        cursor = conexion.cursor()

        # Construcción de la consulta SQL
        consulta = f"SELECT {referencia} FROM {nombre_tabla} WHERE {referencia} = {dato};"
        
        # Ejecución de la consulta
        cursor.execute(consulta)
        
        # Obtención de los datos
        datos = cursor.fetchall()  # Recupera todas las filas del resultado
        for fila in datos:
            print(fila)  # Aquí puedes procesar o guardar los datos como desees

        # Cierre de la conexión
        cursor.close()
        conexion.close()
    except mysql.connector.Error as error:
        print(f"Datos no encontrados: {error}")

def comprobarUsuario(nombre_tabla, dato, referencia)->list:
    try:
        # Conexión a la base de datos
        conexion = conectarse()
        cursor = conexion.cursor()

        # Construcción de la consulta SQL
        consulta = f"SELECT {referencia} FROM {nombre_tabla} WHERE {referencia} = {dato};"
        
        # Ejecución de la consulta
        cursor.execute(consulta)
        
        # Obtención de los datos
        datos = cursor.fetchone()  # Recupera todas las filas del resultado
        for fila in datos:
            print(fila)  # Aquí puedes procesar o guardar los datos como desees

        # Cierre de la conexión
        cursor.close()
        conexion.close()
    except mysql.connector.Error as error:
        print(f"Datos no encontrados: {error}")
#endregion