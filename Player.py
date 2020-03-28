import tkinter as tk
from tkinter import filedialog
from tkinter import *
from Building import building
from PIL import ImageTk,Image


root = tk.Tk()  # lib kinter

root.title("Game")
root.geometry("1024x700")  # Width x Height

canva = tk.Canvas(root, width=1024, height=650)
canva.config(bg="red")
canva.pack()