# ch9_3.py
from tkinter import *

def printInfo():
    print("垂直捲軸值 = %d, 水平捲軸值 = %d" % (sV.get(),sH.get()))
    
root = Tk()
root.title("ch9_3")                           # 視窗標題

sV = Scale(root,label="垂直",from_=0,to=10)   # 建立垂直卷軸
sV.set(5)                                     # 設定垂直卷軸初值是5
sV.pack()

sH = Scale(root,label="水平",from_=0,to=10,   # 建立水平卷軸
                length=300,orient=HORIZONTAL)
sH.set(3)                                     # 設定水平捲軸初值是3
sH.pack()

Button(root,text="Print",command=printInfo).pack()

root.mainloop()






