import sys

import tkinter as tk

from tkinter import ttk
from PIL import ImageTk, Image

import random

print("------------------------------------------------------------")  # 60個
'''
window = tk.Tk()
window.geometry("600x800")
window.title('tkinter的變數類別')

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

#建立變數

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
    #Variable
    cc = variable_string.get()
    print('取得 variable_string 的資料 :', cc)
    cc = variable_int.get()
    print('取得 variable_int 的資料 :', cc)
    cc = variable_double.get()
    print('取得 variable_double 的資料 :', cc)
    cc = variable_boolean.get()
    print('取得 variable_boolean 的資料 :', cc)

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

    #Label
    #Label文字之讀取 TBD
    #cc = label11.get()
        
    label11.configure(text = "設定Label文字為 :" + string_mesg)
    label22.config(text = "設定Label文字為 :" + string_mesg)
    label33.config(text='已按下按鈕')
    label44.config(text='已按下按鈕')

    #label11
   
    value1=entry1.get()
    print('取得 Entry 1 資料 :', value1)
    value2=entry2.get()
    print('取得 Entry 2 資料 :', value2)
    value3=entry3.get()
    print('取得 Entry 3 資料 :', value3)
    value4=entry4.get()
    print('取得 Entry 4 資料 :', value4)

frame1 = tk.Frame(window, bg = '', width = W, height = H)
frame1.pack()

tk.Label(frame1, text = '種類', width=w).grid(row = 0, column = 0, padx = 5, pady = 5)
tk.Label(frame1, text = '字串', width=w).grid(row = 0, column = 1, padx = 5, pady = 5)
tk.Label(frame1, text = '整數', width=w).grid(row = 0, column = 2, padx = 5, pady = 5)
tk.Label(frame1, text = '浮點', width=w).grid(row = 0, column = 3, padx = 5, pady = 5)
tk.Label(frame1, text = '布林', width=w).grid(row = 0, column = 4, padx = 5, pady = 5)

tk.Label(frame1, text = 'Label', width=w).grid(row = 1, column = 0, padx = 5, pady = 5)
label1 = tk.Label(frame1, textvariable=variable_string)
label1.grid(row = 1, column = 1, padx = 5, pady = 5)
label2 = tk.Label(frame1, textvariable=variable_int)
label2.grid(row = 1, column = 2, padx = 5, pady = 5)
label3 = tk.Label(frame1, textvariable=variable_double)
label3.grid(row = 1, column = 3, padx = 5, pady = 5)
label4 = tk.Label(frame1, textvariable=variable_boolean)
label4.grid(row = 1, column = 4, padx = 5, pady = 5)

tk.Label(frame1, text = 'Button', width = w, height = h).grid(row = 2, column = 0, padx = 5, pady = 5)
button1 = tk.Button(frame1, textvariable=variable_string, width = w, height = h)
button1.grid(row = 2, column = 1, padx = 5, pady = 5)
button2 = tk.Button(frame1, textvariable=variable_int, width = w, height = h)
button2.grid(row = 2, column = 2, padx = 5, pady = 5)
button3 = tk.Button(frame1, textvariable=variable_double, width = w, height = h)
button3.grid(row = 2, column = 3, padx = 5, pady = 5)
button4 = tk.Button(frame1, textvariable=variable_boolean, width = w, height = h)
button4.grid(row = 2, column = 4, padx = 5, pady = 5)

tk.Label(frame1, text = 'Entry', width = w, height = h).grid(row = 3, column = 0, padx = 5, pady = 5)
entry1 = tk.Entry(frame1, textvariable=variable_string, width = w)
entry1.grid(row = 3, column = 1, padx = 5, pady = 5)
entry2 = tk.Entry(frame1, textvariable=variable_int, width = w)
entry2.grid(row = 3, column = 2, padx = 5, pady = 5)
entry3 = tk.Entry(frame1, textvariable=variable_double, width = w)
entry3.grid(row = 3, column = 3, padx = 5, pady = 5)
entry4 = tk.Entry(frame1, textvariable=variable_boolean, width = w)
entry4.grid(row = 3, column = 4, padx = 5, pady = 5)

button5 = tk.Button(frame1, text = "讀寫 控件 上的資料", width = w*2, height = h, command = read_write_tk_variables)
button5.grid(row = 4, column = 1, columnspan = 3, padx = 5, pady = 5)


label11 = tk.Label(frame1, text = '一般Label文字之讀寫',width=30)
label11.grid(row = 5, column = 1, columnspan = 3, padx = 5, pady = 5)
label22 = tk.Label(frame1, text = '一般Labe2',width=30)
label22.grid(row = 6, column = 1, columnspan = 3, padx = 5, pady = 5)
label33 = tk.Label(frame1, text = '一般Labe3',width=30)
label33.grid(row = 7, column = 1, columnspan = 3, padx = 5, pady = 5)
label44 = tk.Label(frame1, text = '一般Labe4',width=30)
label44.grid(row = 8, column = 1, columnspan = 3, padx = 5, pady = 5)




separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title('new all 2')

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


label5 = tk.Label(window,
			anchor = tk.E,# 設定文字的位置
			bg = 'blue',	# 設定標簽背景色
			fg = 'red',	# 設定標簽前景色
			text = 'Python',# 設定標簽中的文字
			width = 30,	# 設定標簽的寬度為30
			height = 3)	# 設定標簽的的高度為5
label5.pack()

label2 = tk.Label(window,
			text = 'Python GUI\nTkinter',			# 設定標簽中的文字，在字串中使用換行符
			justify = tk.LEFT,# 設定多行文字為齊左
			width = 30,
			height = 3)
label2.pack()

label3 = tk.Label(window,
			text = 'Python GUI\nTkinter',
			justify = tk.RIGHT,			# 設定多行文字為齊右
			width = 30,
			height = 3)
label3.pack()

label4 = tk.Label(window,
			text = 'Python GUI\nTkinter',
			justify = tk.CENTER,			# 設定多行文字為劇中對齊
			width = 30,
			height = 3)
label4.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

from tkinter.ttk import Separator

#字 前景 背景 寬 高 字位置預設 字型
label=tk.Label(window,text="Welcome to the United States and have a nice day",
            fg="red",bg="gray",
            width=15,height=4,
            font=("Helvetica",8,"bold"))
label.pack()

#字 前景 背景 寬 高 字位置西北
label=tk.Label(window,text="Welcome to the United States and have a nice day",
            fg="blue",bg="lime",
            width=15,height=4,
            anchor="nw")
label.pack()

#字 前景 背景 寬 高 字位置西北 卷寬度
label=tk.Label(window,text="Welcome to the United States and have a nice day",
            fg="blue",bg="yellow",
            width=15,height=4,
            anchor="nw",
            wraplength = 80,
            justify="left")     #left / center / right
label.pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

frame1 = tk.Frame(window, bg = '', width = W, height = H)
frame1.pack()

label=tk.Label(frame1,bitmap="hourglass")
label.grid(row = 0, column = 0, padx = 5, pady = 5)

label=tk.Label(frame1,bitmap="hourglass",compound="left",text="我的天空")
label.grid(row = 0, column = 1, padx = 5, pady = 5)

label=tk.Label(frame1,bitmap="hourglass",compound="top",text="我的天空")
label.grid(row = 0, column = 2, padx = 5, pady = 5)

label=tk.Label(frame1,bitmap="hourglass",compound="center",text="我的天空")
label.grid(row = 0, column = 3, padx = 5, pady = 5)

label=tk.Label(frame1, width = 12, height = 3, text="raised",relief="raised")
label.grid(row = 0, column = 4, padx = 5, pady = 5)

label=tk.Label(frame1, width = 12, height = 3, text="raised",relief="raised",bg="lightyellow",padx=5,pady=10)
label.grid(row = 0, column = 5, padx = 5, pady = 5)

Reliefs = ["flat","groove","raised","ridge","solid","sunken"]

idx = 0
for Relief in Reliefs:
    tk.Label(frame1,text=Relief,relief=Relief,
          fg="blue",
          font="Times 20 bold").grid(row = 1, column = idx, padx = 5, pady = 5)
    idx += 1
    
bitMaps = ["error","hourglass","info","questhead","question",
           "warning","gray12","gray25","gray50","gray75"]

idx = 0
for bitMap in bitMaps:
    tk.Label(frame1,bitmap=bitMap).grid(row = 2+(idx//6), column = idx % 6, padx = 5, pady = 5)
    idx += 1



print('在視窗的右下方顯示兩個Label')
oklabel = tk.Label(window,text="OK",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="blue") # 藍底白字
oklabel.pack(anchor=tk.S,side=tk.RIGHT,   # 從右開始在南方配置
             padx=10,pady=10)       # x和y軸間距皆是10

nolabel = tk.Label(window,text="NO",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="red")  # 藍底白字
nolabel.pack(anchor=tk.S,side=tk.RIGHT,   # 從右開始在南方配置
             pady=10)               # y軸間距皆是10

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# tkinterDialog.py

class MyDialog:		# 定義交談視窗類別
    def __init__(self, root):
        self.top = tk.Toplevel(root)	# 產生Toplevel元件
        label = tk.Label(self.top, text='Please Input')	# 產生標簽元件
        label.pack()
        self.entry = tk.Entry(self.top)	# 產生文字框元件
        self.entry.pack()
        self.entry.focus()			# 讓文字框獲得焦點
        button = tk.Button(self.top, text='Ok',command=self.Ok)
        button.pack()
    def Ok(self):
        self.input = self.entry.get()		# 取得文字框中內容，儲存為input
        self.top.destroy()			# 銷毀交談視窗
    def get(self):	# 傳回在文字框輸入的內容
        return self.input

class MyButton():	# 定義按鈕類別
    def __init__(self, root):
        self.root = root			# 儲存父視窗參考
        self.button = tk.Button(root, text='Create',command = self.Create)# 設定Create按鈕的事件處理函數
        self.button.pack()
    def Create(self):# Create按鈕的事件處理函數
        d = MyDialog(self.root)			# 產生交談視窗
        self.button.wait_window(d.top)		# 等待交談視窗結束
        print('你輸入了 :' + d.get())		# 取得交談視窗中輸入值，並輸出

window = tk.Tk()	# 產生主視窗
window.geometry("600x400")

MyButton(window)	# 產生Create按鈕

window.mainloop()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("準備搬出的")
print("------------------------------------------------------------")  # 60個







print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

""" 搬出


button1 = tk.Button(window, text='pack置中', width=20).pack()
button2 = tk.Button(window, text='pack左', width=20).pack(side=tk.LEFT)
button3 = tk.Button(window, text='pack右', width=20).pack(side=tk.RIGHT)

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

#設定視窗背景色
window.config(bg="red")
window.config(bg="green")
window.config(bg="blue")

# 將4個鈕包裝定位在右下方
button4.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
button3.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
button2.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)
button1.pack(anchor=tk.S,side=tk.RIGHT,padx=5,pady=5)

print("pack版面佈局的示範")

plus=tk.Button(window, width=20, text="加法範例")
plus.pack(side="left")
minus=tk.Button(window, width=20, text="減法範例")
minus.pack(side="left")
multiply=tk.Button(window, width=20, text="乘法範例")
multiply.pack(side="left")
divide=tk.Button(window, width=20, text="除法範例")
divide.pack(side="left")

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(fill=tk.X)                   # 填滿X軸包裝與定位元件
label2.pack(pady=10)                  # y軸增加10像素
label3.pack(fill=tk.X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x400")

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(fill=tk.X,pady=10)           # 填滿X軸,Y軸增加10像素
label2.pack(pady=10)                  # Y軸增加10像素
label3.pack(fill=tk.X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x400")

label1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label2 = tk.Label(window,text="歡迎來到美國",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue",
              width=15)             # 標籤寬度是15
label1.pack(padx=50)                  # 左右邊界間距是50像素
label2.pack(padx=50)                  # 左右邊界間距是50像素
label3.pack(padx=50)                  # 左右邊界間距是50像素

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x400")

label1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label2 = tk.Label(window,text="歡迎來到美國",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue",
              width=15)             # 標籤寬度是15
label1.pack(side=tk.LEFT)
label2.pack(side=tk.LEFT,padx=10)        # 左右間距padx=10
label3.pack(side=tk.LEFT)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x400")

label1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",
              bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",
              bg="lightblue")
label1.pack()
label2.pack(ipadx=10)                 # ipadx=10包裝與定位元件
label3.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x400")

label1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = tk.Label(window,text="歡迎來到美國",
              bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",
              bg="lightblue")
label1.pack()
label2.pack(ipadx=10)                 # ipadx=10包裝與定位元件
label3.pack(ipady=10)                 # ipady=10包裝與定位元件

window.mainloop()



print("------------------------------------------------------------")  # 60個

# place.py

window=tk.Tk()
window.geometry('300x200')
window.configure(bg='white') 
window.title('place配置')

label1=tk.Label(window, text = "五色鳥 Muller's Barbet", font=('微軟正黑體', 18),\
              fg='white',bg='black')
label2=tk.Label(window, text = '啄木鳥目', font=('標楷體', 16),fg='blue',bg='lightblue')
label3=tk.Label(window, text = '五色鳥科', font=('標楷體', 14),fg='green',bg='lightgreen')
msg='分布海平面到2800公尺，全身為鮮艷的翠綠色，在闊葉林中有良好的保護色。'
label4=tk.Label(window, text = msg,font=('細明體', 12),wraplength=170)
label1.place(x=10,y=5,width=280,height=40)
label2.place(x=10,y=50,width=90,height=50)
label3.place(x=10,y=105,width=90,height=50)
label4.place(x=110,y=50,width=180,height=105)

window.mainloop()








window = tk.Tk()
window.geometry("600x400")

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(fill=tk.X)                   # 填滿X軸包裝與定位元件
label2.pack()
label3.pack(fill=tk.X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x400")

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(fill=tk.X)                   # 填滿X軸包裝與定位元件
label2.pack(fill=tk.Y)                   # 填滿Y軸包裝與定位元件
label3.pack(fill=tk.X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x400")

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(side=tk.LEFT)                # 從左配置控件
label2.pack()                         # 預設從上開始配置控件
label3.pack()                         # 預設從上開始配置控件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x400")

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(side=tk.LEFT,fill=tk.Y)         # 從左配置控件fill=tk.Y
label2.pack(fill=tk.X)                   # 預設從上開始配置控件fill=tk.X
label3.pack()                         # 預設從上開始配置控件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x400")

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(side=tk.LEFT,fill=tk.Y)         # 從左配置控件fill=tk.Y
label2.pack(fill=tk.X)                   # 預設從上開始配置控件fill=tk.X
label3.pack(fill=tk.X)                   # 預設從上開始配置控件fill=tk.X

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x400")

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(side=tk.LEFT,fill=tk.Y)         # 從左配置控件fill=tk.Y
label2.pack(fill=tk.X)                   # 預設從上開始配置控件fill=tk.X
label3.pack(fill=tk.BOTH)                # 預設從上開始配置控件fill=tk.BOTH

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x400")

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(side=tk.LEFT,fill=tk.Y)         # 從左配置控件fill=tk.Y
label2.pack(fill=tk.X)                   # 預設從上開始配置控件fill=tk.X
label3.pack(fill=tk.BOTH,expand=True)    # fill=tk.BOTH,expand=True

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x400")
    
Label(window,text='Mississippi',bg='red',fg='white',
      font='Times 24 bold').pack(fill=tk.X)
Label(window,text='Kentucky',bg='green',fg='white',
      font='Arial 24 bold italic').pack(fill=tk.BOTH,expand=True)  
Label(window,text='Purdue',bg='blue',fg='white',
      font='Times 24 bold').pack(fill=tk.X)

window.mainloop() 

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x400")
    
Label(window,text='Mississippi',bg='red',fg='white',
      font='Times 20 bold').pack(side=tk.LEFT,fill=tk.Y)
Label(window,text='Kentucky',bg='green',fg='white',
      font='Arial 20 bold italic').pack(side=tk.LEFT,fill=tk.BOTH,expand=True)  
Label(window,text='Purdue',bg='blue',fg='white',
      font='Times 20 bold').pack(side=tk.LEFT,fill=tk.Y)

window.mainloop() 

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x400")

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow",width=15)
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen",width=15)
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue",width=15)
label1.place(x=0,y=0)                 # 直接定位
label2.place(x=30,y=50)               # 直接定位
label3.place(x=60,y=100)              # 直接定位

window.mainloop()

print('------------------------------------------------------------')	#60個
# Toplevel
print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x400")

tl = tk.Toplevel()
tk.Label(tl,text = 'I am a Toplevel').pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x400")

tl = tk.Toplevel()
tl.title("Toplevel")
tl.geometry("300x180")

tk.Label(tl,text = 'I am a Toplevel').pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x400")

msgYes, msgNo, msgExit = 1,2,3
def MyAnswer():                   # 建立對話方塊
    msgType = random.randint(1,3)   # 隨機數產生對話方塊方式
    if msgType == msgYes:           # 產生Yes字串
        labTxt = 'Yes'
    elif msgType == msgNo:          # 產生No字串
        labTxt = 'No'
    elif msgType == msgExit:        # 產生Exit字串
        labTxt = 'Exit'    
    tl = tk.Toplevel()                 # 建立Toplevel視窗
    tl.geometry("300x180")          # 建立對話方塊大小
    tl.title("My Answer")
    tk.Label(tl,text=labTxt).pack(fill=tk.BOTH,expand=True)

button1 = tk.Button(window,text='Click Me',command = MyAnswer)
button1.pack()

window.mainloop()

"""


'''

