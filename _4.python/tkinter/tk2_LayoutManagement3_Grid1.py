"""
Grid 測試
"""

import sys
import tkinter as tk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("800x800")
window.title("Grid 測試 1")

w = 5
h = 2

for j in range(0, 5):
    for i in range(0, 16):
        label_n = tk.Label(window, text=str(i) + "," + str(j))
        label_n.grid(row=j, column=i)

for j in range(0 + 5, 5 + 5):
    for i in range(0, 16):
        text_n = tk.Text(window, width=w, height=h)
        text_n.grid(row=j, column=i)

for j in range(0 + 5 + 5, 5 + 5 + 5):
    for i in range(0, 16):
        button_n = tk.Button(window, width=w, height=h, text=str(i) + "," + str(j))
        button_n.grid(row=j, column=i)


text1 = tk.Text(window, width=w, height=h)  # 原始數據錄入框
text1.grid(row=1, column=1)
# text1.grid(row = 1, column = 1, rowspan = 1, columnspan = 3)

button0 = tk.Button(window, text="55", width=w, height=h)
button0.grid(row=2, column=2)
# button0.grid(row = 2, column = 2, rowspan = 1, columnspan = 3)

"""
若不指名 rowspan / columnspan, 則所佔為1格
會依據控件的大小 將所在格撐大成設定的格數
"""

"""
for j in range(4, 14, 3):
    for i in range(4, 14, 3):
        entry = tk.Entry(window, width = 10) #寬度為5個字
        if(i == 4):
            entry.grid(row = j, column = i) #預設, 占用1欄
        elif(i == 7):
            entry.grid(row = j, column = i, columnspan = 1) #占用1欄
        elif(i == 10):
            entry.grid(row = j, column = i, columnspan = 2) #占用2欄
        else:
            entry.grid(row = j, column = i, columnspan = 3) #占用3欄
"""
window.mainloop()

print("------------------------------------------------------------")  # 60個

"""
Grid 測試 Button + Canvas
"""

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 3")

# 新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame1 = tk.Frame(window, bg="yellow")
frame1.pack()

message = tk.Message(frame1, text="這個訊息所佔的位置為3R2C")
message.grid(row=1, column=1, rowspan=3, columnspan=2)
tk.Label(frame1, text="姓 : ").grid(row=1, column=3)
tk.Entry(frame1).grid(row=1, column=4, padx=5, pady=5)
tk.Label(frame1, text="名 : ").grid(row=2, column=3)
tk.Entry(frame1).grid(row=2, column=4)
tk.Button(frame1, text="取得姓名").grid(row=3, padx=5, pady=5, column=4, sticky=tk.E)


# 新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame2 = tk.Frame(window, bg="pink")
frame2.pack()


# 新建一個Frame, row, column重新計算, 控件要依附新的Frame
frame3 = tk.Frame(window, bg="cyan")
frame3.pack()

button00 = tk.Button(frame3, text="第0排第0個", width=20)
button00.grid(row=0, column=0, padx=5, pady=5)
button01 = tk.Button(frame3, text="第0排第1個", width=20)
button01.grid(row=0, column=1, padx=5, pady=5)
button02 = tk.Button(frame3, text="第0排第2個", width=20)
button02.grid(row=0, column=2, padx=5, pady=5)
button10 = tk.Button(frame3, text="第1排第0個", width=20)
button10.grid(row=1, column=0, padx=5, pady=5)
button11 = tk.Button(frame3, text="第1排第1個", width=20)
button11.grid(row=1, column=1, padx=5, pady=5)
button12 = tk.Button(frame3, text="第1排第2個", width=20)
button12.grid(row=1, column=2, padx=5, pady=5)

"""
frame3.columnconfigure(0, weight = 1)
frame3.columnconfigure(1, weight = 2)
#column 0 為基礎寬度，column 1 為column0的兩倍寬
"""
"""
frame3.columnconfigure((0, 2, 3), weight = 1)
frame3.columnconfigure(1, weight = 2)
frame3主視窗的，column 0 , 2, 3為基礎寬度，column 1 為其他column的兩倍寬
"""

