"""
綁定鍵盤滑鼠事件 Window
"""

import tkinter as tk
import tkinter.filedialog

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = '綁定鍵盤滑鼠事件 Window'
window.title(title)

def mouseDoubleClick1(event):
    print('雙擊左鍵', end = ' ')

def mouseDoubleClick2(event):
    print('雙擊中鍵', end = ' ')

def mouseDoubleClick3(event):
    print('雙擊右鍵', end = ' ')

def mouseDoubleClick4(event):
    print('?????', end = ' ')

def mouse_down1(event):
    print('你按了滑鼠左鍵', end = ' ')
    """
    print("在控件位置 : ", event.x, event.y, end = ' ')
    print("視窗位置 : ", event.x_root, event.y_root, end = ' ')
    print("按鍵 : ", event.num, end = ' ')
    """
def mouse_down2(event):
    print('你按了滑鼠中鍵', end = ' ')
    
def mouse_down3(event):
    print('你按了滑鼠右鍵', end = ' ')

def mouse_down4(event):
    print('上一頁', end = ' ')
    
def mouse_down5(event):
    print('下一頁', end = ' ')

def mouse_move1(event):
    print('m1', end = ' ')

def mouse_move2(event):
    print('m2', end = ' ')

def mouse_move3(event):
    print('m3', end = ' ')

def mouse_move4(event):
    print('m4', end = ' ')

def mouse_move5(event):
    print('m5', end = ' ')

def mouse_up1(event):
    print('up1', end = ' ')

def mouse_up2(event):
    print('up2', end = ' ')

def mouse_up3(event):
    print('up3', end = ' ')

def mouse_up4(event):
    print('up4', end = ' ')

def mouse_up5(event):
    print('up5', end = ' ')

def mouse_motion(event):
    #print(f'x: {event.x} y: {event.y}')
    #print('滑鼠位置: (%s, %s)' % (event.x, event.y), end = ' ')
    window.title('滑鼠位置: (%s, %s)' % (event.x, event.y))

def mouse_wheel_event(event):
    if event.delta > 0:
        print('上', end = ' ')
    else:
        print('下', end = ' ')

def processKeyEvent(event):
    print("keysym? ", event.keysym, end = ' ')
    print("char? ", event.char, end = ' ')
    print("keycode? ", event.keycode)

#Mouse Double Click
window.bind("<Double-1>", mouseDoubleClick1)    #雙擊左鍵
window.bind("<Double-2>", mouseDoubleClick2)    #雙擊中鍵
window.bind("<Double-3>", mouseDoubleClick3)    #雙擊右鍵
window.bind("<Double-4>", mouseDoubleClick4)    #unknown

#Mouse Down
window.bind("<Button-1>", mouse_down1)  #滑鼠左鍵 單擊
window.bind("<Button-2>", mouse_down2)  #滑鼠中鍵 單擊
window.bind("<Button-3>", mouse_down3)  #滑鼠右鍵 單擊
window.bind("<Button-4>", mouse_down4)  #滑鼠上一頁 單擊
window.bind("<Button-5>", mouse_down5)  #滑鼠下一頁 單擊

#Mouse Move
window.bind('<Button1-Motion>', mouse_move1)    #滑鼠左鍵 移動
window.bind('<Button2-Motion>', mouse_move2)    #滑鼠中鍵 移動
window.bind('<Button3-Motion>', mouse_move3)    #滑鼠右鍵 移動
window.bind('<Button4-Motion>', mouse_move4)    #滑鼠上一頁 移動
window.bind('<Button5-Motion>', mouse_move5)    #滑鼠下一頁 移動

#Mouse Up
window.bind('<ButtonRelease-1>', mouse_up1) #滑鼠左鍵 放開
window.bind('<ButtonRelease-2>', mouse_up2) #滑鼠中鍵 放開
window.bind('<ButtonRelease-3>', mouse_up3) #滑鼠右鍵 放開
window.bind('<ButtonRelease-4>', mouse_up4) #滑鼠上一頁 放開
window.bind('<ButtonRelease-5>', mouse_up5) #滑鼠下一頁 放開

