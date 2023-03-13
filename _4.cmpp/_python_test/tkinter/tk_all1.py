# Python 測試 tkinter 1

import tkinter as tk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 600
size = str(w)+'x'+str(h)
window.geometry(size)

# 設定主視窗標題
title = "圖形化範例-BMI測量"
window.title(title)

tk.Label(window, text='紅', bg='red', width=20).pack()
tk.Label(window, text='綠', bg='green', width=20).pack()
tk.Label(window, text='藍', bg='blue', width=20).pack()


topping = {0:'海苔', 1:'水煮蛋', 2:'豆芽菜', 3:'叉燒'}

check_value={}

for i in range(len(topping)):
	check_value[i] = tk.BooleanVar()
	tk.Checkbutton(window, variable=check_value[i], text = topping[i]).pack(anchor=tk.W)

def buy():
	for i in check_value:
		if check_value[i].get() == True:
			print(topping[i])

tk.Button(window, text='點菜', command=buy).pack()



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




string = tk.StringVar()
entry = tk.Entry(window, textvariable=string).pack()
label = tk.Label(window, textvariable=string).pack()



'''
import tkinter as tk

import tkinter.messagebox as msg

window = tk.Tk()

window.withdraw()

response = msg.askyesno('糟糕!!!', '還好嗎？')


if(response==True):
	print('沒問題');
else:
	print('有問題');
	





import tkinter as tk

window = tk.Tk()

def supermode():
	print('super mode!')

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar)

filemenu.add_command(label='supermode', command=supermode)

menubar.add_cascade(label='Operation', menu=filemenu)

window.config(menu=menubar)






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

menubar.add_cascade(label='File', menu=filemenu)

filemenu.add_command(label='open', command=open)

filemenu.add_separator()

filemenu.add_command(label='exit', command=exit)

editmenu = tk.Menu(menubar)

menubar.add_cascade(label='Edit', menu=editmenu)

editmenu.add_command(label='find', command=find)

window.config(menu=menubar)



'''

	
