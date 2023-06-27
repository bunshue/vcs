# Python 測試 tkinter : Radiobutton

import tkinter as tk
from tkinter import ttk

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

radio1 = ttk.Radiobutton(
	window, 
	text = 'Radiobutton 1', 
	value = 1, 
	variable = 'this is a lion-mouse',
	command = lambda: print('aaa'))
radio1.pack()

radio2 = ttk.Radiobutton(window, text = 'Radiobutton 2', value = 1, variable = 'aaaaaa')
radio2.pack()

def radio_func():
	#print(check_bool.get())
        print('你按了Radiobutton')
# data
radio_string = tk.StringVar()

# widgets
exercise_radio1 = ttk.Radiobutton(
	window, 
	text = 'Radio A', 
	value = 'A', 
	command = radio_func, 
	variable = radio_string)
exercise_radio2 = ttk.Radiobutton(
	window, 
	text = 'Radio B', 
	value = 'B', 
	command = radio_func, 
	variable = radio_string)

# layout
exercise_radio1.pack()
exercise_radio2.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

def choose():
    msg.set("你最喜歡的球類運動：" + choice.get())

choice = tk.StringVar()
msg = tk.StringVar()
label = tk.Label(window, text="選擇最喜歡的球類運動：")
label.pack()
item1 = tk.Radiobutton(window, text="足球", value="足球", variable=choice, command=choose)
item1.pack()
item2 = tk.Radiobutton(window, text="籃球", value="籃球", variable=choice, command=choose)
item2.pack()
item3 = tk.Radiobutton(window, text="棒球", value="棒球", variable=choice, command=choose)
item3.pack()
lblmsg = tk.Label(window, fg="red", textvariable=msg)
lblmsg.pack()
item1.select()
choose()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

# RadioButton測試
tk.Label(text='RadioButton測試').pack()
radio_value = tk.IntVar()
radio_value.set(1)
lunch = {0:'A套餐',1:'B套餐',2:'C套餐'}
tk.Radiobutton(text = lunch[0], variable = radio_value, value = 0).pack()
tk.Radiobutton(text = lunch[1], variable = radio_value, value = 1).pack()
tk.Radiobutton(text = lunch[2], variable = radio_value, value = 2).pack()
def buy():
	value = radio_value.get()
	print(lunch[value])

tk.Button(window, text='點菜', command=buy).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

# RadioButton測試
tk.Label(text='RadioButton測試').pack()

v = tk.IntVar()
tk.Radiobutton(window, text="One", variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(window, text="Two", variable=v, value=2).pack(anchor=tk.W)

MODES = [
    ("Monochrome", "1"),
    ("Grayscale", "L"),
    ("True color", "RGB"),
    ("Color separation", "CMYK"),
]

v = tk.StringVar()
v.set("L") # initialize

for text, mode in MODES:
    b = tk.Radiobutton(window, text=text, variable=v, value=mode)
    b.pack(anchor=tk.W)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

window.mainloop()

