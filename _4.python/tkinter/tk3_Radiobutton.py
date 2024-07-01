"""

Radiobutton


"""

import sys
import glob
import tkinter as tk
from tkinter import ttk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Radiobutton 1")

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def do_select1():
        selection = var.get()                               # 獲得音樂選項
        print('你選擇了 :', selection)

# 建立音樂選項鈕內容的串列
musics = [('AAA', 1),                            # 音樂選單串列
          ('BBB', 2),
          ('CCC', 3)]

# 建立選項紐Radiobutton
var = tk.StringVar()                                       # 設定以字串表示選單編號
var.set('1')                                            # 預設音樂是1
for music, num in musics:                               # 建立系列選項紐
    rb = ttk.Radiobutton(window, text=music, variable=var, value=num)
    rb.pack()

tk.Button(window, text='選擇', command=do_select1).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


rb1 = ttk.Radiobutton(
	window,
	text = 'AAA',
	value = 1,
	variable = 'this is a lion-mouse',
	command = lambda: print('你按了 AAA'))
rb1.pack()

rb2 = ttk.Radiobutton(window, text = 'BBB', value = 1, variable = 'aaaaaa')
rb2.pack()

def radio_func():
        print('你按了 CCC/DDD')
# data
radio_string = tk.StringVar()

# widgets
rb3 = ttk.Radiobutton(
	window, 
	text = 'CCC', 
	value = 'C', 
	command = radio_func, 
	variable = radio_string)
rb3.pack()

rb4 = ttk.Radiobutton(
	window, 
	text = 'DDD', 
	value = 'D', 
	command = radio_func, 
	variable = radio_string)
rb4.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


def choose1():
    msg.set("你選擇了 :" + choice1.get())

choice1 = tk.StringVar()
msg = tk.StringVar()

rb1 = tk.Radiobutton(window, text="AAA", value="aaa", variable=choice1, command=choose1)
rb1.pack()
rb2 = tk.Radiobutton(window, text="BBB", value="bbb", variable=choice1, command=choose1)
rb2.pack()
rb3 = tk.Radiobutton(window, text="CCC", value="ccc", variable=choice1, command=choose1)
rb3.pack()

lblmsg = tk.Label(window, fg="red", textvariable=msg)
lblmsg.pack()

rb1.select()#預設項目

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
    rb = tk.Radiobutton(frame1, text = mp3, variable = choice2, value = mp3, command = choose2)
    if(index == 0):  #選取第1個選項按鈕
        rb.select()
        playsong = preplaysong = mp3
    rb.grid(row = index, column = 0, sticky = 'w')
    index += 1

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def do_select2():
        value = radio_value.get()
        ##print(lunch[value])
        print('你選擇了 : ' + lunch[value])

lunch = {0:'AAA',1:'BBB',2:'CCC'}

radio_value = tk.IntVar()
radio_value.set(2)  # 預選第2項

tk.Radiobutton(window, text = lunch[0], variable = radio_value, value = 0).pack()
tk.Radiobutton(window, text = lunch[1], variable = radio_value, value = 1).pack()
tk.Radiobutton(window, text = lunch[2], variable = radio_value, value = 2).pack()

tk.Button(window, text='選擇', command=do_select2).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

v = tk.IntVar()
tk.Radiobutton(window, text="One", variable=v, value=1).pack()
tk.Radiobutton(window, text="Two", variable=v, value=2).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

MODES = [
    ("AAA", "aaa"),
    ("BBB", "bbb"),
    ("CCC", "ccc"),
    ("DDD", "ddd"),
]

v = tk.StringVar()
v.set("L") # initialize

for text, mode in MODES:
    rb = tk.Radiobutton(window, text=text, variable=v, value=mode)
    rb.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Radiobutton 2")


def rb_click():
    selected_item = area.get()
    lab_result.config(text=AREA_OPTIONS[selected_item][0])

AREA_OPTIONS=(('AAA',0),('BBB',1),('CCC',2))
area = tk.IntVar()
area.set(0)

for item, value in AREA_OPTIONS:
    rb = tk.Radiobutton(window, text=item, variable=area, value=value, command=rb_click)
    rb.pack()

lab_result = tk.Label(window, fg='black')
lab_result.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


def select():
    print('你的選項是 :', var.get())


place = [('AAA', 1), ('BBB', 2), ('CCC', 3),('DDD', 4)]

