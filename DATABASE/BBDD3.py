import sqlite3

conexion = sqlite3.connect("GESTION_DE_DATOS")
cursor = conexion.cursor()

 cursor.execute('''
    CREATE TABLE PRUDUCTOSSS (
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER ,
    SECCION VARCHAR(20))
''')
tablavalores = [
    ("AR01","ropa",30,"clothes"),
    ("AR02","zapatos",60,"clothes"),
    ("AR03","moviles",10,"dispositivos")
 ]


cursor.executemany("INSERT INTO PRUDUCTOSSS  VALUES (?,?,?,?)", tablavalores)
conexion.commit()
conexion.close()