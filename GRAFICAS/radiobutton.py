from tkinter import *





def imprimir():
    print(eleccion.get())

ventana = Tk()

eleccion = IntVar()


Label(ventana, text = "Estas listo ?").pack()
Radiobutton(ventana, text = "si", variable = eleccion, value = 1, command = imprimir).pack()
Radiobutton(ventana, text = "no", variable = eleccion, value = 2 ,command = imprimir).pack()

ventana.mainloop()