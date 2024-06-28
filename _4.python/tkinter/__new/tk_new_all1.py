import sys

import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image

W = 200
H = 200
w = 12
h = 2

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("new all 2")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


label5 = tk.Label(
    window,
    anchor=tk.E,  # 設定文字的位置
    bg="blue",  # 設定標簽背景色
    fg="red",  # 設定標簽前景色
    text="Python",  # 設定標簽中的文字
    width=30,  # 設定標簽的寬度為30
    height=3,
)  # 設定標簽的的高度為5
label5.pack()

label2 = tk.Label(
    window,
    text="Python GUI\nTkinter",  # 設定標簽中的文字，在字串中使用換行符
    justify=tk.LEFT,  # 設定多行文字為齊左
    width=30,
    height=3,
)
label2.pack()

label3 = tk.Label(
    window,
    text="Python GUI\nTkinter",
    justify=tk.RIGHT,  # 設定多行文字為齊右
    width=30,
    height=3,
)
label3.pack()

label4 = tk.Label(
    window,
    text="Python GUI\nTkinter",
    justify=tk.CENTER,  # 設定多行文字為劇中對齊
    width=30,
    height=3,
)
label4.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

from tkinter.ttk import Separator

# 字 前景 背景 寬 高 字位置預設 字型
label = tk.Label(
    window,
    text="Welcome to the United States and have a nice day",
    fg="red",
    bg="gray",
    width=15,
    height=4,
    font=("Helvetica", 8, "bold"),
)
label.pack()

# 字 前景 背景 寬 高 字位置西北
label = tk.Label(
    window,
    text="Welcome to the United States and have a nice day",
    fg="blue",
    bg="lime",
    width=15,
    height=4,
    anchor="nw",
)
label.pack()

# 字 前景 背景 寬 高 字位置西北 卷寬度
label = tk.Label(
    window,
    text="Welcome to the United States and have a nice day",
    fg="blue",
    bg="yellow",
    width=15,
    height=4,
    anchor="nw",
    wraplength=80,
    justify="left",
)  # left / center / right
label.pack()


print("在視窗的右下方顯示兩個Label")
oklabel = tk.Label(
    window,
    text="OK",  # 標籤內容是OK
    font="Times 20 bold",  # Times字型20粗體
    fg="white",
    bg="blue",
)  # 藍底白字
oklabel.pack(anchor=tk.S, side=tk.RIGHT, padx=10, pady=10)  # 從右開始在南方配置  # x和y軸間距皆是10

nolabel = tk.Label(
    window,
    text="NO",  # 標籤內容是OK
    font="Times 20 bold",  # Times字型20粗體
    fg="white",
    bg="red",
)  # 藍底白字
nolabel.pack(anchor=tk.S, side=tk.RIGHT, pady=10)  # 從右開始在南方配置  # y軸間距皆是10

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("new all 2")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

button1 = tk.Button(window, text="pack置中", width=20).pack()
button2 = tk.Button(window, text="pack左", width=20).pack(side=tk.LEFT)
button3 = tk.Button(window, text="pack右", width=20).pack(side=tk.RIGHT)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

# 設定視窗背景色
window.config(bg="red")
window.config(bg="green")
window.config(bg="blue")

"""
# 將4個鈕包裝定位在右下方
button4.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
button3.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
button2.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
button1.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
"""

print("pack版面佈局的示範")

