# Python 測試 tkinter

import tkinter as tk

# 建立主視窗
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
title = "測試grid"
window.title(title)

# 設定主視窗之背景色
window.configure(bg="#7AFEC6")

# 設定主視窗之背景色
#window.config(background="#5cfcff")


'''
#使用icon方法一 .ico
icon_filename = 'C:/_git/vcs/_1.data/______test_files1/python.ico'
window.iconbitmap(icon_filename) #設定icon
'''

#使用icon方法二 .png
logo_filename = 'C:/_git/vcs/_1.data/______test_files1/__pic\_icon/option.png'
icon = tk.PhotoImage(file = logo_filename)
window.iconphoto(True,icon)

show_mesg = tk.StringVar()

#window.resizable(0, 0)  #此行拒絕改變視窗大小

# configure the grid
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.columnconfigure(2, weight = 1)
window.columnconfigure(3, weight = 1)

def buttonClick(cmd):
    #print('你按了 ', cmd)
    show_mesg.set("執行命令 : " +  cmd)
    if cmd == 'button00':
        doFunction00()
    elif cmd == 'button01':
        doFunction01()
    elif cmd == 'button02':
        doFunction02()
    elif cmd == 'button03':
        doFunction03()
    elif cmd == 'button10':
        doFunction10()
    elif cmd == 'button11':
        doFunction11()
    elif cmd == 'button12':
        doFunction12()
    elif cmd == 'button13':
        doFunction13()
    else:
        print('XXXXXXXXXXXXXXXXXXXXXXXX')

def doFunction00():
    print('執行 doFunction00')
def doFunction01():
    print('執行 doFunction01')
def doFunction02():
    print('執行 doFunction02')
def doFunction03():
    print('執行 doFunction03')
def doFunction10():
    print('執行 doFunction10')
def doFunction11():
    print('執行 doFunction11')
def doFunction12():
    print('執行 doFunction12')
def doFunction13():
    print('執行 doFunction13')

button00 = tk.Button(window, text='(0, 0)', width = 20, height = 3, bg = 'white', fg = 'black', command = lambda:buttonClick('button00'))   #給參數
button00.grid(row = 0, column = 0, padx = 5, pady = 5)
button01 = tk.Button(window, text='(0, 1)', width = 20, height = 3, bg = 'white', fg = 'black', command = lambda:buttonClick('button01'))   #給參數
button01.grid(row = 0, column = 1, padx = 5, pady = 5)
button02 = tk.Button(window, text='(0, 2)', width = 20, height = 3, bg = 'white', fg = 'black', command = lambda:buttonClick('button02'))   #給參數
button02.grid(row = 0, column = 2, padx = 5, pady = 5)
button03 = tk.Button(window, text='(0, 3)', width = 20, height = 3, bg = 'white', fg = 'black', command = lambda:buttonClick('button03'))   #給參數
button03.grid(row = 0, column = 3, padx = 5, pady = 5)

button10 = tk.Button(window, text='(1, 0)', width = 20, height = 3, bg = 'white', fg = 'black', command = lambda:buttonClick('button10'))   #給參數
button10.grid(row = 1, column = 0, padx = 5, pady = 5)
button11 = tk.Button(window, text='(1, 1)', width = 20, height = 3, bg = 'white', fg = 'black', command = lambda:buttonClick('button11'))   #給參數
button11.grid(row = 1, column = 1, padx = 5, pady = 5)
button12 = tk.Button(window, text='(1, 2)', width = 20, height = 3, bg = 'white', fg = 'black', command = lambda:buttonClick('button12'))   #給參數
button12.grid(row = 1, column = 2, padx = 5, pady = 5)
button13 = tk.Button(window, text='(1, 3)', width = 20, height = 3, bg = 'white', fg = 'black', command = lambda:buttonClick('button13'))   #給參數
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



