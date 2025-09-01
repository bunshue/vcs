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

tk.Label(window, text = "標準版顯示訊息").pack()
label5 = tk.Label(
    window,
    anchor=tk.E,  # 設定文字的位置
    bg="lightgreen",
    fg="red",
    text="Python",  # 設定標簽中的文字
    width=30,  # 設定標簽的寬度為30
    height=3,
)  # 設定標簽的的高度為5
label5.pack()

label2 = tk.Label(
    window,
    text="Python GUI\nTkinter",  # 設定標簽中的文字，在字串中使用換行符
    bg="pink",
    justify=tk.LEFT,  # 設定多行文字為齊左
    width=30,
    height=3,
)
label2.pack()

label3 = tk.Label(
    window,
    text="Python GUI\nTkinter",
    bg="lightyellow",
    justify=tk.RIGHT,  # 設定多行文字為齊右
    width=30,
    height=3,
)
label3.pack()

label4 = tk.Label(
    window,
    text="Python GUI\nTkinter",
    bg="lightblue",
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
    height=3,
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
    height=3,
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
    height=3,
    anchor="nw",
    wraplength=80,
    justify="left",
)  # left / center / right
label.pack()

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線
print("------------------------------------------------------------")  # 60個

tk.Label(window, text = "在視窗的右下方顯示兩個Label").pack()
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
# filename = 'D:/_git/vcs/_4.python/_data/picture1.jpg' fail

# gif/png ok
# filename = 'D:/_git/vcs/_1.data/______test_files1/__pic/_gif/SpongeBob.gif'
filename = "D:/_git/vcs/_4.python/_data/logo1.png"

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


"""

    def processCheckbutton(self):
        print("check button is " + ("checked " if self.v1.get() == 1 else "unchecked"))


        self.v1 = tk.IntVar()
        cbtBold = tk.Checkbutton(
            frame1, text="Bold", variable=self.v1, command=self.processCheckbutton
        )
        cbtBold.grid(row=1, column=1)


-----

    def processRadiobutton(self):
        print(("Red" if self.v2.get() == 1 else "Yellow") + " is selected ")


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

        rbRed.grid(row=1, column=2)
        rbYellow.grid(row=1, column=3)
        

"""
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

window = tk.Tk()
window.geometry("400x300")
window.title("Python圖形界面")

label1 = ttk.Label(window, text="選擇數字")
label1.pack()


# button被點擊之后會被執行
def clickMe():  # 當acction被點擊時,該函數則生效"顯示當前選擇的數"
    #print(combobox5.current())  # 輸出下所選的索引
    #print(combobox5["values"][combobox5.current()])  # 輸出下所選的索引
    combobox5_value = combobox5["values"][combobox5.current()]
    label1.config(text=str(combobox5_value))

tk.Button(window, text="單擊我", command=clickMe).pack()

# 創建一個下拉列表
number = tk.StringVar()
combobox5 = ttk.Combobox(window, width=12, textvariable=number)
combobox5["values"] = (3, 8, 3, 4, 2)  # 設置下拉列表的值
combobox5.pack()

combobox5.current(0)  # 設置下拉列表默認顯示的值，0為combobox5["values"]的下標值

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("new all 7")

from tkinter.messagebox import showinfo

tk.Button(window, command=lambda *args: showinfo(message="aaaaaaa"), text="獲取").pack()


def display():
    number = int(order.get())
    print('取得 order = ', number)
                
frame2 = tk.Frame(window, bg = 'pink') # Create and add a frame to window
frame2.pack()

tk.Label(frame2, text = "Enter an order: ").pack(side = tk.LEFT)
order = tk.StringVar()
entry = tk.Entry(frame2, textvariable = order, justify = tk.RIGHT).pack(side = tk.LEFT)
tk.Button(frame2, text = 'Do something', command = display).pack(side = tk.LEFT)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個






def changeString():
    stringToCopy = entry1.get()
    stringToCopy = stringToCopy[::-1]
    entry1.delete(0, tk.END)
    entry1.insert(0, stringToCopy)

entry1 = tk.Entry(window)
entry1.pack()

