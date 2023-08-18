# ch7_2.py
from tkinter import *
def printSelection():
    label.config(text="你是"+var.get())

root = Tk()
root.title("ch7_2")                             # 視窗標題

var = StringVar()                               # 選項紐綁定的變數
var.set("男生")                                 # 預設選項是男生
                       
label = Label(root,text="這是預設,尚未選擇", bg="lightyellow",width=30)
label.pack()

rbman = Radiobutton(root,text="男生",           # 男生選項鈕
                    variable=var,value="男生",
                    command=printSelection)
rbman.pack()
rbwoman = Radiobutton(root,text="女生",         # 女生選項鈕
                      variable=var,value="女生",
                      command=printSelection)
rbwoman.pack()

root.mainloop()






