
import sqlite3 
miconexion = sqlite3.connect("BASE DE DATOS 1")  # lo primero es crear una conexion  o conectarse a una usando (sqlite3.connect(""))

cursor = miconexion.cursor() # lo segundo es crear un cursor o puntero para poder escribir en la base de datos

#  cursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO  INTEGER, SECCION VARCHAR(20))") #ESTA LINEA SOLO PUEDE SER EJECUTADA UNA VEZ, SI LA EJECUTAMOS DOS VECES NOS SALTARA UN ERROR, ESO PASA PORQUE EL POGRAMA INTENTARA CREAR OTRA TABLA CON EL MISMO NOMBRE 

#cursor.execute("INSERT INTO PRODUCTOS VALUES ('BALON','50','DEPORTES')")   ---->  # ESTA LINEA NOS SIRVE PARA INSERTAR VALORES A LA TABLA 

# tablavalores = [
#     ("ropa",30,"clothes"),
#     ("zapatos",60,"clothes"),
#     ("moviles",10,"dispositivos")
# ]

# cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?) ",tablavalores)

cursor.execute("SELECT * FROM PRODUCTOS")  # esta linea y la siguiente sirven para obtener los datos que hay dentro de la base

variableramdom = cursor.fetchall() #
print(variableramdom)



miconexion.commit()  # esta linea nos sirve para para confirmar los cambios 
miconexion.close() # lo ultimo es cerrar la conexion para que no nos genere errores 