# Python 測試 tkinter : Checkbutton

def choose():
    str = "你喜歡的球類運動："
    for i in range(0, len(choice)):
        if(choice[i].get() == 1):
            str = str + ball[i] + " "
    print(str)
    msg.set(str)

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

from tkinter import ttk
# checkbutton
check1 = ttk.Checkbutton(
	window, 
	text = 'checkbox 1', 
	command = lambda: print('ccccc'),
	variable = 'ccccc',
	onvalue = 10,
	offvalue = 5)
check1.pack()

check2 = ttk.Checkbutton(
	window, 
	text = 'Checkbox 2',
	command = '')
check2.pack()





separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線


check_bool = tk.BooleanVar()

exercise_check = ttk.Checkbutton(
	window, 
	text = 'exercise check', 
	variable = check_bool, 
	#command = lambda: print(radio_string.get()))
        command = lambda: print('你按了check_button'))
exercise_check.pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=5, pady=5)  #分隔線



window.mainloop()

