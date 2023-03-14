# Python 測試 tkinter 1

import tkinter as tk

window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
size = str(w)+'x'+str(h)
window.geometry(size)

# 設定主視窗標題
title = "這是主視窗"
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



def clickme():
    global count
    count += 1
    labeltext.set("你按我 " + str(count) + " 次了！")
    if(btntext.get() == "按我！"):
        btntext.set("回復原來文字！")
    else:
        btntext.set("按我！")


labeltext = tk.StringVar()
btntext = tk.StringVar()
count = 0
label1 = tk.Label(window, fg="red", textvariable=labeltext)
labeltext.set("歡迎光臨Tkinter！")
label1.pack()

button1 = tk.Button(window, textvariable=btntext, command=clickme)
btntext.set("按我！")
button1.pack()




frame1 = tk.Frame(window)
frame1.pack()

label1=tk.Label(frame1, text="標籤一：")
entry1 = tk.Entry(frame1)
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)

frame2 = tk.Frame(window)
frame2.pack()

button1 = tk.Button(frame2, text="確定")
button2 = tk.Button(frame2, text="取消")
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)



w = tk.Canvas(window, width=200, height=100)
w.pack()
w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
w.create_rectangle(50, 25, 150, 75, fill="blue")



#w = tk.Message(window, text="this is a relatively long message")    #自動換行
w = tk.Message(window, text="this is a relatively long message", width=50)  #限定寬度
w.pack()



#GroupBox之大小, 若小於內附控件大小, 則會撐大
w = 10
h = 10
group = tk.LabelFrame(window, text="Group", padx=w, pady=h)

#GroupBox之位置, 相較於目前表單位置
x_st = 0
y_st = 0
group.pack(padx=x_st, pady=y_st)

#GroupBox內 放幾個控件
w = tk.Entry(group).pack()
w = tk.Entry(group).pack()
w = tk.Entry(group).pack()
w = tk.Entry(group).pack()




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

	