var = tk.IntVar()
var.set(3)
for item, val in place:
    tk.Radiobutton(window, text = item, value = val,
        variable = var, padx = 20,
        command = select).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def select():
    print('你選擇了 :', var.get())

place = [('AAA', 1), ('BBB', 2),('CCC', 3), ('DDD', 4)]

var = tk.IntVar()
var.set(2)
for item, val in place:
    tk.Radiobutton(window, text = item, value = val,
        variable = var, padx = 20,
        command = select).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


""" some fail
def printSelection1():
    label.config(text="你是" + var.get())

var = tk.StringVar()
var.set("男生")                           # 預設選項                       

label = tk.Label(window,text="尚未選擇", bg="lightyellow",width=30)
label.pack()

rb1 = tk.Radiobutton(window,text="男生",
                  variable=var,value='男生',
                  command=printSelection1).pack()
rb2 = tk.Radiobutton(window,text="女生",
                  variable=var,value='女生',
                  command=printSelection1).pack()
"""
separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def printSelection2():
    print(cities[var.get()])

cities = {0:"AAA", 1:"BBB", 2:"CCC",3:"DDD"}

var = tk.IntVar()
var.set(0)                              # 預設選項                       

for val, city in cities.items():        # 建立選項紐    
    tk.Radiobutton(window,
                text=city,
                variable=var,value=val,
                command=printSelection2).pack()
    
separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def printSelection3():
    print(cities[var.get()])            # 列出所選城市

cities = {0:"AAA",1:"BBB",2:"CCC",3:"DDD"}

var = tk.IntVar()
var.set(0)                              # 預設選項                       

for val, city in cities.items():        # 建立選項紐    
    tk.Radiobutton(window,
                text=city,
                indicatoron = 0,        # 用盒子取代選項紐
                width=30,
                variable=var,value=val,
                command=printSelection3).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x800")
window.title("Radiobutton 3")


def select():
    print('你的選項是 :', var.get())


place = [('AAA', 1), ('BBB', 2), ('CCC', 3)]

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

place = [('AAA', 1), ('BBB', 2), ('CCC', 3)]

var = tk.IntVar()
var.set(3)
for item, val in place:
    tk.Radiobutton(window, text = item, value = val,
        variable = var, padx = 20,
        command = select).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


def printSelection4():
    label.config(text="你是" + var.get())

var = tk.StringVar()
var.set("男生")                           # 預設選項                       

label = tk.Label(window,text="尚未選擇", bg="lightyellow",width=30)
label.pack()

rb1 = tk.Radiobutton(window,text="男生",
                  variable=var,value='男生',
                  command=printSelection4).pack()
rb2 = tk.Radiobutton(window,text="女生",
                  variable=var,value='女生',
                  command=printSelection4).pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


def printSelection5():
    print(cities[var.get()])            # 列出所選城市

cities = {0:"AAA",1:"BBB",2:"CCC",3:"DDD"}

var = tk.IntVar()
var.set(0)                              # 預設選項                       

for val, city in cities.items():        # 建立選項紐    
    tk.Radiobutton(window,
                text=city,
                variable=var,value=val,
                command=printSelection5).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print('------------------------------------------------------------')	#60個


def printSelection6():
    print(cities[var.get()])            # 列出所選城市


cities = {0:"AAA",1:"BBB",2:"CCC",3:"DDD"}

var = tk.IntVar()
var.set(0)                              # 預設選項                       

for val, city in cities.items():        # 建立選項紐    
    tk.Radiobutton(window,
                text=city,
                indicatoron = 0,        # 用盒子取代選項紐
                width=30,
                variable=var,value=val,
                command=printSelection6).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from PIL import ImageTk, Image


def printSelection7():
    label.config(text="你選的是" + var.get())


filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"


window = tk.Tk()
window.geometry("600x800")
window.title("Radiobutton 4")

# 檔案 => ImageTk影像
tk_image1 = ImageTk.PhotoImage(file="__new/star.gif")
tk_image2 = ImageTk.PhotoImage(file="__new/moon.gif")
tk_image3 = ImageTk.PhotoImage(file="__new/sun.gif")

var = tk.StringVar()  # 選項紐綁定的變數
var.set("星星")  # 預設選項是男生

label = tk.Label(window, text="這是預設,尚未選擇", bg="lightyellow", width=30)
label.pack()

