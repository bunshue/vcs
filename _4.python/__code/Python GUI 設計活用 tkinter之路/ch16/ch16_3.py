# ch16_3.py
from tkinter import *
from tkinter import messagebox

def newFile():
    messagebox.showinfo("New File","開新檔案")

root = Tk()
root.title("ch16_3")
root.geometry("300x180")

menubar = Menu(root)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar,tearoff=False)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="New File",command=newFile)
filemenu.add_command(label="Exit!",command=root.destroy)
root.config(menu=menubar)           # 顯示功能表物件

root.mainloop()