window = tk.Tk()
window.geometry("600x800")
window.title('tkinter的變數類別')

variable_int0 = tk.IntVar()  # 宣告 variable_int0 為整數物件
variable_int1 = tk.IntVar()  # 宣告 variable_int1 為整數物件
variable_int2 = tk.IntVar()  # 宣告 variable_int2 為整數物件
variable_int3 = tk.IntVar()  # 宣告 variable_int3 為整數物件
variable_string = tk.StringVar()  # 建立一個字串變數, 預設值為空字串

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def printSelection0():
    print('你的選擇是 :', variable_int0.get(), select_items[variable_int0.get()])

print('串列作成選項')
select_items = [(0, 'AAAA'), (1, 'BBBB'), (2, 'CCCC')]

variable_int0.set(1)  # 預設選項

for val, item in select_items:
    tk.Radiobutton(window, text = item, value = val,
                   variable = variable_int0, padx = 20,
                   command = printSelection0).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def printSelection1():
    print(select_items[variable_int1.get()])

print('字典作成選項1, 一般選項紐')
select_items = {0:"東京",1:"紐約",2:"巴黎"}

variable_int1.set(1)  # 預設選項

# 建立選項紐
for val, city in select_items.items():
    tk.Radiobutton(window,
                text=city,
                variable=variable_int1,value=val,
                command=printSelection1).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def printSelection2():
    print(select_items[variable_int2.get()])            # 列出所選城市

