# ch8_7.py
from tkinter import *

root = Tk()
root.title("ch8_7")                         # 視窗標題

msg = "歡迎進入Silicon Stone Educaiton系統"
sseGif = PhotoImage(file="sse.gif")         # Logo影像檔
logo = Label(root,image=sseGif,text=msg,compound=BOTTOM)
logo.pack()

# 以下是LabelFrame標籤框架
labFrame = LabelFrame(root,text="資料驗證") # 建立標籤框架
accountL = Label(labFrame,text="Account")   # account標籤
accountL.grid(row=0,column=0)
pwdL = Label(labFrame,text="Password")      # pwd標籤
pwdL.grid(row=1,column=0)

accountE = Entry(labFrame)                  # 文字方塊account
accountE.grid(row=0,column=1)               # 定位文字方塊account
pwdE = Entry(labFrame,show="*")             # 文字方塊pwd
pwdE.grid(row=1,column=1,pady=10)           # 定位文字方塊pwd
labFrame.pack(padx=10,pady=5,ipadx=5,ipady=5)   # 包裝與定位標籤框架

root.mainloop()






