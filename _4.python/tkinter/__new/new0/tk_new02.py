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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線

'''


import tkinter.messagebox as msg

response = msg.askyesno('糟糕了!!!', '還好嗎？')

if (response == True):
	print('還 OK')
else:
	print('有點麻煩')


print('------------------------------------------------------------')	#60個



import tkinter as tk

window=tk.Tk()
tk.Label(window, text='紅', bg='red', width=20).pack()
tk.Label(window, text='藍', bg='green', width=20).pack()
tk.Label(window, text='綠', bg='blue', width=20).pack()
window.mainloop()



print('------------------------------------------------------------')	#60個



window = tk.Tk()

topping = {0:'海苔', 1:'糖心蛋', 2:'豆芽菜', 3:'叉燒'}

check_value={}

for i in range(len(topping)):
	check_value[i] = tk.BooleanVar()
	tk.Checkbutton(window, variable=check_value[i],

text = topping[i]).pack(anchor=tk.W)

def buy():
	for i in check_value:
		if check_value[i].get() == True:
			print(topping[i])

tk.Button(window, text='點餐', command=buy).pack()

window.mainloop()


print('------------------------------------------------------------')	#60個

import tkinter as tk
window=tk.Tk()
topping = {0:'海苔', 1:'糖心蛋', 2:'豆芽菜', 3:'叉燒'}
check_value={}
for i in range(len(topping)):
	check_value[i] = tk.BooleanVar()
	tk.Checkbutton(window, variable=check_value[i], text = topping[i]).pack(anchor=tk.W)
window.mainloop()

"""
請問迴圈裡面 check_value [i] = tk.BooleanVar() 這一行，能否舉個例子，假設第 0 個按鈕被勾選，check_value 長怎樣；假設第 0、1 個按鈕被勾選，check_value 長怎樣 ... 依此類推
"""

print('------------------------------------------------------------')	#60個

window = tk.Tk()
radio_value = tk.IntVar()
radio_value.set(1)
lunch = {0:'A 套餐',1:'B 套餐',2:'C 套餐'}
tk.Radiobutton(window, text = lunch[0], variable = radio_value, value = 0).pack()
tk.Radiobutton(window, text = lunch[1], variable = radio_value, value = 1).pack()
tk.Radiobutton(window, text = lunch[2], variable = radio_value, value = 2).pack()
def buy():
	value = radio_value.get()
	print(lunch[value])

tk.Button(window, text='點餐', command=buy).pack()
window.mainloop()


print('------------------------------------------------------------')	#60個

window = tk.Tk()
string = tk.StringVar()
entry = tk.Entry(window, textvariable=string).pack()
label = tk.Label(window, textvariable=string).pack()
window.mainloop()


print('------------------------------------------------------------')	#60個

window = tk.Tk()

def fileopen():
	print('進行開啟檔案的處理')

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar)

menubar.add_cascade(label=' 檔案', menu=filemenu)

filemenu.add_command(label='開啟檔案', command=fileopen)

window.config(menu=menubar)

window.mainloop()


print('------------------------------------------------------------')	#60個

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





"""
請參考以下程式，幫我利用 tkinter 生成選單視窗，需要的檔案結構如下：

檔案：
	開啟新檔
	開啟舊檔
	另存為
	結束
編輯：
	剪下
	複製
	貼上
說明：
	關於本程式

----------- 以下是參考的程式架構 --------
"""
""" TBD
import tkinter as tk
import tkinter.filedialog as fd
window = tk.Tk()
def open():
	filename = fd.askopenfilename()
print('open file => ' + filename)
def exit():
	window.destroy()
def find():
	print('find !')
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
window.mainloop()

"""
'''

print("------------------------------------------------------------")  # 60個




window.mainloop()