plus = tk.Button(window, width=20, text="加法範例")
plus.pack(side="left")
minus = tk.Button(window, width=20, text="減法範例")
minus.pack(side="left")
multiply = tk.Button(window, width=20, text="乘法範例")
multiply.pack(side="left")
divide = tk.Button(window, width=20, text="除法範例")
divide.pack(side="left")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack(fill=tk.X)  # 填滿X軸包裝與定位元件
label2.pack(pady=10)  # y軸增加10像素
label3.pack(fill=tk.X)  # 填滿X軸包裝與定位元件

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")  # 標籤背景是淺藍色
label1.pack(fill=tk.X, pady=10)  # 填滿X軸,Y軸增加10像素
label2.pack(pady=10)  # Y軸增加10像素
label3.pack(fill=tk.X)  # 填滿X軸包裝與定位元件

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(
    window, text="歡迎來到美國", bg="lightyellow", width=15  # 標籤背景是淺黃色
)  # 標籤寬度是15
label2 = tk.Label(
    window, text="歡迎來到美國", bg="lightgreen", width=15  # 標籤背景是淺綠色
)  # 標籤寬度是15
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue", width=15)  # 標籤寬度是15
label1.pack(padx=50)  # 左右邊界間距是50像素
label2.pack(padx=50)  # 左右邊界間距是50像素
label3.pack(padx=50)  # 左右邊界間距是50像素

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(
    window, text="歡迎來到美國", bg="lightyellow", width=15  # 標籤背景是淺黃色
)  # 標籤寬度是15
label2 = tk.Label(
    window, text="歡迎來到美國", bg="lightgreen", width=15  # 標籤背景是淺綠色
)  # 標籤寬度是15
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue", width=15)  # 標籤寬度是15
label1.pack(side=tk.LEFT)
label2.pack(side=tk.LEFT, padx=10)  # 左右間距padx=10
label3.pack(side=tk.LEFT)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack()
label2.pack(ipadx=10)  # ipadx=10包裝與定位元件
label3.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("new all 3")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")  # 標籤背景是淺黃色
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack()
label2.pack(ipadx=10)  # ipadx=10包裝與定位元件
label3.pack(ipady=10)  # ipady=10包裝與定位元件

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack(fill=tk.X)  # 填滿X軸包裝與定位元件
label2.pack()
label3.pack(fill=tk.X)  # 填滿X軸包裝與定位元件

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack(fill=tk.X)  # 填滿X軸包裝與定位元件
label2.pack(fill=tk.Y)  # 填滿Y軸包裝與定位元件
label3.pack(fill=tk.X)  # 填滿X軸包裝與定位元件

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack(side=tk.LEFT)  # 從左配置控件
label2.pack()  # 預設從上開始配置控件
label3.pack()  # 預設從上開始配置控件

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack(side=tk.LEFT, fill=tk.Y)  # 從左配置控件fill=tk.Y
label2.pack(fill=tk.X)  # 預設從上開始配置控件fill=tk.X
label3.pack()  # 預設從上開始配置控件

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack(side=tk.LEFT, fill=tk.Y)  # 從左配置控件fill=tk.Y
label2.pack(fill=tk.X)  # 預設從上開始配置控件fill=tk.X
label3.pack(fill=tk.X)  # 預設從上開始配置控件fill=tk.X

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack(side=tk.LEFT, fill=tk.Y)  # 從左配置控件fill=tk.Y
label2.pack(fill=tk.X)  # 預設從上開始配置控件fill=tk.X
label3.pack(fill=tk.BOTH)  # 預設從上開始配置控件fill=tk.BOTH

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("new all 4")

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window, text="歡迎來到美國", bg="lightyellow")
label2 = tk.Label(window, text="歡迎來到美國", bg="lightgreen")
label3 = tk.Label(window, text="歡迎來到美國", bg="lightblue")
label1.pack(side=tk.LEFT, fill=tk.Y)  # 從左配置控件fill=tk.Y
label2.pack(fill=tk.X)  # 預設從上開始配置控件fill=tk.X
label3.pack(fill=tk.BOTH, expand=True)  # fill=tk.BOTH,expand=True

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

tk.Label(window, text="Mississippi", bg="red", fg="white", font="Times 24 bold").pack(
    fill=tk.X
)
tk.Label(
    window, text="Kentucky", bg="green", fg="white", font="Arial 24 bold italic"
).pack(fill=tk.BOTH, expand=True)
tk.Label(window, text="Purdue", bg="blue", fg="white", font="Times 24 bold").pack(
    fill=tk.X
)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

