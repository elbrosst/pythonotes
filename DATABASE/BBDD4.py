import sqlite3

conexion = sqlite3.connect("GESTION DE DATOS B")
cursor = conexion.cursor()

# cursor.execute('''
# CREATE TABLE PRODUCTOS
# (CODIGO_ARTICULO VARCHAR(4),
# NOMBRE_ARTICULO VARCHAR(50),
# PRECIO INTEGER,
# SECCION VARCHAR (20))
# ''')

# pruductos = [
#     ("AR01","ropa",30,"clothes"),
#     ("AR02","zapatos",60,"clothes"),
#     ("AR03","moviles",10,"dispositivos")
# ]

# cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", pruductos)

cursor.execute("UPTADE PRODUCTOS SET PRECIO=40 WHERE NOMBRE_ARTICULO= 'ropa'")


conexion.commit()
conexion.close()