button0 = tk.Button(window, text = 'Change111', command = changeString)
button0.pack()


window.mainloop()


print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Label 1")

canvas1 = tk.Canvas(window, width=500, height=150, bg='pink')
canvas1.pack()

canvas1.create_window(500, 100, window = ttk.Button(window, text= 'this is text in a canvas'))

label1 = tk.Label(window, text = "Blue", bg = "blue").pack()
canvas1.create_window(500, 100, anchor="nw", window = label1)



window.mainloop()





print("------------------------------------------------------------")  # 60個



def printInfo():  # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (entry1.get(), entry2.get()))
    print('清除 entry1 entry2 的資料')
    entry1.delete(0, tk.END)  # 刪除account文字方塊的帳號內容
    entry2.delete(0, tk.END)  # 刪除pwd文字方塊的密碼內容

print("------------------------------------------------------------")  # 60個


window = tk.Tk()
window.geometry("640x480")
window.title("ImageTk 26")

label1 = tk.Label(window, text="Account")  # account標籤
label1.grid(row=1)

label2 = tk.Label(window, text="Password")  # pwd標籤
label2.grid(row=2)

entry1 = tk.Entry(window)  # 文字方塊account
entry2 = tk.Entry(window, show="*")  # 文字方塊pwd
entry1.insert(0, "Kevin")  # 預設Account內容
entry2.insert(0, "pwd")  # 預設pwd內容
entry1.grid(row=1, column=1)  # 定位文字方塊account
entry2.grid(row=2, column=1, pady=10)  # 定位文字方塊pwd

