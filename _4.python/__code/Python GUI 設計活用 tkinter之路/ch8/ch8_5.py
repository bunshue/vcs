# ch8_5.py
from tkinter import *

root = Tk()
root.title("ch8_5")

fm = Frame(width=150,height=80,relief=RAISED,borderwidth=5) # 建立框架
lab = Label(fm,text="請複選常用的程式語言")     # 建立標籤
lab.pack()
python = Checkbutton(fm,text="Python")          # 建立phthon核取方塊          
python.pack(anchor=W)
java = Checkbutton(fm,text="Java")              # 建立java核取方塊
java.pack(anchor=W)
ruby = Checkbutton(fm,text="Ruby")              # 建立ruby核取方塊
ruby.pack(anchor=W)
fm.pack(padx=10,pady=10)                        # 包裝框架

root.mainloop()








