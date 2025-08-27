"""
TextVariable

"""

import sys
import time
import random
import datetime
import tkinter as tk
from tkinter import ttk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("tkinter的變數類別")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

# 建立變數

"""
tkinter 控件的變數類別(4)
tk.StringVar() 字串，
tk.IntVar() 整數，預設值為 0
tk.DoubleVar() 浮點數，預設值為 0.0
tk.Boolean()  # 布林值變數，True是1， False是0 fail
"""

W = 200
H = 200
w = 12
h = 2
count = 0
number_double = 0.0
variable_string = tk.StringVar()  # 建立一個字串變數, 預設值為空字串
variable_int = tk.IntVar()  # 宣告variable_int為整數物件
variable_double = tk.DoubleVar()  # 宣告variable_double為浮點數物件
variable_boolean = tk.BooleanVar()  # 布林值變數，True是1， False是0 fail


def read_write_tk_variables():
    # Variable
    cc = variable_string.get()
    print("取得 variable_string 的資料 :", cc)
    cc = variable_int.get()
    print("取得 variable_int 的資料 :", cc)
    cc = variable_double.get()
    print("取得 variable_double 的資料 :", cc)
    cc = variable_boolean.get()
    print("取得 variable_boolean 的資料 :", cc)

    global count
    global number_double
    count += 1
    number_double += 0.167
    number_double = round(number_double, 2)
    string_mesg = "歡迎來到美國" + str(count)
    variable_string.set(string_mesg)
    variable_int.set(count)
    variable_double.set(number_double)
    if cc == False:
        variable_boolean.set(True)
    else:
        variable_boolean.set(False)

    # Label
    # Label文字之讀取 TBD
    # cc = label11.get()

    label11.configure(text="設定Label文字為 :" + string_mesg)
    label22.config(text="設定Label文字為 :" + string_mesg)
    label33.config(text="已按下按鈕")
    label44.config(text="已按下按鈕")

    # label11

    value1 = entry1.get()
    print("取得 Entry 1 資料 :", value1)
    value2 = entry2.get()
    print("取得 Entry 2 資料 :", value2)
    value3 = entry3.get()
    print("取得 Entry 3 資料 :", value3)
    value4 = entry4.get()
    print("取得 Entry 4 資料 :", value4)


frame1 = tk.Frame(window, bg="", width=W, height=H)
frame1.pack()

tk.Label(frame1, text="種類", width=w).grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame1, text="字串", width=w).grid(row=0, column=1, padx=5, pady=5)
tk.Label(frame1, text="整數", width=w).grid(row=0, column=2, padx=5, pady=5)
tk.Label(frame1, text="浮點", width=w).grid(row=0, column=3, padx=5, pady=5)
tk.Label(frame1, text="布林", width=w).grid(row=0, column=4, padx=5, pady=5)

tk.Label(frame1, text="Label", width=w).grid(row=1, column=0, padx=5, pady=5)
label1 = tk.Label(frame1, textvariable=variable_string)
label1.grid(row=1, column=1, padx=5, pady=5)
label2 = tk.Label(frame1, textvariable=variable_int)
label2.grid(row=1, column=2, padx=5, pady=5)
label3 = tk.Label(frame1, textvariable=variable_double)
label3.grid(row=1, column=3, padx=5, pady=5)
label4 = tk.Label(frame1, textvariable=variable_boolean)
label4.grid(row=1, column=4, padx=5, pady=5)

tk.Label(frame1, text="Button", width=w, height=h).grid(row=2, column=0, padx=5, pady=5)
button1 = tk.Button(frame1, textvariable=variable_string, width=w, height=h)
button1.grid(row=2, column=1, padx=5, pady=5)
button2 = tk.Button(frame1, textvariable=variable_int, width=w, height=h)
button2.grid(row=2, column=2, padx=5, pady=5)
button3 = tk.Button(frame1, textvariable=variable_double, width=w, height=h)
button3.grid(row=2, column=3, padx=5, pady=5)
button4 = tk.Button(frame1, textvariable=variable_boolean, width=w, height=h)
button4.grid(row=2, column=4, padx=5, pady=5)

