from funciones import *
"""
while True:
    salir = input("Desea salir? (s/n): ")
    if salir == "s":
        break
"""
crear_tabla(
    "ciudades",
    id_ciudades="INT AUTO_INCREMENT PRIMARY KEY NOT NULL",
    nombre="VARCHAR(100)",
    entidad="VARCHAR(100)"
)