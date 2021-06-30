from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x300")

w = Spinbox(root,values=("Python","Java","C++"))
w.pack()

e = Spinbox(root,values=("Carne","Verdura","Pasta"))
e.pack()

root.mainloop()