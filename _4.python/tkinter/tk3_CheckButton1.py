# Python 測試 tkinter : Checkbutton

import sys
import tkinter as tk
import tkinter.messagebox

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Checkbutton 1")

print("------------------------------------------------------------")  # 60個

def do_cb_select0():
    print("你選擇了 ：", var1.get(), var2.get(), var3.get())

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

tk.Checkbutton(window, text="鼠", variable=var1, command=do_cb_select0).pack()
tk.Checkbutton(window, text="牛", variable=var2, command=do_cb_select0).pack()
tk.Checkbutton(window, text="虎", variable=var3, command=do_cb_select0).pack()

tk.Button(window, text="選擇0", command=do_cb_select0).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

def do_cb_select1():
    text = "你選擇了 ："
    for i in range(0, len(check_value1)):
        if check_value1[i].get() == 1:
            text += animals[i] + " "
    var_string1.set(text)

    if var_int1.get():
        text += checkbutton1.cget("text")
    if var_int2.get():
        text += checkbutton2.cget("text")
    label6.config(text=text)
    print(text)

check_value1 = []
animals = ["鼠", "牛"]

var_string1 = tk.StringVar()

label2 = tk.Label(window, textvariable=var_string1, fg="blue", bg="yellow", width=30)
label2.pack()

label6 = tk.Label(window, fg="blue", bg="yellow", width=30)
label6.pack()

label6.config(text="尚未選擇")

for i in range(0, len(animals)):
    item = tk.IntVar()
    check_value1.append(item)
    item = tk.Checkbutton(
        window, text=animals[i], variable=check_value1[i], command=do_cb_select1
    )
    item.pack()

var_int1 = tk.IntVar()
checkbutton1 = tk.Checkbutton(window, text="虎", variable=var_int1, command=do_cb_select1)
checkbutton1.pack()

var_int2 = tk.IntVar()
checkbutton2 = tk.Checkbutton(window, text="兔", variable=var_int2, command=do_cb_select1)
checkbutton2.pack()

tk.Button(window, text="選擇1", command=do_cb_select1).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

def do_cb_select2():
    for i in check_value:
        if check_value[i].get() == True:
            print(topping[i])

#字典
topping = {0: "鼠", 1: "牛", 2: "虎"}
check_value = {}

for i in range(len(topping)):
    check_value[i] = tk.BooleanVar()
    tk.Checkbutton(window, variable=check_value[i], text=topping[i]).pack()

tk.Button(window, text="選擇2", command=do_cb_select2).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

print('使用 lambda')
tk.Checkbutton(
    window,
    text="鼠",
    variable="ccccc",
    onvalue=10,
    offvalue=5,
    command=lambda: print("你選擇了 鼠"),
).pack()

var_boolean3 = tk.BooleanVar()

tk.Checkbutton(
    window,
    text="鼠",
    variable=var_boolean3,
    command=lambda: print("你按了 鼠 ", var_boolean3.get()),
).pack()

tk.Checkbutton(window, text="牛", command=lambda: print("你選擇了 牛")).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

def do_cb_select4():
    text = ""
    for i in checkboxes4:  # 檢查此字典
        if checkboxes4[i].get() == True:  # 被選取則執行
            text += sports[i] + " "
    var_string4.set(text)
    print(text)

var_string4 = tk.StringVar()

label4 = tk.Label(window, textvariable=var_string4, fg="blue", bg="yellow", width=30)
label4.pack()

sports = {0: "鼠", 1: "牛", 2: "虎"}  # 動物字典
checkboxes4 = {}  # 字典存放被選取項目
for i in range(len(sports)):  # 將動物字典轉成核取方塊
    checkboxes4[i] = tk.BooleanVar()  # 布林變數物件
    tk.Checkbutton(window, text=sports[i], variable=checkboxes4[i], command=do_cb_select4).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Checkbutton 2")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def fnOk():
    labelframe1 = tk.LabelFrame(window, text="勾選動物(可複選)：")
    labelframe1.pack(pady=10)
    for i in range(3):
        check[i] = tk.BooleanVar()  # 設check[]元素值為布林值物件
        tk.Checkbutton(labelframe1, text=animals[i], variable=check[i]).pack(anchor="w")


def fnMsg():
    if var_boolean6.get() == True:
        msg = "勾選的動物為："
        for i in range(3):
            if check[i].get() == True:  # 若check[i]元素值為True
                msg += animals[i] + "、"  # 將animals[i]元素值加入msg字串
        print("訊息 :", msg[: len(msg) - 1])
    else:
        print("訊息 : 期盼下次你能參加")
    window.destroy()


print("動物問卷")

var_boolean6 = tk.BooleanVar()
checkbutton6 = tk.Checkbutton(window, text="參加選擇", variable=var_boolean6, command=fnOk).pack()

animals = ["鼠", "牛", "虎"]
check = {}

buttonSend = tk.Button(window, text="選擇6", command=fnMsg).pack(pady=5)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

frame1 = tk.Frame(width=150, height=80, relief=tk.RAISED, borderwidth=5)  # 建立框架

tk.Label(frame1, text="Checkbutton測試", fg="blue", bg="yellow", width=30).pack()

tk.Checkbutton(frame1, text="鼠").pack(anchor=tk.W)
tk.Checkbutton(frame1, text="牛").pack(anchor=tk.W)
tk.Checkbutton(frame1, text="虎").pack(anchor=tk.W)

