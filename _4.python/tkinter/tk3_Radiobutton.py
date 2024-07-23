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

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def do_select_string9():
    label_selection_string9.config(text="s9你選擇了 :" + var_string9.get())

tk.Label(window, text = "一個一個建立Radiobutton").pack()

var_string9 = tk.StringVar()
var_string9.set("")  # 預設

label_selection_string9 = tk.Label(window, bg="lightyellow", width=20, text="未選擇")
label_selection_string9.pack()

rb0 = tk.Radiobutton(
    window, text="AAA", variable=var_string9, value="A", command=do_select_string9
)
rb0.pack()
rb1 = tk.Radiobutton(
    window, text="BBB", variable=var_string9, value="B", command=do_select_string9
)
rb1.pack()
rb2 = tk.Radiobutton(
    window, text="CCC", variable=var_string9, value="C", command=do_select_string9
)
rb2.pack()

rb2.select()  # 預設

do_select_string9()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def do_select_int1():
    value = var_int1.get()
    ##print(items1i[value])
    print("i1你選擇了 :" + items1i[value])


items1i = {0: "AAA", 1: "BBB", 2: "CCC"}

var_int1 = tk.IntVar()
var_int1.set(2)  # 預設

tk.Radiobutton(
    window, text=items1i[0], variable=var_int1, value=0, command=do_select_int1
).pack()
tk.Radiobutton(
    window, text=items1i[1], variable=var_int1, value=1, command=do_select_int1
).pack()
tk.Radiobutton(
    window, text=items1i[2], variable=var_int1, value=2, command=do_select_int1
).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

def do_select_int3():
    selected_item = var_int3.get()
    label_selection_int3.config(text=items3i[selected_item][0])
    print("i3你選擇了 :", var_int3.get())

tk.Label(window, text = "用字典串列元組 一次建立一組Radiobutton").pack()

items3i = (("AAA", 0), ("BBB", 1), ("CCC", 2))
print(type(items3i))

label_selection_int3 = tk.Label(window, bg="lightyellow", width=20, text="未選擇")
label_selection_int3.pack()

var_int3 = tk.IntVar()
var_int3.set(2)  # 預設

for item, value in items3i:
    rb = tk.Radiobutton(
        window, text=item, variable=var_int3, value=value, command=do_select_int3
    )
    rb.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def do_select_string1():
    print("s1你選擇了 :", var_string1.get())

tk.Label(window, text = "用字典串列元組 一次建立一組Radiobutton").pack()

items1s = [("AAA", 0), ("BBB", 1), ("CCC", 2)]

var_string1 = tk.StringVar()  # 設定以字串表示選單編號
var_string1.set("2")  # 預設

for selection, num in items1s:
    rb = ttk.Radiobutton(
        window,
        text=selection,
        variable=var_string1,
        value=num,
        command=do_select_string1,
    )
    rb.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

tk.Label(window, text = "使用 lambda").pack()

rb1 = ttk.Radiobutton(window,text="AAA",command=lambda: print("lambda 你選擇了 : AAA"))
rb1.pack()
rb2 = ttk.Radiobutton(window,text="BBB",command=lambda: print("lambda 你選擇了 : BBB"))
rb2.pack()
rb3 = ttk.Radiobutton(window,text="CCC",command=lambda: print("lambda 你選擇了 : CCC"))
rb3.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def do_select_string3():
    print("s3你選擇了 :" + var_string3.get())


var_string3 = tk.StringVar()

rb0 = tk.Radiobutton(
    window, text="AAA", value="aaa", variable=var_string3, command=do_select_string3
)
rb0.pack()
rb1 = tk.Radiobutton(
    window, text="BBB", value="bbb", variable=var_string3, command=do_select_string3
)
rb1.pack()
rb2 = tk.Radiobutton(
    window, text="CCC", value="ccc", variable=var_string3, command=do_select_string3
)
rb2.pack()

rb2.select()  # 預設

do_select_string3()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

items5s = [
    ("AAA", "aaa"),
    ("BBB", "bbb"),
    ("CCC", "ccc"),
]

