# ch11_6.py
from tkinter import *
def key(event):                     # 列出所按的鍵
    print("按了 " + repr(event.char) + " 鍵")

def coordXY(event):                 # 列出滑鼠座標
    frame.focus_set()               # frame物件取得焦點
    print("滑鼠座標 : ", event.x, event.y)
    
root = Tk()
root.title("ch11_6")

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)            # frame物件的<Key>綁定key
frame.bind("<Button-1>", coordXY)   # frame物件按一下綁定coordXY
frame.pack()

root.mainloop()








