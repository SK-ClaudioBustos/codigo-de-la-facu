from tkinter import *

root = Tk()
root.geometry("400x400")

productos = Label(root,text="Productos")
productos.pack()

def agregar():
    listaP.insert(END,entry.get())

#se crea una lista que contendra elementos que se seleccionaran
listaP = Listbox(root,width=50)
listaP.insert(0,"Carne")
listaP.insert(1,"Pollo")
listaP.insert(2,"Verdura")
listaP.insert(3,"Jugo")
listaP.pack()

entry = Entry(root,bd=10)
entry.pack()

b1 = Button(root,text="Agregar elemento",bd=10,command=agregar)
b1.pack()

root.mainloop()