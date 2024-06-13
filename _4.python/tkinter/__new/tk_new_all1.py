import sys

import tkinter as tk

from tkinter import ttk
from PIL import ImageTk, Image

import random

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title('new all 1')

# Label / Entry / Text / 
# 一個按鈕 設定一個變數給控件 並把這個控件的變數讀出來

def show_data_in_label():
    global count
    count += 1
    label1_data.set("Label歡迎來到美國" + str(count))
    cc = label1_data.get()
    print('取得 Label 的資料 :', cc)
    entry1_data.set("Entry歡迎來到美國" + str(count))
    cc = entry1_data.get()
    print('取得 Entry 的資料 :', cc)
    label2.configure(text = "Label :" + entry2.get())
    print('取得Entry的資料 : ', entry2.get())
    height = userH.get()
    weight = userW.get()
    print('取得 height = ', height)
    print('取得 weight = ', weight)

count = 0

tk.Label(window,text="使用 字串 物件").pack()
label1_data = tk.StringVar()#建立一個變數給label
label1 = tk.Label(window, textvariable=label1_data).pack()

entry1_data = tk.StringVar()#建立一個變數給entry
entry1 = tk.Entry(window, textvariable=entry1_data).pack()

entry2 = tk.Entry(window)
entry2.pack()

label2 = tk.Label(window)
label2.pack()

tk.Label(window,text="使用 浮點數 物件").pack()
userH=tk.DoubleVar()		#宣告userH為浮點數物件
entry9 = tk.Entry(window,textvariable=userH).pack()  #textvariable參數值為userH

tk.Label(window,text="使用 整數 物件").pack()
userW=tk.IntVar()		#宣告userW為整數物件
entry10 = tk.Entry(window,textvariable=userW).pack()  #textvariable參數值為userW

button1 = tk.Button(window, text="寫讀 Label/Entry 上的資料", command=show_data_in_label).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

xL1 = tk.StringVar()
label = tk.Label(window,textvariable=xL1)
label.pack()
xL1.set("設定Label的資料1")

xL2 = tk.StringVar()
label = tk.Label(window,textvariable=xL2)
label.pack()
xL2.set("設定Label的資料2")

xL3 = tk.StringVar()
label = tk.Label(window,textvariable=xL3)
label.pack()
xL3.set("設定Label的資料3")

xE2 = tk.StringVar()
entry4 = tk.Entry(window,textvariable=xE2)     # 設定Label內容是變數x
entry4.pack()

def hit():                              # 讀取資料
    print("讀取資料:",xE1.get())
  
xE1 = tk.StringVar()
entry3 = tk.Entry(window,textvariable=xE1)     # 設定Label內容是變數x
entry3.pack()



button1 = tk.Button(window,text="讀取Entry的資料",command=hit)    # 建立讀取按鈕
button1.pack()

def button_command2():
    print(entry5.get())
    t1=entry5.get()
    v.set(t1)

entry5=tk.Entry(window)
entry5.pack()

button1 =tk.Button(window,text="press me1",command=button_command2)
button1.pack()

v = tk.StringVar()
label1 =tk.Label(window,text="Hello World!", textvariable=v)
label1.pack()
v.set("New Text!")

def get_entry_data():
    print('你按了 get')
    cc = entry16.get()
    print(cc)
    cc = entry17.get()
    print(cc)
    
name_data = tk.StringVar()#名字
tk.Label(window,text="使用 整數 物件").pack()
weight_data = tk.IntVar()#體重

entry16 = tk.Entry(window, foreground = "green", textvariable = name_data)
entry16.pack()

entry17 = tk.Entry(window, foreground = "green", textvariable = weight_data)
entry17.pack()

tk.Button(window, text = "取得上面Entry的資料", command = get_entry_data).pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def buttonClick1():
     buttonvar.set("心想事成，天天開心")

def buttonClick2():
     #改變背景顏色
     button2.config(bg = "blue")  

print("按鈕元件(Button)功能示範 Entry")
    
buttonvar = tk.StringVar() 
button1 = tk.Button(window, textvariable=buttonvar, command=buttonClick1)
buttonvar.set("按下我會有祝賀語1")
button1.pack()

button2 = tk.Button(window, text="按我會改變按鈕背景色", command=buttonClick2)
button2.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def button_command3():
    value1=entry6.get()
    print('取得資料 :', value1)
    label1.config(text='已按下按鈕')
    v2.set(str(value1))


v2 = tk.StringVar()
label1 =tk.Label(window,text="Hello World!", textvariable=v2)
label1.pack()
v2.set("New Text!")