print('字典作成選項2, 用盒子取代選項紐')
select_items = {0:"東京",1:"紐約",2:"巴黎"}

variable_int2.set(1)  # 預設選項

for val, city in select_items.items():        # 建立選項紐    
    tk.Radiobutton(window,
                text=city,
                indicatoron = 0,        # 用盒子取代選項紐
                width=30,
                variable=variable_int2,value=val,
                command=printSelection2).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

print('Radiobutton 使用 整數 變數')
def printSelection3():
    num = variable_int3.get()
    if num == 1:
        print("你是男生")
    else:
        print("你是女生")

variable_int3.set(1)  # 預設選項
                       
rbman = tk.Radiobutton(window,text="男生",           # 男生選項鈕
                    variable=variable_int3,value=1,
                    command=printSelection3)
rbman.pack()

rbwoman = tk.Radiobutton(window,text="女生",         # 女生選項鈕
                      variable=variable_int3,value=2,
                      command=printSelection3)
rbwoman.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

print('Radiobutton 使用 字串 變數')
def printSelection4():
    label.config(text="你是"+variable_string.get())

variable_string.set("男生")                                 # 預設選項是男生
                       
label = tk.Label(window,text="這是預設,尚未選擇", bg="lightyellow",width=30)
label.pack()

rbman = tk.Radiobutton(window,text="男生",           # 男生選項鈕
                    variable=variable_string,value="男生",
                    command=printSelection4)
