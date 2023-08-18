# ch4_5.py
from tkinter import *

def yellow():                   # 設定視窗背景是黃色
    root.config(bg="yellow")
def blue():                     # 設定視窗背景是藍色
    root.config(bg="blue")
    
root = Tk()
root.title("ch4_5")
root.geometry("300x200")        # 固定視窗大小
# 依次建立3個鈕
exitbtn = Button(root,text="Exit",command=root.destroy)
bluebtn = Button(root,text="Blue",command=blue)
yellowbtn = Button(root,text="Yellow",command=yellow)
# 將3個鈕包裝定位在右下方
exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

root.mainloop()




