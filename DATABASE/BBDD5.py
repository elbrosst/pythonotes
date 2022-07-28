import sqlite3

conexion = sqlite3.connect("GESTION DE DATOS C")
cursor = conexion.cursor()

# cursor.execute('''
# CREATE TABLE PRODUCTOS
# ( ID INTEGER PRIMARY KEY AUTOINCREMENT ,  
# NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
# PRECIO INTEGER,
# SECCION VARCHAR (20))
# ''')
# En la linea 8 le decimos al pograma que cree una tabla con un campo clave poniendo el nombre ID<-- para hacer referencia a que sera un campo clavo que clasifique los objetos, INTEGER<-- PARA SELECCIONAR QUE VAN NUMEROS ES COMO EL INT EN PYTHON, PRIMARY KEY<--- PARA ASIGNARLO COMO UN CAMPO CLAVE, AUTOINCREMENT<--- PARA QUE SE AUTOINCREMENTE 
# En la linea 9 el comando UNIQUE sirve para decirle al pograma que en ese campo no puede haber nombres repetidos
# pruductos = [
#     ("ropa",30,"clothes"),
#     ("zapatos",60,"clothes"),
#     ("moviles",10,"dispositivos")
# ]

#cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", pruductos)



#cursor.execute("SELECT * FROM PRODCUTOS WHERE SECCION = 'clothes'")

cursor.execute("UPTADE PRODUCTOS SET PRECIO= 40 WHERE NOMBRE_ARTICULO = 'ropa")



conexion.commit()
conexion.close()