tk.Label(frame1, text="Entry", width=w, height=h).grid(row=3, column=0, padx=5, pady=5)
entry1 = tk.Entry(frame1, textvariable=variable_string, width=w)
entry1.grid(row=3, column=1, padx=5, pady=5)
entry2 = tk.Entry(frame1, textvariable=variable_int, width=w)
entry2.grid(row=3, column=2, padx=5, pady=5)
entry3 = tk.Entry(frame1, textvariable=variable_double, width=w)
entry3.grid(row=3, column=3, padx=5, pady=5)
entry4 = tk.Entry(frame1, textvariable=variable_boolean, width=w)
entry4.grid(row=3, column=4, padx=5, pady=5)

button5 = tk.Button(
    frame1, text="讀寫 控件 上的資料", width=w * 2, height=h, command=read_write_tk_variables
)
button5.grid(row=4, column=1, columnspan=3, padx=5, pady=5)


label11 = tk.Label(frame1, text="一般Label文字之讀寫", width=30)
label11.grid(row=5, column=1, columnspan=3, padx=5, pady=5)
label22 = tk.Label(frame1, text="一般Labe2", width=30)
label22.grid(row=6, column=1, columnspan=3, padx=5, pady=5)
label33 = tk.Label(frame1, text="一般Labe3", width=30)
label33.grid(row=7, column=1, columnspan=3, padx=5, pady=5)
label44 = tk.Label(frame1, text="一般Labe4", width=30)
label44.grid(row=8, column=1, columnspan=3, padx=5, pady=5)


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("tkinter的變數類別")

variable_int0 = tk.IntVar()  # 宣告 variable_int0 為整數物件
variable_int1 = tk.IntVar()  # 宣告 variable_int1 為整數物件
variable_int2 = tk.IntVar()  # 宣告 variable_int2 為整數物件
variable_int3 = tk.IntVar()  # 宣告 variable_int3 為整數物件
variable_string = tk.StringVar()  # 建立一個字串變數, 預設值為空字串

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def printSelection0():
    print("你的選擇是 :", variable_int0.get(), select_items[variable_int0.get()])


print("串列作成選項")
select_items = [(0, "AAA"), (1, "BBB"), (2, "CCC")]

variable_int0.set(1)  # 預設選項

for val, item in select_items:
    tk.Radiobutton(
        window,
        text=item,
        value=val,
        variable=variable_int0,
        padx=20,
        command=printSelection0,
    ).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def printSelection1():
    print("你的選擇是 :", variable_int1.get(), select_items[variable_int1.get()])


print("字典作成選項1, 一般選項紐")
select_items = {0: "AAA", 1: "BBB", 2: "CCC"}

variable_int1.set(1)  # 預設選項

# 建立選項紐
for val, city in select_items.items():
    tk.Radiobutton(
        window, text=city, variable=variable_int1, value=val, command=printSelection1
    ).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def printSelection2():
    print(select_items[variable_int2.get()])  # 列出所選城市


print("字典作成選項2, 用盒子取代選項紐")
select_items = {0: "AAA", 1: "BBB", 2: "CCC"}

variable_int2.set(1)  # 預設選項

for val, city in select_items.items():  # 建立選項紐
    tk.Radiobutton(
        window,
        text=city,
        indicatoron=0,  # 用盒子取代選項紐
        width=30,
        variable=variable_int2,
        value=val,
        command=printSelection2,
    ).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

print("Radiobutton 使用 整數 變數")


def printSelection3():
    num = variable_int3.get()
    if num == 1:
        print("你是男生")
    else:
        print("你是女生")


variable_int3.set(1)  # 預設選項

rbman = tk.Radiobutton(
    window, text="男生", variable=variable_int3, value=1, command=printSelection3  # 男生選項鈕
)
rbman.pack()

rbwoman = tk.Radiobutton(
    window, text="女生", variable=variable_int3, value=2, command=printSelection3  # 女生選項鈕
)
rbwoman.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

print("Radiobutton 使用 字串 變數")


def printSelection4():
    label.config(text="你是" + variable_string.get())


variable_string.set("男生")  # 預設選項是男生

label = tk.Label(window, text="這是預設,尚未選擇", bg="lightyellow", width=30)
label.pack()

rbman = tk.Radiobutton(
    window,
    text="男生",  # 男生選項鈕
    variable=variable_string,
    value="男生",
    command=printSelection4,
)
rbman.pack()

rbwoman = tk.Radiobutton(
    window,
    text="女生",  # 女生選項鈕
    variable=variable_string,
    value="女生",
    command=printSelection4,
)
rbwoman.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

variable_string = tk.StringVar()
variable_string.set("1")  # 預設選項

