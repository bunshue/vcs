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

width = 780
height = 780
canvas1 = tk.Canvas(window, bg = "pink", width = width, height = height)
canvas1.pack()

#create_line 繪製直線 (x1, y1)-(x2, y2)
x1, y1, x2, y2 = 20, 20, 120, 20
canvas1.create_line(x1, y1, x2, y2)
x1, y1, x2, y2 = x1, y1+20, x2, y2+20
canvas1.create_line(x1, y1, x2, y2, fill = 'gray50')
x1, y1, x2, y2 = x1, y1+20, x2, y2+20
canvas1.create_line(x1, y1, x2, y2, fill = "red", dash = (4, 4))
x1, y1, x2, y2 = x1, y1+20, x2, y2+20
canvas1.create_line(x1, y1, x2, y2, width = 5)
x1, y1, x2, y2 = x1, y1+20, x2, y2+20
canvas1.create_line(x1, y1, x2, y2,width = 10, fill = 'blue')
x1, y1, x2, y2 = x1, y1+20, x2, y2+20
canvas1.create_line(x1, y1, x2, y2,dash=(10,2,2,2))
x1, y1, x2, y2 = x1, y1+20, x2, y2+20
canvas1.create_line(x1, y1, x2, y2,fill='#FF0000')                     
"""
x1, y1, x2, y2, x3, y3, x1, y1 = 30,30,500,30,265,100,30,30
canvas1.create_line(x1, y1, x2, y2, x3, y3, x1, y1,width=5,joinstyle=tk.ROUND)
x1, y1, x2, y2, x3, y3, x1, y1 = 30,130,500,130,265,200,30,130
canvas1.create_line(x1, y1, x2, y2, x3, y3, x1, y1,width=5,joinstyle=tk.BEVEL)
x1, y1, x2, y2, x3, y3, x1, y1 = 30,230,500,230,265,300,30,230
canvas1.create_line(x1, y1, x2, y2, x3, y3, x1, y1,width=5,joinstyle=tk.MITER)

x1, y1, x2, y2 = 230,30,500,30
canvas1.create_line(x1, y1, x2, y2,width=5,capstyle=tk.BUTT)
x1, y1, x2, y2 = 230,130,500,130
canvas1.create_line(x1, y1, x2, y2,width=5,capstyle=tk.ROUND)
x1, y1, x2, y2 = 230,230,500,230
canvas1.create_line(x1, y1, x2, y2,width=5,capstyle=tk.PROJECTING)

x1, y1, x2, y2 = 230,30,500,30
canvas1.create_line(x1, y1, x2, y2,width=5,stipple="gray25")
x1, y1, x2, y2 = 230,130,500,130
canvas1.create_line(x1, y1, x2, y2,width=5,stipple="questhead")
x1, y1, x2, y2 = 30,230,500,230
canvas1.create_line(x1, y1, x2, y2,width=5,stipple="info")
"""
#create_rectangle 繪製矩形
x_st, y_st, x_sp, y_sp = 220, 20, 320, 70
dy = 60
canvas1.create_rectangle(x_st, y_st, x_sp, y_sp)#無參數, 空心1點, 黑線
x_st, y_st, x_sp, y_sp = x_st, y_st+dy, x_sp, y_sp+dy
canvas1.create_rectangle(x_st, y_st, x_sp, y_sp, dash = (4, 4))#虛線
x_st, y_st, x_sp, y_sp = x_st, y_st+dy, x_sp, y_sp+dy
canvas1.create_rectangle(x_st, y_st, x_sp, y_sp, outline = 'red')#外框線紅色
x_st, y_st, x_sp, y_sp = x_st, y_st+dy, x_sp, y_sp+dy
canvas1.create_rectangle(x_st, y_st, x_sp, y_sp, fill = 'red')#實心
#canvas1.create_rectangle(x_st, y_st, x_sp, y_sp, fill='#FF0000')#實心
x_st, y_st, x_sp, y_sp = x_st, y_st+dy, x_sp, y_sp+dy
canvas1.create_rectangle(x_st, y_st, x_sp, y_sp, fill = 'green', outline = 'red', width = 5)
x_st, y_st, x_sp, y_sp = x_st, y_st+dy, x_sp, y_sp+dy
canvas1.create_rectangle(x_st, y_st, x_sp, y_sp, fill = 'blue', width = 6, dash = (4,2,1,1), outline = 'red')