window.bind('<Motion>', mouse_motion)  #滑鼠鼠標位置
window.bind('<MouseWheel>', mouse_wheel_event)  #滾輪事件

#鍵盤事件
window.bind("<Key>", processKeyEvent)
window.focus_set()

window.bind('<KeyPress>', lambda event: print(f'KeyPress ({event.char})'))
window.bind('<Alt-KeyPress-a>', lambda event: print('你按了Alt+A ', event))

window.mainloop()

print("------------------------------------------------------------")  # 60個

def mouseMotion(event):             # Mouse移動
    x = event.x
    y = event.y
    textvar = "Mouse location - x:{}, y:{}".format(x,y)
    var.set(textvar)
    
window = tk.Tk()
window.title("ch40_20_2")             # 視窗標題
window.geometry("300x180")            # 視窗寬300高180

x, y = 0, 0                         # x,y座標
var = tk.StringVar()
text = "Mouse location - x:{}, y:{}".format(x,y)
var.set(text)

lab = tk.Label(window,textvariable=var)  # 建立標籤
lab.pack(anchor=tk.S,side=tk.RIGHT,padx=10,pady=10)

window.bind("<Motion>",mouseMotion)   # 增加事件處理程式

window.mainloop()

print("------------------------------------------------------------")  # 60個

print('按右鍵 另存新圖')
window = tk.Tk()

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


def mouseMotion(event):             # Mouse移動
    x = event.x
    y = event.y
    textvar = "滑鼠位置 : x:{}, y:{}".format(x,y)
    var.set(textvar)
    
window = tk.Tk()
window.geometry("600x400")

x, y = 0, 0                         # x,y座標
var = tk.StringVar()
text = "Mouse location - x:{}, y:{}".format(x,y)
var.set(text)

lab = tk.Label(window,textvariable=var)  # 建立標籤
lab.pack(anchor=tk.S,side=tk.RIGHT,padx=10,pady=10)

window.bind("<Motion>",mouseMotion)   # 增加事件處理程式

window.mainloop()

print("------------------------------------------------------------")  # 60個

def leave(event):                       # <Esc>事件處理程式
    print('你按了 ESC')
   
window = tk.Tk()
window.geometry("600x400")

window.bind("<Escape>",leave)             # Esc鍵綁定leave函數
lab = tk.Label(window,text="測試Esc鍵",      # 標籤區域
            bg="yellow",fg="blue",
            height = 4, width=15,
            font="Times 12 bold")
lab.pack(padx=30,pady=30)

window.mainloop()

print('------------------------------------------------------------')	#60個

def key(event):                     # 處理鍵盤按a ... z
    print("按了 " + repr(event.char) + " 鍵") 
   
window = tk.Tk()
window.geometry("600x400")

window.bind("<Key>",key)              # <Key>鍵綁定key函數

window.mainloop()

print('------------------------------------------------------------')	#60個

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


print('右鍵選單')

window = tk.Tk()
window.geometry("600x400")

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

window = tk.Tk()
window.geometry("600x400")

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

print("------------------------------------------------------------")  # 60個


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
window.geometry("600x400")

popupmenu = tk.Menu(window,tearoff=False)    # 建立彈出功能表物件
# 在彈出功能表內建立3個指令清單
popupmenu.add_command(label="Cut",command=cutJob)
popupmenu.add_command(label="Copy",command=copyJob)
popupmenu.add_command(label="Paste",command=pasteJob)

# 按滑鼠右鍵綁定顯示彈出功能表
window.bind("<Button-3>",showPopupMenu)

# 建立工具列
toolbar = tk.Frame(window,relief=RAISED,borderwidth=1)
toolbar.pack(side=tk.TOP,fill=X,padx=2,pady=1) 

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





print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




