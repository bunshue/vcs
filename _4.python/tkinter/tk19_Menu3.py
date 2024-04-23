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
