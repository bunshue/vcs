# ch13_1.py
from tkinter import *

root = Tk()
root.title("ch13_1")                   # 視窗標題
root.geometry("300x180")

var = StringVar(root)
optionmenu = OptionMenu(root,var,"Python","Java","C")
optionmenu.pack()

root.mainloop()











