# ch19_5.py
from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_line(30,30,500,30,width=10,stipple="gray25")
canvas.create_line(30,130,500,130,width=40,stipple="questhead")
canvas.create_line(30,230,500,230,width=10,stipple="info")