rbman.pack()

rbwoman = tk.Radiobutton(window,text="女生",         # 女生選項鈕
                      variable=variable_string,value="女生",
                      command=printSelection4)
rbwoman.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

variable_string = tk.StringVar()
variable_string.set('1')  # 預設選項

radio = tk.Radiobutton(window,# 產生單選框元件
			variable = variable_string, # 設定單選框關聯的變數
			value = '1',# 設定勾選單選框時其所關聯的變數的值，即r的值
			indicatoron = 0,			# 將單選框繪製成按鈕型態
			text = 'Radio1')			# 設定單選框顯示的文字
radio.pack()

radio = tk.Radiobutton(window,
			variable = variable_string,
			value = '2',# 當勾選該單選框時r的值為2
			indicatoron = 0,
			text = 'Radio2' )
radio.pack()

radio = tk.Radiobutton(window,
			variable = variable_string,
			value = '3',# 當勾選該單選框時r的值為3
			indicatoron = 0,
			text = 'Radio3' )
radio.pack()

radio = tk.Radiobutton(window,
			variable = variable_string,
			value = '4',# 當勾選該單選框時r的值為4
			indicatoron = 0,
			text = 'Radio4' )
radio.pack()

variable_int = tk.IntVar()		# 使用IntVar產生整數變數用於複選框
variable_int.set(1)  # 預設選項

