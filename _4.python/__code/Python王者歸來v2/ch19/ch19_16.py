# ch19_16.py
from tkinter import *
import time

tk = Tk()
canvas= Canvas(tk, width=500, height=150)
canvas.pack()
canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
for x in range(0, 80):
    canvas.move(1, 5, 0)        # ID=1 x軸移動5像素, y軸不變
    tk.update()                 # 強制tkinter重繪
    time.sleep(0.05)


