from tkinter import *
import time

#creamos una ventana
root = Tk()
#le seteamos un nombre
root.title = "Mi primera ventana"
#y una resolucion
root.geometry("500x300")
#ahora creamos un boton que minimize la ventana root
boton = Button(root,text="Minimizar",command=root.iconify,bg="Red")
boton.pack(side=LEFT)

#en esta parte definimos un boton que al ser presionado mostrara un etiqueta
def imprimir():
    label1 = Label(root,text="Imprimiendo....")
    label1.pack()
#con bg seteamos el color del boton
boton2 = Button(root,text="Imprimir",command=imprimir,bg="blue")
boton2.pack(side=RIGHT)

root.mainloop()
