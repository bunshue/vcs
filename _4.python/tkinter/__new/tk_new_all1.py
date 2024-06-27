import sys

import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image

W = 200
H = 200
w = 12
h = 2

print("------------------------------------------------------------")  # 60個
'''
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

# tkinterDialog.py


class MyDialog:  # 定義交談視窗類別
    def __init__(self, root):
        self.top = tk.Toplevel(root)  # 產生Toplevel元件
        label = tk.Label(self.top, text="Please Input")  # 產生標簽元件
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


class MyButton:  # 定義按鈕類別
    def __init__(self, root):
        self.root = root  # 儲存父視窗參考
        self.button = tk.Button(
            root, text="Create", command=self.Create
        )  # 設定Create按鈕的事件處理函數
        self.button.pack()

    def Create(self):  # Create按鈕的事件處理函數
        d = MyDialog(self.root)  # 產生交談視窗
        self.button.wait_window(d.top)  # 等待交談視窗結束
        print("你輸入了 :" + d.get())  # 取得交談視窗中輸入值，並輸出


window = tk.Tk()  # 產生主視窗
window.geometry("600x400")

MyButton(window)  # 產生Create按鈕

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
window.title("new all 2")

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
window.title("new all 2")

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
'''
print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")

def CreateNewWindow():  # 建立對話方塊
    labTxt = "開啟新視窗1\n開啟新視窗2\n開啟新視窗3\nToplevel"
    tl = tk.Toplevel()  # 建立Toplevel視窗
    tl.geometry("300x180")  # 建立對話方塊大小
    tl.title("開啟新視窗")
    tk.Label(tl, text=labTxt).pack(fill=tk.BOTH, expand=True)

button1 = tk.Button(window, text="開啟新視窗", command=CreateNewWindow)
button1.pack()

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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
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


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

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

from tkinter import Tk, Variable, Entry, Button


def get_entry_data():
    cc = a.get()
    print("你取得了 :", cc)


window = tk.Tk()

a = tk.Variable(window, value="123")
e = tk.Entry(window, textvariable=a)
b = tk.Button(window, text="獲取", command=get_entry_data)
e.pack()
b.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
tk.Label(window, text="帳號：").grid(row=0, column=0)
tk.Label(window, text="密碼：").grid(row=1, column=0)

v1 = tk.StringVar()  # 輸入框里是字符串類型，因此用Tkinter的StringVar類型來存放
v2 = tk.StringVar()  # 需要兩個變量來存放帳號和密碼

e1 = tk.Entry(window, textvariable=v1)
e2 = tk.Entry(window, textvariable=v2, show="*")  # 想要顯示什么就輸入什么

e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)


def show():
    print("帳號：%s" % e1.get())
    print("密碼：%s" % e2.get())


tk.Button(window, text="獲取信息", width=10, command=show).grid(
    row=3, column=0, sticky=tk.W, padx=10, pady=5
)
tk.Button(window, text="退出", width=10, command=window.destroy).grid(
    row=3, column=1, sticky=tk.E, padx=10, pady=5
)

window.mainloop()

print("------------------------------------------------------------")  # 60個

# 創建容器
window = tk.Tk()
window.title("我的GUI界面學習")

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

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import scrolledtext  # 導入滾動文本框的模塊

window = tk.Tk()
window.title("Python GUI")  # 加標題

# 創建一個容器,
monty = ttk.LabelFrame(window, text=" Monty Python ")  # 創建一個容器，其父容器為win
monty.grid(column=0, row=0, padx=10, pady=10)  # 該容器外圍需要留出的空余空間
aLabel = ttk.Label(monty, text="A Label")
ttk.Label(monty, text="Chooes a number").grid(column=1, row=0)  # 添加一個標簽，并將其列設置為1，行設置為0
ttk.Label(monty, text="Enter a name:").grid(
    column=0, row=0, sticky="W"
)  # 設置其在界面中出現的位置,column代表列,row代表行


# button被點擊之后會被執行
def clickMe():  # 當acction被點擊時,該函數則生效
    action.configure(
        text="Hello " + name.get() + " " + numberChosen.get()
    )  # 設置button顯示的內容
    print("check3 is %s %s" % (type(chvarEn.get()), chvarEn.get()))