label1 =tk.Label(window,text="尚未按下按鈕")
label1.pack()

label.config(text="你是男生")

entry6=tk.Entry(window)
entry6.pack()

button1 =tk.Button(window,text="press me2",command=button_command3)
button1.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

# 輸入文字框中的字元被顯示為“*”
entry11 = tk.Entry(window, show = '*', width = 30)
entry11.pack()

# 輸入文字框中的字元被顯示為“#”
entry12 = tk.Entry(window, show = '#', width = 30)
entry12.pack()

# 設定背景色 設定前景色
entry13 = tk.Entry(window, bg = 'red', fg = 'blue')
entry13.pack()

# 設定勾選文字的背景色和前景色
entry14 = tk.Entry(window, selectbackground = 'red', selectforeground = 'gray')
entry14.pack()

# 將文字框設定為禁用
entry15 = tk.Entry(window, state = tk.DISABLED)
entry15.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title('new all 2')

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


label1 = tk.Label(window,
			anchor = tk.E,# 設定文字的位置
			bg = 'blue',	# 設定標簽背景色
			fg = 'red',	# 設定標簽前景色
			text = 'Python',# 設定標簽中的文字
			width = 30,	# 設定標簽的寬度為30
			height = 3)	# 設定標簽的的高度為5
label1.pack()

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




separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title('new all 3')

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

label=tk.Label(window,bitmap="hourglass")
label.pack()  

label=tk.Label(window,bitmap="hourglass",compound="left",text="我的天空")
label.pack()  

label=tk.Label(window,bitmap="hourglass",compound="top",text="我的天空")
label.pack()  

label=tk.Label(window,bitmap="hourglass",compound="center",text="我的天空")
label.pack()  

label=tk.Label(window,text="raised",relief="raised")
label.pack()

label=tk.Label(window,text="raised",relief="raised",bg="lightyellow",padx=5,pady=10)
label.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

Reliefs = ["flat","groove","raised","ridge","solid","sunken"]

for Relief in Reliefs:
    tk.Label(window,text=Relief,relief=Relief,
          fg="blue",
          font="Times 20 bold").pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

bitMaps = ["error","hourglass","info","questhead","question",
           "warning","gray12","gray25","gray50","gray75"]

for bitMap in bitMaps:
    tk.Label(window,bitmap=bitMap).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

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

sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


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






def select():
    print('你的選項是 :', var.get())

place = [('宜蘭', 1), ('台北', 2), ('高雄', 3)]
tk.Label(window,text="使用 整數 物件").pack()
var = tk.IntVar()
var.set(3)

for item, val in place:
    tk.Radiobutton(window, text = item, value = val,
                   variable = var, padx = 20,
                   command = select).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


def printSelection():
    num = var.get()
    if num == 1:
        label.config(text="你是男生")
    else:
        label.config(text="你是女生")

tk.Label(window,text="使用 整數 物件").pack()
var = tk.IntVar()                                  # 選項紐綁定的變數
var.set(1)                                      # 預設選項是男生
                       
label = tk.Label(window,text="這是預設,尚未選擇", bg="lightyellow",width=30)
label.pack()

rbman = tk.Radiobutton(window,text="男生",           # 男生選項鈕
                    variable=var,value=1,
                    command=printSelection)
rbman.pack()
rbwoman = tk.Radiobutton(window,text="女生",         # 女生選項鈕
                      variable=var,value=2,
                      command=printSelection)
rbwoman.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def printSelection():
    label.config(text="你是"+var.get())

var = tk.StringVar()                               # 選項紐綁定的變數
var.set("男生")                                 # 預設選項是男生
                       
label = tk.Label(window,text="這是預設,尚未選擇", bg="lightyellow",width=30)
label.pack()

rbman = tk.Radiobutton(window,text="男生",           # 男生選項鈕
                    variable=var,value="男生",
                    command=printSelection)
rbman.pack()
rbwoman = tk.Radiobutton(window,text="女生",         # 女生選項鈕
                      variable=var,value="女生",
                      command=printSelection)
rbwoman.pack()

window.mainloop()

print('------------------------------------------------------------')	#60個

def printSelection():
    print(cities[var.get()])            # 列出所選城市

window = tk.Tk()
window.geometry("600x800")

cities = {0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"香港"}

tk.Label(window,text="使用 整數 物件").pack()
var = tk.IntVar()
var.set(0)                              # 預設選項                       

for val, city in cities.items():        # 建立選項紐    
    tk.Radiobutton(window,
                text=city,
                variable=var,value=val,
                command=printSelection).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

def printSelection():
    print(cities[var.get()])            # 列出所選城市

