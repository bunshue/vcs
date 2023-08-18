# ch17_20.py
from tkinter import *
from tkinter import messagebox
def cutJob():                           # Cut方法
    text.event_generate("<<Cut>>")
def copyJob():                          # Copy方法
    text.event_generate("<<Copy>>")
def pasteJob():                         # Paste方法
    text.event_generate("<<Paste>>")
def showPopupMenu(event):               # 顯示彈出功能表
    popupmenu.post(event.x_root,event.y_root)
def undoJob():                          # 復原undo方法
    try:
        text.edit_undo()
    except:
        print("先前未有動作")
def redoJob():                          # 重複redo方法
    try:
        text.edit_redo()
    except:
        print("先前未有動作")

root = Tk()
root.title("ch17_20")
root.geometry("300x180")

popupmenu = Menu(root,tearoff=False)    # 建立彈出功能表物件
# 在彈出功能表內建立3個指令清單
popupmenu.add_command(label="Cut",command=cutJob)
popupmenu.add_command(label="Copy",command=copyJob)
popupmenu.add_command(label="Paste",command=pasteJob)
# 按滑鼠右鍵綁定顯示彈出功能表
root.bind("<Button-3>",showPopupMenu)

# 建立工具列
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1) 

# 建立Button
undoBtn = Button(toolbar,text="Undo",command=undoJob)
undoBtn.pack(side=LEFT,pady=2)
redoBtn = Button(toolbar,text="Redo",command=redoJob)
redoBtn.pack(side=LEFT,pady=2)

# 建立Text
text = Text(root,undo=True)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Five Hundred Miles\n")
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")

root.mainloop()












