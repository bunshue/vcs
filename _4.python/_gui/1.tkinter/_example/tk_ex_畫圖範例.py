import sys
import tkinter as tk

print("------------------------------------------------------------")  # 60個
'''
window = tk.Tk()

# 設定主視窗大小
w = 400
h = 400
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


#在半徑為100的援外建立12個點 然後將此12點彼此相連
import math

canvas = tk.Canvas(window, width=640, height=480)
canvas.pack()
x_center, y_center, r = 200, 200, 150
x, y = [], []
for i in range(12):         # 建立圓外圍12個點
    x.append(x_center + r * math.cos(30*i*math.pi/180))
    y.append(y_center + r * math.sin(30*i*math.pi/180))
for i in range(12):         # 執行12個點彼此連線
    for j in range(12):
        canvas.create_line(x[i],y[i],x[j],y[j])

window.mainloop()

print('------------------------------------------------------------')	#60個

import math

window = tk.Tk()

canvas = tk.Canvas(window, width=640, height=480)
canvas.pack()

x_center, y_center, r = 320, 240, 100
x, y = [], []
for i in range(12):         # 建立圓外圍12個點
    x.append(x_center + r * math.cos(30*i*math.pi/180))
    y.append(y_center + r * math.sin(30*i*math.pi/180))
for i in range(12):         # 執行12個點彼此連線
    for j in range(12):
        canvas.create_line(x[i],y[i],x[j],y[j])

window.mainloop()

print('------------------------------------------------------------')	#60個

import math

window = tk.Tk()

canvas = tk.Canvas(window, width=640, height=480)
canvas.pack()

x_center, y_center, r = 320, 240, 100
x, y = [], []
for i in range(12):         # 建立圓外圍12個點
    x.append(x_center + r * math.cos(30*i*math.pi/180))
    y.append(y_center + r * math.sin(30*i*math.pi/180))
for i in range(12):         # 執行12個點彼此連線
    for j in range(12):
        canvas.create_line(x[i],y[i],x[j],y[j])

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import * # Import tkinter
    
def display():
    canvas.delete("line")
    p1 = [width / 2, 10]
    p2 = [10, height - 10]
    p3 = [width - 10, height - 10]
    displayTriangles(order, p1, p2, p3)

def displayTriangles(order, p1, p2, p3):
    if order == 0: # Base condition
        # Draw a triangle to connect three points
        drawLine(p1, p2)
        drawLine(p2, p3)
        drawLine(p3, p1)
    else:    
        # Get the midpoint of each triangle's edge 
        p12 = midpoint(p1, p2)
        p23 = midpoint(p2, p3)
        p31 = midpoint(p3, p1)

        # Recursively display three triangles
        displayTriangles(order - 1, p1, p12, p31)
        displayTriangles(order - 1, p12, p2, p23)
        displayTriangles(order - 1, p31, p23, p3)

def drawLine(p1, p2):
    canvas.create_line(p1[0], p1[1], p2[0], p2[1], tags = "line")
    
# Return the midpoint between two points
def midpoint(p1, p2):
    p = 2 * [0]
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p


window = Tk() # Create a window
window.title("Sierpinski Triangle") # Set a title
    
width = 200
height = 200
canvas = Canvas(window, width = width, height = height)
canvas.pack()

order = 5
display()

window.mainloop()


print("------------------------------------------------------------")  # 60個

from tkinter import *
import math

def paintTree(depth, x1, y1, length, angle):
    if depth >= 0:
        depth -= 1
        x2 = x1 + int(math.cos(angle) * length)
        y2 = y1 - int(math.sin(angle) * length)
        # 繪線
        drawLine(x1, y1, x2, y2)
        # 繪左邊
        paintTree(depth,x2, y2, length*sizeRatio, angle+angleValue)
        # 繪右邊
        paintTree(depth, x2, y2, length*sizeRatio, angle-angleValue)
        
# 繪製p1和p2之間的線條
def drawLine(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2,tags="myline")

# main
tk = Tk()
myWidth = 400
myHeight = 400
canvas = Canvas(tk, width=myWidth, height=myHeight) # 建立畫布
canvas.pack()

frame = Frame(tk)                               # 建立框架
frame.pack(padx=5, pady=5)

depth = 5
angleValue = math.pi / 4                       # 設定角度
sizeRatio = 0.6                                 # 設定下一層的長度與前一層的比率是0.6

canvas.delete("myline")
myDepth = 10
paintTree(myDepth, myWidth/2, myHeight, myHeight/3, math.pi/2)
  


tk.mainloop()


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
    canvas1.create_line(p1[0],p1[1],p2[0],p2[1],tags="myline")
# 傳回2點的中間值
def midpoint(p1, p2):
    p = [0,0]                                   # 初值設定
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p
# 顯示
def show():
    canvas1.delete("myline")
    p1 = [200, 20]
    p2 = [20, 380]
    p3 = [380,380]
    sierpinski(order.get(), p1, p2, p3)
    
tk = Tk()
canvas1 = Canvas(tk, width=400, height=400)      # 建立畫布
canvas1.pack()

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
    canvas1.create_line(p1[0],p1[1],p2[0],p2[1],tags="myline")
# 傳回2點的中間值
def midpoint(p1, p2):
    p = [0,0]                                   # 初值設定
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p
# 顯示
def show():
    canvas1.delete("myline")
    p1 = [200, 20]
    p2 = [20, 380]
    p3 = [380,380]
    sierpinski(order.get(), p1, p2, p3)
    
tk = Tk()
canvas1 = Canvas(tk, width=400, height=400)      # 建立畫布
canvas1.pack()

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

from random import *

window = tk.Tk()

canvas1 = tk.Canvas(window, width=640, height=480)
canvas1.pack()

for i in range(50):                 # 隨機繪50個不同位置與大小的矩形
    x1, y1 = randint(1, 640), randint(1, 480)
    x2, y2 = randint(1, 640), randint(1, 480)
    if x1 > x2: x1,x2 = x2,x1       # 確保左上角x座標小於右下角x座標
    if y1 > y2: y1,y2 = y2,y1       # 確保左上角y座標小於右下角y座標
    canvas1.create_rectangle(x1, y1, x2, y2)

tk.mainloop()


print("------------------------------------------------------------")  # 60個

from tkinter import *
from random import *

tk = Tk()
canvas1 = Canvas(tk, width=640, height=480)
canvas1 = Canvas(tk, width=640, height=240, bg='yellow')

canvas1.pack()

for i in range(50):                 # 隨機繪50個不同位置與大小的矩形
    x1, y1 = randint(1, 640), randint(1, 480)
    x2, y2 = randint(1, 640), randint(1, 480)
    if x1 > x2: x1,x2 = x2,x1       # 確保左上角x座標小於右下角x座標
    if y1 > y2: y1,y2 = y2,y1       # 確保左上角y座標小於右下角y座標
    canvas1.create_rectangle(x1, y1, x2, y2)

mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import * # Import tkinter
    
class SierpinskiTriangle:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Sierpinski Triangle") # Set a title
        
        self.width = 200
        self.height = 200
        self.canvas = Canvas(window, 
            width = self.width, height = self.height)
        self.canvas.pack()
        
        # Add a label, an entry, and a button to frame1
        frame1 = Frame(window) # Create and add a frame to window
        frame1.pack()
        
        Label(frame1, 
            text = "Enter an order: ").pack(side = LEFT)
        self.order = StringVar()
        entry = Entry(frame1, textvariable = self.order, 
                      justify = RIGHT).pack(side = LEFT)
        Button(frame1, text = "Display Sierpinski Triangle", 
            command = self.display).pack(side = LEFT)
        
        window.mainloop() # Create an event loop
        
    def display(self):
        self.canvas.delete("line")
        p1 = [self.width / 2, 10]
        p2 = [10, self.height - 10]
        p3 = [self.width - 10, self.height - 10]
        self.displayTriangles(int(self.order.get()), p1, p2, p3)
    
    def displayTriangles(self, order, p1, p2, p3):
        if order == 0: # Base condition
            # Draw a triangle to connect three points
            self.drawLine(p1, p2)
            self.drawLine(p2, p3)
            self.drawLine(p3, p1)
        else:    
            # Get the midpoint of each triangle's edge 
            p12 = self.midpoint(p1, p2)
            p23 = self.midpoint(p2, p3)
            p31 = self.midpoint(p3, p1)
    
            # Recursively display three triangles
            self.displayTriangles(order - 1, p1, p12, p31)
            self.displayTriangles(order - 1, p12, p2, p23)
            self.displayTriangles(order - 1, p31, p23, p3)
    
    def drawLine(self, p1, p2):
        self.canvas.create_line(
            p1[0], p1[1], p2[0], p2[1], tags = "line")
        
    # Return the midpoint between two points
    def midpoint(self, p1, p2):
        p = 2 * [0]
        p[0] = (p1[0] + p2[0]) / 2
        p[1] = (p1[1] + p2[1]) / 2
        return p

SierpinskiTriangle() # Create GUI




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


def koch(order, p1, p2):
    """繪製科赫雪花碎形(Fractal)"""
    if order == 0:  # 如果階層是0繪製線條
        drawLine(p1, p2)
    else:  # 計算線段間的x, y, z點
        dx = p2[0] - p1[0]  # 計算線段間的x軸距離
        dy = p2[1] - p1[1]  # 計算線段間的y軸距離
        # x是1/3線段點, y是2/3線段點, z是突出點
        x = [p1[0] + dx / 3, p1[1] + dy / 3]
        y = [p1[0] + dx * 2 / 3, p1[1] + dy * 2 / 3]
        z = [
            (int)((p1[0] + p2[0]) / 2 - math.cos(math.radians(30)) * dy / 3),
            (int)((p1[1] + p2[1]) / 2 + math.cos(math.radians(30)) * dx / 3),
        ]
        # 遞迴呼叫繪製科赫雪花碎形
        koch(order - 1, p1, x)
        koch(order - 1, x, z)
        koch(order - 1, z, y)
        koch(order - 1, y, p2)


# 繪製p1和p2之間的線條
def drawLine(p1, p2):
    canvas.create_line(p1[0], p1[1], p2[0], p2[1], tags="myline")


# 顯示koch線段
def koch_demo():
    canvas.delete("myline")
    p1 = [200, 20]
    p2 = [20, 300]
    p3 = [380, 300]
    order = depth.get()
    koch(order, p1, p2)  # 上方點到左下方點
    koch(order, p2, p3)  # 左下方點到右下方點
    koch(order, p3, p1)  # 右下方點到上方點


# main
tk = Tk()
myWidth = 400
myHeight = 400
canvas = Canvas(tk, width=myWidth, height=myHeight)
canvas.pack()

frame = Frame(tk)  # 建立框架
frame.pack(padx=5, pady=5)
# 在框架Frame內建立標籤Label, 輸入order數Entry, 按鈕koch
Label(frame, text="輸入order : ").pack(side=LEFT)
depth = IntVar()
depth.set(0)
entry = Entry(frame, textvariable=depth).pack(side=LEFT, padx=3)
Button(frame, text="koch", command=koch_demo).pack(side=LEFT)

koch_demo()  # 第一次啟動
tk.mainloop()


print("------------------------------------------------------------")  # 60個


from tkinter import *


def htree(order, center, ht):
    """依指定階級數繪製 H 樹碎形"""
    if order >= 0:
        p1 = [center[0] - ht / 2, center[1] - ht / 2]  # 左上點
        p2 = [center[0] - ht / 2, center[1] + ht / 2]  # 左下點
        p3 = [center[0] + ht / 2, center[1] - ht / 2]  # 右上點
        p4 = [center[0] + ht / 2, center[1] + ht / 2]  # 右下點

        drawLine(
            [center[0] - ht / 2, center[1]], [center[0] + ht / 2, center[1]]
        )  # 繪製H水平線
        drawLine(p1, p2)  # 繪製H左邊垂直線
        drawLine(p3, p4)  # 繪製H右邊垂直線

        htree(order - 1, p1, ht / 2)  # 遞迴左上點當中間點
        htree(order - 1, p2, ht / 2)  # 遞迴左下點當中間點
        htree(order - 1, p3, ht / 2)  # 遞迴右上點當中間點
        htree(order - 1, p4, ht / 2)  # 遞迴右下點當中間點


def drawLine(p1, p2):
    """繪製p1和p2之間的線條"""
    canvas.create_line(p1[0], p1[1], p2[0], p2[1], tags="htree")


def show():
    """顯示 htree"""
    canvas.delete("htree")
    length = 200
    center = [200, 200]
    htree(order.get(), center, length)


tk = Tk()
canvas = Canvas(tk, width=400, height=400)  # 建立畫布
canvas.pack()
frame = Frame(tk)  # 建立框架
frame.pack(padx=5, pady=5)
# 在框架Frame內建立標籤Label, 輸入階乘數Entry, 按鈕Button
Label(frame, text="輸入階數 : ").pack(side=LEFT)
order = IntVar()
order.set(0)
entry = Entry(frame, textvariable=order).pack(side=LEFT, padx=3)
Button(frame, text="顯示 htree", command=show).pack(side=LEFT)
tk.mainloop()



print("------------------------------------------------------------")  # 60個

from tkinter import *
import math


def paintTree(depth, x1, y1, length, angle):
    if depth >= 0:
        depth -= 1
        x2 = x1 + int(math.cos(angle) * length)
        y2 = y1 - int(math.sin(angle) * length)
        # 繪線
        drawLine(x1, y1, x2, y2)
        # 繪左邊
        paintTree(depth, x2, y2, length * sizeRatio, angle + angleValue)
        # 繪右邊
        paintTree(depth, x2, y2, length * sizeRatio, angle - angleValue)


# 繪製p1和p2之間的線條
def drawLine(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, tags="myline")


# 顯示
def show():
    canvas.delete("myline")
    myDepth = depth.get()
    paintTree(myDepth, myWidth / 2, myHeight, myHeight / 3, math.pi / 2)


# main
tk = Tk()
myWidth = 400
myHeight = 400
canvas = Canvas(tk, width=myWidth, height=myHeight)  # 建立畫布
canvas.pack()

frame = Frame(tk)  # 建立框架
frame.pack(padx=5, pady=5)
# 在框架Frame內建立標籤Label, 輸入depth數Entry, 按鈕Button
Label(frame, text="輸入depth : ").pack(side=LEFT)
depth = IntVar()
depth.set(0)
entry = Entry(frame, textvariable=depth).pack(side=LEFT, padx=3)
Button(frame, text="Recursive Tree", command=show).pack(side=LEFT)
angleValue = math.pi / 4  # 設定角度
sizeRatio = 0.6  # 設定下一層的長度與前一層的比率是0.6

tk.mainloop()

print("------------------------------------------------------------")  # 60個

'''
print("------------------------------------------------------------")  # 60個