# 創建一個按鈕, text：顯示按鈕上面顯示的文字, command：當這個按鈕被點擊之后會調用command函數
action = ttk.Button(monty, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)  # 設置其在界面中出現的位置,column代表列,row 代表行

# 文本框
name = tk.StringVar()  # StringVar是Tk庫內部定義的字符串變量類型
nameEntered = ttk.Entry(monty, width=12, textvariable=name)  # 創建一個文本框，定義長度為12個字符長度
nameEntered.grid(column=0, row=1, sticky=tk.W)  # 設置其在界面中出現的位置,column代表列,row代表行
nameEntered.focus()  # 當程序運行時,光標默認會出現在該文本框中

# 創建一個下拉列表
number = tk.StringVar()
numberChosen = ttk.Combobox(monty, width=12, textvariable=number, state="readonly")
numberChosen["values"] = (1, 2, 4, 42, 100)  # 設置下拉列表的值
numberChosen.grid(column=1, row=1)  # 設置其在界面中出現的位置,column代表列,row 代表行
numberChosen.current(0)  # 設置下拉列表默認顯示的值，0為 numberChosen['values'] 的下標值

# 復選框
chVarDis = tk.IntVar()  # 用來獲取復選框是否被勾選，其狀態值為int類型,勾選為1,未勾選為0

# text為該復選框后面顯示的名稱, variable將該復選框的狀態賦值給一個變量，當state='disabled'時，該復選框為灰色，不能點的狀態
check1 = tk.Checkbutton(monty, text="Disabled", variable=chVarDis, state="disabled")
check1.select()  # 該復選框是否勾選,select為勾選, deselect為不勾選
check1.grid(
    column=0, row=4, sticky=tk.W
)  # sticky=tk.W(N：北/上對齊,S：南/下對齊,W：西/左對齊,E：東/右對齊)
chvarUn = tk.IntVar()
check2 = tk.Checkbutton(monty, text="UnChecked", variable=chvarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)
chvarEn = tk.IntVar()
check3 = tk.Checkbutton(monty, text="Enabled", variable=chvarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

# 單選按鈕
# 定義幾個顏色的全局變量
colors = ["Blue", "Gold", "Red"]


# 單選按鈕回調函數,就是當單選按鈕被點擊會執行該函數
def radCall():
    radSel = radVar.get()
    if radSel == 0:
        window.configure(background=colors[0])  # 設置整個界面的背景顏色
        print(radVar.get())
    elif radSel == 1:
        window.configure(background=colors[1])
    elif radSel == 2:
        window.configure(background=colors[2])


radVar = tk.IntVar()  # 通過tk.IntVar(),獲取單選按鈕value參數對應的值
radVar.set(99)
for col in range(3):
    # 當該單選按鈕被點擊時，會觸發參數command對應的函數
    curRad = tk.Radiobutton(
        monty, text=colors[col], variable=radVar, value=col, command=radCall
    )
    curRad.grid(column=col, row=5, sticky=tk.W)  # 參數sticky對應的值參考復選框的解釋

# 滾動文本框
scrolW = 30  # 設置文本框的長度
scrolH = 3  # 設置文本框的高度
# wrap=tk.WORD這個值表示在行的末尾如果有一個單詞跨行，會將該單詞放到下一行顯示
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

window.mainloop()

print("------------------------------------------------------------")  # 60個


# 定義繼承Frame的Application類
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        # 調用initWidgets()方法初始化界面
        self.initWidgets()

    def initWidgets(self):
        # 創建Label對象，第一個參數指定該Label放入root
        w = tk.Label(self)
        # 創建一個位圖
        bm = tk.PhotoImage(file="images/a.png")
        # 必須用一個不會被釋放的變量引用該圖片，否則該圖片會被回收
        w.x = bm
        # 設置顯示的圖片是bm
        w["image"] = bm
        w.pack()
        # 創建Button對象，第一個參數指定該Button放入root
        okButton = tk.Button(self, text="確定")
        okButton.configure(background="red")
        okButton.pack()


# 創建Application對象
app = Application()

# Frame有個默認的master屬性，該屬性值是Tk對象（窗口）
print(type(app.master))
# 通過master屬性來設置窗口標題
app.master.title("窗口標題")

app.mainloop()

print("------------------------------------------------------------")  # 60個


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 創建第一個容器
        fm1 = tk.Frame(self.master)
        # 該容器放在左邊排列
        fm1.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        # 向fm1中添加3個按鈕
        # 設置按鈕從頂部開始排列，且按鈕只能在垂直（X）方向填充
        tk.Button(fm1, text="第一個").pack(side=tk.TOP, fill=tk.X, expand=tk.YES)
        tk.Button(fm1, text="第二個").pack(side=tk.TOP, fill=tk.X, expand=tk.YES)
        tk.Button(fm1, text="第三個").pack(side=tk.TOP, fill=tk.X, expand=tk.YES)
        # 創建第二個容器
        fm2 = tk.Frame(self.master)
        # 該容器放在左邊排列，就會挨著fm1
        #        fm2.pack(side=tk.LEFT, padx=10, expand=tk.YES)
        fm2.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=tk.YES)
        # 向fm2中添加3個按鈕
        # 設置按鈕從右邊開始排列
        tk.Button(fm2, text="第一個").pack(side=tk.RIGHT, fill=tk.Y, expand=tk.YES)
        tk.Button(fm2, text="第二個").pack(side=tk.RIGHT, fill=tk.Y, expand=tk.YES)
        tk.Button(fm2, text="第三個").pack(side=tk.RIGHT, fill=tk.Y, expand=tk.YES)
        # 創建第三個容器
        fm3 = tk.Frame(self.master)
        # 該容器放在右邊排列，就會挨著fm1
        fm3.pack(side=tk.RIGHT, padx=10, fill=tk.BOTH, expand=tk.YES)
        # 向fm3中添加3個按鈕
        # 設置按鈕從底部開始排列，且按鈕只能在垂直（Y）方向填充
        tk.Button(fm3, text="第一個").pack(side=tk.BOTTOM, fill=tk.Y, expand=tk.YES)
        tk.Button(fm3, text="第二個").pack(side=tk.BOTTOM, fill=tk.Y, expand=tk.YES)
        tk.Button(fm3, text="第三個").pack(side=tk.BOTTOM, fill=tk.Y, expand=tk.YES)


