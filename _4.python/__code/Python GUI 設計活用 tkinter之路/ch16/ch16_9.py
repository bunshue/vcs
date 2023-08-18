# ch16_9.py
from tkinter import *
from tkinter import messagebox
def minimizeIcon():                     # 縮小視窗為圖示
    root.iconify()
def showPopupMenu(event):               # 顯示彈出功能表
    popupmenu.post(event.x_root,event.y_root)

root = Tk()
root.title("ch16_9")
root.geometry("300x180")

popupmenu = Menu(root,tearoff=False)    # 建立彈出功能表物件
# 在彈出功能表內建立2個指令清單
popupmenu.add_command(label="Minimize",command=minimizeIcon)
popupmenu.add_command(label="Exit",command=root.destroy)
# 按滑鼠右鍵綁定顯示彈出功能表
root.bind("<Button-3>",showPopupMenu)

root.mainloop()