button20 = tk.Button(frame3, text="第2排第0個")
button20.grid(row=2, column=0, ipadx=10, ipady=10)
button21 = tk.Button(frame3, text="第2排第1個")
button21.grid(row=2, column=1, ipadx=10, ipady=10)
button22 = tk.Button(frame3, text="第2排第2個")
button22.grid(row=2, column=2, ipadx=10, ipady=10)

"""
參數Sticky填充元件大小
sticky 可以輸入N ,S, E, W或是 混搭例如:EW，NS，NSEW，代表靠N(北方) 、S(南方)、E(東方)、W(西方)，NS(北南延伸)，EW(東西延伸)，NSEW(全方位延伸)
"""

button30 = tk.Button(frame3, text="第3排第0個")
button30.grid(row=3, column=0, ipadx=10, ipady=10, sticky="EW")
button31 = tk.Button(frame3, text="第3排第1個")
button31.grid(row=3, column=1, ipadx=10, ipady=10, sticky="EW")
button32 = tk.Button(frame3, text="第3排第2個")
button32.grid(row=3, column=2, ipadx=10, ipady=10, sticky="EW")


window.mainloop()


print("------------------------------------------------------------")  # 60個


"""
Grid 測試 grid
"""


def get_data():
    print("取得資料")
    data1 = entry_1_0.get()
    data2 = entry_1_1.get()
    data3 = entry_1_2.get()
    data4 = int(spinbox_3_0.get())
    data5 = entry_3_1.get()
    data6 = float(spinbox_3_2.get())
    print(data1, data2, data3, data4, data5, data6)


def set_data():
    print("設定資料")


def clear_data():
    print("清除資料")
    entry_1_0.delete(0, tk.END)
    entry_1_1.delete(0, tk.END)
    entry_1_2.delete(0, tk.END)
    spinbox_3_0.delete(0, tk.END)
    spinbox_3_0.insert(0, "1")
    entry_3_1.delete(0, tk.END)
    spinbox_3_2.delete(0, tk.END)
    spinbox_3_2.insert(0, "0.0")


window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 4")

frame = tk.Frame(window, bg="magenta")
frame.pack(padx=20, pady=10)

print("第 0 row, Label")
label_0_0 = tk.Label(frame, text="Label 0 0")
label_0_0.grid(row=0, column=0)
label_0_1 = tk.Label(frame, text="Label 0 1")
label_0_1.grid(row=0, column=1)
label_0_2 = tk.Label(frame, text="Label 0 2")
label_0_2.grid(row=0, column=2)

print("第 1 row, Entry")
entry_1_0 = tk.Entry(frame)
entry_1_0.grid(row=1, column=0)
entry_1_1 = tk.Entry(frame)
entry_1_1.grid(row=1, column=1)
entry_1_2 = tk.Entry(frame)
entry_1_2.grid(row=1, column=2)

print("第 2 row, Label")
label_2_0 = tk.Label(frame, text="Label 2 0")
label_2_0.grid(row=2, column=0)
label_2_1 = tk.Label(frame, text="Label 2 1")
label_2_1.grid(row=2, column=1)
label_2_2 = tk.Label(frame, text="Label 2 2")
label_2_2.grid(row=2, column=2)

print("第 3 row, Spinbox Entry Spinbox")
spinbox_3_0 = tk.Spinbox(frame, from_=1, to=100)
spinbox_3_0.grid(row=3, column=0)

entry_3_1 = tk.Entry(frame)
entry_3_1.grid(row=3, column=1)

spinbox_3_2 = tk.Spinbox(frame, from_=0.0, to=500, increment=0.5)
spinbox_3_2.grid(row=3, column=2)

print("第 4 row, Button")
button_4_0 = tk.Button(frame, text="Button 4 0")
button_4_0.grid(row=4, column=0, pady=5)

button_4_1 = tk.Button(frame, text="Button 4 1")
button_4_1.grid(row=4, column=1, pady=5)

