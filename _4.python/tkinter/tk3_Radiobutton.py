"""

Radiobutton


"""

import sys
import glob
import tkinter as tk
from tkinter import ttk

print("------------------------------------------------------------")  # 60個

# 建立主視窗
window = tk.Tk()

# 設定主視窗大小
w = 700
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

rb1 = ttk.Radiobutton(
	window,
	text = 'AAAA',
	value = 1,
	variable = 'this is a lion-mouse',
	command = lambda: print('你按了 AAAA'))
rb1.pack()

rb2 = ttk.Radiobutton(window, text = 'BBBB', value = 1, variable = 'aaaaaa')
rb2.pack()

def radio_func():
        print('你按了 CCCC/DDDD')
# data
radio_string = tk.StringVar()

# widgets
rb3 = ttk.Radiobutton(
	window, 
	text = 'CCCC', 
	value = 'C', 
	command = radio_func, 
	variable = radio_string)
rb3.pack()

rb4 = ttk.Radiobutton(
	window, 
	text = 'DDDD', 
	value = 'D', 
	command = radio_func, 
	variable = radio_string)
rb4.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


def choose1():
    msg.set("你最喜歡的球類運動：" + choice1.get())

choice1 = tk.StringVar()
msg = tk.StringVar()
item1 = tk.Radiobutton(window, text="足球", value="足球", variable=choice1, command=choose1)
item1.pack()
item2 = tk.Radiobutton(window, text="籃球", value="籃球", variable=choice1, command=choose1)
item2.pack()
item3 = tk.Radiobutton(window, text="棒球", value="棒球", variable=choice1, command=choose1)
item3.pack()
lblmsg = tk.Label(window, fg="red", textvariable=msg)
lblmsg.pack()

item1.select()

choose1()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def choose2():
    print('你選擇了 : ' + choice2.get())

frame1 = tk.Frame(window)  # mp3 歌曲容器
frame1.pack()

source_dir = 'C:/_git/vcs/_1.data/______test_files1/_mp3/'

mp3files = glob.glob(source_dir + "*.mp3")

playsong = preplaysong = ""
index = 0
choice2 = tk.StringVar()

for mp3 in mp3files:  #建立歌曲選項按鈕
    rbtem = tk.Radiobutton(frame1, text = mp3, variable = choice2, value = mp3, command = choose2)
    if(index == 0):  #選取第1個選項按鈕
        rbtem.select()
        playsong = preplaysong = mp3
    rbtem.grid(row = index, column = 0, sticky = 'w')
    index += 1

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def do_select():
        value = radio_value.get()
        print(lunch[value])

lunch = {0:'AAAA',1:'BBBB',2:'CCCC'}

radio_value = tk.IntVar()
radio_value.set(2)  # 預選第2項

tk.Radiobutton(window, text = lunch[0], variable = radio_value, value = 0).pack()
tk.Radiobutton(window, text = lunch[1], variable = radio_value, value = 1).pack()
tk.Radiobutton(window, text = lunch[2], variable = radio_value, value = 2).pack()

tk.Button(window, text='選擇', command=do_select).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

v = tk.IntVar()
tk.Radiobutton(window, text="One", variable=v, value=1).pack()
tk.Radiobutton(window, text="Two", variable=v, value=2).pack()

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
    b.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

# 建立主視窗
window = tk.Tk()

# 設定主視窗大小
w = 700
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

def radbut_click():
    selected_item = area.get()
    lab_result.config(text=AREA_OPTIONS[selected_item][0])

print("試題與測驗分析程式")

AREA_OPTIONS=(('屏東縣',0),('高雄市',1),('台南市',2),('台東縣',3))
area = tk.IntVar()
area.set(0)

for item, value in AREA_OPTIONS:
    radbut = tk.Radiobutton(window, text=item, variable=area, value=value, command=radbut_click)
    radbut.pack()

lab_result = tk.Label(window, fg='black')
lab_result.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

print('程式語言能力調查：')


