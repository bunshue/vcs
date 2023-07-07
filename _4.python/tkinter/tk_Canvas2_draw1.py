import tkinter as tk
from tkinter import Tk, Canvas, NW
from tkinter import ttk

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

def drawABar(x, percent, color, title):
    canvas2.create_line(0, height - 10, width, height - 10)
    canvas2.create_rectangle(x, (1 - percent) * (height - 30), x + width / 4.3 - 5, height - 10, fill = color)
    canvas2.create_text((x + x + width / 4.3 - 5) / 2, (1 - percent) * (height - 30) - 10, text = title)

width = 400
height = 200
canvas2 = tk.Canvas(window, bg = "pink", width = width, height = height)
canvas2.pack()

x = 10
drawABar(x, 0.4, "red", "Project -- 20%")
  
x += width / 4.3 - 5 + 10  
drawABar(x, 0.1, "blue", "Quizzes -- 10%")

x += width / 4.3 - 5 + 10  
drawABar(x, 0.3, "green", "Midterm -- 30%")

x += width / 4.3 - 5 + 10  
drawABar(x, 0.4, "orange", "Final -- 40%")

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

width = 750
height = 250
canvas3 = tk.Canvas(window, bg = "pink", width = width, height = height)
canvas3.pack()

#直線
canvas3.create_line(0, 0, 100, 100)
canvas3.create_line(100, 100, 0, 0)
canvas3.create_line(0, 100, 100, 0)
canvas3.create_line(0, 0, 100, 150, fill = 'gray50')
canvas3.create_line(0, 0, 400, 200, fill = "red", dash = (4, 4))

#矩形
x1 = 25
y1 = 125
x2 = x1 + 100
y2 = y1 + 50
canvas3.create_rectangle(x1, y1, x2, y2, fill = 'red')

x1 = 150
y1 = 100
x2 = x1 + 100
y2 = y1 + 100
canvas3.create_rectangle(x1, y1, x2, y2, fill = 'green', outline = 'black', width = 1)

x1 = 275
y1 = 125
x2 = x1 + 100
y2 = y1 + 50
canvas3.create_rectangle(x1, y1, x2, y2, fill = 'blue', width = 6, dash = (4,2,1,1), outline = 'red')


#圓形
cx = 50
cy = 50
radius = 50
canvas3.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, tags = "oval")

cx = 150
cy = 50
canvas3.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, fill = 'green')

x_st = 300
y_st = 0
canvas3.create_polygon((x_st,y_st, x_st+50,y_st+50, x_st+50,y_st+100, x_st,y_st+100), fill = 'gray')

canvas3.create_text(400, 100, text = '寫上文字1', fill = 'red', width = 20)
canvas3.create_text(420, 200, anchor="nw", text = '寫上文字2')

canvas3.create_window(500, 100, window = ttk.Button(window, text= 'this is text in a canvas'))

label1 = tk.Label(window, text = "Blue", bg = "blue").pack()
canvas3.create_window(500, 100, anchor="nw", window = label1)

cx = 400
cy = 0
radius = 100
canvas3.create_arc(
        (cx, cy, cx + radius, cy + radius),
        fill = 'red',
        start = 45,
        extent = 140,
        style = tk.CHORD,
        outline = 'red',
        width = 1)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線



window.mainloop()

