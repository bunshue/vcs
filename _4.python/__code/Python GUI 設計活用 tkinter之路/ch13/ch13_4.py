# ch13_4.py
from tkinter import *
def printSelection():
    print("The selection is : ", var.get())
    
root = Tk()
root.title("ch13_4")                        # 視窗標題
root.geometry("300x180")

omTuple = ("Python","Java","C")             # tuple儲存表單項目
var = StringVar(root)
var.set("Python")                           # 建立預設選項
optionmenu = OptionMenu(root,var,*omTuple)  # 建立OptionMenu
optionmenu.pack(pady=10)

btn = Button(root,text="Print",command=printSelection)
btn.pack(pady=10,anchor=S,side=BOTTOM)

root.mainloop()