radio = tk.Radiobutton(
    window,  # 產生單選框元件
    variable=variable_string,  # 設定單選框關聯的變數
    value="1",  # 設定勾選單選框時其所關聯的變數的值，即r的值
    indicatoron=0,  # 將單選框繪製成按鈕型態
    text="AAA",
)  # 設定單選框顯示的文字
radio.pack()

radio = tk.Radiobutton(
    window,
    variable=variable_string,
    value="2",  # 當勾選該單選框時r的值為2
    indicatoron=0,
    text="BBB",
)
radio.pack()

radio = tk.Radiobutton(
    window,
    variable=variable_string,
    value="3",  # 當勾選該單選框時r的值為3
    indicatoron=0,
    text="CCC",
)
radio.pack()

radio = tk.Radiobutton(
    window,
    variable=variable_string,
    value="4",  # 當勾選該單選框時r的值為4
    indicatoron=0,
    text="DDD",
)
radio.pack()

variable_int = tk.IntVar()  # 使用IntVar產生整數變數用於複選框
variable_int.set(1)  # 預設選項

check = tk.Checkbutton(
    window,
    text="Checkbutton",  # 設定複選框的文字
    variable=variable_int,  # 設定複選框關聯的變數
    indicatoron=0,  # 將複選框繪製成按鈕型態
    onvalue=1,  # 當勾選複選框時，c的值為1
    offvalue=2,
)  # 當未勾選複選框時，c的值為2
check.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

variable_string.set("1")  # 預設選項
radio = tk.Radiobutton(
    window,  # 產生單選框元件
    variable=variable_string,  # 設定單選框關聯的變數
    value="1",  # 設定勾選單選框時其所關聯的變數的值，即r的值
    text="AAA",
)  # 設定單選框顯示的文字
radio.pack()

radio = tk.Radiobutton(
    window, variable=variable_string, value="2", text="BBB"  # 當勾選該單選框時r的值為2
)
radio.pack()

radio = tk.Radiobutton(
    window, variable=variable_string, value="3", text="CCC"  # 當勾選該單選框時r的值為3
)
radio.pack()

radio = tk.Radiobutton(
    window, variable=variable_string, value="4", text="DDD"  # 當勾選該單選框時r的值為4
)
radio.pack()

variable_int.set(1)  # 預設選項

check = tk.Checkbutton(
    window,
    text="Checkbutton",  # 設定複選框的文字
    variable=variable_int,  # 設定複選框關聯的變數
    onvalue=1,  # 當勾選複選框時，c的值為1
    offvalue=2,
)  # 當未勾選複選框時，c的值為2
check.pack()


print(variable_string.get())  # 輸出 字串變數 的值
print(variable_int.get())  # 輸出 整數變數 的值

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


cnt = 0


def buttonClick1():
    global cnt
    mesg = "設定Button之Text " + str(cnt)
    cnt += 1
    button1_data.set(mesg)


print("按鈕元件(Button)功能示範 Entry")

button1_data = tk.StringVar()
button1 = tk.Button(window, textvariable=button1_data, command=buttonClick1)
button1_data.set("設定Button之Text")
button1.pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


# Button測試
tk.Label(text="Button測試").pack()


def buttonClick1():
    global count
    count += 1
    labeltext.set("你按我 " + str(count) + " 次了！")
    if btntext.get() == "按我！":
        btntext.set("回復原來文字！")
    else:
        btntext.set("按我！")


labeltext = tk.StringVar()
btntext = tk.StringVar()
count = 0
label1 = tk.Label(window, fg="red", textvariable=labeltext)
labeltext.set("歡迎光臨Tkinter！")
label1.pack()

button1 = tk.Button(window, textvariable=btntext, command=buttonClick1)
btntext.set("按我！")
button1.pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def buttonClick2b():
    textvar.set("我已經被按過了！")


textvar = tk.StringVar()
button1 = tk.Button(window, textvariable=textvar, command=buttonClick2b)
textvar.set("按鈕")
button1.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def buttonClick3():
    global count
    count = count + 1
    print("Beep! " + str(count))
    button1.config(text="Clicked " + str(count))


count = 0

button1 = tk.Button(window, text="按鍵數次數, 不指定按鍵大小", command=buttonClick3)
button1.pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


