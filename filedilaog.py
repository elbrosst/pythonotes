from tkinter import *
from tkinter import filedialog

root = Tk()

def abrirfichero():
    archivo = filedialog.askopenfilename( title =  "Abrirzzzz", initialdir = "C:", filetypes= (("Ficheros de texto","*.txt"), ("Ficheros de excel", "*.xlsx"), ("Todos los archivos", "*.*")))
    print(archivo)

def salir():
    root.destroy()

boton = Button(root, text = "Abrir archivo", command = abrirfichero)
boton.pack() 
botonsalir = Button(root, text = "salir", command = salir )
botonsalir.pack()

root.mainloop()