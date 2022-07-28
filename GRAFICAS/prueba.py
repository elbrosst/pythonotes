from tkinter import * 

m = ""
def zpantalla(x):
    global m
    m = x 

#------ventana-----------
ventana = Tk()
ventana.geometry("700x500")
ventana.resizable(0,0)

#-------frame-------------

frame = Frame()
frame.pack()
frame.config(width = 600, height = 400 )
frame.place(x = 50, y = 25)



#-------Entry--------------
zc = Entry(frame)
zc.grid(row = 0, column = 0, sticky = "n")


#-------Labels------------

cartel = Label(ventana, text = m)
cartel.place(x = 500, y = 400)


#-------button-----------
boton1 = Button(frame,text = "Imprimir en pantalla ", command = print ("zzzz")) #zpantalla(zc.get)

boton1.grid(row = 0,column = 1)


#-------command-------------
ventana.mainloop()