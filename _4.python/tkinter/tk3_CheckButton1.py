# Python 測試 tkinter : Checkbutton

import sys
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

print("------------------------------------------------------------")  # 60個

def checkbutton_select1():
    str = "你喜歡的動物："
    for i in range(0, len(choice)):
        if choice[i].get() == 1:
            str = str + ball[i] + " "
    print(str)
    msg.set(str)


window = tk.Tk()
window.geometry("600x800")
window.title("Checkbutton 1")

choice = []
ball = ["鼠", "牛", "虎", "兔"]
msg = tk.StringVar()
label2 = tk.Label(window, fg="red", textvariable=msg)
label2.pack()

for i in range(0, len(ball)):
    item = tk.IntVar()
    choice.append(item)
    item = tk.Checkbutton(
        window, text=ball[i], variable=choice[i], command=checkbutton_select1
    )
    item.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

var = tk.IntVar()

c = tk.Checkbutton(window, text="CheckButton", variable=var)
c.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

topping = {0: "鼠", 1: "牛", 2: "虎", 3: "兔"}

check_value = {}

for i in range(len(topping)):
    check_value[i] = tk.BooleanVar()
    tk.Checkbutton(window, variable=check_value[i], text=topping[i]).pack()


def checkbutton_select2():
    for i in check_value:
        if check_value[i].get() == True:
            print(topping[i])


tk.Button(window, text="點菜", command=checkbutton_select2).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

topping = {0: "鼠", 1: "牛", 2: "虎", 3: "兔"}

check_value = {}

for i in range(len(topping)):
    check_value[i] = tk.BooleanVar()
    tk.Checkbutton(window, variable=check_value[i], text=topping[i]).pack()


def checkbutton_select3():
    for i in check_value:
        if check_value[i].get() == True:
            print(topping[i])


tk.Button(window, text="點餐", command=checkbutton_select3).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

topping = {0: "鼠", 1: "牛", 2: "虎", 3: "兔"}
check_value = {}
for i in range(len(topping)):
    check_value[i] = tk.BooleanVar()
    tk.Checkbutton(window, variable=check_value[i], text=topping[i]).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

print("試題與測驗分析程式")


def checkbutton_select6():
    selected_options = ""
    if asia.get():
        selected_options += chkbut_asia.cget("text")
    if america.get():
        selected_options += chkbut_america.cget("text")
    if europe.get():
        selected_options += chkbut_europe.cget("text")
    lab_result.config(text=selected_options)


asia = tk.IntVar()
chkbut_asia = tk.Checkbutton(window, text="亞洲", variable=asia, anchor=tk.W)
chkbut_asia.pack()

america = tk.IntVar()
chkbut_america = tk.Checkbutton(window, text="美洲", variable=america, anchor=tk.W)
chkbut_america.pack()

europe = tk.IntVar()
chkbut_europe = tk.Checkbutton(window, text="歐洲", variable=europe, anchor=tk.W)
chkbut_europe.pack()

but = tk.Button(window, text="確定", command=checkbutton_select6, padx=15)
but.pack()

lab_result = tk.Label(window, fg="black", width=20)
lab_result.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

check1 = ttk.Checkbutton(
    window,
    text="checkbox 1",
    command=lambda: print("ccccc"),
    variable="ccccc",
    onvalue=10,
    offvalue=5,
)
check1.pack()

check2 = ttk.Checkbutton(window, text="Checkbox 2", command="")
check2.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

check_bool = tk.BooleanVar()

exercise_check = ttk.Checkbutton(
    window,
    text="exercise check",
    variable=check_bool,
    # command = lambda: print(radio_string.get()))
    command=lambda: print("你按了check_button"),
)
exercise_check.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def checkbutton_select7():  # 回應核取方塊變數狀態
    print("這學期預定選修的科目包括:", var1.get(), var2.get(), var3.get())


lb1 = tk.Label(window, text="選修的科目：").pack()
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
btnShow = tk.Button(window, text="列出選修結果", command=checkbutton_select7)
btnShow.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Checkbutton 2")

"""
請問迴圈裡面 check_value [i] = tk.BooleanVar() 這一行，能否舉個例子，假設第 0 個按鈕被勾選，check_value 長怎樣；假設第 0、1 個按鈕被勾選，check_value 長怎樣 ... 依此類推
"""


