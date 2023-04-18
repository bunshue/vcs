import tkinter as tk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
size = str(w)+'x'+str(h)
window.geometry(size)

# 設定主視窗標題
title = "這是主視窗"
window.title(title)

# 設定主視窗之背景色
window.configure(bg="#7AFEC6")

#window.iconbitmap('heart_green.ico')

def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

def showPopupMenu(event):
    popupmenu.post(event.x_root,event.y_root)

def undo():
    try:
        text.edit_undo()
    except:
        print("No action")

def redo():
    try:
        text.edit_redo()
    except:
        print("No action")

popupmenu=tk.Menu(window,tearoff=False)
popupmenu.add_command(label="cut",command=cut)
popupmenu.add_command(label="copy",command=copy)
popupmenu.add_command(label="paste",command=paste)

window.bind("<Button-3>",showPopupMenu)

toolbar=tk.Frame(window,relief="raised",borderwidth=1)
toolbar.pack(side="top",fill="x",padx=2,pady=1)

undoBtn = tk.Button(toolbar, text="Undo", command=undo)
undoBtn.pack(side="left", pady=2)
redoBtn = tk.Button (toolbar, text="Redo", command=redo)
redoBtn.pack(side="left", pady=2)

text = tk.Text (window, undo=True)
text.pack(fill="both", expand=True, padx=3, pady=2)
text.insert ('end', "我沒有說謊 我何必說謊\n")
text.insert ('end', "妳懂我的 我對妳從來就不會假裝 \n")
text.insert ('end', "我哪有說謊\n")
text.insert ('end', "請別以為妳有多難忘 笑是真的不是我逞強\n")

window.mainloop()


