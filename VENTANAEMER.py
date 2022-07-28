from tkinter import *
from tkinter import messagebox  #esta es la libreria para ventanas emergentes

window = Tk()

def InfoAdicional():
    messagebox.showinfo("VENTANA EMERGENTE DE PRUEBA", "THE WINDOW")

def secondwindow():
    messagebox.showwarning("PELIGRO TU PC SE DESTRUIRA EN CINCO MINUTOS", "SO BAD")

def salirapp():
    #valor =messagebox.askquestion("salir", "Deseas salir de la aplicacion?") ---- con esta linea deberiamos asignar if valor == "yes":----
    valor =messagebox.askokcancel("salir", "Deseas salir de la aplicacion?")
    if valor == True:
        window.destroy()

def cerrardocumento():
    valor =messagebox.askretrycancel("reintentar", "No es posible cerrar el documento bloqueado")
    if valor == False:
        window.destroy()

BOTON1 = Button(window, text = "Pulsar para abrir la ventana", command = InfoAdicional )
BOTON1.pack()


BOTON2 = Button(window, text = "abrir la segunda ventana", command =secondwindow )
BOTON2.pack()


BOTON3 = Button(window, text = "salir", command =salirapp )
BOTON3.pack()

BOTON4 = Button(window, text = "reintentar", command = cerrardocumento)
BOTON4.pack()



window.mainloop()