frame1.pack(padx=10, pady=10)  # 包裝框架

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def do_cb_selecta():
    if var_boolean1.get():
        label_mesg2.config(text="選取 鼠")
    else:
        label_mesg2.config(text="取消選取 鼠")


def do_cb_selectb():
    if var_boolean2.get():
        label_mesg2.config(text="選取 牛")
    else:
        label_mesg2.config(text="取消選取 牛")

labelframe2 = tk.LabelFrame(window, text="LabelFrame")
labelframe2.pack(pady=10)

label_mesg2 = tk.Label(labelframe2, bg="yellow", fg="blue", width=12, height=2)
label_mesg2.pack()

var_boolean1 = tk.BooleanVar()
checkbutton1 = tk.Checkbutton(
    labelframe2,
    text="鼠",
    variable=var_boolean1,
    command=do_cb_selecta,
)
checkbutton1.pack()

var_boolean2 = tk.BooleanVar()
checkbutton2 = tk.Checkbutton(
    labelframe2,
    text="牛",
    variable=var_boolean2,
    command=do_cb_selectb,
)
checkbutton2.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def processCheckbutton():
    print("check button is " + ("checked " if v1.get() == 1 else "unchecked"))


def processRadiobutton():
    print(("Red" if v2.get() == 1 else "Yellow") + " is selected ")


def processButton():
    print("Your name is " + name.get())


# window = tk.Tk()
# window.title("Widgets Demo")

# Window下的第一個Frame
# Add a button, a check button, and a radio button to frame1
frame1 = tk.Frame(window, bg="green")  # Create and add a frame to window
frame1.pack()

v1 = tk.IntVar()
cbtBold = tk.Checkbutton(frame1, text="Bold", variable=v1, command=processCheckbutton)
v2 = tk.IntVar()
rbRed = tk.Radiobutton(
    frame1, text="Red", bg="red", variable=v2, value=1, command=processRadiobutton
)
rbYellow = tk.Radiobutton(
    frame1, text="Yellow", bg="yellow", variable=v2, value=2, command=processRadiobutton
)
cbtBold.grid(row=1, column=1)
rbRed.grid(row=1, column=2)
rbYellow.grid(row=1, column=3)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

def do_cb_select9():
    text = "選擇："
    for i in range(0, len(check_value9)):
        if check_value9[i].get() == 1:
            text += animals_list[i] + " "
    msg.set(text)
    print(text)


x_st = 20
y_st = 500
dx = 120
dy = 80
w = 12
h = 3

check_value9 = []

animals_list = [
    "鼠",
    "牛",
    "虎",
    "兔",
    "龍",
    "蛇",
    "馬",
    "羊",
    "猴",
    "雞",
    "狗",
    "豬",
]

msg = tk.StringVar()

label_mesg5 = tk.Label(window, text="選擇動物 :")
label_mesg5.place(x=x_st + dx * 0, y=y_st + dy * 2 - 20)

label2 = tk.Label(window, fg="red", textvariable=msg)
label2.place(x=x_st + dx * 0, y=y_st + dy * 2 + 80)

# 加入 Checkbutton
dx2 = dx * 4 / 4  # 為了微調距離用
for i in range(0, len(animals_list)):
    item = tk.IntVar()
    check_value9.append(item)
    item = tk.Checkbutton(window, text=animals_list[i], variable=check_value9[i], command=do_cb_select9)
    item.pack()
    item.place(x=x_st + dx2 * (i % 4), y=y_st + dy * 2 + int(i / 4) * 25)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


window.mainloop()


print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

items = ("鼠", "牛", "虎")

print("------------------------------------------------------------")  # 60個


def do_cb_select7():  # 回應核取方塊變數狀態
    print("目前選取的動物 :", var1.get(), var2.get(), var3.get())

item1 = "鼠"
var1 = tk.StringVar()
chk1 = tk.Checkbutton(window, text=item1, variable=var1, onvalue=item1, offvalue="")
chk1.pack()

item2 = "牛"
var2 = tk.StringVar()
chk2 = tk.Checkbutton(window, text=item2, variable=var2, onvalue=item2, offvalue="")
chk2.pack()

item3 = "虎"
var3 = tk.StringVar()
chk3 = tk.Checkbutton(window, text=item3, variable=var3, onvalue=item3, offvalue="")
chk3.pack()

buttonShow = tk.Button(window, text="選擇7", command=do_cb_select7)
buttonShow.pack()

print("------------------------------------------------------------")  # 60個

label_mesg = tk.Label(window, bg="yellow", width=20, text="empty")
label_mesg.pack()

def do_cb_select8():
    if (var1.get() == 1) & (var2.get() == 0):
        label_mesg.config(text="鼠")
    elif (var1.get() == 0) & (var2.get() == 1):
        label_mesg.config(text="牛")
    elif (var1.get() == 0) & (var2.get() == 0):
        label_mesg.config(text="皆無")
    else:
        label_mesg.config(text="鼠 + 牛")


var1 = tk.IntVar()
c1 = tk.Checkbutton(window, text="鼠", variable=var1, onvalue=1, offvalue=0, command=do_cb_select8)
c1.pack()

var2 = tk.IntVar()
c2 = tk.Checkbutton(window, text="牛", variable=var2, onvalue=1, offvalue=0, command=do_cb_select8)
c2.pack()

print("------------------------------------------------------------")  # 60個



"""
請問迴圈裡面 check_value [i] = tk.BooleanVar() 這一行，能否舉個例子，假設第 0 個按鈕被勾選，check_value 長怎樣；假設第 0、1 個按鈕被勾選，check_value 長怎樣 ... 依此類推
"""

