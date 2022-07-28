
import tkinter  

ventana = tkinter.Tk()
ventana.geometry("500x500")

etiqueta = tkinter.Label(ventana, text = "ZETA", bg = "blue")
#etiqueta.pack(fill = tkinter.X)


boton = tkinter.Button(ventana, text = "Boton",width = 10, height= 5)
boton.grid(row = 2, column = 0)

ventana.mainloop()
