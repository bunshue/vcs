import tkinter as tk
from tkinter import Tk, Canvas, NW
from PIL import Image, ImageTk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

tk.Label(text = 'Canvas 測試').pack()

color = "#FF0000"
canvas = tk.Canvas(window, width = 500, height = 150, bg=color)
canvas.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def changeCanvasBgColor():
    red = 255
    green = 128
    blue = 0
    color = "#%02x%02x%02x" % (red, green, blue)
    canvas.config(bg = color)

def drawCanvas():
    print('draw')
    x_st = 0
    y_st = 0
    radius = 50
    for i in range(0, 10):
        canvas.create_oval(x_st + 50 * i, y_st, x_st + 50 * i + radius, y_st + radius, tags = "oval")
        canvas.create_oval(x_st + 50 * i, y_st + 75, x_st + 50 * i + radius, y_st + 75 + radius)

def deleteCanvas():
    print('delete')
    canvas.delete("oval")
    canvas.delete("rect", "oval", "line")

button1 = tk.Button(window, text = '改變Canvas背景色', command = changeCanvasBgColor)
button1.pack()

button2 = tk.Button(window, text = '在 Canvas 上畫一些東西', command = drawCanvas)
button2.pack()

button3 = tk.Button(window, text = '刪除 Canvas 上畫的部分東西', command = deleteCanvas)
button3.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()