tk.Label(window, text="Mississippi", bg="red", fg="white", font="Times 20 bold").pack(
    side=tk.LEFT, fill=tk.Y
)
tk.Label(
    window, text="Kentucky", bg="green", fg="white", font="Arial 20 bold italic"
).pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
tk.Label(window, text="Purdue", bg="blue", fg="white", font="Times 20 bold").pack(
    side=tk.LEFT, fill=tk.Y
)

window.mainloop()

print("------------------------------------------------------------")  # 60個
# Toplevel
print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

tl = tk.Toplevel()
tk.Label(tl, text="I am a Toplevel").pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

tl = tk.Toplevel()
tl.title("Toplevel")
tl.geometry("300x180")

tk.Label(tl, text="I am a Toplevel").pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個


# 開啟新視窗
class MyDialog:  # 定義交談視窗類別
    def __init__(self, root):
        self.top = tk.Toplevel(root)  # 產生Toplevel元件
        label = tk.Label(self.top, text="請輸入密碼")  # 產生標簽元件
        label.pack()
        self.entry = tk.Entry(self.top)  # 產生文字框元件
        self.entry.pack()
        self.entry.focus()  # 讓文字框獲得焦點
        button = tk.Button(self.top, text="Ok", command=self.Ok)
        button.pack()

    def Ok(self):
        self.input = self.entry.get()  # 取得文字框中內容，儲存為input
        self.top.destroy()  # 銷毀交談視窗

    def get(self):  # 傳回在文字框輸入的內容
        return self.input


window = tk.Tk()
window.geometry("600x800")
window.title("new all 6")


def CreateNewWindow1():  # 建立對話方塊
    labTxt = "開啟新視窗1\n開啟新視窗2\n開啟新視窗3\nToplevel"
    tl = tk.Toplevel()  # 建立Toplevel視窗
    tl.geometry("300x180")  # 建立對話方塊大小
    tl.title("開啟新視窗")
    tk.Label(tl, text=labTxt).pack(fill=tk.BOTH, expand=True)


button1 = tk.Button(window, text="開啟新視窗", command=CreateNewWindow1)
button1.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


def CreateNewWindow2():  # Create按鈕的事件處理函數
    d = MyDialog(window)  # 產生交談視窗
    button2.wait_window(d.top)  # 等待交談視窗結束
    print("你輸入了 :" + d.get())  # 取得交談視窗中輸入值，並輸出


button2 = tk.Button(
    window, text="開啟新視窗取得資料", command=CreateNewWindow2
)  # 設定Create按鈕的事件處理函數
button2.pack()

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


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("new all 6")


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

entry8 = tk.Entry(window, bg="#ffff00", borderwidth=3)
entry8.insert(0, "AAAA")
entry8.insert("2", "BBBB")
entry8.insert("end", "CCCC")
entry8.delete(0, 2)  # 刪除前面兩個字元
entry8.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

tk.Label(window, text="on the window").pack()

frm = tk.Frame(window)
frm.pack()

frm_l = tk.Frame(
    frm,
)

frm_r = tk.Frame(frm)
frm_l.pack(side="left")
frm_r.pack(side="right")

tk.Label(frm_l, text="on the frm_l1").pack()
tk.Label(frm_l, text="on the frm_l2").pack()
tk.Label(frm_r, text="on the frm_r1").pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個


# e = tk.Entry(window, show="*")
e = tk.Entry(window, show="1")
e.pack()


def insert_point():
    var = e.get()
    t.insert("insert", var)


def insert_end():
    var = e.get()
    # t.insert('end', var)
    t.insert(2.2, var)


b1 = tk.Button(window, text="insert point", width=15, height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text="insert end", command=insert_end)
b2.pack()
t = tk.Text(window, height=2)
t.pack()


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

frame1 = tk.Frame(window)
frame1.pack()

