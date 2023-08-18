# ch7_5.py
from tkinter import *
def printSelection():
    label.config(text="你選的是"+var.get())

root = Tk()
root.title("ch7_5")                             # 視窗標題

imgStar = PhotoImage(file="star.gif")
imgMoon = PhotoImage(file="moon.gif")
imgSun = PhotoImage(file="sun.gif")

var = StringVar()                               # 選項紐綁定的變數
var.set("星星")                                 # 預設選項是男生
                       
label = Label(root,text="這是預設,尚未選擇", bg="lightyellow",width=30)
label.pack()

rbStar = Radiobutton(root,image=imgStar,        # 星星選項鈕
                     variable=var,value="星星",
                     command=printSelection)
rbStar.pack()
rbMoon = Radiobutton(root,image=imgMoon,        # 月亮選項鈕
                     variable=var,value="月亮",
                     command=printSelection)
rbMoon.pack()
rbSun = Radiobutton(root,image=imgSun,          # 太陽選項鈕
                    variable=var,value="太陽",
                    command=printSelection)
rbSun.pack()

root.mainloop()






