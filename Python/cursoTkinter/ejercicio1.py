from tkinter import *

root = Tk()
root.title("ejercicio 1")
root.geometry("500x200")

etiqueta1 = Label(root,text="Haz click aqui para saludar --->")
etiqueta1.place(x=30,y=50)
etiqueta2 = Label(root,text="Haz click aqui para minimizar --->")
etiqueta2.place(x=30,y=100)

def saludar():
    print("hola Pelotudo")

boton1 = Button(root,text="Saludar",bg="Red",command=saludar)
boton1.place(x=300,y=50)
boton2 = Button(root,text="Minimizar",command=root.iconify,bg="blue")
boton2.place(x=300,y=100)


root.mainloop()