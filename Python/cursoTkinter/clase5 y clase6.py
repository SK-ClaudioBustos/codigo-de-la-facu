from tkinter import *

root = Tk()
root.title("Entrada")
root.geometry("400x300")
#esto se usa para que el usuario no modifique el aspecto de la pantalla
root.resizable(0,0)
#lo que creamos aca son variables que guardaran los valores intruducidos en los entrys
nombre = StringVar()
apellido = StringVar()
saludo = StringVar()

#en esta parte seteamos que aparece sobre las entrys
nombre.set("Escribe aqui tu nombre")
apellido.set("Escribe aqui tu apellido")

#esta funcion representa la funcion que hara el boton
def saludar():
    saludo.set("Hola " + nombre.get() + " " + apellido.get())
#con bg elejimos el color del label,con bd el ancho del borde del label,con font elejimos la fuente y el tamaño de la misma
etiqueta1 = Label(root,text="Introduce tu nombre: ",bd=4,bg="blue",font=("Curier 10"))
etiqueta1.place(x=10,y=10)
entry1 = Entry(root,textvariable=nombre,bd=5)
entry1.place(x=170,y=10)

etiqueta2 = Label(root,text="Introduce tu apellido: ",bd=4,bg="green",font=("Curier 10"))
etiqueta2.place(x=10,y=40)
entry2 = Entry(root,textvariable=apellido,bd=5)
entry2.place(x=170,y=40)

boton1 = Button(root,text="Saludar Ahora",bg="red",command=saludar,bd=6)
boton1.place(x=190,y=123)
#con state le decimos que el texto que aparece en la entry no es modificable,tomar nota que no se aplica el color elegido 
#con el parametro state activado
entry3 = Entry(root,bd=20,textvariable=saludo,state="disable",bg="yellow")
entry3.place(x=130,y=220)

root.mainloop()