var_string5 = tk.StringVar()
var_string5.set("ccc")  # 預設

for text, mode in items5s:
    rb = tk.Radiobutton(window, text=text, variable=var_string5, value=mode)
    rb.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Radiobutton 2")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def do_select_int4():
    print("i4你選擇了 :", var_int4.get())


items4i = [("AAA", 0), ("BBB", 1), ("CCC", 2)]

var_int4 = tk.IntVar()
var_int4.set(2)  # 預設

for item, val in items4i:
    tk.Radiobutton(
        window, text=item, value=val, variable=var_int4, padx=20, command=do_select_int4
    ).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def do_select_int5():
    print("i5你選擇了 :", var_int5.get())


items5i = [("AAA", 0), ("BBB", 1), ("CCC", 2)]

var_int5 = tk.IntVar()
var_int5.set(2)  # 預設

for item, val in items5i:
    tk.Radiobutton(
        window, text=item, value=val, variable=var_int5, padx=20, command=do_select_int5
    ).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def do_select_int6():
    print(items6[var_int6.get()])


tk.Label(window, text = "用字典串列元組 一次建立一組Radiobutton").pack()

items6 = {0: "AAA", 1: "BBB", 2: "CCC"}

var_int6 = tk.IntVar()
var_int6.set(2)  # 預設

for val, city in items6.items():
    tk.Radiobutton(
        window, text=city, variable=var_int6, value=val, command=do_select_int6
    ).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def do_select_int7():
    print(items7i[var_int7.get()])  # 列出所選城市


tk.Label(window, text = "用字典串列元組 一次建立一組Radiobutton").pack()

items7i = {0: "AAA", 1: "BBB", 2: "CCC"}

var_int7 = tk.IntVar()
var_int7.set(2)  # 預設

for val, city in items7i.items():
    tk.Radiobutton(
        window,
        text=city,
        indicatoron=0,  # 用盒子取代選項紐
        width=30,
        variable=var_int7,
        value=val,
        command=do_select_int7,
    ).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def do_select_int8():
    print("i8你選擇了 :", var_int8.get())


items8i = [("AAA", 0), ("BBB", 1), ("CCC", 2)]

var_int8 = tk.IntVar()
var_int8.set(2)  # 預設

for item, val in items8i:
    tk.Radiobutton(
        window, text=item, value=val, variable=var_int8, padx=20, command=do_select_int8
    ).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def do_select_int9():
    print("i9你選擇了 :", var_int9.get())


items9i = [("AAA", 0), ("BBB", 1), ("CCC", 2)]

var_int9 = tk.IntVar()
var_int9.set(2)  # 預設

for item, val in items9i:
    tk.Radiobutton(
        window, text=item, value=val, variable=var_int9, padx=20, command=do_select_int9
    ).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def do_select_inta():
    print(itemsa[var_inta.get()])  # 列出所選城市


tk.Label(window, text = "用字典串列元組 一次建立一組Radiobutton").pack()

itemsa = {0: "AAA", 1: "BBB", 2: "CCC"}

var_inta = tk.IntVar()
var_inta.set(2)  # 預設

for val, city in itemsa.items():
    tk.Radiobutton(
        window, text=city, variable=var_inta, value=val, command=do_select_inta
    ).pack()

"""
# 用盒子取代選項紐
for val, city in itemsa.items():
    tk.Radiobutton(window,
                text=city,
                indicatoron = 0,        # 用盒子取代選項紐
                width=30,
                variable=var_inta,value=val,
                command=do_select_inta).pack()
"""

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def do_select_intd():
    print("id你選擇了 :", var_intd.get())


itemsdi = [("AAA", 1), ("BBB", 2), ("CCC", 3)]

var_intd = tk.IntVar()
var_intd.set(2)  # 預設

for item, val in itemsdi:
    tk.Radiobutton(
        window, text=item, value=val, variable=var_intd, padx=20, command=do_select_intd
    ).pack()


window.mainloop()

