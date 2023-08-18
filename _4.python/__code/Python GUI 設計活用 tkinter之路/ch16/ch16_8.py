# ch16_8.py
from tkinter import *
from tkinter import messagebox
def findNext():
    messagebox.showinfo("Find Next","尋找下一筆")
def findPre():
    messagebox.showinfo("Find Pre","尋找上一筆")

root = Tk()
root.title("ch16_8")
root.geometry("300x180")

menubar = Menu(root)                        # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar)               
menubar.add_cascade(label="File",menu=filemenu,underline=0)
# 在File功能表內建立功能表清單
# 首先在File功能表內建立find子功能表物件
findmenu = Menu(filemenu,tearoff=False)     # 取消分隔線
findmenu.add_command(label="Find Next",command=findNext)
findmenu.add_command(label="Find Pre",command=findPre)
filemenu.add_cascade(label="Find",menu=findmenu)
# 下列是增加分隔線和建立Exit!指令
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=root.destroy,underline=0)

root.config(menu=menubar)                   # 顯示功能表物件

root.mainloop()












