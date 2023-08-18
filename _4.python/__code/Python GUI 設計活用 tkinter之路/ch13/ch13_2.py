# ch13_2.py
from tkinter import *

root = Tk()
root.title("ch13_2")                        # 視窗標題
root.geometry("300x180")

omTuple = ("Python","Java","C")             # tuple儲存表單項目
var = StringVar(root)
optionmenu = OptionMenu(root,var,*omTuple)  # 建立OptionMenu
optionmenu.pack()

root.mainloop()











