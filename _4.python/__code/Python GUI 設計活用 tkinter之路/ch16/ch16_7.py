# ch16_7.py
from tkinter import *
from tkinter import messagebox
def newFile():
    messagebox.showinfo("New File","開新檔案")    
    
root = Tk()
root.title("ch16_7")
root.geometry("300x180")

menubar = Menu(root)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar)               
menubar.add_cascade(label="File",menu=filemenu,underline=0)
# 在File功能表內建立功能表清單
filemenu.add_command(label="New File",command=newFile,
                     accelerator="Ctrl+N")
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=root.destroy,underline=0)
root.config(menu=menubar)           # 顯示功能表物件
root.bind("<Control-N>",            # 快捷鍵綁定
          lambda event:messagebox.showinfo("New File","開新檔案"))

root.mainloop()