button_4_2 = tk.Button(frame, text="Button 4 2")
button_4_2.grid(row=4, column=2, pady=5)

print("第 5 row, Button")
button_5_0 = tk.Button(frame, text="取得資料", command=get_data)
button_5_0.grid(row=5, column=0, pady=5)

button_5_1 = tk.Button(frame, text="設定資料", command=set_data)
button_5_1.grid(row=5, column=1, pady=5)

button_5_2 = tk.Button(frame, text="清除資料", command=clear_data)
button_5_2.grid(row=5, column=2, pady=5)

button_row6 = tk.Button(frame, text="橫跨的大Button")
button_row6.grid(row=6, column=0, columnspan=3, sticky="news", padx=20, pady=5)
button_row7 = tk.Button(frame, text="橫跨的大Button")
button_row7.grid(row=7, column=0, columnspan=3, sticky="news", padx=20, pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 8 Label")

lab1 = tk.Label(window, text="Label位置00", bg="lightyellow", width=25)  # 標籤背景是淺黃色  # 標籤寬度是15
lab2 = tk.Label(window, text="Label位置01", bg="lightgreen", width=25)  # 標籤背景是淺綠色  # 標籤寬度是15
lab3 = tk.Label(window, text="Label位置02", bg="lightblue", width=25)  # 標籤背景是淺綠色  # 標籤寬度是15
lab4 = tk.Label(window, text="Label位置10", bg="lightgreen", width=25)  # 標籤背景是淺黃色  # 標籤寬度是15
lab5 = tk.Label(window, text="Label位置11", bg="lightblue", width=25)  # 標籤背景是淺綠色  # 標籤寬度是15
lab6 = tk.Label(window, text="Label位置12", bg="lightyellow", width=25)  # 標籤背景是淺綠色  # 標籤寬度是15
lab7 = tk.Label(window, text="Label位置20", bg="lightblue", width=25)  # 標籤背景是淺黃色  # 標籤寬度是15
lab8 = tk.Label(window, text="Label位置21", bg="lightyellow", width=25)  # 標籤背景是淺綠色  # 標籤寬度是15
lab9 = tk.Label(window, text="Label位置22", bg="lightgreen", width=25)  # 標籤背景是淺綠色  # 標籤寬度是15

lab1.grid(row=0, column=0)  # 格狀包裝
lab2.grid(row=0, column=1)  # 格狀包裝
lab3.grid(row=0, column=2)  # 格狀包裝
lab4.grid(row=1, column=0)  # 格狀包裝
lab5.grid(row=1, column=1)  # 格狀包裝
lab6.grid(row=1, column=2)  # 格狀包裝
lab7.grid(row=2, column=0)  # 格狀包裝
lab8.grid(row=2, column=1)  # 格狀包裝
lab9.grid(row=2, column=2)  # 格狀包裝

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 9")

lab1 = tk.Label(window, text="Label位置00", relief="raised")
lab2 = tk.Label(window, text="Label位置01", relief="raised")
lab3 = tk.Label(window, text="Label位置02", relief="raised")
lab4 = tk.Label(window, text="Label位置03", relief="raised")
lab5 = tk.Label(window, text="Label位置10", relief="raised")
lab6 = tk.Label(window, text="Label位置11", relief="raised")
lab7 = tk.Label(window, text="Label位置12", relief="raised")
lab8 = tk.Label(window, text="Label位置13", relief="raised")
lab1.grid(row=0, column=0)
lab2.grid(row=0, column=1)
lab3.grid(row=0, column=2)
lab4.grid(row=0, column=3)
lab5.grid(row=1, column=0)
lab6.grid(row=1, column=1)
lab7.grid(row=1, column=2)
lab8.grid(row=1, column=3)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 10")

lab1 = tk.Label(window, text="Label位置00", relief="raised")
lab2 = tk.Label(window, text="Label位置01", relief="raised")
lab4 = tk.Label(window, text="Label位置03", relief="raised")

lab5 = tk.Label(window, text="Label位置10", relief="raised")
lab6 = tk.Label(window, text="Label位置11", relief="raised")
lab7 = tk.Label(window, text="Label位置12", relief="raised")
lab8 = tk.Label(window, text="Label位置13", relief="raised")
lab1.grid(row=0, column=0)
lab2.grid(row=0, column=1, columnspan=2)
lab4.grid(row=0, column=3)
lab5.grid(row=1, column=0)
lab6.grid(row=1, column=1)
lab7.grid(row=1, column=2)
lab8.grid(row=1, column=3)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 11")

lab1 = tk.Label(window, text="Label位置00", relief="raised")
lab2 = tk.Label(window, text="Label位置01", relief="raised")
lab3 = tk.Label(window, text="Label位置02", relief="raised")
lab4 = tk.Label(window, text="Label位置03", relief="raised")
lab5 = tk.Label(window, text="Label位置10", relief="raised")
lab7 = tk.Label(window, text="Label位置12", relief="raised")
lab8 = tk.Label(window, text="Label位置13", relief="raised")
lab1.grid(row=0, column=0)
lab2.grid(row=0, column=1, rowspan=2)
lab3.grid(row=0, column=2)
lab4.grid(row=0, column=3)
lab5.grid(row=1, column=0)
lab7.grid(row=1, column=2)
lab8.grid(row=1, column=3)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 30")

label1 = tk.Label(window, text="標籤1", relief="raised")
label2 = tk.Label(window, text="標籤2", relief="raised")
label4 = tk.Label(window, text="標籤4", relief="raised")
label5 = tk.Label(window, text="標籤5", relief="raised")
label8 = tk.Label(window, text="標籤8", relief="raised")
label1.grid(row=0, column=0)
label2.grid(row=0, column=1, rowspan=2, columnspan=2)
label4.grid(row=0, column=3)
label5.grid(row=1, column=0)
label8.grid(row=1, column=3)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 31")

label1 = tk.Label(window, text="標籤1", relief="raised")
label2 = tk.Label(window, text="標籤2", relief="raised")
label3 = tk.Label(window, text="標籤3", relief="raised")
label4 = tk.Label(window, text="標籤4", relief="raised")
label5 = tk.Label(window, text="標籤5", relief="raised")
label6 = tk.Label(window, text="標籤6", relief="raised")
label7 = tk.Label(window, text="標籤7", relief="raised")
label8 = tk.Label(window, text="標籤8", relief="raised")
label1.grid(row=0, column=0, padx=5, pady=5)
label2.grid(row=0, column=1, padx=5, pady=5)
label3.grid(row=0, column=2, padx=5, pady=5)
label4.grid(row=0, column=3, padx=5, pady=5)
label5.grid(row=1, column=0, padx=5)
label6.grid(row=1, column=1, padx=5)
label7.grid(row=1, column=2, padx=5)
label8.grid(row=1, column=3, padx=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

"""
pLabel1= tk.Label(window, text="難度計算過程", fg="black", bg="silver", font=("新細明體",12),padx=20,pady=10 )


text1 = tk.StringVar(value='GUI1')
ent1 = tk.Entry(window, textvariable=text1, width=15, justify=tk.CENTER)
ent1.grid(row=0, column=0, padx=5, pady=5)
text2 = tk.StringVar(value='GUI2')
ent2 = tk.Entry(window, textvariable=text2, width=15, justify=tk.CENTER)
ent2.grid(row=0, column=2, padx=5, pady=5, sticky=tk.N)
text3 = tk.StringVar(value='GUI3')
ent3 = tk.Entry(window, textvariable=text3, width=15, justify=tk.CENTER)
ent3.grid(row=1, column=1, padx=5, pady=5)
"""

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 15")


# Frame測試
tk.Label(text="Frame測試").pack()
frame1 = tk.Frame(window)
frame1.pack()

label1 = tk.Label(frame1, text="標籤一：")
entry1 = tk.Entry(frame1)
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)

frame2 = tk.Frame(window)
frame2.pack()

button1 = tk.Button(frame2, text="確定")
button2 = tk.Button(frame2, text="取消")
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)

separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線


separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN).pack(
    fill=tk.X, padx=5, pady=5
)  # 分隔線

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 16")

label1 = tk.Label(window, text="Label 1", background="red")
label2 = tk.Label(window, text="Label 2", background="green", width=10)
label3 = tk.Label(window, text="Label 3", background="blue", width=10)

# label1.pack()
# label2.pack()

# grid
window.columnconfigure((0, 2), weight=1, uniform="a")  # column 為  0 1 2
window.rowconfigure((0, 2), weight=1, uniform="a")  # row 為  0 1 2

"""
label1.grid(row = 0, column = 0)
label2.grid(row = 1, column = 0, sticky = 'nsew')
label3.grid(row = 0, column = 1)
"""

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)

window.mainloop()

print("------------------------------------------------------------")  # 60個

"""

label = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label.pack()                        # 包裝與定位元件


lab1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = tk.Label(window,text="歡迎來到日本",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = tk.Label(window,text="歡迎來到加拿大",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=1,column=2)           # 格狀包裝
lab3.grid(row=2,column=1)           # 格狀包裝


button1 = tk.Button(window, text='push1')
button2 = tk.Button(window, text='push2')
button3 = tk.Button(window, text='push3')

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=1, column=1)


"""

print("------------------------------------------------------------")  # 60個

