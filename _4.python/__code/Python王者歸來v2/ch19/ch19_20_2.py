# ch19_20_2.py
from tkinter import *
def mouseMotion(event):             # Mouse移動
    x = event.x
    y = event.y
    textvar = "Mouse location - x:{}, y:{}".format(x,y)
    var.set(textvar)
    
root = Tk()
root.title("ch19_20_2")             # 視窗標題
root.geometry("300x180")            # 視窗寬300高180

x, y = 0, 0                         # x,y座標
var = StringVar()
text = "Mouse location - x:{}, y:{}".format(x,y)
var.set(text)

lab = Label(root,textvariable=var)  # 建立標籤
lab.pack(anchor=S,side=RIGHT,padx=10,pady=10)

root.bind("<Motion>",mouseMotion)   # 增加事件處理程式

root.mainloop()








