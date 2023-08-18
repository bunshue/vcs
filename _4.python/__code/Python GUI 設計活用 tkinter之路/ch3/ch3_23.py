# ch3_23.py
from tkinter import *

root = Tk()
root.title("ch3_23")
root.geometry("300x180")            # 設定視窗勘寬300高180
print("執行前",root.pack_slaves())
oklabel=Label(root,text="OK",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="blue") # 藍底白字
oklabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             padx=10,pady=10)       # x和y軸間距皆是10
nolabel=Label(root,text="NO",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="red")  # 藍底白字
nolabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             pady=10)               # y軸間距皆是10
print("執行後",root.pack_slaves())

root.mainloop()




