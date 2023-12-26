# ch19_29.py
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




