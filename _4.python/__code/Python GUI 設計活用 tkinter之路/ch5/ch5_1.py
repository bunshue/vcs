# ch5_1.py
from tkinter import *

root = Tk()
root.title("ch5_1")                     # 視窗標題

nameL = Label(root,text="Name ")        # name標籤
nameL.grid(row=0)
addressL = Label(root,text="Address")   # address標籤
addressL.grid(row=1)

nameE = Entry(root)                     # 文字方塊name
addressE = Entry(root)                  # 文字方塊address
nameE.grid(row=0,column=1)              # 定位文字方塊name
addressE.grid(row=1,column=1)           # 定位文字方塊address

root.mainloop()