print("------------------------------------------------------------")  # 60個

from PIL import ImageTk, Image


def do_select_string7():
    label_selection_string7.config(text="你選的是" + var_string7.get())


filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

window = tk.Tk()
window.geometry("600x800")
window.title("Radiobutton 3")

# 檔案 => ImageTk影像
tk_image1 = ImageTk.PhotoImage(file="__new/star.gif")
tk_image2 = ImageTk.PhotoImage(file="__new/moon.gif")
tk_image3 = ImageTk.PhotoImage(file="__new/sun.gif")

var_string7 = tk.StringVar()  # 選項紐綁定的變數
var_string7.set("星星")  # 預設

label_selection_string7 = tk.Label(window, text="這是預設,尚未選擇", bg="lightyellow", width=30)
label_selection_string7.pack()

rb1 = tk.Radiobutton(
    window,
    image=tk_image1,
    variable=var_string7,
    value="星星",
    command=do_select_string7,  # 星星選項鈕
)
rb1.pack()

rb2 = tk.Radiobutton(
    window,
    image=tk_image2,
    variable=var_string7,
    value="月亮",
    command=do_select_string7,  # 月亮選項鈕
)
rb2.pack()

rb3 = tk.Radiobutton(
    window,
    image=tk_image3,
    variable=var_string7,
    value="太陽",
    command=do_select_string7,  # 太陽選項鈕
)
rb3.pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def do_select_string8():
    label_selection_string8.config(text="你選的是" + var_string8.get())


# 檔案 => ImageTk影像
tk_image1 = ImageTk.PhotoImage(file="__new/star.gif")
tk_image2 = ImageTk.PhotoImage(file="__new/moon.gif")
tk_image3 = ImageTk.PhotoImage(file="__new/sun.gif")

var_string8 = tk.StringVar()  # 選項紐綁定的變數
var_string8.set("星星")  # 預設

label_selection_string8 = tk.Label(window, text="這是預設,尚未選擇", bg="lightyellow", width=30)
label_selection_string8.pack()

rb1 = tk.Radiobutton(
    window,
    image=tk_image1,  # 星星選項鈕
    text="星星",
    compound=tk.RIGHT,
    variable=var_string8,
    value="星星",
    command=do_select_string8,
)
rb1.pack()

rb2 = tk.Radiobutton(
    window,
    image=tk_image2,  # 月亮選項鈕
    text="月亮",
    compound=tk.RIGHT,
    variable=var_string8,
    value="月亮",
    command=do_select_string8,
)
rb2.pack()

rb3 = tk.Radiobutton(
    window,
    image=tk_image3,  # 太陽選項鈕
    text="太陽",
    compound=tk.RIGHT,
    variable=var_string8,
    value="太陽",
    command=do_select_string8,
)
rb3.pack()

print("------------------------------------------------------------")  # 60個

""" lack pic
def do_select_intc():
    if var_intc.get()==0:
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

tk.Label(window,text="請點選想了解的動物簡介:").pack()

var_intc = tk.IntVar()
var_intc.set(0)  # 預設

pic1 = tk.PhotoImage(file="cattle.gif")
pic2 = tk.PhotoImage(file="deer.gif")

tk.Radiobutton(window,image=pic1,variable=var_intc,value=0).pack()
tk.Radiobutton(window,image=pic2,variable=var_intc,value=1).pack()
tk.Button(window,text="進一步了解", command=do_select_intc).pack()

window.mainloop()
"""

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


window.mainloop()
sys.exit()


"""

# 預設音樂是1


"""


def do_select_string4():
    print("s4你選擇了 : " + var_string4.get())


frame1 = tk.Frame(window)  # mp3 歌曲容器
frame1.pack()

source_dir = "C:/_git/vcs/_1.data/______test_files1/_mp3/"

mp3files = glob.glob(source_dir + "*.mp3")

playsong = preplaysong = ""
index = 0

var_string4 = tk.StringVar()

