"""

相關抽出

特殊模組抽出
tk
turtle
pygame
qt
matplotlib


"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


import tkinter as tk

root = tk.Tk()  # 產生 tkinter 視窗
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(width, height)
root.destroy()  # 關閉視窗


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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