check = tk.Checkbutton(window,
			text = 'Checkbutton',			# 設定複選框的文字
			variable = variable_int,# 設定複選框關聯的變數
			indicatoron = 0,			# 將複選框繪製成按鈕型態
			onvalue = 1,# 當勾選複選框時，c的值為1
			offvalue = 2)# 當未勾選複選框時，c的值為2
check.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

variable_string.set('1')  # 預設選項
radio = tk.Radiobutton(window,# 產生單選框元件
			variable = variable_string, # 設定單選框關聯的變數
			value = '1',# 設定勾選單選框時其所關聯的變數的值，即r的值
			text = 'Radio1')			# 設定單選框顯示的文字
radio.pack()

radio = tk.Radiobutton(window,
			variable = variable_string,
			value = '2',# 當勾選該單選框時r的值為2
			text = 'Radio2' )
radio.pack()

radio = tk.Radiobutton(window,
			variable = variable_string,
			value = '3',# 當勾選該單選框時r的值為3
			text = 'Radio3' )
radio.pack()

radio = tk.Radiobutton(window,
			variable = variable_string,
			value = '4',# 當勾選該單選框時r的值為4
			text = 'Radio4' )
radio.pack()

variable_int.set(1)  # 預設選項

check = tk.Checkbutton(window,
			text = 'Checkbutton',			# 設定複選框的文字
			variable = variable_int,# 設定複選框關聯的變數
			onvalue = 1,# 當勾選複選框時，c的值為1
			offvalue = 2)# 當未勾選複選框時，c的值為2
