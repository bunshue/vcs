# ch19_3.py
from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_line(30,30,500,30,265,100,30,30,
                   width=20,joinstyle=ROUND)
canvas.create_line(30,130,500,130,265,200,30,130,
                   width=20,joinstyle=BEVEL)
canvas.create_line(30,230,500,230,265,300,30,230,
                   width=20,joinstyle=MITER)








