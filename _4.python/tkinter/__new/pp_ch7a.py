import sys

import tkinter as tk

print('------------------------------------------------------------')	#60個

base = tk.Tk()

base.mainloop()

print('------------------------------------------------------------')	#60個

base = tk.Tk()

base.mainloop()

button = tk.Button(base, text='PUSH!')

button.pack()

print('------------------------------------------------------------')	#60個

base = tk.Tk()

button1 = tk.Button(base, text='push1')

button2 = tk.Button(base, text='push2')

button3 = tk.Button(base, text='push3')

button1.pack()

button2.pack()

button3.pack()


print('------------------------------------------------------------')	#60個

base = tk.Tk()

button1 = tk.Button(base, text='push1', width=20).pack()

button2 = tk.Button(base, text='push2', width=20).pack(side=tk.LEFT)

button3 = tk.Button(base, text='push3', width=20).pack(side=tk.RIGHT)


print('------------------------------------------------------------')	#60個

base = tk.Tk()

button1 = tk.Button(base, text='push1')

button2 = tk.Button(base, text='push2')

button3 = tk.Button(base, text='push3')

button1.grid(row=0, column=0)

button2.grid(row=0, column=1)

button3.grid(row=1, column=1)

print('------------------------------------------------------------')	#60個

base = tk.Tk()

button1 = tk.Button(base, text='push1')

button2 = tk.Button(base, text='push2')

button3 = tk.Button(base, text='push3')

button1.place(x=0, y=0)

button2.place(x=50, y=30)

button3.place(x=100, y=60)

print('------------------------------------------------------------')	#60個

base = tk.Tk()

def push():

	print('MELON !')

button = tk.Button(base, text="WATER", command=push).pack()

print('------------------------------------------------------------')	#60個

base=tk.Tk()

tk.Label(base, text='紅', bg='red', width=20).pack()

tk.Label(base, text='綠', bg='green', width=20).pack()

tk.Label(base, text='藍', bg='blue', width=20).pack()

print('------------------------------------------------------------')	#60個

base = tk.Tk()

topping = {0:'海苔', 1:'水煮蛋', 2:'豆芽菜', 3:'叉燒'}

check_value={}

for i in range(len(topping)):

	check_value[i] = tk.BooleanVar()

	tk.Checkbutton(base, variable=check_value[i], text = topping[i]).pack(anchor=tk.W)




def buy():

	for i in check_value:

		if check_value[i].get() == True:

			print(topping[i])



tk.Button(base, text='點菜', command=buy).pack()

print('------------------------------------------------------------')	#60個

base = tk.Tk()

radio_value = tk.IntVar()

radio_value.set(1)

lunch = {0:'A套餐',1:'B套餐',2:'C套餐'}

tk.Radiobutton(text = lunch[0], variable = radio_value, value = 0).pack()

tk.Radiobutton(text = lunch[1], variable = radio_value, value = 1).pack()

tk.Radiobutton(text = lunch[2], variable = radio_value, value = 2).pack()

def buy():

	value = radio_value.get()

	print(lunch[value])


tk.Button(base, text='點菜', command=buy).pack()

print('------------------------------------------------------------')	#60個

import tkinter.messagebox as msg

base = tk.Tk()

base.withdraw()

response = msg.askyesno('糟糕!!!', '還好嗎？')

if(response==True):
	print('沒問題');
else:
	print('有問題');
	
print('------------------------------------------------------------')	#60個

base = tk.Tk()

string = tk.StringVar()

entry = tk.Entry(base, textvariable=string).pack()

label = tk.Label(base, textvariable=string).pack()

print('------------------------------------------------------------')	#60個

base = tk.Tk()

def supermode():

	print('super mode!')

menubar = tk.Menu(base)

filemenu = tk.Menu(menubar)

filemenu.add_command(label='supermode', command=supermode)

menubar.add_cascade(label='Operation', menu=filemenu)

base.config(menu=menubar)

print('------------------------------------------------------------')	#60個

import tkinter.filedialog as fd

base = tk.Tk()

def open():
	filename = fd.askopenfilename()
	print('open file => ' + filename)

def exit():
	base.destroy()

def find():
	print('find ! ')


menubar = tk.Menu(base)

filemenu = tk.Menu(menubar)

menubar.add_cascade(label='File', menu=filemenu)

filemenu.add_command(label='open', command=open)

filemenu.add_separator()

filemenu.add_command(label='exit', command=exit)

editmenu = tk.Menu(menubar)

menubar.add_cascade(label='Edit', menu=editmenu)

editmenu.add_command(label='find', command=find)

base.config(menu=menubar)

print('------------------------------------------------------------')	#60個



