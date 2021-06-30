from tkinter import *

#creamos una ventana general
ventana = Tk()

#creamos una etiqueta que estara en root y tendra el texto "Hola Mundo"
texto = Label(ventana,text="Hola Mundo")

#esto sirve para posicionar la etiqueta
texto.pack()

#con esto hacemos que la ventana no se cierre nunca
ventana.mainloop()