# 建立Login 按鈕
tk.Button(window, text="Login", command=printInfo).grid(row=3, column=0, sticky=tk.W, pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("640x480")
window.title("ImageTk 27")

label1 = tk.Label(window, text="Account")  # account標籤
label1.grid(row=1)

label2 = tk.Label(window, text="Password")  # pwd標籤
label2.grid(row=2)

entry1 = tk.Entry(window)  # 文字方塊account
entry2 = tk.Entry(window, show="*")  # 文字方塊pwd
entry1.insert(1, "Kevin")  # 預設Account內容
entry2.insert(1, "pwd")  # 預設pwd內容
entry1.grid(row=1, column=1)  # 定位文字方塊account
entry2.grid(row=2, column=1, pady=10)  # 定位文字方塊pwd

# 建立Login 按鈕
tk.Button(window, text="Login", command=printInfo).grid(row=3, column=0, sticky=tk.W, pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("640x480")
window.title("ImageTk 28")

# 以下是 LabelFrame 標籤框架
labelframe1 = tk.LabelFrame(window, text="資料驗證")  # 建立標籤框架
labelframe1.pack(padx=10, pady=5, ipadx=5, ipady=5)  # 包裝與定位標籤框架

label1 = tk.Label(labelframe1, text="Account")  # account標籤
label1.grid(row=0, column=0)

label2 = tk.Label(labelframe1, text="Password")  # pwd標籤
label2.grid(row=1, column=0)

entry1 = tk.Entry(labelframe1)  # 文字方塊account
entry1.grid(row=0, column=1)  # 定位文字方塊account
entry2 = tk.Entry(labelframe1, show="*")  # 文字方塊pwd
entry2.grid(row=1, column=1, pady=10)  # 定位文字方塊pwd

# 建立Login 按鈕
tk.Button(labelframe1, text="Login", command=printInfo).grid(row=2, column=0, sticky=tk.W, pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個



window = tk.Tk()
window.geometry("600x800")
window.title("new all 2")


# Window下的第二個Frame
# Add a button, a check button, and a radio button to frame1
frame2 = tk.Frame(window, bg="pink")  # Create and add a frame to window
frame2.pack()

label = tk.Label(frame2, text="Enter your name: ")
name = tk.StringVar()
entryName = tk.Entry(frame2, textvariable=name)
btGetName = tk.Button(frame2, text="Get Name", command="")
label.grid(row=1, column=1)
entryName.grid(row=1, column=2)
btGetName.grid(row=1, column=3)


window.mainloop()


print("------------------------------------------------------------")  # 60個


class ChangeLabelDemo:
    def __init__(self):
        window = tk.Tk()
        window.geometry("500x400")
        window.title("Change Label Demo")

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


import tkinter as tk
from tkinter import ttk


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=0.3, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        # create the widgets
        menu_button1 = ttk.Button(self, text="Button 1")
        menu_button2 = ttk.Button(self, text="Button 2")
        menu_button3 = ttk.Button(self, text="Button 3")

        menu_slider1 = ttk.Scale(self, orient="vertical")
        menu_slider2 = ttk.Scale(self, orient="vertical")

        toggle_frame = ttk.Frame(self)
        menu_toggle1 = ttk.Checkbutton(toggle_frame, text="check 1")
        menu_toggle2 = ttk.Checkbutton(toggle_frame, text="check 2")

        entry = ttk.Entry(self)

        # create the grid
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

        # place the widgets
        menu_button1.grid(row=0, column=0, sticky="nswe", columnspan=2)
        menu_button2.grid(row=0, column=2, sticky="nswe")
        menu_button3.grid(row=1, column=0, columnspan=3, sticky="nsew")

        menu_slider1.grid(row=2, column=0, rowspan=2, sticky="nsew", pady=20)
        menu_slider2.grid(row=2, column=2, rowspan=2, sticky="nsew", pady=20)

        # toggle layout
        toggle_frame.grid(row=4, column=0, columnspan=3, sticky="nsew")
        menu_toggle1.pack(side="left", expand=True)
        menu_toggle2.pack(side="left", expand=True)

        # entry layout
        entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor="center")


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
        # Entry(self, 'Entry 1','Button 1','green')
        # Entry(self, 'Entry 2','Button 2','blue')
        my_list(self, "Entry 1", "Entry 2", "Entry 3", "Button 1", "blue")
        my_list(self, "Entry 1", "Entry 2", "Entry 3", "Button 1", "red")
        my_list(self, "Entry 1", "Entry 2", "Entry 3", "Button 1", "red")
        my_list(self, "Entry 1", "Entry 2", "Entry 3", "Button 1", "red")


class Entry(ttk.Frame):
    def __init__(self, parent, label_text, button_text, label_background):
        super().__init__(parent)

        label = ttk.Label(self, text=label_text, background=label_background)
        button = ttk.Button(self, text=button_text)

        label.pack(expand=True, fill="both")
        button.pack(expand=True, fill="both", pady=10)

        self.pack(side="left", expand=True, fill="both", padx=20, pady=20)


class my_list(ttk.Frame):
    def __init__(
        self,
        parent,
        entry_text1,
        entry_text2,
        entry_text3,
        button_text,
        button_background,
    ):
        super().__init__(parent)
        entry1 = tk.Entry(self, background="red", text=entry_text1)
        entry1.pack(side="left")
        entry2 = tk.Entry(self, background="green", text=entry_text2)
        entry2.pack(side="left")
        entry3 = tk.Entry(self, foreground="blue", text=entry_text3)
        entry3.pack(side="left")
        button = ttk.Button(self, text=button_text)
        button.pack(side="left")
        # self.pack(side = 'left', expand = True, fill = 'both', padx = 20, pady = 20)
        self.pack()


window = tk.Tk()
window.geometry("800x600")
window.title("這是主視窗")

menu = Menu(window)
main = Main(window)

window.mainloop()

print("------------------------------------------------------------")  # 60個

print('有用到 pickle')
print('grid 範例')

import pickle
import os.path
from tkinter import *  # Import tkinter
import tkinter.messagebox


class Address:
    def __init__(self, name, street, city, state, zip):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip


class AddressBook:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("AddressBook")  # Set title

        self.nameVar = StringVar()
        self.streetVar = StringVar()
        self.cityVar = StringVar()
        self.stateVar = StringVar()
        self.zipVar = StringVar()

        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, text="Name").grid(row=1, column=1, sticky=W)
        Entry(frame1, textvariable=self.nameVar, width=40).grid(row=1, column=2)

        frame2 = Frame(window)
        frame2.pack()
        Label(frame2, text="Street").grid(row=1, column=1, sticky=W)
        Entry(frame2, textvariable=self.streetVar, width=40).grid(row=1, column=2)

        frame3 = Frame(window)
        frame3.pack()
        Label(frame3, text="City", width=5).grid(row=1, column=1, sticky=W)
        Entry(frame3, textvariable=self.cityVar).grid(row=1, column=2)
        Label(frame3, text="State").grid(row=1, column=3, sticky=W)
        Entry(frame3, textvariable=self.stateVar, width=5).grid(row=1, column=4)
        Label(frame3, text="ZIP").grid(row=1, column=5, sticky=W)
        Entry(frame3, textvariable=self.zipVar, width=5).grid(row=1, column=6)

        frame4 = Frame(window)
        frame4.pack()
        Button(frame4, text="Add", command=self.processAdd).grid(row=1, column=1)
        btFirst = Button(frame4, text="First", command=self.processFirst).grid(
            row=1, column=2
        )
        btNext = Button(frame4, text="Next", command=self.processNext).grid(
            row=1, column=3
        )
        btPrevious = Button(frame4, text="Previous", command=self.processPrevious).grid(
            row=1, column=4
        )
        btLast = Button(frame4, text="Last", command=self.processLast).grid(
            row=1, column=5
        )

        self.addressList = self.loadAddress()
        self.current = 0

        length = len(self.addressList)

        if length > 0:
            self.setAddress()
            print("aaaaaaaaaaaaa, len =", length)
            for i in range(length):
                print(i)
                print(self.addressList[i].name)
                print(self.addressList[i].street)
                print(self.addressList[i].city)
                print(self.addressList[i].state)
                print(self.addressList[i].zip)

        window.mainloop()  # Create an event loop

    def saveAddress(self):
        outfile = open("address.dat", "wb")
        pickle.dump(self.addressList, outfile)
        tkinter.messagebox.showinfo("Address saved", "A new address is saved")
        outfile.close()

    def loadAddress(self):
        if not os.path.isfile("address.dat"):
            return []  # Return an empty list

        print("使用 pickle 讀取檔案")

        try:
            infile = open("address.dat", "rb")
            addressList = pickle.load(infile)
        except EOFError:
            addressList = []

        infile.close()
        print(addressList)
        return addressList

    def processAdd(self):
        address = Address(
            self.nameVar.get(),
            self.streetVar.get(),
            self.cityVar.get(),
            self.stateVar.get(),
            self.zipVar.get(),
        )
        self.addressList.append(address)
        self.saveAddress()

    def processFirst(self):
        self.current = 0
        self.setAddress()

    def processNext(self):
        if self.current < len(self.addressList) - 1:
            self.current += 1
            self.setAddress()

    def processPrevious(self):
        pass  # Left as exercise

    def processLast(self):
        pass  # Left as exercise

    def setAddress(self):
        self.nameVar.set(self.addressList[self.current].name)
        self.streetVar.set(self.addressList[self.current].street)
        self.cityVar.set(self.addressList[self.current].city)
        self.stateVar.set(self.addressList[self.current].state)
        self.zipVar.set(self.addressList[self.current].zip)


AddressBook()  # Create GUI


print("------------------------------------------------------------")  # 60個

# GridManagerDemo

from tkinter import *  # Import tkinter


class GridManagerDemo:
    window = Tk()  # Create a window
    window.title("Grid Manager Demo")  # Set title

    message = Message(
        window, text="This Message widget occupies three rows and two columns"
    )
    message.grid(row=1, column=1, rowspan=3, columnspan=2)
    Label(window, text="First Name:").grid(row=1, column=3)
    Entry(window).grid(row=1, column=4, padx=5, pady=5)
    Label(window, text="Last Name:").grid(row=2, column=3)
    Entry(window).grid(row=2, column=4)
    Button(window, text="Get Name").grid(row=3, padx=5, pady=5, column=4, sticky=E)

    window.mainloop()  # Create an event loop


GridManagerDemo()  # Create GUI

print("------------------------------------------------------------")  # 60個

# PackManagerDemoWithSide

from tkinter import *  # Import tkinter


class PackManagerDemoWithSide:
    window = Tk()  # Create a window
    window.title("Pack Manager Demo 2")  # Set title

    Label(window, text="Blue", bg="blue").pack(side=LEFT)
    Label(window, text="Red", bg="red").pack(side=LEFT, fill=BOTH, expand=1)
    Label(window, text="Green", bg="green").pack(side=LEFT, fill=BOTH)

    window.mainloop()  # Create an event loop


PackManagerDemoWithSide()  # Create GUI

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("800x600")
window.title("這是主視窗")

frame1 = tk.Frame(window)
frame1.pack()

#Entry 之 Text 之 對齊
tk.Entry(frame1, width=5, justify=tk.RIGHT).pack(side=tk.LEFT)
tk.Entry(frame1, width=5, justify=tk.RIGHT).pack(side=tk.LEFT)
tk.Entry(frame1, width=5, justify=tk.RIGHT).pack(side=tk.LEFT)


print("Toolbox 測試")
tk.Button(window, text="OK").pack(side=tk.LEFT)
tk.Button(window, text="Cancel").pack(side=tk.LEFT)
tk.Label(window, text="Enter your name:").pack(side=tk.LEFT)
tk.Entry(window, text="Type Name").pack(side=tk.LEFT)
tk.Checkbutton(window, text="Bold").pack(side=tk.LEFT)
tk.Checkbutton(window, text="Italic").pack(side=tk.LEFT)
tk.Radiobutton(window, text="Red").pack(side=tk.LEFT)
tk.Radiobutton(window, text="Yellow").pack(side=tk.LEFT)







window.mainloop()


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


"""

label1 = tk.Label(window, fg = "red", textvariable = labeltext)

item1 = tk.Radiobutton(window, text="足球", value="足球", variable=choice, command=choose)
entryUrl = tk.Entry(window, textvariable=score)

cb = Combobox(window, textvariable=cbVar)
labelShow = Label(window, textvariable=labelVar)
slider = tk.Scale(window, from_=0, to=goal)
canvas = tk.Canvas(window, height=300, width=300, bg=colour)

取得entry的資料
guess = int(guessBox.get())

取得entry的資料
number = int(entry1.get())  #加了輸入欄位

取得entry的資料
name = nameEntry.get()

設定entry的資料
result.delete(0, tk.END)
result.insert(0, sentence)

取定text的資料
mesg = text1.get("1.0","end")

設定button的text
    button.config(text="按這裡" + str(count))


def click1():
    textvar.set("我已經被按過了！")

textvar = tk.StringVar()
textvar.set("按鈕")

tk.Button(window, textvariable=textvar, command=click1).pack()


text.pack(fill=tk.BOTH,expand=True,padx=3,pady=2)
text.pack(fill=tk.BOTH, expand=True)


tk之string的用法

radio_var = tk.StringVar()

print(radio_var.get()))

check_var = tk.IntVar(value = 10)
print(check_var.get()),
check_var.set(5))

button_string = tk.StringVar(value = 'A button with string var')

print("------------------------------------------------------------")  # 60個

place 參數
label.place(relx=0.1, rely=0.1, relheight=0.8)
label1.place(x=0, y=200, width=601, height=203)
label2.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.8)

pack 參數
label1.pack(anchor=tk.S,side=tk.RIGHT,padx=10,pady=10)

def get_entry1_data():
    cc = entry1.get()
    print(cc)

entry1_data = tk.StringVar()
entry1 = tk.Entry(frame2, width=40, textvariable=entry1_data)
entry1.pack(side=tk.LEFT)

tk.Button(frame2, text="取得entry1資料", command=get_entry1_data).pack()

def getTextData3():
    mesg = text3.get("1.0", "end")
    print("取得Text的資料 :", mesg)

tk.Button(window, text="取得Text的資料", command=getTextData3).pack()

def add_text():
    text = "測試字串......."
    # 輸出到界面
    text4.delete(1.0, tk.END)
    text4.insert(1.0, text)

button3 = tk.Button(window, text="蓋過字串", command=add_text)
button3.pack()


比較
button1.pack(padx=5, pady=5) #預設button大小
#button1.pack(padx=5, pady=5, fill="x") # button大小 填滿 x 軸



sticky 之解釋
curRad.pack(column=col, row=5, sticky=tk.W)  # 參數sticky對應的值參考復選框的解釋


print('寫讀 Entry 上的資料')

# Label / Entry / Text / 
# 一個按鈕 設定一個變數給控件 並把這個控件的變數讀出來

tk.StringVar() 字串，
tk.IntVar() 整數，預設值為 0
tk.DoubleVar() 浮點數，預設值為 0.0
tk.Boolean()  # 布林值變數，True是1， False是0 fail

menu1.add_command(label="離開", command=window.destroy)
menu1.add_command(label="結束", command=window.quit)
buttonQuit = tk.Button(window, text="結束", command=window.destroy)

buttonQuit.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)

# 使用place + anchor
button1 = tk.Button(window, text="按鈕 視窗正中央", width=20)
button1.place(relx=0.5, rely=0.5, anchor="center")

button2 = tk.Button(window, text="按鈕 視窗左上", width=20)
button2.place(relx=0.1, rely=0.1, anchor="nw")

button3 = tk.Button(window, text="按鈕 視窗左下", width=20)
button3.place(relx=0.1, rely=0.8, anchor="w")  # ???


# 使用side

pack()#沒寫, 中間靠上 視窗最上邊
pack(side="left")#視窗最左邊
pack(side="right")#視窗最右邊
pack(side="bottom")#視窗最下邊

pack 參數

lb1.pack(side=tk.LEFT,padx=5,pady=10)
lb2.pack(anchor=tk.N,side=tk.LEFT,padx=5,pady=10)
button1.pack(side=tk.LEFT,padx=10,pady=5)
cb.pack(side=tk.LEFT)


print("------------------------------------------------------------")  # 60個

Exit = tk.Button(window, text='Exit', fg='Black', bg='Blue', command=exit)

boolean
var = tk.BooleanVar()
cb = tk.Checkbutton(window,text="大到小排序",variable=var)

print("------------------------------------------------------------")  # 60個
print("tk的font")
print("------------------------------------------------------------")  # 60個

import tkinter.font as tkfont
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)

用法 加 font = default_font
radbut = tk.Radiobutton(window, text=item, variable=area, value=value, command=radbut_click, font=default_font)
lab_result = tk.Label(window, font=default_font, fg='black')
lab_result = tk.Label(window, font=default_font, fg='black', width=18)

combox = ttk.Combobox(window, value=AREA_OPTIONS, textvariable=area, font=default_font)


ft1 =('新細明體', 14)
ft2 = ('標楷體', 18)
chk1 = tk.Checkbutton(window, text = item1, font = ft1, variable = var1, onvalue = item1, offvalue = '')
chk2 = tk.Checkbutton(window, text = item2, font = ft1, variable = var2, onvalue = item2, offvalue = '')
chk3 = tk.Checkbutton(window, text = item3, font = ft1, variable = var3, onvalue = item3, offvalue = '')

ft1 =('新細明體', 14)
ft2 = ('標楷體', 18)

entry = tk.Entry(window, bg="#ffff00", font = "新細明體 16 bold" ,borderwidth = 3)

# menu button
menu_button = ttk.Menubutton(window, text = 'Menu Button')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff = False)
button_sub_menu.add_command(label = 'entry 1', command = lambda: print('test 1'))
button_sub_menu.add_checkbutton(label = 'check 1')
# menu_button.configure(menu = button_sub_menu)
menu_button['menu']= button_sub_menu

print("------------------------------------------------------------")  # 60個

tk.Label(text = '測試測試測試').pack(anchor=tk.W)

# pack
# label1.pack(side = 'left', expand = True, fill = 'y')
# label2.pack(side = 'left', expand = True, fill = 'both')

# label1.grid(row = 0, column = 1, sticky = 'nsew')
# label2.grid(row = 1, column = 1, columnspan = 2, sticky = 'nsew')

# grid 設定
# window.columnconfigure(0, weight = 1)
# window.columnconfigure(1, weight = 1)
# window.columnconfigure(2, weight = 2)
# window.rowconfigure(0, weight = 1)
# window.rowconfigure(1, weight = 1)

"""