window = tk.Tk()
window.title("Pack布局")
display = App(window)
window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# 單獨的 或無法合併的 搬到最後面


import calendar

window = tk.Tk()
window.config(background="grey")
window.title("Calender for the year")
window.geometry("550x600")

year = 2024
content = calendar.calendar(year)
calYear = tk.Label(window, text=content, font="Consolas 10 bold")
calYear.grid(row=5, column=1, padx=20)

window.mainloop()

print("------------------------------------------------------------")  # 60個


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



class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 創建一個輸入組件
        e = tk.Entry(relief=tk.SUNKEN, font=("Courier New", 24), width=25)
        # 對該輸入組件使用Pack布局，放在容器頂部
        e.pack(side=tk.TOP, pady=10)
        p = tk.Frame(self.master)
        p.pack(side=tk.TOP)
        # 定義字符串的元組
        names = (
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "+",
            "-",
            "*",
            "/",
            ".",
            "=",
        )
        # 遍歷字符串元組
        for i in range(len(names)):
            # 創建Button，將Button放入p組件中
            b = tk.Button(p, text=names[i], font=("Verdana", 20), width=6)
            b.grid(row=i // 4, column=i % 4)


window = tk.Tk()
window.title("Grid布局")
App(window)

window.mainloop()

print("------------------------------------------------------------")  # 60個


from tkinter import messagebox


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)  # super()代表的是父類的定義， 而不是父類對象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """通過 grid 布局實現登錄界面"""
        self.label01 = tk.Label(self, text="用戶名")
        self.label01.grid(row=0, column=0)
        self.entry01 = tk.Entry(self)
        self.entry01.grid(row=0, column=1)
        tk.Label(self, text="用戶名為手機號").grid(row=0, column=2)
        tk.Label(self, text="密碼").grid(row=1, column=0)
        tk.Entry(self, show="*").grid(row=1, column=1)
        tk.Button(self, text="登錄").grid(row=2, column=1, sticky=tk.E + tk.W)
        tk.Button(self, text="取消").grid(row=2, column=2, sticky=tk.E)


window = tk.Tk()
window.geometry("400x90+200+300")
app = Application(master=window)

window.title("Grid布局")
window.mainloop()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

