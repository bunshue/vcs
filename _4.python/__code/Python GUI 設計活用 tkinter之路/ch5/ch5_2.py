# ch5_2.py
from tkinter import *

root = Tk()
root.title("ch5_2")                     # 視窗標題

accountL = Label(root,text="Account")   # account標籤
accountL.grid(row=0)
pwdL = Label(root,text="Password")      # pwd標籤
pwdL.grid(row=1)

accountE = Entry(root)                  # 文字方塊account
pwdE = Entry(root,show="*")             # 文字方塊pwd
accountE.grid(row=0,column=1)           # 定位文字方塊account
pwdE.grid(row=1,column=1)               # 定位文字方塊pwd

root.mainloop()






