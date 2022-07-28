from tkinter import *

ventana = Tk()

BarraMenu = Menu(ventana)
ventana.config(menu = BarraMenu)

archivoMenu = Menu(BarraMenu)

archivoEdicion = Menu(BarraMenu)

archivoHerramientas = Menu(BarraMenu)

archivo1ayuda = Menu(BarraMenu)

BarraMenu.add_cascade(Label = "Archivo", menu = BarraMenu)








ventana.mainloop()