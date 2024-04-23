import sys

print("------------------------------------------------------------")  # 60個

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Menu')

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

import tkinter as tk

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

import tkinter as tk

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


'''
menu
import tkinter as tk

window = tk.Tk()

def supermode():
	print('super mode!')

menu = tk.Menu(window)

menu1 = tk.Menu(menu)

menu1.add_command(label = 'supermode', command = supermode)

menu.add_cascade(label = 'Operation', menu = menu1)

window.config(menu = menu)
'''



'''

import tkinter as tk

import tkinter.filedialog as fd

window = tk.Tk()

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



'''
window.mainloop()

print("------------------------------------------------------------")  # 60個

# 以Menu元件建置功能表
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

import tkinter as tk
from tkinter import filedialog, messagebox

base = tk.Tk()

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


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


