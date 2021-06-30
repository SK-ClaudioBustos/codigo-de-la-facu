from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("RadioButton")
root.resizable(0,0)
#el bg es para establecer un color de fondo
root.config(bg="goldenrod3")
#definimos la funcion con la cual multiplicaremos
def operacion():
    numero = nro.get()
    if opcion.get()==1:
        total = numero * 5
    elif opcion.get()==2:
        total = numero * 10
    elif opcion.get()==3:
        total = numero * 20
    elif opcion.get()==4:
        total = numero * 30
    elif opcion.get()==5:
        total = numero *40
    else:
        total = numero * numero
    print(f"El total es: {str(total)}")

#en esta caso debemos usar un int,por ende usamos IntVar
opcion = IntVar()
nro = IntVar()

eti1 = Label(root,text="Introduzca un numero: ",bg="goldenrod3")
eti1.place(x=20,y=40)
ent1 = Entry(root,bd=7,font="Helvetica 12")
ent1.place(x=160,y=40)

#aca empezaremos creando un radiobutton
x5 = Radiobutton(root,text="x5",value=1,bg="goldenrod3",bd=5,variable=opcion)
x5.place(x=20,y=80)

x10 = Radiobutton(root,text="x10",value=2,bg="goldenrod3",bd=5,variable=opcion)
x10.place(x=70,y=80)

x20 = Radiobutton(root,text="x20",value=3,bg="goldenrod3",bd=5,variable=opcion)
x20.place(x=120,y=80)

x30 = Radiobutton(root,text="x30",value=4,bg="goldenrod3",bd=5,variable=opcion)
x30.place(x=20,y=110)

x40 = Radiobutton(root,text="x40",value=5,bg="goldenrod3",bd=5,variable=opcion)
x40.place(x=70,y=110)

but1 = Button(root,text="Multiplicar valor introducido",command=operacion)
but1.place(x=20,y=140)

root.mainloop()