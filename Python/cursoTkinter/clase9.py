from tkinter import *
from tkinter import messagebox
root = Tk()
#configuramos un menu en nuestro root
menuBar = Menu(root)
root.config(menu=menuBar)

#en este apartado creamos las funciones que tendran los botones del menus
def cerrar():
    messagebox.askquestion("Cerrar",message="¿Estas seguro?")

def version():
    messagebox.showinfo("Version",message="Version 1.0")

def error():
    messagebox.showerror("Error critico",message="Se encontro un error fatal")

def advertencia():
    messagebox.showwarning("Advertencia",message="Se borrara el actual")

#creamos un submenu que se llamara Archivo y su contenido sera nuevo,abrir,guardar,cerrar,salir
archivoMenu = Menu(menuBar,tearoff=0)
archivoMenu.add_command(label = "Nuevo")
archivoMenu.add_command(label = "Abrir",command=advertencia)
archivoMenu.add_command(label = "Guardar",command=error)
archivoMenu.add_command(label = "Cerrar",command=cerrar)
#esto es simplemente un separador
archivoMenu.add_separator()
archivoMenu.add_command(label = "Salir",command=root.quit)

#se crea otro submenu llamado Editar
editMenu = Menu(menuBar,tearoff=0)
editMenu.add_command(label="Cortar")
editMenu.add_command(label="Copiar")
editMenu.add_command(label="Pegar")

#otro submenu llamado Ayuda
ayudaMenu = Menu(menuBar,tearoff=0)
ayudaMenu.add_command(label="Version",command=version)
ayudaMenu.add_command(label="Ayuda")

#se agrega los submenues al menu central
menuBar.add_cascade(label="Archivo",menu=archivoMenu)
menuBar.add_cascade(label="Editar",menu=editMenu)
menuBar.add_cascade(label="Ayuda",menu=ayudaMenu)

root.mainloop()