# account - password

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 20")

lab1 = tk.Label(window, text="Account ").grid(row=0)
lab2 = tk.Label(window, text="Password").grid(row=1)

e1 = tk.Entry(window)  # 文字方塊1
e2 = tk.Entry(window, show="*")  # 文字方塊2
e1.grid(row=0, column=1)  # 定位文字方塊1
e2.grid(row=1, column=1)  # 定位文字方塊2

window.mainloop()

print("------------------------------------------------------------")  # 60個


def printInfo():  # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(), e2.get()))


window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 21")

lab1 = tk.Label(window, text="Account ").grid(row=0)
lab2 = tk.Label(window, text="Password").grid(row=1)

e1 = tk.Entry(window)  # 文字方塊1
e2 = tk.Entry(window, show="*")  # 文字方塊2
e1.grid(row=0, column=1)  # 定位文字方塊1
e2.grid(row=1, column=1)  # 定位文字方塊2

btn1 = tk.Button(window, text="Print", command=printInfo)
btn1.grid(row=2, column=0)
btn2 = tk.Button(window, text="Quit", command=window.quit)
btn2.grid(row=2, column=1)

window.mainloop()

print("------------------------------------------------------------")  # 60個


def printInfo():  # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(), e2.get()))


window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 22")

lab1 = tk.Label(window, text="Account ").grid(row=0)
lab2 = tk.Label(window, text="Password").grid(row=1)

e1 = tk.Entry(window)  # 文字方塊1
e2 = tk.Entry(window, show="*")  # 文字方塊2
e1.grid(row=0, column=1)  # 定位文字方塊1
e2.grid(row=1, column=1)  # 定位文字方塊2

btn1 = tk.Button(window, text="Print", command=printInfo)
# sticky=tk.W可以設定物件與上面的Label切齊, pady設定上下間距是10
btn1.grid(row=2, column=0, sticky=tk.W, pady=10)
btn2 = tk.Button(window, text="Quit", command=window.quit)
# sticky=tk.W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2, column=1, sticky=tk.W, pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個


def printInfo():  # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(), e2.get()))


window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 23")

lab1 = tk.Label(window, text="Account ").grid(row=0)
lab2 = tk.Label(window, text="Password").grid(row=1)

e1 = tk.Entry(window)  # 文字方塊1
e2 = tk.Entry(window, show="*")  # 文字方塊2
e1.insert(1, "Kevin")  # 預設文字方塊1內容
e2.insert(1, "pwd")  # 預設文字方塊2內容
e1.grid(row=0, column=1)  # 定位文字方塊1
e2.grid(row=1, column=1)  # 定位文字方塊2

