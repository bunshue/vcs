import sys

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個


from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_line(100,100,500,100)
canvas.create_line(100,125,500,125,width=5)
canvas.create_line(100,150,500,150,width=10,fill='blue')
canvas.create_line(100,175,500,175,dash=(10,2,2,2))

mainloop()

print("------------------------------------------------------------")  # 60個

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

mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_line(30,30,500,30,width=10,capstyle=BUTT)
canvas.create_line(30,130,500,130,width=10,capstyle=ROUND)
canvas.create_line(30,230,500,230,width=10,capstyle=PROJECTING)
# 以下垂直線
canvas.create_line(30,20,30,240)
canvas.create_line(500,20,500,250)

mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_line(30,30,500,30,width=10,stipple="gray25")
canvas.create_line(30,130,500,130,width=40,stipple="questhead")
canvas.create_line(30,230,500,230,width=10,stipple="info")

mainloop()

print("------------------------------------------------------------")  # 60個

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

mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *
from random import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_rectangle(10, 10, 120, 60, fill='red')
canvas.create_rectangle(130, 10, 200, 80, fill='yellow', outline='blue')
canvas.create_rectangle(210, 10, 300, 60, fill='green', outline='grey')

mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
# 以下以圓形為基礎
canvas.create_arc(10, 10, 110, 110, extent=45, style=ARC)
canvas.create_arc(210, 10, 310, 110, extent=90, style=ARC)
canvas.create_arc(410, 10, 510, 110, extent=180, fill='yellow')
canvas.create_arc(10, 110, 110, 210, extent=270, style=ARC)
canvas.create_arc(210, 110, 310, 210, extent=359, style=ARC, width=5)
# 以下以橢圓形為基礎
canvas.create_arc(10, 250, 310, 350, extent=90, style=ARC, start=90)
canvas.create_arc(320, 250, 620, 350, extent=180, style=ARC)
canvas.create_arc(10, 360, 310, 460, extent=270, style=ARC, outline='blue')
canvas.create_arc(320, 360, 620, 460, extent=359, style=ARC)

mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
# 以下以圓形為基礎
canvas.create_arc(10, 10, 110, 110, extent=180, style=ARC)
canvas.create_arc(210, 10, 310, 110, extent=180, style=CHORD)
canvas.create_arc(410, 10, 510, 110, start=30, extent=120, style=PIESLICE)

mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
# 以下是圓形
canvas.create_oval(10, 10, 110, 110)
canvas.create_oval(150, 10, 300, 160, fill='yellow')
# 以下是橢圓形
canvas.create_oval(10, 200, 310, 350)
canvas.create_oval(350, 200, 550, 300, fill='aqua', outline='blue', width=5)

mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_polygon(10,10, 100,10, 50,80, fill='', outline='black')
canvas.create_polygon(120,10, 180,30, 250,100, 200,90, 130,80)
canvas.create_polygon(200,10, 350,30, 420,70, 360,90, fill='aqua')
canvas.create_polygon(400,10,600,10,450,80,width=5,outline='blue',fill='yellow')

mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_text(200, 50, text='Ming-Chi Institute of Technology')
canvas.create_text(200, 80, text='Ming-Chi Institute of Technology', fill='blue')
canvas.create_text(300, 120, text='Ming-Chi Institute of Technology', fill='blue',
                   font=('Old English Text MT',20))
canvas.create_text(300, 160, text='Ming-Chi Institute of Technology', fill='blue',
                   font=('華康新綜藝體 Std W7',20))
canvas.create_text(300, 200, text='明志科技大學', fill='blue',
                   font=('華康新綜藝體 Std W7',20))

mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=240, bg='yellow')
canvas.pack()

mainloop()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

from tkinter import *
from PIL import Image, ImageTk

tk = Tk()
img = Image.open(filename)
rushMore = ImageTk.PhotoImage(img)

canvas = Canvas(tk, width=img.size[0]+40,
                height=img.size[1]+30)
canvas.create_image(20,15,anchor=NW,image=rushMore)
canvas.pack(fill=BOTH,expand=True)

mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *

tk = Tk()
canvas= Canvas(tk, width=500, height=150)
canvas.pack()
id = canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
ballPos = canvas.coords(id)
print(ballPos)

mainloop()

print("------------------------------------------------------------")  # 60個


from tkinter import *
# 依據特定階級數繪製Sierpinski三角形
def sierpinski(order, p1, p2, p3):
    if order == 0:      # 階級數為0
        # 將3個點連接繪製成三角形
        drawLine(p1, p2)
        drawLine(p2, p3)
        drawLine(p3, p1)
    else:
        # 取得三角形各邊長的中點
        p12 = midpoint(p1, p2)
        p23 = midpoint(p2, p3)
        p31 = midpoint(p3, p1)
        # 遞迴呼叫處理繪製三角形
        sierpinski(order - 1, p1, p12, p31)
        sierpinski(order - 1, p12, p2, p23)
        sierpinski(order - 1, p31, p23, p3)   
