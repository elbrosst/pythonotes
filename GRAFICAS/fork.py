from tkinter import *


ventana = Tk()

wordonscreen = StringVar()

#--------funciones-----

    
ventana.geometry("700x500")

ventana.title("KARLAS'S APP")
ventana.iconbitmap("favicon.ico")

frame = Frame(ventana)

frame.pack()

frame.place(x = 0, y = 50)

frame.config(width="400", height ="250")

ventana.config(bg = "purple")
web = Label(frame, text = "Sitio web:")
web.pack()
web.grid(row = 0, column = 0)


cuenta = Label(frame, text = "Cuenta:")

cuenta.grid(row = 1, column = 0)


contraseña = Label(frame, text = "Contraseña:")

contraseña.grid(row = 2, column = 0)

textolabel = Label(frame, text = "Comentario")
textolabel.grid(row = 3, column =0, sticky = "n")



texto = Text(frame, width = 15, height = 5,)
texto.grid(row = 3, column = 1)

#-------- repasar-----------------
scroll = Scrollbar(frame, command =texto.yview)
scroll.grid(row = 3, column= 2, sticky = "nsew ")

texto.config(yscrollcommand = scroll.set)
#---------repasar-----------------
cuadroweb = Entry(frame,textvariable = wordonscreen, )
cuadroweb.grid(row = 0, column = 1)

cuadrocuenta = Entry(frame)
cuadrocuenta.grid(row = 1, column = 1)

cuadrocontraseña = Entry(frame)
cuadrocontraseña.grid (row = 2, column = 1 )
cuadrocontraseña.config( show ="^")

#imagen = PhotoImage(file = "devilman.gif")
#Label(ventana, image = imagen).place(x = 50, y = 150 )


#textoenpantalla = Label(raiz, text=)

    

adatos = open("datosdelpograma.txt","w")
l = str(cuadrocuenta)
o = str(cuadrocontraseña)

c = adatos.write(l)
d = adatos.write(o)

adatos.close()

ventana.mainloop()

    
