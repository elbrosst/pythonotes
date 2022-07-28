from tkinter import *

root = Tk()

BarraMenu = Menu(root)
root.config(menu = BarraMenu)

archivoMenu = Menu(BarraMenu, tearoff = 0)
archivoMenu.add_command(Label = "Abrir")
archivoMenu.add_command(Label = "Guardar")
archivoMenu.add_command(Label = "Editar")
archivoMenu.add_separator()
archivoMenu.add_command(Label = "Cerrar")





archivoEdicion = Menu(BarraMenu)

archivoHerramientas = Menu(BarraMenu)

archivo1ayuda = Menu(BarraMenu)

BarraMenu.add_cascade( Label = "Archivo", menu = archivoMenu  )



ventana.mainloop()