rb1 = tk.Radiobutton(
    window, image=tk_image1, variable=var, value="星星", command=printSelection7  # 星星選項鈕
)
rb1.pack()

rb2 = tk.Radiobutton(
    window, image=tk_image2, variable=var, value="月亮", command=printSelection7  # 月亮選項鈕
)
rb2.pack()

rb3 = tk.Radiobutton(
    window, image=tk_image3, variable=var, value="太陽", command=printSelection7  # 太陽選項鈕
)
rb3.pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print('------------------------------------------------------------')	#60個

def printSelection8():
    label.config(text="你選的是" + var.get())


# 檔案 => ImageTk影像
tk_image1 = ImageTk.PhotoImage(file="__new/star.gif")
tk_image2 = ImageTk.PhotoImage(file="__new/moon.gif")
tk_image3 = ImageTk.PhotoImage(file="__new/sun.gif")

var = tk.StringVar()  # 選項紐綁定的變數
var.set("星星")  # 預設選項是男生

label = tk.Label(window, text="這是預設,尚未選擇", bg="lightyellow", width=30)
label.pack()

rb1 = tk.Radiobutton(
    window,
    image=tk_image1,  # 星星選項鈕
    text="星星",
    compound=tk.RIGHT,
    variable=var,
    value="星星",
    command=printSelection8,
)
rb1.pack()

rb2 = tk.Radiobutton(
    window,
    image=tk_image2,  # 月亮選項鈕
    text="月亮",
    compound=tk.RIGHT,
    variable=var,
    value="月亮",
    command=printSelection8,
)
rb2.pack()

rb3 = tk.Radiobutton(
    window,
    image=tk_image3,  # 太陽選項鈕
    text="太陽",
    compound=tk.RIGHT,
    variable=var,
    value="太陽",
    command=printSelection8,
)
rb3.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

""" lack pic
def more():
    if choice.get()==0:
        str1="牛是對少部份牛科動物的統稱 \n\
              包括和人類習習相關的黃牛、水牛和氂牛" 
        print("cattle的簡介",str1)
    else:
        str2="鹿有別於牛、羊等的動物。 \n \
              包括麝科和鹿科動物"
        print("deer的簡介",str2)
    
window = tk.Tk()
window.geometry("600x800")
window.title('messagebox 6')

lb = tk.Label(window,text="請點選想了解的動物簡介:").pack()
choice = tk.IntVar()
choice.set(0)

pic1 = tk.PhotoImage(file="cattle.gif")
pic2 = tk.PhotoImage(file="deer.gif")

tk.Radiobutton(window,image=pic1,variable=choice,value=0).pack()
tk.Radiobutton(window,image=pic2,variable=choice,value=1).pack()
tk.Button(window,text="進一步了解", command=more).pack()

window.mainloop()
"""

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title("my window")
window.geometry("200x200")

var = tk.StringVar()
l = tk.Label(window, bg="yellow", width=20, text="empty")
l.pack()


def print_selection():
    l.config(text="you have selected " + var.get())


rb1 = tk.Radiobutton(
    window, text="Option A", variable=var, value="A", command=print_selection
)
rb1.pack()

rb2 = tk.Radiobutton(
    window, text="Option B", variable=var, value="B", command=print_selection
)
rb2.pack()

rb3 = tk.Radiobutton(
    window, text="Option C", variable=var, value="C", command=print_selection
)
rb3.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



def checkbutton_select8():
    print("你的選項是 :", var.get())


tk.Label(window, text="請問您的最高學歷: ", justify=tk.LEFT, padx=20).pack()
place = [("博士", 1), ("碩士", 2), ("大學", 3), ("高中", 4)]
var = tk.IntVar()
var.set(2)
for item, val in place:
    tk.Radiobutton(
        window, text=item, value=val, variable=var, padx=20, command=checkbutton_select8
    ).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def checkbutton_select9():
    print("你的選項是 :", var.get())


tk.Label(window, text="請選擇精通的程式語言: ", justify=tk.LEFT, padx=20).pack()
place = [("Python語言", 1), ("C語言", 2), ("C++語言", 3), ("Java語言", 4)]
var = tk.IntVar()
var.set(3)

for item, val in place:
    tk.Radiobutton(
        window, text=item, value=val, variable=var, padx=20, command=checkbutton_select9
    ).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個



