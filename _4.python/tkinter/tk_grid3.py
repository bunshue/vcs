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
title = "這是主視窗"
window.title(title)

button1 = tk.Button(window, text="這是按鈕一", width=20)
button1.grid(row=0, column=0, padx=5, pady=5)
button2 = tk.Button(window, text="這是按鈕二", width=20)
button2.grid(row=0, column=1, padx=5, pady=5)
button3 = tk.Button(window, text="這是按鈕三", width=20)
button3.grid(row=0, column=2, padx=5, pady=5)
button4 = tk.Button(window, text="這是按鈕四", width=20)
button4.grid(row=1, column=0, padx=5, pady=5)
button5 = tk.Button(window, text="這是按鈕五", width=20)
button5.grid(row=1, column=1, padx=5, pady=5)
button6 = tk.Button(window, text="這是按鈕六", width=20)
button6.grid(row=1, column=2, padx=5, pady=5)

window.mainloop()


'''
button01 = tk.Button(window, text="第0排第0個", width=20)
button01.grid(row=0, column=0, padx=5, pady=5)
button02 = tk.Button(window, text="第0排第1個", width=20)
button02.grid(row=0, column=1, padx=5, pady=5)
button03 = tk.Button(window, text="第0排第2個", width=20)
button03.grid(row=0, column=2, padx=5, pady=5)

button04 = tk.Button(window, text="第1排第0個", width=20)
button04.grid(row=1, column=0, padx=5, pady=5)
button05 = tk.Button(window, text="第1排第1個", width=20)
button05.grid(row=1, column=1, padx=5, pady=5)
button06 = tk.Button(window, text="第1排第2個", width=20)
button06.grid(row=1, column=2, padx=5, pady=5)

'''

