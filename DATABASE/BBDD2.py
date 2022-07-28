import sqlite3
conexion = sqlite3.connect("BASE DE DATOS 2")
cursor = conexion.cursor()

cursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO  VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR (20))")

cursor.execute("INSERT INTO PRODUCTOS VALUES ('RAMDOM1','50','DEPORTES')")

conexion.commit()

conexion.close()