def checkbutton_select5():
    selection = ""
    for i in checkboxes:  # 檢查此字典
        if checkboxes[i].get() == True:  # 被選取則執行
            selection = selection + sports[i] + " "
    x.set(selection)

sports = {0: "鼠", 1: "牛", 2: "虎", 3: "兔"}  # 動物字典

checkboxes = {}  # 字典存放被選取項目
for i in range(len(sports)):  # 將動物字典轉成核取方塊
    checkboxes[i] = tk.BooleanVar()  # 布林變數物件
    tk.Checkbutton(window, text=sports[i], variable=checkboxes[i]).pack()

tk.Button(window, text="確定", width=10, command=checkbutton_select5).pack()

x = tk.StringVar()
display = tk.Label(window, textvariable=x, bg="lightgreen", width=30)
display.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

def printInfo1():
    selection = ""
    for i in checkboxes:  # 檢查此字典
        if checkboxes[i].get() == True:  # 被選取則執行
            selection = selection + sports[i] + "\t"
    print(selection)

tk.Label(window, text="請選擇喜歡的動物", fg="blue", bg="lightyellow", width=30).pack()

sports = {0: "鼠", 1: "牛", 2: "虎", 3: "兔"}  # 動物字典
checkboxes = {}  # 字典存放被選取項目
for i in range(len(sports)):  # 將動物字典轉成核取方塊
    checkboxes[i] = tk.BooleanVar()  # 布林變數物件
    tk.Checkbutton(window, text=sports[i], variable=checkboxes[i]).pack()

button1 = tk.Button(window, text="選取", width=10, command=printInfo1)
button1.pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

var1 = tk.IntVar()
tk.Checkbutton(window, text="鼠", variable=var1).pack()
var2 = tk.IntVar()
tk.Checkbutton(window, text="牛", variable=var2).pack()
var3 = tk.IntVar()
tk.Checkbutton(window, text="虎", variable=var3).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def checkbutton_select4():
    selection = ""
    for i in checkboxes:  # 檢查此字典
        if checkboxes[i].get() == True:  # 被選取則執行
            selection = selection + sports[i] + "\t"
    print(selection)

sports = {0: "鼠", 1: "牛", 2: "虎", 3: "兔"}  # 動物字典

checkboxes = {}  # 字典存放被選取項目
for i in range(len(sports)):  # 將動物字典轉成核取方塊
    checkboxes[i] = tk.BooleanVar()  # 布林變數物件
    tk.Checkbutton(window, text=sports[i], variable=checkboxes[i]).pack()

tk.Button(window, text="確定", width=10, command=checkbutton_select4).pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, bg="yellow", width=20, text="empty")
label1.pack()


def checkbutton_select8():
    if (var1.get() == 1) & (var2.get() == 0):
        label1.config(text="I love only Python ")
    elif (var1.get() == 0) & (var2.get() == 1):
        label1.config(text="I love only C++")
    elif (var1.get() == 0) & (var2.get() == 0):
        label1.config(text="I do not love either")
    else:
        label1.config(text="I love both")


var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(
    window, text="Python", variable=var1, onvalue=1, offvalue=0, command=checkbutton_select8
)
c2 = tk.Checkbutton(
    window, text="C++", variable=var2, onvalue=1, offvalue=0, command=checkbutton_select8
)
c1.pack()
c2.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

def checkbutton_select9():
    str = "選擇："
    for i in range(0, len(choice)):
        if choice[i].get() == 1:
            str = str + animals_list[i] + " "
    print(str)
    msg.set(str)


x_st = 20
y_st = 500
dx = 140
dy = 80
w = 12
h = 3

choice = []

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
label1 = tk.Label(window, text="選擇動物 :")
label1.pack()
label1.place(x=x_st + dx * 0, y=y_st + dy * 2 - 20)
label2 = tk.Label(window, fg="red", textvariable=msg)
label2.pack()
label2.place(x=x_st + dx * 0, y=y_st + dy * 2 + 80)


# 加入 Checkbutton
dx2 = dx * 4 / 4  # 為了微調距離用
for i in range(0, len(animals_list)):
    item = tk.IntVar()
    choice.append(item)
    item = tk.Checkbutton(window, text=animals_list[i], variable=choice[i], command=checkbutton_select9)
    item.pack()
    item.place(x=x_st + dx2 * (i % 4), y=y_st + dy * 2 + int(i / 4) * 25)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Checkbutton 4")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def check():  # 回應核取方塊變數狀態
    print("選取項目 :", var1.get(), var2.get(), var3.get())


