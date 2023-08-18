# ch9_4_1.py
from tkinter import *
from tkinter.colorchooser import *

def bgUpdate():
    ''' 更改視窗背景顏色 '''
    myColor = askcolor()            # 列出色彩對話方塊
    print(type(myColor),myColor)    # 列印傳回值
    root.config(bg=myColor[1])      # 設定視窗背景顏色
        
root = Tk()
root.title("ch9_4_1")
root.geometry("360x240")

btn = Button(text="Select Color",command=bgUpdate)
btn.pack(pady=5)

root.mainloop()















