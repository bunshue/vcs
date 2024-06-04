"""
# 以Menu元件建置功能表


"""
'''
import sys
import tkinter as tk
from tkinter import ttk

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
title = "這是主視窗"
window.title(title)

#建立功能選單
menu = tk.Menu(window)
window.config(menu = menu)   #顯示功能表單

#第1排功能選單
menu1 = tk.Menu(menu, tearoff = False)
menu1.add_command(label = 'New', command = lambda: print('New file'))
menu1.add_command(label = 'Open', command = lambda: print('Open file'))
menu1.add_separator()
menu.add_cascade(label = 'File', menu = menu1)

#第2排功能選單
menu2 = tk.Menu(menu, tearoff = False)
menu2.add_command(label = 'Help entry', command = lambda: print(help_check_string.get()))

help_check_string = tk.StringVar()
menu2.add_checkbutton(label = 'check', onvalue = 'on', offvalue = 'off', variable = help_check_string)

menu.add_cascade(label = 'Help', menu = menu2)

#第3排功能選單
# add another menu to the main menu, this one should have a sub menu
# try to read the website below and add a submenu
# docs: https://www.tutorialspoint.com/python/tk_menu.htm
menu3 = tk.Menu(menu, tearoff = False)
menu3.add_command(label = 'exercise test 1')
menu.add_cascade(label = 'Exercise', menu = menu3)

menu3b = tk.Menu(menu, tearoff = False)
menu3b.add_command(label = 'some more stuff')
menu3.add_cascade(label = 'more stuff', menu = menu3b)

# menu button
menu_button = ttk.Menubutton(window, text = 'Menu Button')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff = False)
button_sub_menu.add_command(label = 'entry 1', command = lambda: print('test 1'))
button_sub_menu.add_checkbutton(label = 'check 1')
# menu_button.configure(menu = button_sub_menu)
menu_button['menu']= button_sub_menu

window.mainloop()

print("------------------------------------------------------------")  # 60個

def add(): 
    string3.set(eval(string1.get()) + eval(string2.get()))
    
def subtract():
    string3.set(eval(string1.get()) - eval(string2.get()))
    
def multiply():
    string3.set(eval(string1.get()) * eval(string2.get()))
    
def divide():
    string3.set(eval(string1.get()) / eval(string2.get()))

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
title = "這是主視窗"
window.title(title)

#建立功能選單
menu = tk.Menu(window)
window.config(menu = menu)   #顯示功能表單

#第1排功能選單
menu1 = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Operation", menu = menu1)
menu1.add_command(label = "Add", command = add)
menu1.add_command(label = "Subtract", command = subtract)
menu1.add_separator()
menu1.add_command(label = "Multiply", command = multiply)
menu1.add_command(label = "Divide", command = divide)

#第2排功能選單
menu2 = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Exit", menu = menu2)
menu2.add_command(label = "Quit", command = window.quit)


# Add labels and entries to frame1
frame1 = tk.Frame(window, bg = 'pink')
frame1.grid(row = 2, column = 1, pady = 10)
tk.Label(frame1, text = "Number 1:").pack(side = tk.LEFT)
string1 = tk.StringVar()
tk.Entry(frame1, width = 5, textvariable = string1, justify = tk.RIGHT).pack(side = tk.LEFT)
tk.Label(frame1, text = "Number 2:").pack(side = tk.LEFT)
string2 = tk.StringVar()
tk.Entry(frame1, width = 5, textvariable = string2, justify = tk.RIGHT).pack(side = tk.LEFT)
tk.Label(frame1, text = "Result:").pack(side = tk.LEFT)
string3 = tk.StringVar()
tk.Entry(frame1, width = 5, textvariable = string3, justify = tk.RIGHT).pack(side = tk.LEFT)

window.mainloop()

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
title = "這是主視窗"
window.title(title)

def callback():
    print("called the callback!")

#建立功能選單
menu = tk.Menu(window)
window.config(menu = menu)   #顯示功能表單

#第1排功能選單
#menu1 = tk.Menu(menu)
menu1 = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label = "File", menu = menu1)
menu1.add_command(label = "Open", command = callback)
menu1.add_command(label = "Save", command = callback)
menu1.add_separator()
menu1.add_command(label = "Exit", command = window.quit)

#第2排功能選單
menu2 = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Edit", menu = menu2)
menu2.add_command(label = "Cut", command = callback)
menu2.add_command(label = "Copy", command = callback)
menu2.add_command(label = "Paste", command = callback)

#第3排功能選單
#menu3 = tk.Menu(menu)
menu3 = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Help", menu = menu3)
menu3.add_command(label = "About...", command = callback)

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
title = "這是主視窗"
window.title(title)

def supermode():
	print('super mode!')

menu = tk.Menu(window)

menu1 = tk.Menu(menu)

menu1.add_command(label = 'supermode', command = supermode)

menu.add_cascade(label = 'Operation', menu = menu1)

window.config(menu = menu)

print("------------------------------------------------------------")  # 60個

import tkinter.filedialog as fd

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
title = "這是主視窗"
window.title(title)


def open():
	filename = fd.askopenfilename()
	print('open file => ' + filename)

def exit():
	window.destroy()


def find():
	print('find ! ')


menu = tk.Menu(window)

menu1 = tk.Menu(menu)

menu.add_cascade(label = 'File', menu = menu1)

menu1.add_command(label = 'open', command = open)

menu1.add_separator()

menu1.add_command(label = 'exit', command = exit)

menu2 = tk.Menu(menu)

menu.add_cascade(label = 'Edit', menu = menu2)

menu2.add_command(label = 'find', command = find)

window.config(menu = menu)

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *
from tkinter import messagebox

# 定義回應函式
def New():
    messagebox.showinfo('新檔案',
        '檔案功能表下的開啟新檔指令')
    
def Open():
    messagebox.showinfo('開啟舊檔',
        '檔案功能表下的開啟舊檔指令')

def Save():
    messagebox.showinfo('儲存檔案',
        '檔案功能表下的儲存檔案指令')
    
def Copyright():
    messagebox.showinfo('版權宣告',
        '我的第一支含視窗功能表程式-使用Python語言撰寫')

wnd = Tk()#主視窗物件
wnd.title('GUI介面-Menu')

# 1.產生功能表物件menuBar
menuBar = Menu(wnd)

# 2.將功能表物件menuBar佈置到主視窗的頂部
wnd.config(menu = menuBar)

# 3.加入主功能表項目
menu_file = Menu(menuBar, tearoff = 0)
menu_font = Menu(menuBar, tearoff = 0)
menu_help = Menu(menuBar, tearoff = 0)

# 4. 產生主功能項目實體
menuBar.add_cascade(label = '檔案', menu = menu_file)
menuBar.add_cascade(label = '字體大小', menu = menu_font)
menuBar.add_cascade(label = '版權宣告', menu = menu_help)

# 5-1. 加入'檔案'功能表下拉選單
menu_file.add_command(label = '新檔案',
        underline = 1, accelerator = 'Ctrl+N',
        command = New)
menu_file.add_command(label = '開啟',
        underline = 1, accelerator = 'Ctrl+O',
        command = Open)
menu_file.add_separator()#加入分隔線
menu_file.add_command(label = '儲存',
        underline = 1, accelerator = 'Ctrl+S',
        command = Save)
menu_file.add_separator()#加入分隔線
menu_file.add_command(label = '離開',
        underline = 1, accelerator = 'Ctrl+Q',
        command = lambda : wnd.destroy())

# 5-2. 加入'字體大小'功能表下拉選單
labels = ('大', '中', '小')
for item in labels:
    menu_font.add_radiobutton(label = item)

# 5-3. 加入'版權宣告'功能表下拉選單
menu_help.add_command(label = '原創者聲明', command = Copyright)

mainloop()


print("------------------------------------------------------------")  # 60個

from tkinter import filedialog, messagebox

base = tk.Tk()
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
title = "這是主視窗"
window.title(title)

def new_file():
    print('Create a new file')

def open_file():
    filename = filedialog.askopenfilename()
    print('open file => ' + filename)

def save_as():
    filename = filedialog.asksaveasfilename()
    print('save file as => ' + filename)

def exit_app():
    base.destroy()

def cut_text():
    print('Cut text')

def copy_text():
    print('Copy text')

def paste_text():
    print('Paste text')

def about_app():
    messagebox.showinfo("About", "This is a basic program.")

menubar = tk.Menu(base)

# File menu
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='檔案', menu=filemenu)
filemenu.add_command(label='開啟新檔', command=new_file)
filemenu.add_command(label='開啟舊檔', command=open_file)
filemenu.add_command(label='另存為', command=save_as)
filemenu.add_separator()
filemenu.add_command(label='結束', command=exit_app)

# Edit menu
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='編輯', menu=editmenu)
editmenu.add_command(label='剪下', command=cut_text)
editmenu.add_command(label='複製', command=copy_text)
editmenu.add_command(label='貼上', command=paste_text)

# About menu
helpmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='說明', menu=helpmenu)
helpmenu.add_command(label='關於本程式', command=about_app)

base.config(menu=menubar)

base.mainloop()

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
title = "這是主視窗"
window.title(title)

menubar = tk.Menu(win)
win.config(menu = menubar)
file_menu = tk.Menu(menubar)
menubar.add_cascade(label = "檔案", menu = file_menu)
edit_menu = tk.Menu(menubar)
menubar.add_cascade(label = "編輯", menu = edit_menu)
run_menu = tk.Menu(menubar)
menubar.add_cascade(label = "執行", menu =run_menu)
window_menu = tk.Menu(menubar)
menubar.add_cascade(label = "視窗", menu = window_menu)
online_menu = tk.Menu(menubar)
menubar.add_cascade(label = "線上說明", menu = online_menu)

win.mainloop()

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
title = "這是主視窗"
window.title(title)

menubar = tk.Menu(window,tearoff=0)
window.config(menu = menubar)
file_menu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label = "檔案", menu = file_menu)
file_menu.add_command(label = "開啟舊檔")  
edit_menu = tk.Menu(menubar)
menubar.add_cascade(label = "編輯", menu = edit_menu)
edit_menu.add_command(label = "復原") 
run_menu = tk.Menu(menubar)
menubar.add_cascade(label = "執行", menu =run_menu)
run_menu.add_command(label = "編譯及執行本程式")
window_menu = tk.Menu(menubar)
menubar.add_cascade(label = "視窗", menu = window_menu)
online_menu = tk.Menu(menubar)
menubar.add_cascade(label = "線上說明", menu = online_menu)

window.mainloop()

print('------------------------------------------------------------')	#60個

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
title = "這是主視窗"
window.title(title)

menubar = tk.Menu(window,tearoff=0)
window.config(menu = menubar)
file_menu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label = "檔案", menu = file_menu)
file_menu.add_command(label = "開啟舊檔")  
edit_menu = tk.Menu(menubar)
menubar.add_cascade(label = "編輯", menu = edit_menu)
edit_menu.add_command(label = "復原") 
run_menu = tk.Menu(menubar)
menubar.add_cascade(label = "執行", menu =run_menu)
run_menu.add_command(label = "編譯及執行本程式")
window_menu = tk.Menu(menubar)
menubar.add_cascade(label = "視窗", menu = window_menu)
online_menu = tk.Menu(menubar)
menubar.add_cascade(label = "線上說明", menu = online_menu)

window.mainloop()

print('------------------------------------------------------------')	#60個

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
title = "這是主視窗"
window.title(title)

menubar = tk.Menu(window)
window.config(menu = menubar)
file_menu = tk.Menu(menubar)
menubar.add_cascade(label = "檔案", menu = file_menu)
edit_menu = tk.Menu(menubar)
menubar.add_cascade(label = "編輯", menu = edit_menu)
run_menu = tk.Menu(menubar)
menubar.add_cascade(label = "執行", menu =run_menu)
window_menu = tk.Menu(menubar)
menubar.add_cascade(label = "視窗", menu = window_menu)
online_menu = tk.Menu(menubar)
menubar.add_cascade(label = "線上說明", menu = online_menu)

window.mainloop()

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
title = "這是主視窗"
window.title(title)

menubar = tk.Menu(window,tearoff=0)
window.config(menu = menubar)
file_menu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label = "檔案", menu = file_menu)
file_menu.add_command(label = "開啟舊檔")  
edit_menu = tk.Menu(menubar)
menubar.add_cascade(label = "編輯", menu = edit_menu)
edit_menu.add_command(label = "復原") 
run_menu = tk.Menu(menubar)
menubar.add_cascade(label = "執行", menu =run_menu)
run_menu.add_command(label = "編譯及執行本程式")
window_menu = tk.Menu(menubar)
menubar.add_cascade(label = "視窗", menu = window_menu)
online_menu = tk.Menu(menubar)
menubar.add_cascade(label = "線上說明", menu = online_menu)

window.mainloop()

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
title = "這是主視窗"
window.title(title)

menubar = tk.Menu(window,tearoff=0)
window.config(menu = menubar)
file_menu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label = "檔案", menu = file_menu)
file_menu.add_command(label = "開啟舊檔")  
edit_menu = tk.Menu(menubar)
menubar.add_cascade(label = "編輯", menu = edit_menu)
edit_menu.add_command(label = "復原") 
run_menu = tk.Menu(menubar)
menubar.add_cascade(label = "執行", menu =run_menu)
run_menu.add_command(label = "編譯及執行本程式")
window_menu = tk.Menu(menubar)
menubar.add_cascade(label = "視窗", menu = window_menu)
online_menu = tk.Menu(menubar)
menubar.add_cascade(label = "線上說明", menu = online_menu)

window.mainloop()

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
title = "這是主視窗"
window.title(title)

def fileopen():
	print('進行開啟檔案的處理')

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar)

menubar.add_cascade(label=' 檔案', menu=filemenu)

filemenu.add_command(label='開啟檔案', command=fileopen)

window.config(menu=menubar)

window.mainloop()


print('------------------------------------------------------------')	#60個

import tkinter.filedialog as fd

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
title = "這是主視窗"
window.title(title)


def open(): 
	filename = fd.askopenfilename()
	print('open file => ' + filename)

def exit(): 
	window.destroy()

def find():
	print('find ! ')

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar)

menubar.add_cascade(label='File', menu=filemenu)

filemenu.add_command(label='open', command=open)

filemenu.add_separator()

filemenu.add_command(label='exit', command=exit)

editmenu = tk.Menu(menubar)

menubar.add_cascade(label='Edit', menu=editmenu)

editmenu.add_command(label='find', command=find)

window.config(menu=menubar)





"""
請參考以下程式，幫我利用 tkinter 生成選單視窗，需要的檔案結構如下：

檔案：
	開啟新檔
	開啟舊檔
	另存為
	結束
編輯：
	剪下
	複製
	貼上
說明：
	關於本程式

----------- 以下是參考的程式架構 --------
"""
""" TBD
import tkinter.filedialog as fd

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
title = "這是主視窗"
window.title(title)


def open():
	filename = fd.askopenfilename()
print('open file => ' + filename)

def exit():
	window.destroy()

def find():
	print('find !')

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='open', command=open)
filemenu.add_separator()
filemenu.add_command(label='exit', command=exit)
editmenu = tk.Menu(menubar)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='find', command=find)
window.config(menu=menubar)

window.mainloop()

"""
print("------------------------------------------------------------")  # 60個

import tkinter.messagebox as tkmessagebox
import tkinter.font as tkfont

def Cal():
    tkmessagebox.showinfo(title="計算", message="計算資料中的試題難度")

def View():
    tkmessagebox.showinfo(title="檢視", message="檢視計算的結果")    

def About():
    tkmessagebox.showinfo(title="關於我們", message="程式設計者:屏東大學教育學系陳新豐")

def Exit():
    win.destroy()

window = tk.Tk()
window.geometry("800x600")
window.title("試題與測驗分析程式")

default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
menubar = tk.Menu(window)
window.config(menu=menubar)
menu_file = tk.Menu(menubar, tearoff = 0)
menu_cal  = tk.Menu(menubar, tearoff = 0)
menu_help = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label='檔案', menu=menu_file)
menubar.add_cascade(label='計算', menu=menu_cal)
menubar.add_cascade(label='Help', menu=menu_help)
menu_file.add_command(label='結束', command=Exit)
menu_cal.add_command(label='計算', command=Cal)
menu_cal.add_command(label='檢視', command=View)
menu_help.add_command(label='關於', command=About)

window.mainloop()

print("------------------------------------------------------------")  # 60個

import tkinter.messagebox as tkmessagebox
import tkinter.filedialog as tkfiledialog
import tkinter.font as tkfont


def Cal():
    options = {}
    options['filetypes'] = [("allfiles","*"),("text","*.txt")]
    options['initialdir'] = "c:\\"
    options['multiple'] = False
    options['title'] = "開啟分析檔案"
    fs = tkfiledialog.askopenfile(**options)    
    if fs:
        f = open(fs.name,'r')
        fc = f.readlines()
        f.close()
        fo = open('output.txt','w')
        fo.write("試題分析結果\n")
        pitem = int(fc[0][0:3])
        fo.write('題數:'+str(pitem)+'\n')
        pmiss = fc[0][4:5]
        fo.write('缺失:'+pmiss+'\n')
        pomit = fc[0][6:7]
        fo.write('遺漏:'+pomit+'\n')
        pid   = int(fc[0][8:10])
        fo.write('ID長度:'+str(pid)+'\n')
        pans  = fc[1]
        fo.write('答案:'+pans)
        pnum  = len(fc)-2
        fo.write('人數:'+str(pnum)+'\n')        
        psitem = []
        for j in range(0, pitem, 1):
            psitem.append(0)
        for i in range(0,pnum, 1):            
            for j in range(0,pitem, 1):                
                if (fc[2+i][pid+j]==pans[j]):                    
                    psitem[j] = psitem[j]+1                
        for j in range(0, pitem):
            fo.write('第'+str(j+1).rjust(2,'0')+'題，難度值p='+str(round(psitem[j]/pnum,2)).ljust(4,'0')+'\n')
        fo.close()
        tkmessagebox.showinfo(title="試題分析", message="分析完成")
    else:   
	     print ("沒有選擇檔案")
def View():
    options = {}
    options['filetypes'] = [("allfiles","*")]
    options['initialdir'] = "c:\\"
    options['multiple'] = False
    options['title'] = "開啟分析檔案"
    fs = tkfiledialog.askopenfile(**options)    
    if fs:        
        f = open(fs.name,'r')
        fc= f.readlines()
        f.close()
        ptext = tk.Text(win, width=800, height=600)        
        for i in range(0, len(fc), 1):
            ptext.insert(tk.INSERT, fc[i])        
        ptext.pack()
        ptext.config(state=tk.DISABLED)       
    else:   
	     print ("沒有選擇檔案")
def About():
    tkmessagebox.showinfo(title="關於我們", message="程式設計者:屏東大學教育學系陳新豐")

def Exit():
    win.destroy() 

window = tk.Tk()
window.geometry("800x600")
window.title("試題與測驗分析程式")

default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
menubar = tk.Menu(window)
window.config(menu=menubar)
menu_file = tk.Menu(menubar, tearoff = 0)
menu_cal  = tk.Menu(menubar, tearoff = 0)
menu_help = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label='檔案', menu=menu_file)
menubar.add_cascade(label='計算', menu=menu_cal)
menubar.add_cascade(label='Help', menu=menu_help)
menu_file.add_command(label='結束', command=Exit)
menu_cal.add_command(label='計算', command=Cal)
menu_cal.add_command(label='檢視', command=View)
menu_help.add_command(label='關於', command=About)

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def openFile(): 
    filenameforReading = askopenfilename()
    infile = open(filenameforReading, "r")
    text.insert("end", infile.read()) # Read all from the file
    infile.close()  # Close the input file
    
def saveFile():
    filenameforWriting = asksaveasfilename()
    outfile = open(filenameforWriting, "w")
    # Write to the file
    outfile.write(text.get(1.0, "end")) 
    outfile.close() # Close the output file
    
window = tk.Tk()
window.title("簡易文字編輯器")
        
menubar = tk.Menu(window)
window.config(menu = menubar) # Display the menu bar
        
# create a pulldown menu, and add it to the menu bar
operationMenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = operationMenu)
operationMenu.add_command(label = "Open", command = openFile)
operationMenu.add_command(label = "Save", command = saveFile)
        
# Add a tool bar frame 
frame0 = tk.Frame(window) # Create and add a frame to window
frame0.grid(row = 1, column = 1, sticky = "W")
        
# Create images
opneImage = tk.PhotoImage(file = "open.gif")
saveImage = tk.PhotoImage(file = "save.gif")
        
tk.Button(frame0, image = opneImage, command = openFile).grid(
                row = 1, column = 1, sticky = "W")
tk.Button(frame0, image = saveImage, command = saveFile).grid(
                row = 1, column = 2)
        
frame1 = tk.Frame(window) # Hold editor pane
frame1.grid(row = 2, column = 1)
        
scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side = "right", fill = "y")
text = tk.Text(frame1, width = 40, height = 20, wrap = "word",
               yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config(command = text.yview)
        
window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

def supermode():
	print('super mode!')

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
filemenu.add_command(label='supermode', command=supermode)
menubar.add_cascade(label='Operation', menu=filemenu)
window.config(menu=menubar)

print('------------------------------------------------------------')	#60個

import tkinter.filedialog as fd

window = tk.Tk()

def open():
	filename = fd.askopenfilename()
	print('open file => ' + filename)
def exit():
	window.destroy()

def find():
	print('find ! ')

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='open', command=open)
filemenu.add_separator()
filemenu.add_command(label='exit', command=exit)
editmenu = tk.Menu(menubar)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='find', command=find)
window.config(menu=menubar)

print('------------------------------------------------------------')	#60個

import tkinter.filedialog as fd

window = tk.Tk()

def open():
    filename = fd.askopenfilename()
    print('open file => ' + filename)

def exit():
    window.destroy()

def find():
    print('find ! ')

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='open', command=open)
filemenu.add_separator()
filemenu.add_command(label='exit', command=exit)
editmenu = tk.Menu(menubar)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='find', command=find)
window.config(menu=menubar)

window.mainloop()

print("------------------------------------------------------------")  # 60個

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("My Application")
        self.create_menu()
        self.pack()

    def create_menu(self):
        # 建立主功能表
        menubar = tk.Menu(self.master)

        # 建立檔案主功能
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="開啟檔案", command=self.open_file)
        file_menu.add_command(label="儲存檔案", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="結束", command=self.master.quit)
        menubar.add_cascade(label="檔案", menu=file_menu)

        # 建立編輯主功能
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="複製", command=self.copy)
        edit_menu.add_command(label="剪下", command=self.cut)
        edit_menu.add_command(label="貼上", command=self.paste)
        menubar.add_cascade(label="編輯", menu=edit_menu)

        # 建立執行主功能
        run_menu = tk.Menu(menubar, tearoff=0)
        run_menu.add_command(label="執行程式", command=self.run)
        menubar.add_cascade(label="執行", menu=run_menu)

        # 建立線上說明主功能
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="使用說明", command=self.show_help)
        menubar.add_cascade(label="線上說明", menu=help_menu)

        # 設定主功能表
        self.master.config(menu=menubar)

    def open_file(self):
        print("開啟檔案")

    def save_file(self):
        print("儲存檔案")

    def copy(self):
        print("複製")

    def cut(self):
        print("剪下")

    def paste(self):
        print("貼上")

    def run(self):
        print("執行程式")

    def show_help(self):
        print("使用說明")

# 建立主視窗
root = tk.Tk()

# 建立應用程式
app = Application(master=root)

# 執行主迴圈
app.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *
from tkinter import messagebox

# 定義回應函式
def New():
    messagebox.showinfo('新檔案',
        '檔案功能表下的開啟新檔指令')
    
def Open():
    messagebox.showinfo('開啟舊檔',
        '檔案功能表下的開啟舊檔指令')

def Save():
    messagebox.showinfo('儲存檔案',
        '檔案功能表下的儲存檔案指令')
    
def Copyright():
    messagebox.showinfo('版權宣告',
        '我的第一支含視窗功能表程式-使用Python語言撰寫')

wnd = Tk()#主視窗物件
wnd.title('GUI介面-Menu')

# 1.產生功能表物件menuBar
menuBar = Menu(wnd)

# 2.將功能表物件menuBar佈置到主視窗的頂部
wnd.config(menu = menuBar)

# 3.加入主功能表項目
menu_file = Menu(menuBar, tearoff = 0)
menu_font = Menu(menuBar, tearoff = 0)
menu_help = Menu(menuBar, tearoff = 0)

# 4. 產生主功能項目實體
menuBar.add_cascade(label = '檔案', menu = menu_file)
menuBar.add_cascade(label = '字體大小', menu = menu_font)
menuBar.add_cascade(label = '版權宣告', menu = menu_help)

# 5-1. 加入'檔案'功能表下拉選單
menu_file.add_command(label = '新檔案',
        underline = 1, accelerator = 'Ctrl+N',
        command = New)
menu_file.add_command(label = '開啟',
        underline = 1, accelerator = 'Ctrl+O',
        command = Open)
menu_file.add_separator()#加入分隔線
menu_file.add_command(label = '儲存',
        underline = 1, accelerator = 'Ctrl+S',
        command = Save)
menu_file.add_separator()#加入分隔線
menu_file.add_command(label = '離開',
        underline = 1, accelerator = 'Ctrl+Q',
        command = lambda : wnd.destroy())

# 5-2. 加入'字體大小'功能表下拉選單
labels = ('大', '中', '小')
for item in labels:
    menu_font.add_radiobutton(label = item)

# 5-3. 加入'版權宣告'功能表下拉選單
menu_help.add_command(label = '原創者聲明', command = Copyright)

mainloop()

print("------------------------------------------------------------")  # 60個


# tkinterMenu.py

root = tk.Tk()

menu = tk.Menu(root)						# 產生選單
submenu = tk.Menu(menu, tearoff=0)					# 產生下拉選單
submenu.add_command(label="Open")					# 向下拉選單中加入Open指令
submenu.add_command(label="Save")					# 向下拉選單中加入Save指令
submenu.add_command(label="Close")					# 向下拉選單中加入Close指令
menu.add_cascade(label="File", menu=submenu)				# 將下拉選單新增到選單中
submenu = tk.Menu(menu, tearoff=0)					# 產生下拉選單
submenu.add_command(label="Copy")					# 向下拉選單中加入Copy指令
submenu.add_command(label="Paste")					# 向下拉選單中加入Paste指令
submenu.add_separator()							# 向下拉選單中加入分隔符
submenu.add_command(label="Cut")					# 向下拉選單中加入Cut指令
menu.add_cascade(label="Edit", menu=submenu)				# 將下拉選單新增到選單中
submenu = tk.Menu(menu, tearoff=0)					# 產生下拉選單
submenu.add_command(label="About")					# 向下拉選單中加入About指令
menu.add_cascade(label="Help", menu=submenu)				# 將下拉選單新增到選單中
root.config(menu=menu)

root.mainloop()


print("------------------------------------------------------------")  # 60個

print("右鍵選單")
# tkinterPopupmenu.py

root = tk.Tk()

menu = tk.Menu(root, tearoff=0)				# 建立選單
menu.add_command(label="Copy")					# 向出現式選單中加入Copy指令
menu.add_command(label="Paste")					# 向出現式選單中加入Paste指令
menu.add_separator()						# 向出現式選單中加入分隔符
menu.add_command(label="Cut")					# 向出現式選單中加入Cut指令
def popupmenu(event):						# 定義右鍵事件處理函數
    menu.post(event.x_root, event.y_root)			# 顯示選單
root.bind("<Button-3>", popupmenu)				# 在主視窗中綁定右鍵事件

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *

from tkinter import messagebox

def hello():
    messagebox.showinfo("Hello","歡迎使用功能表")

root = Tk()
root.geometry("300x180")

# 建立最上層功能表
menubar = Menu(root)
menubar.add_command(label="Hello!",command=hello)
menubar.add_command(label="Exit!",command=root.destroy)
root.config(menu=menubar)           # 顯示功能表物件

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import messagebox

def newFile():
    messagebox.showinfo("New File","開新檔案")

root = Tk()
root.geometry("300x180")

menubar = Menu(root)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="New File",command=newFile)
filemenu.add_command(label="Exit!",command=root.destroy)
root.config(menu=menubar)           # 顯示功能表物件

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import messagebox

def newFile():
    messagebox.showinfo("New File","開新檔案")

root = Tk()
root.geometry("300x180")

menubar = Menu(root)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar,tearoff=False)               
menubar.add_cascade(label="File",menu=filemenu)
# 在File功能表內建立功能表清單
filemenu.add_command(label="New File",command=newFile)
filemenu.add_command(label="Exit!",command=root.destroy)
root.config(menu=menubar)           # 顯示功能表物件

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import messagebox

def newFile():
    messagebox.showinfo("New File","開新檔案")
def openFile():
    messagebox.showinfo("New File","開啟舊檔")
def saveFile():
    messagebox.showinfo("New File","儲存檔案")
def saveAsFile():
    messagebox.showinfo("New File","另存新檔")
    
root = Tk()
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
root.config(menu=menubar)           # 顯示功能表物件

root.mainloop()

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

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
root.geometry("300x180")

menubar = Menu(root)                # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar)               
menubar.add_cascade(label="File",menu=filemenu,underline=0)
# 在File功能表內建立功能表清單
filemenu.add_command(label="New File",command=newFile,underline=0)
filemenu.add_command(label="Open File",command=openFile,underline=0)
filemenu.add_separator()
filemenu.add_command(label="Save",command=saveFile,underline=0)
filemenu.add_command(label="Save As",command=saveAsFile,underline=5)
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=root.destroy,underline=0)
# 建立功能表類別物件,和將此功能表類別命名Help 
helpmenu = Menu(menubar)               
menubar.add_cascade(label="Help",menu=helpmenu,underline=0)
# 在Help功能表內建立功能表清單
helpmenu.add_command(label="About me",command=aboutMe,underline=1)
root.config(menu=menubar)           # 顯示功能表物件

root.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import messagebox
def newFile():
    messagebox.showinfo("New File","開新檔案")    
    
root = Tk()
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

print("------------------------------------------------------------")  # 60個

from tkinter import messagebox
def findNext():
    messagebox.showinfo("Find Next","尋找下一筆")
def findPre():
    messagebox.showinfo("Find Pre","尋找上一筆")

root = Tk()
root.geometry("300x180")

menubar = Menu(root)                        # 建立最上層功能表
# 建立功能表類別物件,和將此功能表類別命名File 
filemenu = Menu(menubar)               
menubar.add_cascade(label="File",menu=filemenu,underline=0)
# 在File功能表內建立功能表清單
# 首先在File功能表內建立find子功能表物件
findmenu = Menu(filemenu,tearoff=False)     # 取消分隔線
findmenu.add_command(label="Find Next",command=findNext)
findmenu.add_command(label="Find Pre",command=findPre)
filemenu.add_cascade(label="Find",menu=findmenu)
# 下列是增加分隔線和建立Exit!指令
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=root.destroy,underline=0)

root.config(menu=menubar)                   # 顯示功能表物件

root.mainloop()
print("------------------------------------------------------------")  # 60個

from tkinter import messagebox

def minimizeIcon():                     # 縮小視窗為圖示
    root.iconify()
def showPopupMenu(event):               # 顯示彈出功能表
    popupmenu.post(event.x_root,event.y_root)

root = Tk()
root.geometry("300x180")

popupmenu = Menu(root,tearoff=False)    # 建立彈出功能表物件
# 在彈出功能表內建立2個指令清單
popupmenu.add_command(label="Minimize",command=minimizeIcon)
popupmenu.add_command(label="Exit",command=root.destroy)
# 按滑鼠右鍵綁定顯示彈出功能表
root.bind("<Button-3>",showPopupMenu)

root.mainloop()

print("------------------------------------------------------------")  # 60個


def status():                       # 設定是否顯示狀態列
    if demoStatus.get():
        statusLabel.pack(side=BOTTOM,fill=X)
    else:
        statusLabel.pack_forget()
       
root = Tk()
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

print("------------------------------------------------------------")  # 60個
       
root = Tk()
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
'''

print("------------------------------------------------------------")  # 60個

import tkinter as tk

window = tk.Tk()
window.title("")


# 儲存選單
def save():
    print('你按了save')

# 結束選單
def exit():
    print('你按了exit')
    window.destroy()

# 建立選單畫面
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="save", command=save)
filemenu.add_separator()
filemenu.add_command(label="exit", command=exit)
window.config(menu=menubar)

window.mainloop()




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


