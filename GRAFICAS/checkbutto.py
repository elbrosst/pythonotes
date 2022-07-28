from tkinter import * 
ventana = Tk()
ventana.title("Checkbutton")

foto= PhotoImage(file="zzz.png")
Label(ventana, image= foto).pack()


opcion1 = IntVar()
opcion2 = IntVar()
opcion3 = IntVar()



def seleccion():

    opcionescogida = ""
    if (opcion1.get()==1):
        opcionescogida += "opcion1"

    if (opcion2.get()==1):
        opcionescogida += "opcion2"

    if (opcion3.get()==1):
        opcionescogida += "opcion3"

    twxtf.config(text = labelfinal)

frame=Frame(ventana)
frame.pack()

Label(frame,text = "Elige una opcion", width = 50).pack() 


Checkbutton(ventana, text = "Opcion 1 ", variable = opcion1, onvalue = 1, offvalue = 0,command = seleccion).pack()
Checkbutton(ventana, text = "Opcion 2 ", variable = opcion2, onvalue = 1, offvalue = 0,command = seleccion).pack()
Checkbutton(ventana, text = "Opcion 3 ", variable = opcion3, onvalue = 1, offvalue = 0,command = seleccion).pack()




ventana.mainloop()