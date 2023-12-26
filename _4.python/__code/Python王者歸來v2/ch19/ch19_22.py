# ch19_22.py
from tkinter import *

tk = Tk()
canvas= Canvas(tk, width=500, height=150)
canvas.pack()
id = canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
ballPos = canvas.coords(id)
print(ballPos)


