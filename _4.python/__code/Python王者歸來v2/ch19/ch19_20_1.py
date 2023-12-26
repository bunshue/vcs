# ch19_20_1.py
from tkinter import *
def callback(event):                        # 事件處理程式
    print("Clicked at", event.x, event.y)   # 列印座標
    
root = Tk()
root.title("ch19_20_1")
canvas = Canvas(root,width=300,height=180)
canvas.bind("<Button-1>",callback)           # 按一下綁定callback
canvas.pack()

root.mainloop()