def select():
    print('你的選項是 :', var.get())


place = [('Python語言', 1), ('C語言', 2), ('C++語言', 3),('Java語言', 4)]

var = tk.IntVar()
var.set(3)
for item, val in place:
    tk.Radiobutton(window, text = item, value = val,
        variable = var, padx = 20,
        command = select).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def select():
    print('你的選項是 :', var.get())

place = [('博士', 1), ('碩士', 2),('大學', 3), ('高中', 4)]

var = tk.IntVar()
var.set(2)
for item, val in place:
    tk.Radiobutton(window, text = item, value = val,
        variable = var, padx = 20,
        command = select).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


""" some fail
def printSelection():
    label.config(text="你是" + var.get())

var = tk.StringVar()
var.set("男生")                           # 預設選項                       

label = tk.Label(window,text="尚未選擇", bg="lightyellow",width=30)
label.pack()

rb1 = tk.Radiobutton(window,text="男生",
                  variable=var,value='男生',
                  command=printSelection).pack()
rb2 = tk.Radiobutton(window,text="女生",
                  variable=var,value='女生',
                  command=printSelection).pack()
"""
separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def printSelection():
    print(cities[var.get()])            # 列出所選城市

cities = {0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"香港"}

var = tk.IntVar()
var.set(0)                              # 預設選項                       

for val, city in cities.items():        # 建立選項紐    
    tk.Radiobutton(window,
                text=city,
                variable=var,value=val,
                command=printSelection).pack()
    
separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def printSelection():
    print(cities[var.get()])            # 列出所選城市

cities = {0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"香港"}

var = tk.IntVar()
var.set(0)                              # 預設選項                       

for val, city in cities.items():        # 建立選項紐    
    tk.Radiobutton(window,
                text=city,
                indicatoron = 0,        # 用盒子取代選項紐
                width=30,
                variable=var,value=val,
                command=printSelection).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print('------------------------------------------------------------')	#60個

# 建立主視窗
window = tk.Tk()

# 設定主視窗大小
w = 700
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
print("------------------------------------------------------------")  # 60個


def select():
    print('你的選項是 :', var.get())


place = [('宜蘭', 1), ('台北', 2), ('高雄', 3)]

var = tk.IntVar()
var.set(3)
for item, val in place:
    tk.Radiobutton(window, text = item, value = val,
        variable = var, padx = 20,
        command = select).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

print("運動類型調查表")


def select():
    print('你的選項是 :', var.get())

place = [('籃球', 1), ('桌球', 2), ('游泳', 3)]

var = tk.IntVar()
var.set(3)
for item, val in place:
    tk.Radiobutton(window, text = item, value = val,
        variable = var, padx = 20,
        command = select).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


def printSelection():
    label.config(text="你是" + var.get())

var = tk.StringVar()
var.set("男生")                           # 預設選項                       

label = tk.Label(window,text="尚未選擇", bg="lightyellow",width=30)
label.pack()

rb1 = tk.Radiobutton(window,text="男生",
                  variable=var,value='男生',
                  command=printSelection).pack()
rb2 = tk.Radiobutton(window,text="女生",
                  variable=var,value='女生',
                  command=printSelection).pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


def printSelection():
    print(cities[var.get()])            # 列出所選城市

cities = {0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"香港"}

var = tk.IntVar()
var.set(0)                              # 預設選項                       

for val, city in cities.items():        # 建立選項紐    
    tk.Radiobutton(window,
                text=city,
                variable=var,value=val,
                command=printSelection).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print('------------------------------------------------------------')	#60個


def printSelection():
    print(cities[var.get()])            # 列出所選城市


cities = {0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"香港"}

var = tk.IntVar()
var.set(0)                              # 預設選項                       

for val, city in cities.items():        # 建立選項紐    
    tk.Radiobutton(window,
                text=city,
                indicatoron = 0,        # 用盒子取代選項紐
                width=30,
                variable=var,value=val,
                command=printSelection).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


