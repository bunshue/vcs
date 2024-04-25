import sys

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print("------------------------------------------------------------")  # 60個

import tkinter as tk
from tkinter import Tk, Canvas, NW
from tkinter import ttk

window = tk.Tk()

# 設定主視窗大小
W = 1000
H = 800
x_st = 900
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

width = 980
height = 780
canvas1 = tk.Canvas(window, bg = "pink", width = width, height = height)
canvas1.pack()

canvas1.create_line(0, H//2, W, H//2)
canvas1.create_line(W//2, 0, W//2, H)


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
x_st, y_st, x_sp, y_sp = 150, 20, 250, 70
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
cx, cy = 320, 50
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
x_st, y_st, x_sp, y_sp = 400, 20, 500, 80#左上-右下
canvas1.create_oval(x_st, y_st, x_sp, y_sp) # 橢圓

x_st, y_st, x_sp, y_sp = x_st, y_st+100, x_sp, y_sp+100#左上-右下
canvas1.create_oval(x_st, y_st, x_sp, y_sp, fill='aqua', outline='blue', width=5)

#create_arc 繪製圓弧
#圓之左上-右下
x_st, y_st, x_sp, y_sp = 1000//2, 0, 1000//2 + 100, 0 + 100#左上-右下

start, extent = 45, 180#起始45度, 掃描180度
canvas1.create_arc(
        (x_st, y_st, x_sp, y_sp),
        fill = 'red',
        start = start,
        extent = extent,
        style = tk.CHORD,
        outline = 'green',
        width = 5)

"""
style
style = tk.PIESLICE  # 派形
style = tk.ARC  # 僅弧線
style = tk.CHORD  # 弓形
"""

diameter = 100
dx = 100
dy = 80
x_st, y_st, x_sp, y_sp = 1000//2, 120, 1000//2 + diameter, 120 + diameter#左上-右下
canvas1.create_arc(x_st, y_st, x_sp, y_sp)#無參數 空心1點黑線0~90度
x_st, y_st, x_sp, y_sp = x_st+dx, y_st, x_sp+dx, y_sp

canvas1.create_arc(x_st, y_st, x_sp, y_sp, style = tk.ARC)#僅弧線
x_st, y_st, x_sp, y_sp = x_st+dx, y_st, x_sp+dx, y_sp
canvas1.create_arc(x_st, y_st, x_sp, y_sp, style = tk.PIESLICE)#派形
x_st, y_st, x_sp, y_sp = x_st+dx, y_st, x_sp+dx, y_sp
canvas1.create_arc(x_st, y_st, x_sp, y_sp, style = tk.CHORD)#弓形

x_st, y_st, x_sp, y_sp = 1000//2, 120+dy, 1000//2 + diameter, 120 + diameter+dy#左上-右下
canvas1.create_arc(x_st, y_st, x_sp, y_sp, extent=180, fill='yellow')
x_st, y_st, x_sp, y_sp = x_st+dx, y_st, x_sp+dx, y_sp
canvas1.create_arc(x_st, y_st, x_sp, y_sp, extent=180, style=tk.ARC, width=5)


#create_polygon 繪製多邊形
dx = 1000//2
dy = 800//2
canvas1.create_polygon( 40 + dx, 40 + dy,  60 + dx, 20 + dy,  80 + dx, 40 + dy,  80 + dx, 80 + dy,  40 + dx, 80 + dy)#無參數, 黑色實心
#空心 外框線
canvas1.create_polygon(100 + dx, 40 + dy, 120 + dx, 20 + dy, 140 + dx, 40 + dy, 140 + dx, 80 + dy, 100 + dx, 80 + dy, fill = '', outline = 'red')
#實心
canvas1.create_polygon(160 + dx, 80 + dy, 200 + dx, 80 + dy, 180 + dx, 20 + dy, fill = 'green')
#實心 外框線
canvas1.create_polygon(220 + dx, 80 + dy, 260 + dx, 80 + dy, 240 + dx, 20 + dy, fill = 'blue', outline = 'yellow', width=5)


#create_text 繪製文字

x_st, y_st = W//4, H//2
dy = 40
canvas1.create_text(x_st, y_st, text = "歡迎來到美國1")#無參數
x_st, y_st = x_st, y_st+dy
canvas1.create_text(x_st, y_st, text = '歡迎來到美國2', fill = 'red', width = 20)
x_st, y_st = x_st, y_st+dy
canvas1.create_text(x_st, y_st, text = '歡迎來到美國3', anchor="nw")
x_st, y_st = x_st, y_st+dy
canvas1.create_text(x_st, y_st, text='Welcome to the United States', fill='blue')
x_st, y_st = x_st, y_st+dy
canvas1.create_text(x_st, y_st, text='Welcome to the United States', fill='blue', font=('Old English Text MT',20))
x_st, y_st = x_st, y_st+dy
canvas1.create_text(x_st, y_st, text='Welcome to the United States', fill='blue', font=('華康新綜藝體 Std W7',20))
x_st, y_st = x_st, y_st+dy
canvas1.create_text(x_st, y_st, text='歡迎來到美國4', fill='blue', font=('華康新綜藝體 Std W7',20))
x_st, y_st = x_st, y_st+dy
canvas1.create_text(x_st, y_st, text = '歡迎來到美國5', font = ('Arial', 36))



"""
canvas1.create_window(500, 100, window = ttk.Button(window, text= 'this is text in a canvas'))

label1 = tk.Label(window, text = "Blue", bg = "blue").pack()
canvas1.create_window(500, 100, anchor="nw", window = label1)

"""
separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()

sys.exit()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

from tkinter import *
from PIL import Image, ImageTk

tk = Tk()
img = Image.open(filename)
image = ImageTk.PhotoImage(img)

canvas1 = Canvas(tk, width=img.size[0]+40, height=img.size[1]+30)
canvas1.create_image(20,15,anchor=NW,image=image)
canvas1.pack(fill=BOTH,expand=True)

mainloop()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/lena_color.png'

import tkinter as tk
import tkinter.font as tkfont

win = tk.Tk()

default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
photo = tk.PhotoImage(file=filename)

gs = tk.Canvas(win,width=400,height=300)
gs.create_image(60,120,image=photo)
gs.pack()
win.mainloop()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個





"""

id = canvas1.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
ballPos = canvas1.coords(id)
print(ballPos)


"""



