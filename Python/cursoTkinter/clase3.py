import tkinter as tk
from tkinter import ttk
#seteamos la ventana principals
root = tk.Tk()
root.title("tercera clase")
root.geometry("500x300")

#definimos una funcion para mostrar lo seleccionado
def seleccionar(opcion):
    print(opcion)

#creamos 3 botones con distintas opciones
ttk.Button(root,text="Python",command=lambda:seleccionar("Python")).pack()
ttk.Button(root,text="Java",command=lambda:seleccionar("Java")).pack()
ttk.Button(root,text="C++",command=lambda:seleccionar("C++")).pack()

root.mainloop()