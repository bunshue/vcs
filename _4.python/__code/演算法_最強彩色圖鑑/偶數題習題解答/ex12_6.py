# ex12_6.py
from tkinter import *
import math

def koch(order, p1, p2):
    ''' 繪製科赫雪花碎形(Fractal) '''
    if order == 0:                  # 如果階層是0繪製線條
        drawLine(p1, p2)
    else:                           # 計算線段間的x, y, z點 
        dx = p2[0] - p1[0]          # 計算線段間的x軸距離
        dy = p2[1] - p1[1]          # 計算線段間的y軸距離
# x是1/3線段點, y是2/3線段點, z是突出點
        x = [p1[0] + dx / 3, p1[1] + dy / 3]
        y = [p1[0] + dx * 2 / 3, p1[1] + dy * 2 / 3]
        z = [(int)((p1[0]+p2[0]) / 2 - math.cos(math.radians(30)) * dy / 3),
          (int)((p1[1]+p2[1]) / 2 + math.cos(math.radians(30)) * dx / 3)]
        # 遞迴呼叫繪製科赫雪花碎形
        koch(order - 1, p1, x)
        koch(order - 1, x, z)
        koch(order - 1, z, y)
        koch(order - 1, y, p2)

# 繪製p1和p2之間的線條
def drawLine(p1, p2):
    canvas.create_line(p1[0], p1[1], p2[0], p2[1],tags="myline")

# 顯示koch線段
def koch_demo():
    canvas.delete("myline")
    p1 = [200, 20]
    p2 = [20, 300]
    p3 = [380, 300]
    order = depth.get()
    koch(order, p1, p2)             # 上方點到左下方點
    koch(order, p2, p3)             # 左下方點到右下方點
    koch(order, p3, p1)             # 右下方點到上方點

# main
tk = Tk()
myWidth = 400
myHeight = 400
canvas = Canvas(tk, width=myWidth, height=myHeight) 
canvas.pack()

frame = Frame(tk)                   # 建立框架
frame.pack(padx=5, pady=5)
# 在框架Frame內建立標籤Label, 輸入order數Entry, 按鈕koch
Label(frame, text="輸入order : ").pack(side=LEFT)
depth = IntVar()
depth.set(0)
entry = Entry(frame, textvariable=depth).pack(side=LEFT,padx=3)
Button(frame, text="koch",command=koch_demo).pack(side=LEFT)

koch_demo()                         # 第一次啟動
tk.mainloop()