item1 = "鼠"
var1 = tk.StringVar()
chk = tk.Checkbutton(window, text=item1, variable=var1, onvalue=item1, offvalue="")
chk.pack()

item2 = "牛"
var2 = tk.StringVar()
chk2 = tk.Checkbutton(window, text=item2, variable=var2, onvalue=item2, offvalue="")
chk2.pack()

item3 = "虎"
var3 = tk.StringVar()
chk3 = tk.Checkbutton(window, text=item3, variable=var3, onvalue=item3, offvalue="")
chk3.pack()

buttonShow = tk.Button(window, text="選取項目", command=check)
buttonShow.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def fnOk():
    lfrmSpot = tk.LabelFrame(window, text="勾選建議地點(可複選)：")
    lfrmSpot.pack(pady=10)
    for i in range(3):
        check[i] = tk.BooleanVar()  # 設check[]元素值為布林值物件
        tk.Checkbutton(lfrmSpot, text=spots[i], variable=check[i]).pack(anchor="w")


def fnMsg():
    if ok.get() == True:
        msg = "勾選的地點為："
        for i in range(3):
            if check[i].get() == True:  # 若check[i]元素值為True
                msg += spots[i] + "、"  # 將spots[i]元素值加入msg字串
        print("訊息 :", msg[: len(msg) - 1])
    else:
        print("訊息 : 期盼下次你能參加")
    window.destroy()


print("旅遊問卷")

ok = tk.BooleanVar()
chkOK = tk.Checkbutton(window, text="參加旅遊", variable=ok, command=fnOk).pack()

spots = ["九份與金瓜石", "日月潭", "墾丁國家公園"]
check = {}

buttonSend = tk.Button(window, text=" 送出 ", command=fnMsg).pack(pady=5)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

frame1 = tk.Frame(width=150, height=80, relief=tk.RAISED, borderwidth=5)  # 建立框架
lab = tk.Label(frame1, text="Checkbutton測試").pack()

checkbutton1 = tk.Checkbutton(frame1, text="鼠")
checkbutton1.pack(anchor=tk.W)

checkbutton2 = tk.Checkbutton(frame1, text="牛")
checkbutton2.pack(anchor=tk.W)

checkbutton3 = tk.Checkbutton(frame1, text="虎")
checkbutton3.pack(anchor=tk.W)

frame1.pack(padx=10, pady=10)  # 包裝框架

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def command_checkbutton1():
    if var_checkbutton1.get():
        label1.config(text="選取cb1")
    else:
        label1.config(text="取消選取cb1")


def command_checkbutton2():
    if var_checkbutton2.get():
        label1.config(text="選取cb2")
    else:
        label1.config(text="取消選取cb2")


var_checkbutton1 = tk.BooleanVar()
checkbutton1 = tk.Checkbutton(
    window,
    text="鼠",
    variable=var_checkbutton1,
    command=command_checkbutton1,
)
checkbutton1.pack()

var_checkbutton2 = tk.BooleanVar()
checkbutton2 = tk.Checkbutton(
    window,
    text="牛",
    variable=var_checkbutton2,
    command=command_checkbutton2,
)
checkbutton2.pack()

label1 = tk.Label(window, bg="yellow", fg="blue", width=12, height=2)
label1.pack()

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

# Window下的第二個Frame
# Add a button, a check button, and a radio button to frame1
frame2 = tk.Frame(window, bg="pink")  # Create and add a frame to window
frame2.pack()

label = tk.Label(frame2, text="Enter your name: ")
name = tk.StringVar()
entryName = tk.Entry(frame2, textvariable=name)
btGetName = tk.Button(frame2, text="Get Name", command=processButton)
label.grid(row=1, column=1)
entryName.grid(row=1, column=2)
btGetName.grid(row=1, column=3)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線


var1 = tk.IntVar()
checkbutton1 = tk.Checkbutton(window, text="鼠", variable=var1)
checkbutton1.pack()

var2 = tk.IntVar()
checkbutton2 = tk.Checkbutton(window, text="牛", variable=var2)
checkbutton2.pack()

var3 = tk.IntVar()
checkbutton3 = tk.Checkbutton(window, text="虎", variable=var3)
checkbutton3.pack()

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


window.mainloop()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


items = ("鼠", "牛", "虎")