#create_oval 繪製圓形、橢圓

#圓形
cx, cy = 400, 50
radius = 30
dy = 60

canvas1.create_oval(cx - radius, cy - radius, cx + radius, cy + radius) #無參數, 空心1點, 黑線
cx, cy = cx, cy + dy
canvas1.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, tags = "oval")#多了tags參數
cx, cy = cx, cy + dy
canvas1.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, fill = 'green')#實心圓, 黑色外框1點
cx, cy = cx, cy + dy
canvas1.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, outline = 'red') #外框線紅色
cx, cy = cx, cy + dy

#橢圓形

x_st, y_st, x_sp, y_sp = 0, 150, 200, 250#左上-右下
canvas1.create_oval(x_st, y_st, x_sp, y_sp) # 橢圓
x_st, y_st, x_sp, y_sp = 0, 150+100, 200, 250+100#左上-右下
canvas1.create_oval(x_st, y_st, x_sp, y_sp, fill='aqua', outline='blue', width=5)


#create_polygon 繪製多邊形
dx = 400
dy = 100
canvas1.create_polygon( 40 + dx, 40 + dy,  60 + dx, 20 + dy,  80 + dx, 40 + dy,  80 + dx, 80 + dy,  40 + dx, 80 + dy)
canvas1.create_polygon(100 + dx, 40 + dy, 120 + dx, 20 + dy, 140 + dx, 40 + dy, 140 + dx, 80 + dy, 100 + dx, 80 + dy, fill = '', outline = 'black')
canvas1.create_polygon(160 + dx, 80 + dy, 200 + dx, 80 + dy, 180 + dx, 20 + dy, fill = 'yellow')
canvas1.create_polygon(220 + dx, 80 + dy, 260 + dx, 80 + dy, 240 + dx, 20 + dy, fill = 'red', outline = 'black')

x_st = 500
y_st = 0
canvas1.create_polygon((x_st,y_st, x_st+50,y_st+50, x_st+50,y_st+100, x_st,y_st+100), fill = 'gray')

#canvas1.create_polygon(10,10, 100,10, 50,80, fill='', outline='black')
#canvas1.create_polygon(120,10, 180,30, 250,100, 200,90, 130,80)
#canvas1.create_polygon(200,10, 350,30, 420,70, 360,90, fill='aqua')
#canvas1.create_polygon(400,10,600,10,450,80,width=5,outline='blue',fill='yellow')


"""
#create_arc 繪製圓弧

cx = 400
cy = 0
radius = 100
canvas1.create_arc(
        (cx, cy, cx + radius, cy + radius),
        fill = 'red',
        start = 45,
        extent = 140,
        style = tk.CHORD,
        outline = 'red',
        width = 1)


dx = 50
dy = 280
canvas1.create_arc( 10 + dx,  10 + dy, 100 + dx, 100 + dy)
canvas1.create_arc(110 + dx,  10 + dy, 200 + dx, 100 + dy, extent = 45)
canvas1.create_arc(210 + dx,  10 + dy, 300 + dx, 100 + dy, extent = 180)
canvas1.create_arc( 10 + dx, 110 + dy, 100 + dx, 210 + dy, style = tk.ARC)
canvas1.create_arc(110 + dx, 110 + dy, 200 + dx, 210 + dy, style = tk.PIESLICE)
canvas1.create_arc(210 + dx, 110 + dy, 300 + dx, 210 + dy, style = tk.CHORD)

# 以下以圓形為基礎
canvas1.create_arc(10, 10, 110, 110, extent=45, style=tk.ARC)
canvas1.create_arc(210, 10, 310, 110, extent=90, style=tk.ARC)
canvas1.create_arc(410, 10, 510, 110, extent=180, fill='yellow')
canvas1.create_arc(10, 110, 110, 210, extent=270, style=tk.ARC)
canvas1.create_arc(210, 110, 310, 210, extent=359, style=tk.ARC, width=5)
# 以下以橢圓形為基礎
canvas1.create_arc(10, 250, 310, 350, extent=90, style=tk.ARC, start=90)
canvas1.create_arc(320, 250, 620, 350, extent=180, style=tk.ARC)
canvas1.create_arc(10, 360, 310, 460, extent=270, style=tk.ARC, outline='blue')
canvas1.create_arc(320, 360, 620, 460, extent=359, style=tk.ARC)


# 以下以圓形為基礎
canvas1.create_arc(10, 10, 110, 110, extent=180, style=tk.ARC)
canvas1.create_arc(210, 10, 310, 110, extent=180, style=tk.CHORD)
canvas1.create_arc(410, 10, 510, 110, start=30, extent=120, style=tk.PIESLICE)

"""


