from tkinter import *
from tkinter import messagebox

t = Tk()
t.geometry("100x100")

def clique_aqui():
    msg = messagebox.showinfo("Curso de Python", "Seja bem vindo")

btn = Button(t, text = "Click aqui", command = clique_aqui)
btn.place(x=50, y=50)

t.mainloop()