btn1 = tk.Button(window, text="Print", command=printInfo)
# sticky=tk.W可以設定物件與上面的Label切齊, pady設定上下間距是10
btn1.grid(row=2, column=0, sticky=tk.W, pady=10)
btn2 = tk.Button(window, text="Quit", command=window.quit)
# sticky=tk.W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2, column=1, sticky=tk.W, pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個


def printInfo():  # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(), e2.get()))
    e1.delete(0, tk.END)  # 刪除文字方塊1
    e2.delete(0, tk.END)  # 刪除文字方塊2


window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 24")

lab1 = tk.Label(window, text="Account ").grid(row=0)
lab2 = tk.Label(window, text="Password").grid(row=1)

e1 = tk.Entry(window)  # 文字方塊1
e2 = tk.Entry(window, show="*")  # 文字方塊2
e1.insert(1, "Kevin")  # 預設文字方塊1內容
e2.insert(1, "pwd")  # 預設文字方塊2內容
e1.grid(row=0, column=1)  # 定位文字方塊1
e2.grid(row=1, column=1)  # 定位文字方塊2

btn1 = tk.Button(window, text="Print", command=printInfo)
# sticky=tk.W可以設定物件與上面的Label切齊, pady設定上下間距是10
btn1.grid(row=2, column=0, sticky=tk.W, pady=10)
btn2 = tk.Button(window, text="Quit", command=window.quit)
# sticky=tk.W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2, column=1, sticky=tk.W, pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 25")
window.title("GUI介面- Checkbutton 核取方塊")


def check():  # 回應核取方塊變數狀態
    print("選取的炸物有:", var1.get(), var2.get(), var3.get())


ft1 = ("新細明體", 14)
ft2 = ("標楷體", 18)
lb1 = tk.Label(window, text="請勾選要買的品項：", font=ft1)
lb1.grid(row=0, column=0)
item1 = "炸雞排"
var1 = tk.StringVar()
chk = tk.Checkbutton(
    window, text=item1, font=ft1, variable=var1, onvalue=item1, offvalue=""
)
chk.grid(row=1, column=0)
item2 = "高麗菜"
var2 = tk.StringVar()
chk2 = tk.Checkbutton(
    window, text=item2, font=ft1, variable=var2, onvalue=item2, offvalue=""
)
chk2.grid(row=2, column=0)
item3 = "炸花枝"
var3 = tk.StringVar()
chk3 = tk.Checkbutton(
    window, text=item3, font=ft1, variable=var3, onvalue=item3, offvalue=""
)
chk3.grid(row=3, column=0)

btnQuit = tk.Button(window, text="離開", font=ft2, command=window.destroy)
btnQuit.grid(row=2, column=1, pady=4)
btnShow = tk.Button(window, text="購買明細", font=ft2, command=check)
btnShow.grid(row=2, column=2, pady=4)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 26")

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

label1 = tk.Label(window, text="北", font=("標楷體", 40))
label2 = tk.Label(window, text="東", font=("標楷體", 40), bg="yellow")
label3 = tk.Label(window, text="西", font=("標楷體", 40), bg="lightgreen")
label4 = tk.Label(window, text="中", font=("標楷體", 40), bg="pink")
label5 = tk.Label(window, text="南", font=("標楷體", 40), bg="lightblue")
label1.grid(row=0, column=0, columnspan=2, sticky="nswe")
label2.grid(row=0, column=2, rowspan=2, sticky="nswe")
label3.grid(row=1, column=0, rowspan=2, sticky="nswe")
label4.grid(row=1, column=1, sticky="nswe")
label5.grid(row=2, column=1, columnspan=2, sticky="nswe")

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 32")

w = 20
h = 5
button1 = tk.Button(window, width=w, height=h, text="歡迎來到美國")
button2 = tk.Button(window, width=w, height=h, bg="yellow")
button3 = tk.Button(window, width=w, height=h, text="歡迎來到美國")
button4 = tk.Button(window, width=w, height=h, bg="aqua")
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=1, column=0)
button4.grid(row=1, column=1)

