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

menu = tk.Menu(window)
window.config(menu = menu)

#第1排功能選單
#filemenu = tk.Menu(menu)
filemenu = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Open", command = callback)
filemenu.add_command(label = "Save", command = callback)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = window.quit)

#第2排功能選單
editmenu = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Cut", command = callback)
editmenu.add_command(label = "Copy", command = callback)
editmenu.add_command(label = "Paste", command = callback)

#第3排功能選單
#helpmenu = tk.Menu(menu)
helpmenu = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "About...", command = callback)


'''
menu
import tkinter as tk

window = tk.Tk()

def supermode():
	print('super mode!')

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar)

filemenu.add_command(label = 'supermode', command = supermode)

menubar.add_cascade(label = 'Operation', menu = filemenu)

window.config(menu = menubar)
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


menubar = tk.Menu(window)

filemenu = tk.Menu(menubar)

menubar.add_cascade(label = 'File', menu = filemenu)

filemenu.add_command(label = 'open', command = open)

filemenu.add_separator()

filemenu.add_command(label = 'exit', command = exit)

editmenu = tk.Menu(menubar)

menubar.add_cascade(label = 'Edit', menu = editmenu)

editmenu.add_command(label = 'find', command = find)

window.config(menu = menubar)



'''







window.mainloop()
