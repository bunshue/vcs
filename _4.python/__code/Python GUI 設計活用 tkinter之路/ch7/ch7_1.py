# ch7_1.py
from tkinter import *
def printSelection():
    num = var.get()
    if num == 1:
        label.config(text="你是男生")
    else:
        label.config(text="你是女生")

root = Tk()
root.title("ch7_1")                             # 視窗標題

var = IntVar()                                  # 選項紐綁定的變數
var.set(1)                                      # 預設選項是男生
                       
label = Label(root,text="這是預設,尚未選擇", bg="lightyellow",width=30)
label.pack()

rbman = Radiobutton(root,text="男生",           # 男生選項鈕
                    variable=var,value=1,
                    command=printSelection)
rbman.pack()
rbwoman = Radiobutton(root,text="女生",         # 女生選項鈕
                      variable=var,value=2,
                      command=printSelection)
rbwoman.pack()

root.mainloop()






