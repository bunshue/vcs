# ch18_24.py
from tkinter import *
def printSelection():
    label.config(text="你是" + var.get())

window = Tk()
window.title("ch18_24")                   # 視窗標題

var = StringVar()
var.set("男生")                           # 預設選項                       
label = Label(window,text="尚未選擇", bg="lightyellow",width=30)
label.pack()

rb1 = Radiobutton(window,text="男生",
                  variable=var,value='男生',
                  command=printSelection).pack()
rb2 = Radiobutton(window,text="女生",
                  variable=var,value='女生',
                  command=printSelection).pack()

window.mainloop()