lab1 = tk.Label(frame1, text="你好，這是Checkbutton操作界面")
lab1.pack()


def button1back_handle():
    print("button1 down")


button2val = tk.IntVar()
button2 = tk.Checkbutton(
    frame1,
    text="BUTTON2",
    variable=button2val,  # variable為按鍵的狀態值
    anchor="n",  # 按鍵文本位置為n
    bd=5,  # 將borderwidth（邊框寬度）設置為5
    command=button1back_handle,  # 傳入回調函數
    justify="left",  # 按鍵文本為左對齊
    cursor="right_ptr",  # 將光標移動至按鍵時的顯示修改為
    font=("宋體", 15, "bold", "italic"),  # 設置按鍵的字體、大小、加粗、斜體
    padx=5,
    pady=5,  # 指定按鍵文本或圖像距離邊框的距離
    relief=tk.RAISED,  # 指定按鍵的樣式
    state=tk.ACTIVE,  # 指定按鍵的狀態
    width=10,
    height=5,  # 制定按鍵的寬、高
)
button2.pack()
# 為了看到按鍵值使用Lable控件顯示下按鍵的值
tk.Label(frame1, textvariable=button2val).pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

# jpg fail
# filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg' fail

# gif/png ok
# filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/SpongeBob.gif'
filename = "C:/_git/vcs/_4.python/_data/logo1.png"

label1 = tk.Label(window)
# 創建一個位圖
bm = tk.PhotoImage(file=filename)
# 必須用一個不會被釋放的變量引用該圖片，否則該圖片會被回收
label1.x = bm
# 設置顯示的圖片是bm
label1["image"] = bm
label1.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

# 單獨的 或無法合併的 搬到最後面


class WidgetsDemo:
    def __init__(self):
        window = tk.Tk()
        window.title("Widgets Demo")  # Set a title

        # Add a button, a check button, and a radio button to frame1
        frame1 = tk.Frame(window)
        frame1.pack()
        self.v1 = tk.IntVar()
        cbtBold = tk.Checkbutton(
            frame1, text="Bold", variable=self.v1, command=self.processCheckbutton
        )
        self.v2 = tk.IntVar()
        rbRed = tk.Radiobutton(
            frame1,
            text="Red",
            bg="red",
            variable=self.v2,
            value=1,
            command=self.processRadiobutton,
        )
        rbYellow = tk.Radiobutton(
            frame1,
            text="Yellow",
            bg="yellow",
            variable=self.v2,
            value=2,
            command=self.processRadiobutton,
        )
        cbtBold.grid(row=1, column=1)
        rbRed.grid(row=1, column=2)
        rbYellow.grid(row=1, column=3)

        # Add a button, a check button, and a radio button to frame1
        frame2 = tk.Frame(window)
        frame2.pack()
        label = tk.Label(frame2, text="Enter your name: ")
        self.name = tk.StringVar()
        entryName = tk.Entry(frame2, textvariable=self.name)
        btGetName = tk.Button(frame2, text="Get Name", command=self.processButton)
        message = tk.Message(frame2, text="It is a widgets demo")
        label.grid(row=1, column=1)
        entryName.grid(row=1, column=2)
        btGetName.grid(row=1, column=3)
        message.grid(row=1, column=4)

        # Add a text
        text = tk.Text(window)  # Create a text add to the window
        text.pack()
        text.insert(tk.END, "Tip\nThe best way to learn Tkinter is to read ")
        text.insert(tk.END, "these carefully designed examples and use them ")
        text.insert(tk.END, "to create your applications.")

        window.mainloop()  # Create an event loop

    def processCheckbutton(self):
        print("check button is " + ("checked " if self.v1.get() == 1 else "unchecked"))

    def processRadiobutton(self):
        print(("Red" if self.v2.get() == 1 else "Yellow") + " is selected ")

    def processButton(self):
        print("Your name is " + self.name.get())


