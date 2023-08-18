# ch19_6.py
from tkinter import *
from random import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
for i in range(50):                 # 隨機繪50個不同位置與大小的矩形
    x1, y1 = randint(1, 640), randint(1, 480)
    x2, y2 = randint(1, 640), randint(1, 480)
    if x1 > x2: x1,x2 = x2,x1       # 確保左上角x座標小於右下角x座標
    if y1 > y2: y1,y2 = y2,y1       # 確保左上角y座標小於右下角y座標
    canvas.create_rectangle(x1, y1, x2, y2)