"""


修改Button 的 Text

button01_text = tk.StringVar()
#button01 = tk.Button(window, textvariable = button01_text, command = lambda:button01Click(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
button01 = tk.Button(window, textvariable = button01_text, width = w, height = h, command = lambda:button01Click())
#button01 = tk.Button(window, command = xxxxxxx, text='----')
button01_text.set("----")

button01_text.set("開啟資料庫...")


buttontext = tk.StringVar() # 產生關聯按鈕文字的變數
buttontext.set('askokcancel')								# 設定buttontext值
button = tk.Button(window,								# 產生按鈕
		textvariable = buttontext,						# 設定關聯變數
		command = cmd)								# 設定事件處理函數
button.pack()

		buttontext.set('askokcancel')
		buttontext.set('showwarning')
		buttontext.set('showinfo')
		buttontext.set('showerror')
		buttontext.set('askyesno')
		buttontext.set('skquestion')						# 變更按鈕上的文字

"""


print("------------------------------------------------------------")  # 60個


def selAll():  # 選取全部字串
    entry.select_range(0, tk.END)


def deSel():  # 取消選取
    entry.select_clear()


def clr():  # 刪除文字
    entry.delete(0, tk.END)


def readonly():  # 設定Entry狀態
    if var.get() == True:
        entry.config(state=tk.DISABLED)  # 設為DISABLED
    else:
        entry.config(state=tk.NORMAL)  # 設為NORMAL


window = tk.Tk()
window.geometry("600x800")
window.title("Entry 文字選取")

# 以下row=0建立Entry
entry = tk.Entry(window)
entry.pack()

# 以下row=1建立Button
buttonSel = tk.Button(window, text="選取", command=selAll)
buttonSel.pack()
buttonDesel = tk.Button(window, text="取消選取", command=deSel)
buttonDesel.pack()
buttonClr = tk.Button(window, text="刪除", command=clr)
buttonClr.pack()

# 以下row=2建立Checkboxes
var = tk.BooleanVar()
var.set(False)
chkReadonly = tk.Checkbutton(window, text="唯讀", variable=var, command=readonly)
chkReadonly.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

# Entry與Label測試
tk.Label(text="Entry與Label同步改變Text").pack()

string = tk.StringVar()
entry = tk.Entry(window, textvariable=string)
entry.pack()
label = tk.Label(window, textvariable=string)
label.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

# Entry 預設值
entry_string = tk.StringVar(value="Entry 預設值")
entry = tk.Entry(window, textvariable=entry_string)
entry.pack()

print("Entry內容 :", entry_string.get())  # Entry取值


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

var = tk.StringVar()
l = tk.Label(
    window, textvariable=var, bg="green", font=("Arial", 12), width=15, height=2
)
# l = tk.Label(window, text='OMG! this is TK!', bg='green', font=('Arial', 12), width=15, height=2)
l.pack()

on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("you hit me")
    else:
        on_hit = False
        var.set("")


b = tk.Button(window, text="hit me", width=15, height=2, command=hit_me)
b.pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

from tkinter import Tk, Variable, Entry, Button


def get_entry_data():
    cc = a.get()
    print("你取得了 :", cc)


a = tk.Variable(window, value="123")
e = tk.Entry(window, textvariable=a)
b = tk.Button(window, text="獲取", command=get_entry_data)
e.pack()
b.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


import tkinter.simpledialog  # 匯入tkSimpleDialog模組


def InStr():
    # 建立 字串 輸入交談視窗
    r = tkinter.simpledialog.askstring(
        "Python Tkinter", "Input String", initialvalue="Tkinter"  # 指定提示字元
    )  # 指定起始化文字
    print(r)  # 輸出傳回值


def InInt():
    # 建立 整數 輸入交談視窗
    r = tkinter.simpledialog.askinteger("Python Tkinter", "Input Integer")
    print(r)


def InFlo():
    # 建立 浮點數 輸入交談視窗
    r = tkinter.simpledialog.askfloat("Python Tkinter", "Input Float")
    print(r)


button1 = tk.Button(window, text="Input String", command=InStr)
button1.pack()
button2 = tk.Button(window, text="Input Integer", command=InInt)
button2.pack()
button2 = tk.Button(window, text="Input Float", command=InFlo)
button2.pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

"""
print('字串變數之 set 與 get')
foldername = tk.StringVar()
foldername.set('D:/_git/vcs/_1.data/______test_files1/_mp3/')
print(foldername.get())




entry_data = tk.StringVar()
entry_data.set("test")

entry1 = tk.Entry(window, textvariable=entry_data, width=8)
entry1.pack()


   



"""
