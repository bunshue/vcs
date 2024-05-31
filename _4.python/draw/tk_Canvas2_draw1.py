import sys

import tkinter as tk
'''
print("------------------------------------------------------------")  # 60個

window = tk.Tk()

# 設定主視窗大小
W = 750
H = 750
x_st = 1150
y_st = 100
# size = str(w)+'x'+str(h)
# size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
# window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
# print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

title = "tk畫圖大集合"
window.title(title)

print("建立畫布")
width = W - 20
height = H - 20
canvas1 = tk.Canvas(window, bg="pink", width=width, height=height)
canvas1.pack()

canvas1.create_line(0, H // 2, W, H // 2)
canvas1.create_line(W // 2, 0, W // 2, H)

# create_line 繪製直線 (x1, y1)-(x2, y2)
x1, y1, x2, y2 = 20, 20, 120, 20
canvas1.create_line(x1, y1, x2, y2)
x1, y1, x2, y2 = x1, y1 + 20, x2, y2 + 20
canvas1.create_line(x1, y1, x2, y2, fill="gray50")
x1, y1, x2, y2 = x1, y1 + 20, x2, y2 + 20
canvas1.create_line(x1, y1, x2, y2, fill="red", dash=(4, 4))
x1, y1, x2, y2 = x1, y1 + 20, x2, y2 + 20
canvas1.create_line(x1, y1, x2, y2, width=5)
x1, y1, x2, y2 = x1, y1 + 20, x2, y2 + 20
canvas1.create_line(x1, y1, x2, y2, width=10, fill="blue")
x1, y1, x2, y2 = x1, y1 + 20, x2, y2 + 20
canvas1.create_line(x1, y1, x2, y2, dash=(10, 2, 2, 2))
x1, y1, x2, y2 = x1, y1 + 20, x2, y2 + 20
canvas1.create_line(x1, y1, x2, y2, fill="#FF0000")

""" 直線連線
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
# create_rectangle 繪製矩形
x_st, y_st, x_sp, y_sp = 150, 20, 250, 60
dy = 55
canvas1.create_rectangle(x_st, y_st, x_sp, y_sp)  # 無參數, 空心1點, 黑線
x_st, y_st, x_sp, y_sp = x_st, y_st + dy, x_sp, y_sp + dy
canvas1.create_rectangle(x_st, y_st, x_sp, y_sp, dash=(4, 4))  # 虛線
x_st, y_st, x_sp, y_sp = x_st, y_st + dy, x_sp, y_sp + dy
canvas1.create_rectangle(x_st, y_st, x_sp, y_sp, outline="red")  # 外框線紅色
x_st, y_st, x_sp, y_sp = x_st, y_st + dy, x_sp, y_sp + dy
canvas1.create_rectangle(x_st, y_st, x_sp, y_sp, fill="red")  # 實心
# canvas1.create_rectangle(x_st, y_st, x_sp, y_sp, fill='#FF0000')#實心
x_st, y_st, x_sp, y_sp = x_st, y_st + dy, x_sp, y_sp + dy
canvas1.create_rectangle(x_st, y_st, x_sp, y_sp, fill="green", outline="red", width=5)
x_st, y_st, x_sp, y_sp = x_st, y_st + dy, x_sp, y_sp + dy
canvas1.create_rectangle(
    x_st, y_st, x_sp, y_sp, fill="blue", width=6, dash=(4, 2, 1, 1), outline="red"
)

# create_oval 繪製圓形、橢圓

# 圓形
cx, cy = 300, 40
radius = 30
dy = 60

canvas1.create_oval(cx - radius, cy - radius, cx + radius, cy + radius)  # 無參數, 空心1點, 黑線
cx, cy = cx, cy + dy
canvas1.create_oval(
    cx - radius, cy - radius, cx + radius, cy + radius, tags="oval"
)  # 多了tags參數
cx, cy = cx, cy + dy
canvas1.create_oval(
    cx - radius, cy - radius, cx + radius, cy + radius, fill="green"
)  # 實心圓, 黑色外框1點
cx, cy = cx, cy + dy
canvas1.create_oval(
    cx - radius, cy - radius, cx + radius, cy + radius, outline="red"
)  # 外框線紅色
cx, cy = cx, cy + dy

# 橢圓形
dy = 70
x_st, y_st, x_sp, y_sp = 270, 260, 420, 320  # 左上-右下
canvas1.create_oval(x_st, y_st, x_sp, y_sp)  # 橢圓

x_st, y_st, x_sp, y_sp = x_st, y_st + dy, x_sp, y_sp + dy  # 左上-右下
canvas1.create_oval(x_st, y_st, x_sp, y_sp, fill="aqua", outline="blue", width=5)

# create_arc 繪製圓弧
# 圓之左上-右下
x_st, y_st, x_sp, y_sp = 400, 0, 400 + 100, 0 + 100  # 左上-右下

start, extent = 45, 180  # 起始45度, 掃描180度
canvas1.create_arc(
    (x_st, y_st, x_sp, y_sp),
    fill="red",
    start=start,
    extent=extent,
    style=tk.CHORD,
    outline="green",
    width=5,
)
"""
style = tk.PIESLICE  # 派形
style = tk.ARC  # 僅弧線
style = tk.CHORD  # 弓形
"""

diameter = 100
dx = 80
dy = 80
x_st, y_st, x_sp, y_sp = 350, 120, 350 + diameter, 120 + diameter  # 左上-右下
canvas1.create_arc(x_st, y_st, x_sp, y_sp)  # 無參數 空心1點黑線0~90度
x_st, y_st, x_sp, y_sp = x_st + dx, y_st, x_sp + dx, y_sp

canvas1.create_arc(x_st, y_st, x_sp, y_sp, style=tk.ARC)  # 僅弧線
x_st, y_st, x_sp, y_sp = x_st + dx, y_st, x_sp + dx, y_sp
canvas1.create_arc(x_st, y_st, x_sp, y_sp, style=tk.PIESLICE)  # 派形
x_st, y_st, x_sp, y_sp = x_st + dx, y_st, x_sp + dx, y_sp
canvas1.create_arc(x_st, y_st, x_sp, y_sp, style=tk.CHORD)  # 弓形

x_st, y_st, x_sp, y_sp = 400, 120 + dy, 400 + diameter, 120 + diameter + dy  # 左上-右下
canvas1.create_arc(x_st, y_st, x_sp, y_sp, extent=180, fill="yellow")
x_st, y_st, x_sp, y_sp = x_st + dx, y_st, x_sp + dx, y_sp
canvas1.create_arc(x_st, y_st, x_sp, y_sp, extent=180, style=tk.ARC, width=5)

# create_polygon 繪製多邊形
dx = 400
dy = 280
canvas1.create_polygon(
    40 + dx,
    40 + dy,
    60 + dx,
    20 + dy,
    80 + dx,
    40 + dy,
    80 + dx,
    80 + dy,
    40 + dx,
    80 + dy,
)  # 無參數, 黑色實心
# 空心 外框線
canvas1.create_polygon(
    100 + dx,
    40 + dy,
    120 + dx,
    20 + dy,
    140 + dx,
    40 + dy,
    140 + dx,
    80 + dy,
    100 + dx,
    80 + dy,
    fill="",
    outline="red",
)
# 實心
canvas1.create_polygon(
    160 + dx, 80 + dy, 200 + dx, 80 + dy, 180 + dx, 20 + dy, fill="green"
)
# 實心 外框線
canvas1.create_polygon(
    220 + dx,
    80 + dy,
    260 + dx,
    80 + dy,
    240 + dx,
    20 + dy,
    fill="blue",
    outline="yellow",
    width=5,
)


# create_text 繪製文字

x_st, y_st = W // 4, H // 2
dy = 40
canvas1.create_text(x_st, y_st, text="歡迎來到美國1")  # 無參數
x_st, y_st = x_st, y_st + dy
canvas1.create_text(x_st, y_st, text="歡迎來到美國2", fill="red", width=20)
x_st, y_st = x_st, y_st + dy
canvas1.create_text(x_st, y_st, text="歡迎來到美國3", anchor="nw")
x_st, y_st = x_st, y_st + dy
canvas1.create_text(x_st, y_st, text="Welcome to the United States", fill="blue")
x_st, y_st = x_st, y_st + dy
canvas1.create_text(
    x_st,
    y_st,
    text="Welcome to the United States",
    fill="blue",
    font=("Old English Text MT", 20),
)
x_st, y_st = x_st, y_st + dy
canvas1.create_text(
    x_st,
    y_st,
    text="Welcome to the United States",
    fill="blue",
    font=("華康新綜藝體 Std W7", 20),
)
x_st, y_st = x_st, y_st + dy
canvas1.create_text(x_st, y_st, text="歡迎來到美國4", fill="blue", font=("華康新綜藝體 Std W7", 20))
x_st, y_st = x_st, y_st + dy
canvas1.create_text(x_st, y_st, text="歡迎來到美國5", font=("Arial", 36))

window.mainloop()
'''
print("------------------------------------------------------------")  # 60個

