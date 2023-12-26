# ch19_11.py
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_polygon(10,10, 100,10, 50,80, fill='', outline='black')
canvas.create_polygon(120,10, 180,30, 250,100, 200,90, 130,80)
canvas.create_polygon(200,10, 350,30, 420,70, 360,90, fill='aqua')
canvas.create_polygon(400,10,600,10,450,80,width=5,outline='blue',fill='yellow')





