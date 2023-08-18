# ch16_5.py
from tkinter import *
from tkinter import messagebox
def newFile():
    messagebox.showinfo("New File","開新檔案")
def openFile():
    messagebox.showinfo("New File","開啟舊檔")
def saveFile():
    messagebox.showinfo("New File","儲存檔案")
def saveAsFile():
    messagebox.showinfo("New File","另存新檔")
def aboutMe():
    messagebox.showinfo("New File","洪錦魁著")    
    
root = Tk()
root.title("ch16_5")
root.geometry("300x180")

menubar = Menu(root)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="New File",command=newFile)
filemenu.add_command(label="Open File",command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Save As",command=saveAsFile)
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=root.destroy)
# 建立功能表類別物件,和將此功能表類別命名Help 
helpmenu = Menu(menubar)               
menubar.add_cascade(label="Help",menu=helpmenu)
# 在Help功能表內建立功能表清單
helpmenu.add_command(label="About me",command=aboutMe)
root.config(menu=menubar)           # 顯示功能表物件

root.mainloop()












