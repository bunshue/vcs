"""
#右鍵選單

環境選單（英文：Context Menu，又稱作右鍵選單、右鍵菜單、快捷選單、快捷菜單、快顯功能表、彈出式選單）

"""

import sys
import tkinter as tk

print("------------------------------------------------------------")  # 60個

def popup(event):
    menu.post(event.x_root, event.y_root)

def menu_function1():
    print('你按了 右鍵選單 第 1 項')

def menu_function2():
    print('你按了 右鍵選單 第 2 項')

def menu_function3():
    print('你按了 右鍵選單 第 3 項')

def menu_function4():
    print('你按了 右鍵選單 第 4 項')

window = tk.Tk()
window.geometry("600x800")
window.title("綁定鍵盤滑鼠事件 Window, 右鍵選單")

#右鍵選單
menu = tk.Menu(window, tearoff = 0)
menu.add_command(label = "右鍵選單 第 1 項", command = menu_function1)
menu.add_command(label = "右鍵選單 第 2 項", command = menu_function2)
menu.add_command(label = "右鍵選單 第 3 項", command = menu_function3)
menu.add_command(label = "右鍵選單 第 4 項", command = menu_function4)

# 把Canvas放到window裡面
canvas = tk.Canvas(window, width = 300, height = 200, bg = 'pink')
canvas.pack()

# Bind popup to canvas
canvas.bind("<Button-3>", popup)

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import messagebox

def cutJob():                           # Cut方法
    copyJob()                           # 複製選取文字
    text.delete(SEL_FIRST,SEL_LAST)     # 刪除選取文字

def copyJob():                          # Copy方法
    try:
        text.clipboard_clear()          # 清除剪貼簿
        copyText = text.get(SEL_FIRST,SEL_LAST)             # 複製選取區域
        text.clipboard_append(copyText) # 寫入剪貼簿
    except TclError:
        print("沒有選取")

def pasteJob():                         # Paste方法
    try:
        copyText = text.selection_get(selection="CLIPBOARD") # 讀取剪貼簿內容
        text.insert(INSERT,copyText)        # 插入內容
    except TclError:
        print("剪貼簿沒有資料")

def showPopupMenu(event):               # 顯示彈出功能表
    popupmenu.post(event.x_root,event.y_root)


window = tk.Tk()
window.geometry("600x800")
window.title("綁定鍵盤滑鼠事件 Window, 右鍵選單")

popupmenu = tk.Menu(window,tearoff=False)    # 建立彈出功能表物件
# 在彈出功能表內建立3個指令清單
popupmenu.add_command(label="Cut",command=cutJob)
popupmenu.add_command(label="Copy",command=copyJob)
popupmenu.add_command(label="Paste",command=pasteJob)

# 按滑鼠右鍵綁定顯示彈出功能表
window.bind("<Button-3>",showPopupMenu)

# 建立Text
text = tk.Text(window)
text.pack(fill=tk.BOTH,expand=True,padx=3,pady=2)

text.insert(tk.END,"黃鶴樓送孟浩然之廣陵\n李白\n")
text.insert(tk.END,"故人西辭黃鶴樓，\n")
text.insert(tk.END,"煙花三月下揚州。\n")
text.insert(tk.END,"孤帆遠影碧空盡，\n")
text.insert(tk.END,"唯見長江天際流。\n")

window.mainloop()

print('------------------------------------------------------------')	#60個

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

window = tk.Tk()
window.geometry("600x800")
window.title("綁定鍵盤滑鼠事件 Window, 右鍵選單")

popupmenu = tk.Menu(window,tearoff=False)    # 建立彈出功能表物件
# 在彈出功能表內建立3個指令清單
popupmenu.add_command(label="Cut",command=cutJob)
popupmenu.add_command(label="Copy",command=copyJob)
popupmenu.add_command(label="Paste",command=pasteJob)

# 按滑鼠右鍵綁定顯示彈出功能表
window.bind("<Button-3>",showPopupMenu)

# 建立工具列
toolbar = tk.Frame(window,relief=tk.RAISED,borderwidth=1)
toolbar.pack(side=tk.TOP,fill=tk.X,padx=2,pady=1) 

# 建立Button
undoButton = tk.Button(toolbar,text="Undo",command=undoJob)
undoButton.pack(side=tk.LEFT,pady=2)
redoButton = tk.Button(toolbar,text="Redo",command=redoJob)
redoButton.pack(side=tk.LEFT,pady=2)

# 建立Text
text = tk.Text(window,undo=True)
text.pack(fill=tk.BOTH,expand=True,padx=3,pady=2)