# 繪製p1和p2之間的線條
def drawLine(p1,p2):
    canvas.create_line(p1[0],p1[1],p2[0],p2[1],tags="myline")
# 傳回2點的中間值
def midpoint(p1, p2):
    p = [0,0]                                   # 初值設定
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p
# 顯示
def show():
    canvas.delete("myline")
    p1 = [200, 20]
    p2 = [20, 380]
    p3 = [380,380]
    sierpinski(order.get(), p1, p2, p3)
    
# main
tk = Tk()
canvas = Canvas(tk, width=400, height=400)      # 建立畫布
canvas.pack()

frame1 = Frame(tk)                              # 建立框架
frame1.pack(padx=5, pady=5)
# 在框架Frame內建立標籤Label, 輸入階乘數Entry, 按鈕Button
Label(frame1, text="輸入階數 : ").pack(side=LEFT)
order = IntVar()
order.set(0)
entry = Entry(frame1, textvariable=order).pack(side=LEFT,padx=3)
Button(frame1, text="顯示Sierpinski三角形",
       command=show).pack(side=LEFT)

tk.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *

tk = Tk()
canvas= Canvas(tk, width=500, height=150)
canvas.pack()
id = canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
ballPos = canvas.coords(id)
print(ballPos)

print("------------------------------------------------------------")  # 60個

from tkinter import *
# 依據特定階級數繪製Sierpinski三角形
def sierpinski(order, p1, p2, p3):
    if order == 0:      # 階級數為0
        # 將3個點連接繪製成三角形
        drawLine(p1, p2)
        drawLine(p2, p3)
        drawLine(p3, p1)
    else:
        # 取得三角形各邊長的中點
        p12 = midpoint(p1, p2)
        p23 = midpoint(p2, p3)
        p31 = midpoint(p3, p1)
        # 遞迴呼叫處理繪製三角形
        sierpinski(order - 1, p1, p12, p31)
        sierpinski(order - 1, p12, p2, p23)
        sierpinski(order - 1, p31, p23, p3)   
# 繪製p1和p2之間的線條
def drawLine(p1,p2):
    canvas.create_line(p1[0],p1[1],p2[0],p2[1],tags="myline")
# 傳回2點的中間值
def midpoint(p1, p2):
    p = [0,0]                                   # 初值設定
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p
# 顯示
def show():
    canvas.delete("myline")
    p1 = [200, 20]
    p2 = [20, 380]
    p3 = [380,380]
    sierpinski(order.get(), p1, p2, p3)
    
# main
tk = Tk()
canvas = Canvas(tk, width=400, height=400)      # 建立畫布
canvas.pack()

frame = Frame(tk)                               # 建立框架
frame.pack(padx=5, pady=5)
# 在框架Frame內建立標籤Label, 輸入階乘數Entry, 按鈕Button
Label(frame, text="輸入階數 : ").pack(side=LEFT)
order = IntVar()
order.set(0)
entry = Entry(frame, textvariable=order).pack(side=LEFT,padx=3)
Button(frame, text="顯示Sierpinski三角形",
       command=show).pack(side=LEFT)

tk.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
x_center, y_center, r = 320, 240, 100
x, y = [], []
for i in range(12):         # 建立圓外圍12個點
    x.append(x_center + r * math.cos(30*i*math.pi/180))
    y.append(y_center + r * math.sin(30*i*math.pi/180))
for i in range(12):         # 執行12個點彼此連線
    for j in range(12):
        canvas.create_line(x[i],y[i],x[j],y[j])

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_4.python/_data/lena_color.png'

import tkinter as tk
import tkinter.font as tkfont
win = tk.Tk()
win.geometry("400x300")
win.title("圖形顯示")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
photo = tk.PhotoImage(file=filename)
gs = tk.Canvas(win)
gs.create_image(60,120,image=photo)
gs.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter as tk
import tkinter.font as tkfont
win = tk.Tk()
win.geometry("400x300")
win.title("幾何圖形")
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
photo = tk.PhotoImage(file=filename)
gs = tk.Canvas(win,width=400,height=300)
gs.pack()
gs.create_rectangle(50,20,150,80)
gs.create_rectangle(80,60,200,100,fill='#FF0000')
gs.create_line(200,200,220,200)
gs.create_line(200,160,320,160,fill='#FF0000')                     
win.mainloop()


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


