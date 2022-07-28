from tkinter import * 

raiz = Tk()

raiz.title("Youtube")
raiz.iconbitmap("youtube.ico")
raiz.config(bg = "blue")
raiz.geometry("650x300")
#raiz.resizable(0,0)
frame = Frame()
frame.pack(side = "top", anchor="n")
frame.config(bg = "white")
frame.config(width="400", height ="250")

frame.config(bd = "5")
frame.place(x = 0, y = 50)
frame.config(relief = "sunken")
frame.config(cursor="pirate")
#image = PhotoImage(file = "ramdomz.png")
milabel = Label(frame,)
milabel.pack()
cuadrotexto = Entry(frame)
cuadrotexto.pack()




raiz.mainloop()