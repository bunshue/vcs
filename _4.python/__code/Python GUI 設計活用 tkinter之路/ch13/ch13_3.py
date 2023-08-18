# ch13_3.py
from tkinter import *

root = Tk()
root.title("ch13_3")                        # 視窗標題
root.geometry("300x180")

omTuple = ("Python","Java","C")             # tuple儲存表單項目
var = StringVar(root)
var.set("Python")                           # 建立預設選項
optionmenu = OptionMenu(root,var,*omTuple)  # 建立OptionMenu
optionmenu.pack()

root.mainloop()











