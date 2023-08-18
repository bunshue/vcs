# ch6_6.py
from tkinter import *

def callbackW(name,index,mode):         # 內容被更改時執行
    xL.set(xE.get())                    # 更改標籤內容
    print("name = %r, index = %r, mode = %r" % (name,index,mode)) 
  
root = Tk()
root.title("ch6_5")                     # 視窗標題
    
xE = StringVar()                        # Entry的變數內容

entry = Entry(root,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)
xE.trace("w",callbackW)                 # 若是有更改執行callbackW

xL = StringVar()                        # Label的變數內容
label = Label(root,textvariable=xL)
xL.set("同步顯示")
label.pack(pady=5,padx=10)

root.mainloop()






