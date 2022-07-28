from io import open
z = open("archivo.txt","r")
a = z.read()
z.close 
print(a)