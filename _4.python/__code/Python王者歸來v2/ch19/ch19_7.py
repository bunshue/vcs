# ch19_7.py
from tkinter import *
from random import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_rectangle(10, 10, 120, 60, fill='red')
canvas.create_rectangle(130, 10, 200, 80, fill='yellow', outline='blue')
canvas.create_rectangle(210, 10, 300, 60, fill='green', outline='grey')











