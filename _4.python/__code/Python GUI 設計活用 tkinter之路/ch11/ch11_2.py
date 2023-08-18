# ch11_2.py
from tkinter import *
def callback(event):                        # 事件處理程式
    print("Clicked at", event.x, event.y)   # 列印座標
    
root = Tk()
root.title("ch11_2")
frame = Frame(root,width=300,height=180)
frame.bind("<Button-1>",callback)           # 按一下綁定callback
frame.pack()

root.mainloop()








