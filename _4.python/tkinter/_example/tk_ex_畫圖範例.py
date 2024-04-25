import sys

print("------------------------------------------------------------")  # 60個
'''
import tkinter as tk

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
'''
print("------------------------------------------------------------")  # 60個

from random import *

import tkinter as tk

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




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

""" 離開時有點問題
from tkinter import *

def displayFan(startingAngle):
    canvas.delete("fan")    
    canvas.create_arc(xWidth / 2 - r, yHeight / 2 - r, xWidth / 2 + r, yHeight / 2 + r,
            start = startAngle + 0, extent = 60, fill = "green", tags = "fan")        
    canvas.create_arc(xWidth / 2 - r, yHeight / 2 - r, xWidth / 2 + r, yHeight / 2 + r,
            start = startAngle + 120, extent = 60, fill = "green", tags = "fan")        
    canvas.create_arc(xWidth / 2 - r, yHeight / 2 - r, xWidth / 2 + r, yHeight / 2 + r,
            start = startAngle + 240, extent = 60, fill = "green", tags = "fan")        

xWidth = 300
yHeight = 300
r = 120

window = Tk() 
window.title("fan")
        
canvas = Canvas(window,width=xWidth, height=yHeight)
canvas.pack()

startAngle = 0
while True:
    startAngle += 5
    displayFan(startAngle)
    canvas.after(50) 
    canvas.update()
            
window.mainloop() 
"""

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