# 用字典串列元組 一次建立一組Radiobutton
for mp3 in mp3files:
    rb = tk.Radiobutton(
        frame1, text=mp3, variable=var_string4, value=mp3, command=do_select_string4
    )
    if index == 0:  # 選取第1個選項按鈕
        rb.select()  # 預設
        playsong = preplaysong = mp3
    rb.grid(row=index, column=0, sticky="w")
    index += 1

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

from PIL import ImageTk, Image


def printSelection():
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

rbStar = tk.Radiobutton(
    window, image=tk_image1, variable=var, value="星星", command=printSelection  # 星星選項鈕
)
rbStar.pack()

rbMoon = tk.Radiobutton(
    window, image=tk_image2, variable=var, value="月亮", command=printSelection  # 月亮選項鈕
)
rbMoon.pack()

rbSun = tk.Radiobutton(
    window, image=tk_image3, variable=var, value="太陽", command=printSelection  # 太陽選項鈕
)
rbSun.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個


def printSelection():
    label.config(text="你選的是" + var.get())


filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

window = tk.Tk()
window.geometry("600x800")
window.title("Radiobutton 5")


# 檔案 => ImageTk影像
tk_image1 = ImageTk.PhotoImage(file="__new/star.gif")
tk_image2 = ImageTk.PhotoImage(file="__new/moon.gif")
tk_image3 = ImageTk.PhotoImage(file="__new/sun.gif")

var = tk.StringVar()  # 選項紐綁定的變數
var.set("星星")  # 預設選項是男生

label = tk.Label(window, text="這是預設,尚未選擇", bg="lightyellow", width=30)
label.pack()

rbStar = tk.Radiobutton(
    window,
    image=tk_image1,  # 星星選項鈕
    text="星星",
    compound=tk.RIGHT,
    variable=var,
    value="星星",
    command=printSelection,
)
rbStar.pack()

rbMoon = tk.Radiobutton(
    window,
    image=tk_image2,  # 月亮選項鈕
    text="月亮",
    compound=tk.RIGHT,
    variable=var,
    value="月亮",
    command=printSelection,
)
rbMoon.pack()

rbSun = tk.Radiobutton(
    window,
    image=tk_image3,  # 太陽選項鈕
    text="太陽",
    compound=tk.RIGHT,
    variable=var,
    value="太陽",
    command=printSelection,
)
rbSun.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個


def choose():
    print("你點選了 :", choice.get())


def add_radiobutton_controls():
    global choice
    frame1 = tk.Frame(window)
    frame1.pack()

    list_data = ["aaa", "bbb", "ccc", "ddd", "eee"]

    index = 0
    choice = tk.StringVar()
    for line in list_data:
        prbutton = tk.Radiobutton(
            frame1, text=line, variable=choice, value=line, command=choose
        )
        if index == 0:
            prbutton.select()
        prbutton.grid(row=index, column=0, sticky="w")
        index += 1


import tkinter as tk
import glob

window = tk.Tk()
window.geometry("640x480")
window.title("")

frame0 = tk.Frame(window)
frame0.pack()

button7 = tk.Button(frame0, text="讀取檔案", width=8, command=add_radiobutton_controls)
button7.grid(row=1, column=0, padx=5, pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")
window.title("new all 7")

# 單選按鈕
# 定義幾個顏色的全局變量
colors = ["紅", "綠", "藍"]


# 單選按鈕回調函數,就是當單選按鈕被點擊會執行該函數
def radCall():
    select_value = radVar.get()
    print(select_value)
    if select_value == 0:
        window.configure(background='red')  # 設置整個界面的背景顏色
    elif select_value == 1:
        window.configure(background='green')
    elif select_value == 2:
        window.configure(background='blue')


radVar = tk.IntVar()  # 通過tk.IntVar(),獲取單選按鈕value參數對應的值
radVar.set(99)
for col in range(3):
    # 當該單選按鈕被點擊時，會觸發參數command對應的函數
    curRad = tk.Radiobutton(
        window, text=colors[col], variable=radVar, value=col, command=radCall
    )
    curRad.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

