"""
Button 排列 與 空函數


"""

print('------------------------------------------------------------')	#60個

import os
import sys
import csv
import time
import sqlite3
import tkinter as tk
from tkinter.filedialog import askopenfile #tk之openFileDialog
from tkinter.filedialog import asksaveasfile #tk之saveFileDialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def button00Click():
    print('你按了button00')

def button01Click():
    print('你按了button01')

def button02Click():
    print('你按了button02')

def button03Click():
    print('你按了button03')

def button04Click():
    print('你按了button04')

def button05Click():
    print('你按了button05')

def button10Click():
    print('你按了button10')

def button11Click():
    print('你按了button11')

def button12Click():
    print('你按了button12')

def button13Click():
    print('你按了button13')

def button14Click():
    print('你按了button14')
    #清空Text
    text1.delete(1.0, 'end')

def button15Click():
    #print('你按了button15')
    message = "匯入生產資料 完成\n"
    #print(message)
    text1.insert('end', message)


window = tk.Tk()

# 設定主視窗大小
W = 800
H = 800
x_st = 100
y_st = 100
#size = str(W)+'x'+str(H)
#size = str(W)+'x'+str(H)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(W, H, x_st, y_st))
#print('{0:d}x{1:d}+{2:d}+{3:d}'.format(W, H, x_st, y_st))

# 設定主視窗標題
window.title('功能測試')

# 設定主視窗之背景色
#window.configure(bg = "#7AFEC6")

x_st = 50
y_st = 50
dx = 120
dy = 80
w = 12
h = 3

button00 = tk.Button(window, width = w, height = h, command = button00Click, text = '----')
button00.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button01 = tk.Button(window, width = w, height = h, command = button01Click, text = '----')
button01.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button02 = tk.Button(window, width = w, height = h, command = button02Click, text = '----')
button02.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button03 = tk.Button(window, width = w, height = h, command = button03Click, text = '----')
button03.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button04 = tk.Button(window, width = w, height = h, command = button04Click, text = '----')
button04.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button05 = tk.Button(window, width = w, height = h, command = button05Click, text = '----')
button05.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button00.place(x = x_st + dx * 0, y = y_st + dy * 0)
button01.place(x = x_st + dx * 1, y = y_st + dy * 0)
button02.place(x = x_st + dx * 2, y = y_st + dy * 0)
button03.place(x = x_st + dx * 3, y = y_st + dy * 0)
button04.place(x = x_st + dx * 4, y = y_st + dy * 0)
button05.place(x = x_st + dx * 5, y = y_st + dy * 0)

button10 = tk.Button(window, width = w, height = h, command = button10Click, text = '----')
button10.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button11 = tk.Button(window, width = w, height = h, command = button11Click, text = '----')
button11.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button12 = tk.Button(window, width = w, height = h, command = button12Click, text = '----')
button12.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button13 = tk.Button(window, width = w, height = h, command = button13Click, text = '----')
button13.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button14 = tk.Button(window, width = w, height = h, command = button14Click, text = '----')
button14.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button15 = tk.Button(window, width = w, height = h, command = button15Click, text = '----')
button15.pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
button10.place(x = x_st + dx * 0, y = y_st + dy * 1)
button11.place(x = x_st + dx * 1, y = y_st + dy * 1)
button12.place(x = x_st + dx * 2, y = y_st + dy * 1)
button13.place(x = x_st + dx * 3, y = y_st + dy * 1)
button14.place(x = x_st + dx * 4, y = y_st + dy * 1)
button15.place(x = x_st + dx * 5, y = y_st + dy * 1)

# 加入 Text
text1 = tk.Text(window, width = 100, height = 42)  # 放入多行輸入框
text1.pack()
text1.place(x = x_st + dx * 0, y = y_st + dy * 2 + 10)

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

