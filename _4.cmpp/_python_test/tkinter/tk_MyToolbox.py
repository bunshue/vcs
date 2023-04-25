# Python 測試 tkinter

import tkinter as tk

# 建立主視窗
window = tk.Tk()

# 設定主視窗大小
w = 800
h = 600
size = str(w)+'x'+str(h)
window.geometry(size)

# 設定主視窗標題
title = "測試grid"
window.title(title)

# 設定主視窗之背景色
window.configure(bg="#7AFEC6")

filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/python.ico'
window.iconbitmap(filename) #設定icon

show_mesg = tk.StringVar()

#window.resizable(0, 0)  #此行拒絕改變視窗大小

# configure the grid
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.columnconfigure(2, weight = 1)
window.columnconfigure(3, weight = 1)

def button00Click():
    print('你按了 button00')
    show_mesg.set("執行命令 : \n")
def button01Click():
    print('你按了 button01')
    show_mesg.set("執行命令 : \n")
def button02Click():
    print('你按了 button02')
    show_mesg.set("執行命令 : \n")
def button03Click():
    print('你按了 button03')
    show_mesg.set("執行命令 : \n")
def button10Click():
    print('你按了 button10')
    show_mesg.set("執行命令 : \n")
def button11Click():
    print('你按了 button11')
    show_mesg.set("執行命令 : \n")
def button12Click():
    print('你按了 button12')
    show_mesg.set("執行命令 : \n")
def button13Click():
    print('你按了 button13')
    show_mesg.set("執行命令 : \n")

button00 = tk.Button(window, text='(0, 0)', width = 20, height = 3, bg = 'white', fg = 'black', command = button00Click)
button00.grid(row = 0, column = 0, padx = 5, pady = 5)
button01 = tk.Button(window, text='(0, 1)', width = 20, height = 3, bg = 'white', fg = 'black', command = button01Click)
button01.grid(row = 0, column = 1, padx = 5, pady = 5)
button02 = tk.Button(window, text='(0, 2)', width = 20, height = 3, bg = 'white', fg = 'black', command = button02Click)
button02.grid(row = 0, column = 2, padx = 5, pady = 5)
button03 = tk.Button(window, text='(0, 3)', width = 20, height = 3, bg = 'white', fg = 'black', command = button03Click)
button03.grid(row = 0, column = 3, padx = 5, pady = 5)

button10 = tk.Button(window, text='(1, 0)', width = 20, height = 3, bg = 'white', fg = 'black', command = button10Click)
button10.grid(row = 1, column = 0, padx = 5, pady = 5)
button11 = tk.Button(window, text='(1, 1)', width = 20, height = 3, bg = 'white', fg = 'black', command = button11Click)
button11.grid(row = 1, column = 1, padx = 5, pady = 5)
button12 = tk.Button(window, text='(1, 2)', width = 20, height = 3, bg = 'white', fg = 'black', command = button12Click)
button12.grid(row = 1, column = 2, padx = 5, pady = 5)
button13 = tk.Button(window, text='(1, 3)', width = 20, height = 3, bg = 'white', fg = 'black', command = button13Click)
button13.grid(row = 1, column = 3, padx = 5, pady = 5)

#像是richTextBox
text1 = tk.Text(window, height = 20)  # 放入多行輸入框
text1.grid(row = 2, column = 0, columnspan = 4, padx = 5, pady = 5, sticky='news')

font_size = 24
w = 40
h = 30

# 設定 Label
label1 = tk.Label(window, textvariable = show_mesg, foreground = "red", font = ("標楷體", font_size), padx = w, pady = h)
label1.grid(row = 3, column = 0, columnspan = 4, padx = 5, pady = 5, sticky='news')


window.mainloop()



