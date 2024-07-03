import sys

import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image

W = 200
H = 200
w = 12
h = 2
'''
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
        text.insert(tk.END, "AAAA\n")
        text.insert(tk.END, "BBBB\n")
        text.insert(tk.END, "CCCC\n")

        window.mainloop()

    def processCheckbutton(self):
        print("check button is " + ("checked " if self.v1.get() == 1 else "unchecked"))

    def processRadiobutton(self):
        print(("Red" if self.v2.get() == 1 else "Yellow") + " is selected ")

    def processButton(self):
        print("Your name is " + self.name.get())


WidgetsDemo()

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
'''


print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("new all 7")

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
        window, text=colors[col], variable=radVar, value=col, command=radCall
    )
    curRad.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import scrolledtext  # 導入滾動文本框的模塊

window = tk.Tk()
window.geometry("600x800")
window.title("new all 7")

# 滾動文本框
scrolW = 30  # 設置文本框的長度
scrolH = 3  # 設置文本框的高度
# wrap=tk.WORD這個值表示在行的末尾如果有一個單詞跨行，會將該單詞放到下一行顯示
scr = scrolledtext.ScrolledText(window, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)


window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("new all 7")



from tkinter.messagebox import showinfo

button1 = tk.Button(window, command=lambda *args: showinfo(message="aaaaaaa"), text="獲取")
button1.pack()



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



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
