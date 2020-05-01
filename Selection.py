import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image


class interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1366x700")
        self.config(bg="green", bd=25, relief="sunken")
        self.myframe = Frame(self)
        self.myframe.pack()
        self.myframe.config(bg="grey", width=1020, height=700)

        # canvas = tk.Canvas(bg="grey",width=400,height=400)
        # canvas.pack()
        tk.Button(self, text="Start Game", command=self.StartGame, width=16).place(x=950, y=500)
        tk.Button(self, text="Designer",command=self.Designer, width=16).place(x=950, y=550)


    def Designer(self):
        self.destroy()
        exec(open("./Designer.py").read())

    def StartGame(self):  # re center and delete
        self.destroy()
        exec(open("./Player.py").read())


if __name__ == "__main__":
    interfaz().mainloop()