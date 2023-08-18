# ch19_17_1.py
from tkinter import *

tk = Tk()
canvas= Canvas(tk, width=500, height=300)
canvas.pack()
canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
for x in range(0, 80):
    canvas.move(1, 5, 2)        # ID=1 x軸移動5像素, y軸移動2像素
    tk.update()                 # 強制tkinter重繪
    canvas.after(50)


