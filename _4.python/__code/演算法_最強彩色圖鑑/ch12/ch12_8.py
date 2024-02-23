# ch12_8.py
from tkinter import *
def htree(order, center, ht):
    ''' 依指定階級數繪製 H 樹碎形 '''
    if order >= 0:
        p1 = [center[0] - ht / 2, center[1] - ht / 2]   # 左上點
        p2 = [center[0] - ht / 2, center[1] + ht / 2]   # 左下點
        p3 = [center[0] + ht / 2, center[1] - ht / 2]   # 右上點
        p4 = [center[0] + ht / 2, center[1] + ht / 2]   # 右下點

        drawLine([center[0] - ht / 2, center[1]], 
            [center[0] + ht / 2, center[1]])            # 繪製H水平線
        drawLine(p1, p2)                                # 繪製H左邊垂直線
        drawLine(p3, p4)                                # 繪製H右邊垂直線
        
        htree(order - 1, p1, ht / 2)                    # 遞迴左上點當中間點
        htree(order - 1, p2, ht / 2)                    # 遞迴左下點當中間點
        htree(order - 1, p3, ht / 2)                    # 遞迴右上點當中間點
        htree(order - 1, p4, ht / 2)                    # 遞迴右下點當中間點
def drawLine(p1,p2):
    ''' 繪製p1和p2之間的線條 '''
    canvas.create_line(p1[0],p1[1],p2[0],p2[1],tags="htree")
def show():
    ''' 顯示 htree '''
    canvas.delete("htree")
    length = 200
    center = [200, 200]
    htree(order.get(), center, length)
    
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
Button(frame, text="顯示 htree",
       command=show).pack(side=LEFT)
tk.mainloop()




