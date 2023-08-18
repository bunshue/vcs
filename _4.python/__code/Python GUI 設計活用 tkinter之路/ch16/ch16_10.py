# ch16_10.py
from tkinter import *

def status():                       # 設定是否顯示狀態列
    if demoStatus.get():
        statusLabel.pack(side=BOTTOM,fill=X)
    else:
        statusLabel.pack_forget()
       
root = Tk()
root.title("ch16_10")
root.geometry("300x180")

menubar = Menu(root)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar,tearoff=False)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單Exit
filemenu.add_command(label="Exit",command=root.destroy)
# 建立功能表類別物件,和將此功能表類別命名View 
viewmenu = Menu(menubar,tearoff=False)               
menubar.add_cascade(label="View",menu=viewmenu)
# 在View功能表內建立Check menu button
demoStatus = BooleanVar()
demoStatus.set(True)
viewmenu.add_checkbutton(label="Status",command=status,
                         variable=demoStatus)
root.config(menu=menubar)           # 顯示功能表物件

statusVar = StringVar()
statusVar.set("顯示")
statusLabel = Label(root,textvariable=statusVar,relief="raised")
statusLabel.pack(side=BOTTOM,fill=X)

root.mainloop()












