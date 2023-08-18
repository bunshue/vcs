# ch16_11.py
from tkinter import *
       
root = Tk()
root.title("ch16_11")
root.geometry("300x180")

menubar = Menu(root)                    # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar,tearoff=False)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單Exit
filemenu.add_command(label="Exit",command=root.destroy)

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=3)
# 在工具列內建立按紐
sunGif = PhotoImage(file="sun.gif")
exitBtn = Button(toolbar,image=sunGif,command=root.destroy)
exitBtn.pack(side=LEFT,padx=3,pady=3)   # 包裝按鈕
toolbar.pack(side=TOP,fill=X)           # 包裝工具列
root.config(menu=menubar)               # 顯示功能表物件

root.mainloop()