#create_text 繪製文字

x_st, y_st = 550, 200
dy = 40
canvas1.create_text(x_st, y_st, text = "繪製文字1")#無參數
x_st, y_st = x_st, y_st+dy
canvas1.create_text(x_st, y_st, text = '寫上文字1', fill = 'red', width = 20)
x_st, y_st = x_st, y_st+dy
canvas1.create_text(x_st, y_st, text = '寫上文字2', anchor="nw")

x_st, y_st = x_st, y_st+dy
canvas1.create_text(x_st, y_st, text='Ming-Chi Institute of Technology', fill='blue')
x_st, y_st = x_st, y_st+dy
canvas1.create_text(x_st, y_st, text='Ming-Chi Institute of Technology', fill='blue',
                   font=('Old English Text MT',20))
x_st, y_st = x_st, y_st+dy
canvas1.create_text(x_st, y_st, text='Ming-Chi Institute of Technology', fill='blue',
                   font=('華康新綜藝體 Std W7',20))
x_st, y_st = x_st, y_st+dy
canvas1.create_text(x_st, y_st, text='明志科技大學', fill='blue',
                   font=('華康新綜藝體 Std W7',20))

x_st, y_st = x_st, y_st+dy
canvas1.create_text(x_st, y_st, text = '繪製文字2', font = ('Arial', 36))


"""
canvas1.create_window(500, 100, window = ttk.Button(window, text= 'this is text in a canvas'))

label1 = tk.Label(window, text = "Blue", bg = "blue").pack()
canvas1.create_window(500, 100, anchor="nw", window = label1)

"""
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


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()

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
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
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
win.mainloop()


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


print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_2.py

from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_line(100,100,500,100)
canvas.create_line(100,125,500,125,width=5)
canvas.create_line(100,150,500,150,width=10,fill='blue')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_3.py

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

print("------------------------------------------------------------")  # 60個

from tkinter import *
from random import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_rectangle(10, 10, 120, 60, fill='red')
canvas.create_rectangle(130, 10, 200, 80, fill='yellow', outline='blue')
canvas.create_rectangle(210, 10, 300, 60, fill='green', outline='grey')




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


print("------------------------------------------------------------")  # 60個

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_polygon(10,10, 100,10, 50,80, fill='', outline='black')
canvas.create_polygon(120,10, 180,30, 250,100, 200,90, 130,80)
canvas.create_polygon(200,10, 350,30, 420,70, 360,90, fill='aqua')
canvas.create_polygon(400,10,600,10,450,80,width=5,outline='blue',fill='yellow')




print("------------------------------------------------------------")  # 60個

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
#canvas = Canvas(tk, width=640, height=240, bg='yellow')
canvas.pack()

canvas.create_text(200, 50, text='Ming-Chi Institute of Technology')
canvas.create_text(200, 80, text='Ming-Chi Institute of Technology', fill='blue')
canvas.create_text(300, 120, text='Ming-Chi Institute of Technology', fill='blue',
                   font=('Old English Text MT',20))
canvas.create_text(300, 160, text='Ming-Chi Institute of Technology', fill='blue',
                   font=('華康新綜藝體 Std W7',20))
canvas.create_text(300, 200, text='明志科技大學', fill='blue',
                   font=('華康新綜藝體 Std W7',20))



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個






