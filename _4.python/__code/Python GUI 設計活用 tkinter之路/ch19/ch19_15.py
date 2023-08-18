# ch19_15.py
from tkinter import *
def paint(event):                           # 拖曳可以繪圖
    x1,y1 = (event.x, event.y)              # 設定左上角座標
    x2,y2 = (event.x, event.y)              # 設定右下角座標
    canvas.create_oval(x1,y1,x2,y2,fill="blue")
def cls():                                  # 清除畫面
    canvas.delete("all")
    
tk = Tk()
lab = Label(tk,text="拖曳滑鼠可以繪圖")     # 建立標題
lab.pack()
canvas = Canvas(tk,width=640, height=300)   # 建立畫布
canvas.pack()

btn = Button(tk,text="清除",command=cls)    # 建立清除按鈕
btn.pack(pady=5)

canvas.bind("<B1-Motion>",paint)            # 滑鼠拖曳綁定paint

canvas.mainloop()