# Display a rectangle
def displayRect():
    canvas.create_rectangle(10, 10, 190, 90, tags = "rect")

# Display an oval
def displayOval():
    canvas.create_oval(10, 10, 190, 90, fill = "red", tags = "oval")

# Display an arc
def displayArc():
    canvas.create_arc(10, 10, 190, 90, start = 0, extent = 90, width = 8, fill = "red", tags = "arc")

# Display a polygon
def displayPolygon():
    canvas.create_polygon(10, 10, 190, 90, 30, 50, tags = "polygon")

# Display a line
def displayLine():
    canvas.create_line(10, 10, 190, 90, fill = "red", tags = "line")
    canvas.create_line(10, 90, 190, 10, width = 9, arrow = "last", activefill = "blue", tags = "line")

# Display a string
def displayString():
    canvas.create_text(60, 40, text = "Hi, I am a string", font = "Times 10 bold underline", tags = "string")

# Clear drawings
def clearCanvas():
    canvas.delete("rect", "oval", "arc", "polygon", "line", "string")

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
title = "Grid 測試"
window.title(title)

canvas = tk.Canvas(window, width = 400, height = 400, bg = "white")
canvas.pack()

btRectangle = tk.Button(window, text = "Rectangle", command = displayRect)
btOval = tk.Button(window, text = "Oval", command = displayOval)
btArc = tk.Button(window, text = "Arc", command = displayArc)
btPolygon = tk.Button(window, text = "Polygon", command = displayPolygon)
btLine = tk.Button(window, text = "Line", command = displayLine)
btString = tk.Button(window, text = "String", command = displayString)
btClear = tk.Button(window, text = "Clear", command = clearCanvas)