import time
import random


def reset():
    # 重設長條圖
    global i
    i = 0  # 重設索引
    random.shuffle(mylist)
    newBar()


def go():
    # 執行排序
    global i
    if i > len(mylist) - 1:
        print("排序完成")
        return
    # 將mylist[i]插入mylist[0 .. i-1]
    currentValue = mylist[i]
    k = i - 1
    # 找尋mylist[i]適當位置
    while k >= 0 and mylist[k] > currentValue:
        mylist[k + 1] = mylist[k]
        k -= 1
    # 正式執行插入list[k + 1]
    mylist[k + 1] = currentValue

    newBar()  # 繪製新的長條圖
    i += 1  # 增加串列指標


def newBar():
    global i, gap
    canvas.delete("line")  # 刪除bar
    canvas.delete("text")  # 刪除bar上方數字
    canvas.create_line(10, ht - gap, wd - 10, ht - gap, tag="line")
    barWd = (wd - 20) / len(mylist)

    maxC = int(max(mylist))
    for j in range(len(mylist)):
        canvas.create_rectangle(
            j * barWd + 10,
            (ht - gap) * (1 - mylist[j] / (maxC + 4)),
            (j + 1) * barWd + 10,
            ht - gap,
            tag="line",
        )

        canvas.create_text(
            j * barWd + 10 + barWd / 2,
            (ht - gap) * (1 - mylist[j] / (maxC + 4)) - 8,
            text=str(mylist[j]),
            tag="text",
        )

    if i >= 0:
        canvas.create_rectangle(
            i * barWd + 10,
            (ht - gap) * (1 - mylist[i] / (maxC + 4)),
            (i + 1) * barWd + 10,
            ht - gap,
            fill="blue",
            tag="line",
        )


wd = 400  # 視窗寬度
ht = 200  # 視窗高度
gap = 20  # 長條圖與視窗的間距
i = 0  # 這是目前排序指標

window = tk.Tk()

canvas = tk.Canvas(window, width=wd, height=ht)
canvas.pack()

frame = tk.Frame(window)
frame.pack()

btnStep = tk.Button(frame, text="執行", command=go)
btnStep.pack(side=tk.LEFT)
btnReset = tk.Button(frame, text="重置", command=reset)
btnReset.pack(side=tk.LEFT)
btnReset = tk.Button(frame, text="結束", command=window.destroy)
btnReset.pack(side=tk.LEFT)

mylist = [x for x in range(1, 20)]
reset()
newBar()

window.mainloop()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