button1 = tk.Button(window, width=w, height=h, text="歡迎來到美國")
button2 = tk.Button(window, width=w, height=h, bg="yellow")
button3 = tk.Button(window, width=w, height=h, text="歡迎來到美國")
button4 = tk.Button(window, width=w, height=h, bg="aqua")
button1.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W + tk.E)
button2.grid(row=2, column=1, padx=5, pady=5)
button3.grid(row=3, column=0, padx=5)
button4.grid(row=3, column=1, padx=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 36")

Colors = ["red", "orange", "yellow", "green", "blue", "purple"]

r = 0  # row編號
for color in Colors:
    tk.Label(window, text=color, relief="groove", width=20).grid(row=r, column=0)
    tk.Label(window, bg=color, relief="ridge", width=20).grid(row=r, column=1)
    r += 1

window.mainloop()

print("------------------------------------------------------------")  # 60個

#設定列欄權重

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 37")

window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

label1 = tk.Label(window, text="Label 1", bg="pink")
label1.grid(row=0, column=0, padx=5, pady=5)

label2 = tk.Label(window, text="Label 2", bg="lightblue")
label2.grid(row=0, column=1, padx=5, pady=5)

label3 = tk.Label(window, text="Label 3", bg="yellow")
label3.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 38")

window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

label1 = tk.Label(window, text="Label 1", bg="pink")
label1.grid(row=0, column=0, padx=5, pady=5, stick=tk.W)

label2 = tk.Label(window, text="Label 2", bg="lightblue")
label2.grid(row=0, column=1, padx=5, pady=5)

label3 = tk.Label(window, bg="yellow")
label3.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.W + tk.E)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 39")
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

label1 = tk.Label(window, text="Label 1", bg="pink")
label1.grid(row=0, column=0, padx=5, pady=5, stick=tk.W + tk.E)

label2 = tk.Label(window, text="Label 2", bg="lightblue")
label2.grid(row=0, column=1, padx=5, pady=5)

label3 = tk.Label(window, text="Label 3", bg="yellow")
label3.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.W + tk.E)

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import ttk

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 47")

style = ttk.Style()  # 改用Style
style.theme_use("alt")  # 改用alt支援Style

fm1 = tk.Frame(window, width=150, height=80, relief="flat")
fm1.grid(row=0, column=0, padx=5, pady=5)

fm2 = tk.Frame(window, width=150, height=80, relief="groove")
fm2.grid(row=0, column=1, padx=5, pady=5)

fm3 = tk.Frame(window, width=150, height=80, relief="raised")
fm3.grid(row=0, column=2, padx=5, pady=5)

fm4 = tk.Frame(window, width=150, height=80, relief="ridge")
fm4.grid(row=1, column=0, padx=5, pady=5)

fm5 = tk.Frame(window, width=150, height=80, relief="solid")
fm5.grid(row=1, column=1, padx=5, pady=5)

fm6 = tk.Frame(window, width=150, height=80, relief="sunken")
fm6.grid(row=1, column=2, padx=5, pady=5)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title("Grid 測試 2")

# create all of the main containers
top_frame = tk.Frame(window, bg="cyan", width=450, height=50, pady=3)
center = tk.Frame(window, bg="gray2", width=50, height=40, padx=3, pady=3)

# layout all of the main containers
window.grid_rowconfigure(1, weight=2)
window.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")

# create the widgets for the top frame
model_label = tk.Label(top_frame, text="Model Dimensions")
width_label = tk.Label(top_frame, text="Width:")
length_label = tk.Label(top_frame, text="Length:")
entry_W = tk.Entry(top_frame, background="pink")
entry_L = tk.Entry(top_frame, background="orange")

# layout the widgets in the top frame
model_label.grid(row=0, columnspan=3)
width_label.grid(row=1, column=0)
length_label.grid(row=1, column=2)
entry_W.grid(row=1, column=1)
entry_L.grid(row=1, column=3)

# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = tk.Frame(center, bg="blue", width=100, height=190)
ctr_mid = tk.Frame(center, bg="yellow", width=250, height=190, padx=3, pady=3)
ctr_right = tk.Frame(center, bg="green", width=100, height=190, padx=3, pady=3)

ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=2, sticky="ns")

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

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

