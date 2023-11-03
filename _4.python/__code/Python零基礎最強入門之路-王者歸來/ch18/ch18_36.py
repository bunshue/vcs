# ch18_36.py
from tkinter import *
from tkinter import messagebox

def newfile():
    messagebox.showinfo("開新檔案","可在此撰寫開新檔案程式碼")
    
def savefile():
    messagebox.showinfo("儲存檔案","可在此撰寫儲存檔案程式碼")
   
def about():
    messagebox.showinfo("程式說明","作者:洪錦魁")

window = Tk()
window.title("ch18_36")
window.geometry("300x160")          # 視窗寬300高160

menu = Menu(window)                 # 建立功能表物件
window.config(menu=menu)

filemenu = Menu(menu)               # 建立檔案功能表
menu.add_cascade(label="檔案",menu=filemenu)
filemenu.add_command(label="開新檔案",command=newfile)
filemenu.add_separator()            # 增加分隔線
filemenu.add_command(label="儲存檔案",command=savefile)
filemenu.add_separator()            # 增加分隔線
filemenu.add_command(label="結束",command=window.destroy)

helpmenu = Menu(menu)               # 建立說明功能表
menu.add_cascade(label="說明",menu=helpmenu)
helpmenu.add_command(label="程式說明",command=about)

mainloop()