text.insert(tk.END,"黃鶴樓送孟浩然之廣陵\n李白\n")
text.insert(tk.END,"故人西辭黃鶴樓，\n")
text.insert(tk.END,"煙花三月下揚州。\n")
text.insert(tk.END,"孤帆遠影碧空盡，\n")
text.insert(tk.END,"唯見長江天際流。\n")

window.mainloop()

print('------------------------------------------------------------')	#60個

print('按右鍵 另存新圖')

window = tk.Tk()
window.geometry("600x800")
window.title("綁定鍵盤滑鼠事件 Window, 右鍵選單")

from PIL import ImageTk, Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
img = ImageTk.PhotoImage(Image.open(filename))
label1 =tk.Label(window, image = img)
label1.pack()

def save(event):
    filename = tkinter.filedialog.asksaveasfilename(title="儲存檔案", initialfile="tmp_picture1.jpg")
    if filename and hasattr(label1, "qr_img"):
        label1.qr_img.save(filename)


window.bind("<Button-3>", save)

window.mainloop()

print("------------------------------------------------------------")  # 60個

print('按右鍵 右鍵選單 另存新圖')

window = tk.Tk()
window.geometry("600x800")
window.title("綁定鍵盤滑鼠事件 Window, 右鍵選單")

from PIL import ImageTk, Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
img = ImageTk.PhotoImage(Image.open(filename))
label1 =tk.Label(window, image = img)
label1.pack()

def save():
    filename = tkinter.filedialog.asksaveasfilename(title="儲存檔案", initialfile="tmp_picture2.jpg")
    if filename and hasattr(label1, "qr_img"):
        label1.qr_img.save(filename)


def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)


context_menu = tk.Menu(window, tearoff=0)
context_menu.add_command(label="儲存圖片", command=save)

window.bind("<Button-3>", show_context_menu)

window.mainloop()

print("------------------------------------------------------------")  # 60個

print('右鍵選單')

def displayRect():
    canvas.create_rectangle(10, 10, 190, 90, tags = "rect")

def displayOval():
    canvas.create_oval(10, 10, 190, 90, tags = "oval")

def displayLine():
    canvas.create_line(10, 10, 190, 90, tags = "line")
    canvas.create_line(10, 90, 190, 10, tags = "line")

def clearCanvas():
    canvas.delete("rect", "oval", "line")

def popup(event):
    menu.post(event.x_root, event.y_root)


window = tk.Tk()
window.title("右鍵選單")

# Create a popup menu
menu = tk.Menu(window, tearoff = 0)
menu.add_command(label = "Draw a line", command = displayLine)
menu.add_command(label = "Draw an oval", command = displayOval)
menu.add_command(label = "Draw a rectangle", command = displayRect)
menu.add_command(label = "Clear", command = clearCanvas)

# 把Canvas放到window裡面
canvas = tk.Canvas(window, width = 200, height = 100, bg = "white")
canvas.pack()

# Bind popup to canvas
canvas.bind("<Button-3>", popup)

window.mainloop()
        
print("------------------------------------------------------------")  # 60個

def minimizeIcon():                     # 縮小視窗為圖示
    window.iconify()

def showPopupMenu(event):               # 顯示彈出功能表
    popupmenu.post(event.x_root,event.y_root)

window = tk.Tk()
window.geometry("400x300")
window.title("右鍵選單")

popupmenu = tk.Menu(window,tearoff=False)    # 建立彈出功能表物件
# 在彈出功能表內建立2個指令清單
popupmenu.add_command(label="Minimize",command=minimizeIcon)
popupmenu.add_command(label="Exit",command=window.destroy)

# 按滑鼠右鍵綁定顯示彈出功能表
window.bind("<Button-3>",showPopupMenu)

window.mainloop()

print("------------------------------------------------------------")  # 60個

print("右鍵選單")

window = tk.Tk()
window.geometry("400x300")
window.title("右鍵選單")

menu = tk.Menu(window, tearoff=0)				# 建立選單
menu.add_command(label="Copy")					# 向出現式選單中加入Copy指令
menu.add_command(label="Paste")					# 向出現式選單中加入Paste指令
menu.add_separator()						# 向出現式選單中加入分隔符
menu.add_command(label="Cut")					# 向出現式選單中加入Cut指令

def popupmenu(event):						# 定義右鍵事件處理函數
    menu.post(event.x_root, event.y_root)			# 顯示選單

window.bind("<Button-3>", popupmenu)				# 在主視窗中綁定右鍵事件

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


