from tkinter import *

root = Tk()
root.title("clase 4")
root.geometry("400x200")

#creo un etiqueta y un boton,luego los ubico con grid
etiqueta = Label(root,text="etiqueta 1")
etiqueta.grid(row=0,column=0)

boton = Button(root,text="boton1")
boton.grid(row=0,column=1)

#una forma alternativa es usando place
boton2 = Button(root,text="boton 2")
boton2.place(x=30,y=50)

root.mainloop()