check.pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個




separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個




separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個



print(variable_string.get())  # 輸出 字串變數 的值
print(variable_int.get())  # 輸出 整數變數 的值



# 產生多行文字框元件
text1 = tk.Text(window,	selectbackground = 'red', selectforeground = 'gray')
text1.pack()




""" 缺檔案
def more():
    if variable_int.get()==0:
        str1="牛是對少部份牛科動物的統稱 \n\
              包括和人類習習相關的黃牛、水牛和氂牛" 
        print("cattle的簡介 :", str1)
    else:
        str2="鹿有別於牛、羊等的動物。 \n \
              包括麝科和鹿科動物"
        print("deer的簡介 :", str2)
    
lb=tk.Label(window,text="請點選想了解的動物簡介:").pack()
variable_int.set(0)  # 預設選項
pic1=ImageTk.PhotoImage(file="image/cattle.gif")
pic2=ImageTk.PhotoImage(file="image/deer.gif")
tk.Radiobutton(window,image=pic1,variable=variable_int,value=0).pack()
tk.Radiobutton(window,image=pic2,variable=variable_int,value=1).pack()
tk.Button(window,text="進一步了解", command=more).pack()
"""



entry8 = tk.Entry(window, bg="#ffff00", borderwidth = 3)
entry8.insert(0,"AAAA")
entry8.insert("2","BBBB")
entry8.insert("end","CCCC")
entry8.delete(0, 2)  #刪除前面兩個字元
entry8.pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

import tkinter.simpledialog	# 匯入tkSimpleDialog模組

def InStr():
    # 建立 字串 輸入交談視窗
    r = tkinter.simpledialog.askstring('Python Tkinter',
                                       'Input String',			# 指定提示字元
                                       initialvalue='Tkinter')		# 指定起始化文字
    print(r)	# 輸出傳回值
def InInt():
    # 建立 整數 輸入交談視窗
    r = tkinter.simpledialog.askinteger('Python Tkinter','Input Integer')
    print(r)
def InFlo():
    # 建立 浮點數 輸入交談視窗
    r = tkinter.simpledialog.askfloat('Python Tkinter','Input Float')
    print(r)

button1 = tk.Button(window,text = 'Input String', command = InStr)
button1.pack()
button2 = tk.Button(window,text = 'Input Integer', command = InInt)
button2.pack()
button2 = tk.Button(window,text = 'Input Float', command = InFlo)
button2.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個



def buttonClick2():
     #改變背景顏色
     button2.config(bg = "blue")  

button2 = tk.Button(window, text="改變Button之背景顏色", command=buttonClick2)
button2.pack()


"""

-------


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

print('寫讀 Entry 上的資料')

# Label / Entry / Text / 
# 一個按鈕 設定一個變數給控件 並把這個控件的變數讀出來




label4 =tk.Label(window,text="尚未按下按鈕")
label4.pack()
label4.config(text="你是男生")

tk.StringVar() 字串，
tk.IntVar() 整數，預設值為 0
tk.DoubleVar() 浮點數，預設值為 0.0
tk.Boolean()  # 布林值變數，True是1， False是0 fail





"""