cities = {0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"香港"}

tk.Label(window,text="使用 整數 物件").pack()
var = tk.IntVar()
var.set(0)                              # 預設選項                       

for val, city in cities.items():        # 建立選項紐    
    tk.Radiobutton(window,
                text=city,
                indicatoron = 0,        # 用盒子取代選項紐
                width=30,
                variable=var,value=val,
                command=printSelection).pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個




separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


r = tk.StringVar()		# 使用StringVar產生字串變數用於單選框元件
r.set('1')			# 起始化變數值

radio = tk.Radiobutton(window,# 產生單選框元件
			variable = r, # 設定單選框關聯的變數
			value = '1',# 設定勾選單選框時其所關聯的變數的值，即r的值
			indicatoron = 0,			# 將單選框繪製成按鈕型態
			text = 'Radio1')			# 設定單選框顯示的文字
radio.pack()

radio = tk.Radiobutton(window,
			variable = r,
			value = '2',# 當勾選該單選框時r的值為2
			indicatoron = 0,
			text = 'Radio2' )
radio.pack()

radio = tk.Radiobutton(window,
			variable = r,
			value = '3',# 當勾選該單選框時r的值為3
			indicatoron = 0,
			text = 'Radio3' )
radio.pack()

radio = tk.Radiobutton(window,
			variable = r,
			value = '4',# 當勾選該單選框時r的值為4
			indicatoron = 0,
			text = 'Radio4' )
radio.pack()


tk.Label(window,text="使用 整數 物件").pack()
c = tk.IntVar()		# 使用IntVar產生整數變數用於複選框
c.set(1)
check = tk.Checkbutton(window,
			text = 'Checkbutton',			# 設定複選框的文字
			variable = c,# 設定複選框關聯的變數
			indicatoron = 0,			# 將複選框繪製成按鈕型態
			onvalue = 1,# 當勾選複選框時，c的值為1
			offvalue = 2)# 當未勾選複選框時，c的值為2
check.pack()

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

r = tk.StringVar()		# 使用StringVar產生字串變數用於單選框元件
r.set('1')			# 起始化變數值
radio = tk.Radiobutton(window,# 產生單選框元件
			variable = r, # 設定單選框關聯的變數
			value = '1',# 設定勾選單選框時其所關聯的變數的值，即r的值
			text = 'Radio1')			# 設定單選框顯示的文字
radio.pack()

radio = tk.Radiobutton(window,
			variable = r,
			value = '2',# 當勾選該單選框時r的值為2
			text = 'Radio2' )
radio.pack()

radio = tk.Radiobutton(window,
			variable = r,
			value = '3',# 當勾選該單選框時r的值為3
			text = 'Radio3' )
radio.pack()

radio = tk.Radiobutton(window,
			variable = r,
			value = '4',# 當勾選該單選框時r的值為4
			text = 'Radio4' )
radio.pack()

tk.Label(window,text="使用 整數 物件").pack()
c = tk.IntVar()		# 使用IntVar產生整數變數用於複選框
c.set(1)

check = tk.Checkbutton(window,
			text = 'Checkbutton',			# 設定複選框的文字
			variable = c,# 設定複選框關聯的變數
			onvalue = 1,# 當勾選複選框時，c的值為1
			offvalue = 2)# 當未勾選複選框時，c的值為2
check.pack()


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個




separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個




separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個



print(r.get())			# 輸出r的值
print(c.get())		# 輸出c的值







""" config = configure
    label2.config(text="Button clicked")
    label2.configure(text = "Label :" + entry2.get())
"""



# 產生多行文字框元件
text1 = tk.Text(window,	selectbackground = 'red', selectforeground = 'gray')
text1.pack()





""" 缺檔案
def more():
    if choice.get()==0:
        str1="牛是對少部份牛科動物的統稱 \n\
              包括和人類習習相關的黃牛、水牛和氂牛" 
        print("cattle的簡介 :", str1)
    else:
        str2="鹿有別於牛、羊等的動物。 \n \
              包括麝科和鹿科動物"
        print("deer的簡介 :", str2)
    
lb=tk.Label(window,text="請點選想了解的動物簡介:").pack()
tk.Label(window,text="使用 整數 物件").pack()
choice=tk.IntVar()
choice.set(0)
pic1=ImageTk.PhotoImage(file="image/cattle.gif")
pic2=ImageTk.PhotoImage(file="image/deer.gif")
tk.Radiobutton(window,image=pic1,variable=choice,value=0).pack()
tk.Radiobutton(window,image=pic2,variable=choice,value=1).pack()
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


