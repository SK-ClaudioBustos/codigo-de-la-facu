from tkinter import *
root = Tk()
root.config(bd=20,bg="goldenrod3")
root.title("Casa de comidas")

#con esta funcion se muestra lo que se selecciono
def orden():
    lista = ""
    if queso.get():
        lista +=" Con queso"
    else:
        lista +=" Sin queso"
    if lechuga.get():
        lista += " con lechuga"
    else:
        lista += " sin lechuga"  
    imprimir.config(text=lista)

#variables que guardan las opciones seleccionadas
queso = IntVar()
lechuga = IntVar()

#creamos una variable que guarde la imagen
imagen = PhotoImage(file="hamburgesa.gif")
#creamos una etiqueta con la imagen
Label(root,image=imagen).pack(side=LEFT)

#creamos un frame o un marco
frame = Frame(root)
frame.pack(side=RIGHT)
frame.config(bg="goldenrod3")

#la w significa west,osea donde se ubicara
Label(frame,text="Como quieres tu hamburguesa?",bg="goldenrod3",font="Curier 15").pack(anchor="w")

#onvalue:valor que toma el check cuando este seleccionado
#offvalue:valor que toma el check cuando no esta seleccionado
Checkbutton(frame,text="Con queso",variable=queso,onvalue=1,offvalue=0,bg="goldenrod3",font="Curier 10",command=orden).pack(anchor="w")
Checkbutton(frame,text="Con lechuga",variable=lechuga,onvalue=1,offvalue =0,bg="goldenrod3",font="Curier 10",command=orden).pack(anchor="w")

#con esto imprimiremos lo que seleccione el usuario
imprimir = Label(frame,bg="goldenrod3")
imprimir.pack()
imprimir.config(font="Calibri 10")

root.mainloop()
