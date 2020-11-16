from tkinter import *
from tkinter.messagebox import *

import sqlite3

def root():
    global ventana_login
    global username_en
    global password_en
    numero_dos = 5000
    ventana_login = Tk()
    ventana_login.title("Login Gk")
    ventana_login.geometry("350x320+500+250")

    # img 

    img = PhotoImage(file="/Users/hever/Desktop/login-tk-py/img/userlogin.png")
    img = img.subsample(3,3)
    Label(ventana_login, image=img).pack()

    # Username
    Label(ventana_login, text="Usuario", font="Ubuntu 15").pack()
    username_en = Entry(ventana_login, font="Ubuntu 12", justify="center")
    username_en.pack()

    # Password
    Label(ventana_login, text="Contraseña", font="Ubuntu 15").pack()
    password_en = Entry(ventana_login, show="*", font="Ubuntu 12", justify="center")
    password_en.pack()

    # Button login
    entrar = Button(text="Iniciar sesión", font="Ubuntu 14", command=login)
    entrar.config(activebackground="dark blue")
    entrar.pack()

    ventana_login.mainloop()

def login():
    DB_PATH = "/Users/hever/Desktop/login-tk-py/login.db"

    db = sqlite3.connect(DB_PATH)

    c = db.cursor()

    usuario = username_en.get()
    password = password_en.get()

    print(usuario)
    print(password)

    c.execute("SELECT * FROM usuarios WHERE usuario = ? AND pass = ?", (usuario, password))

    if c.fetchone():
        showinfo(title="Login exitoso", message="Sesión iniciada correctamente")
    else: 
        showerror(title="Ups, algo ha salido mal", message="Usuario o contraseña incorrectos")
        opcion = askretrycancel(title="Reintentar", message="¿Desea reintentar?")
        if opcion == True:
            showinfo(title="Nuevo intento", message="Introduce tus datos correctamente")
        else:
            ventana_login.destroy()

    c.close()

    

if __name__ == "__main__":
    root()