btRectangle.pack()
btOval.pack()
btArc.pack()
btPolygon.pack()
btLine.pack()
btString.pack()
btClear.pack()



window.mainloop()


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


"""


#新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame4 = tk.Frame(window)
frame4.pack()

width = 100
height = 100

canvas1 = tk.Canvas(frame4, width = width, height = height)
canvas1.create_line(10, 10, width - 10, height - 10)
canvas1.create_line(width - 10, 10, 10, height - 10)
canvas1.grid(row = 3, column = 1)

canvas2 = tk.Canvas(frame4, width = width, height = height)
canvas2.create_rectangle(10, 10, width - 10, height - 10)
canvas2.grid(row = 3, column = 2)

canvas3 = tk.Canvas(frame4, width = width, height = height)
canvas3.create_oval(10, 10, width - 10, height - 10)
canvas3.grid(row = 3, column = 3)

canvas4 = tk.Canvas(frame4, width = width, height = height)
canvas4.create_arc(10, 10, width - 10, height - 10, start = 0, extent = 145)
canvas4.grid(row = 3, column = 4)

canvas5 = tk.Canvas(frame4, width = width, height = height)
canvas5.create_rectangle(10, 10, width - 10, height - 10, fill = "red")
canvas5.grid(row = 3, column = 5)

canvas6 = tk.Canvas(frame4, width = width, height = height)
canvas6.create_oval(10, 10, width - 10, height - 10, fill = "red")
canvas6.grid(row = 3, column = 6)

canvas7 = tk.Canvas(frame4, width = width, height = height)
canvas7.create_arc(10, 10, width - 10, height - 10, start = 0, extent = 145, fill = "red")
canvas7.grid(row = 3, column = 7)


"""
