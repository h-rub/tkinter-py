from tkinter import *

from tkinter import ttk

# Configuración de la ventana
ventana = Tk()
ventana.geometry("300x200")
ventana.configure(bg='beige')
ventana.title("Mi primer ventana")

def mensaje():
    print("Hola mundo")

# Botones

ttk.Button(ventana, text="Mensaje", command=mensaje).pack(side=LEFT)
ttk.Button(ventana, text="Salir", command=quit).pack(side=RIGHT)

entrada_texto = Entry(ventana)
entrada_texto.pack()




ventana.mainloop()

