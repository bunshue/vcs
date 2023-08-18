# ch6_4.py
from tkinter import *

def callback(*args):
    xL.set(xE.get())                    # 更改標籤內容
    print("data changed : ",xE.get())   # Python Shell視窗輸出
   
root = Tk()
root.title("ch6_4")                     # 視窗標題
    
xE = StringVar()                        # Entry的變數內容
entry = Entry(root,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)
xE.trace("w",callback)                  # 若是有更改執行callback

xL = StringVar()                        # Label的變數內容
label = Label(root,textvariable=xL)
xL.set("同步顯示")
label.pack(pady=5,padx=10)   

root.mainloop()






