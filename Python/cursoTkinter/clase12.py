from tkinter import Tk,Text

root = Tk()
root.resizable(False,False)
root.geometry("400x400")
root.title("Bloc de notas")

text = Text(root,height=8)
text.pack()
#1.0 es para indicarle un tamaño
text.insert("1.0","Esto es un ejemplo de bloc de notas")

root.mainloop()