WidgetsDemo()  # Create GUI

print("------------------------------------------------------------")  # 60個


class ChangeLabelDemo:
    def __init__(self):
        window = tk.Tk()  # Create a window
        window.title("Change Label Demo")  # Set a title

        # Add a label to frame1
        frame1 = tk.Frame(window)
        frame1.pack()
        self.lbl = tk.Label(frame1, text="Programming is fun")
        self.lbl.pack()

        # Add a label, an entry, a button, and two radio buttons to frame2
        frame2 = tk.Frame(window)
        frame2.pack()
        label = tk.Label(frame2, text="Enter text: ")
        self.msg = tk.StringVar()
        entry = tk.Entry(frame2, textvariable=self.msg)
        btChangeText = tk.Button(frame2, text="Change Text", command=self.processButton)
        self.v1 = tk.StringVar()
        rbRed = tk.Radiobutton(
            frame2,
            text="Red",
            bg="red",
            variable=self.v1,
            value="R",
            command=self.processRadiobutton,
        )
        rbYellow = tk.Radiobutton(
            frame2,
            text="Yellow",
            bg="yellow",
            variable=self.v1,
            value="Y",
            command=self.processRadiobutton,
        )

        label.grid(row=1, column=1)
        entry.grid(row=1, column=2)
        btChangeText.grid(row=1, column=3)
        rbRed.grid(row=1, column=4)
        rbYellow.grid(row=1, column=5)

        window.mainloop()

    def processRadiobutton(self):
        if self.v1.get() == "R":
            self.lbl["fg"] = "red"
        elif self.v1.get() == "Y":
            self.lbl["fg"] = "yellow"

    def processButton(self):
        self.lbl["text"] = self.msg.get()  # New text for the label


ChangeLabelDemo()  # Create GUI


print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("700x220")
window.title("制作鋼琴按鍵布局")

# Frame 是一個矩形區域， 就是用來防止其他子組件
f1 = tk.Frame(window)
f1.pack()

f2 = tk.Frame(window)
f2.pack()

btnText = ("流行風", "中國風", "倫敦風", "古典風", "輕音樂")
for txt in btnText:
    tk.Button(f1, text=txt).pack(side="left", padx="10")
    for i in range(1, 20):
        tk.Button(f2, width=5, height=10, bg="black" if i % 2 == 0 else "white").pack(
            side="left"
        )
window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("使用 grid")
window = tk.Tk()
window.title("Python圖形界面")

label1 = ttk.Label(window, text="選擇數字")
label1.grid(column=1, row=0)  # 添加一個標簽，并將其列設置為1，行設置為0


# button被點擊之后會被執行
def clickMe():  # 當acction被點擊時,該函數則生效"顯示當前選擇的數"
    print(numberChosen.current())  # 輸出下所選的索引

    if numberChosen.current() == 0:  # 判斷列表當前所選~~~~~~~~~~~
        label1.config(text="選了1")  # 注意，上面的label1如果直接.grid會出錯
    if numberChosen.current() == 1:
        label1.config(text="選了6")
    if numberChosen.current() == 2:
        label1.config(text="選了第" + str(numberChosen.current() + 1) + "個")


# 按鈕
action = ttk.Button(
    window, text="單擊我", command=clickMe
)  # 創建一個按鈕, text：顯示按鈕上面顯示的文字, command：當這個按鈕被點擊之后會調用command函數
action.grid(column=2, row=1)  # 設置其在界面中出現的位置,column代表列,row代表行
# 創建一個下拉列表
number = tk.StringVar()
numberChosen = ttk.Combobox(window, width=12, textvariable=number)
numberChosen["values"] = (1, 6, 3)  # 設置下拉列表的值
numberChosen.grid(column=1, row=1)  # 設置其在界面中出現的位置,column代表列,row代表行
numberChosen.current(0)  # 設置下拉列表默認顯示的值，0為numberChosen['values']的下標值

window.mainloop()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
