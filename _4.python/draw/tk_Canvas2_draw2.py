import tkinter as tk
from tkinter import Tk, Canvas, NW

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 900
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

width = 750
height = 460
canvas = tk.Canvas(window, bg = "pink", width = width, height = height)
canvas.pack()

#create_text 繪製文字
dx = 50
dy = 10
canvas.create_text(100 + dx,  50 + dy, text = '繪製文字1')
canvas.create_text(100 + dx, 100 + dy, text = '繪製文字2', font = ('Arial', 36))
canvas.create_text(  0 + dx,   0 + dy, text = '繪製文字3', anchor = 'nw')

#create_line 繪製直線
dx = 400
dy = 10
canvas.create_line(20 + dx, 20 + dy, 280 + dx, 20 + dy)
canvas.create_line(20 + dx, 40 + dy, 280 + dx, 40 + dy, dash = (4, 4))
canvas.create_line(20 + dx, 60 + dy, 280 + dx, 60 + dy, width = 5)
canvas.create_line(20 + dx, 80 + dy, 280 + dx, 80 + dy, fill = 'red')

#create_rectangle 繪製矩形
dx = 0
dy = 150
canvas.create_rectangle( 10 + dx, 10 + dy,  90 + dx, 100 + dy)
canvas.create_rectangle(110 + dx, 10 + dy, 190 + dx, 100 + dy, dash = (4, 4))
canvas.create_rectangle(210 + dx, 10 + dy, 290 + dx, 100 + dy, fill = 'red')
canvas.create_rectangle(310 + dx, 10 + dy, 390 + dx, 100 + dy, outline = 'blue')

#create_oval 繪製圓形、橢圓
dx = 400
dy = 150
canvas.create_oval( 10 + dx,  10 + dy, 100 + dx, 100 + dy) # 圓形
canvas.create_oval(110 + dx,  10 + dy, 200 + dx, 100 + dy, fill = 'red') # 圓形
canvas.create_oval(210 + dx,  10 + dy, 300 + dx, 100 + dy, outline = 'blue') # 圓形
canvas.create_oval( 10 + dx, 110 + dy, 290 + dx, 190 + dy) # 橢圓

#create_arc 繪製圓弧
dx = 50
dy = 280
canvas.create_arc( 10 + dx,  10 + dy, 100 + dx, 100 + dy)
canvas.create_arc(110 + dx,  10 + dy, 200 + dx, 100 + dy, extent = 45)
canvas.create_arc(210 + dx,  10 + dy, 300 + dx, 100 + dy, extent = 180)
canvas.create_arc( 10 + dx, 110 + dy, 100 + dx, 210 + dy, style = tk.ARC)
canvas.create_arc(110 + dx, 110 + dy, 200 + dx, 210 + dy, style = tk.PIESLICE)
canvas.create_arc(210 + dx, 110 + dy, 300 + dx, 210 + dy, style = tk.CHORD)

#create_polygon 繪製多邊形
dx = 400
dy = 360
canvas.create_polygon( 40 + dx, 40 + dy,  60 + dx, 20 + dy,  80 + dx, 40 + dy,  80 + dx, 80 + dy,  40 + dx, 80 + dy)
canvas.create_polygon(100 + dx, 40 + dy, 120 + dx, 20 + dy, 140 + dx, 40 + dy, 140 + dx, 80 + dy, 100 + dx, 80 + dy, fill = '', outline = 'black')
canvas.create_polygon(160 + dx, 80 + dy, 200 + dx, 80 + dy, 180 + dx, 20 + dy, fill = 'yellow')
canvas.create_polygon(220 + dx, 80 + dy, 260 + dx, 80 + dy, 240 + dx, 20 + dy, fill = 'red', outline = 'black')



separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()

