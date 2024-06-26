import sys

import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image

import random

W = 200
H = 200
w = 12
h = 2

print("------------------------------------------------------------")  # 60個
'''
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

window = tk.Tk()
window.geometry("600x800")
window.title('new all 2')

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

button1 = tk.Button(window, text='pack置中', width=20).pack()
button2 = tk.Button(window, text='pack左', width=20).pack(side=tk.LEFT)
button3 = tk.Button(window, text='pack右', width=20).pack(side=tk.RIGHT)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

#設定視窗背景色
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

plus=tk.Button(window, width=20, text="加法範例")
plus.pack(side="left")
minus=tk.Button(window, width=20, text="減法範例")
minus.pack(side="left")
multiply=tk.Button(window, width=20, text="乘法範例")
multiply.pack(side="left")
divide=tk.Button(window, width=20, text="除法範例")
divide.pack(side="left")

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(fill=tk.X)                   # 填滿X軸包裝與定位元件
label2.pack(pady=10)                  # y軸增加10像素
label3.pack(fill=tk.X)                   # 填滿X軸包裝與定位元件

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(fill=tk.X,pady=10)           # 填滿X軸,Y軸增加10像素
label2.pack(pady=10)                  # Y軸增加10像素
label3.pack(fill=tk.X)                   # 填滿X軸包裝與定位元件

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

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

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

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
window.geometry("600x800")
window.title('new all 2')

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = tk.Label(window,text="歡迎來到美國",
              bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",
              bg="lightblue")
label1.pack()
label2.pack(ipadx=10)                 # ipadx=10包裝與定位元件
label3.pack(ipady=10)                 # ipady=10包裝與定位元件

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(fill=tk.X)                   # 填滿X軸包裝與定位元件
label2.pack()
label3.pack(fill=tk.X)                   # 填滿X軸包裝與定位元件

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(fill=tk.X)                   # 填滿X軸包裝與定位元件
label2.pack(fill=tk.Y)                   # 填滿Y軸包裝與定位元件
label3.pack(fill=tk.X)                   # 填滿X軸包裝與定位元件

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(side=tk.LEFT)                # 從左配置控件
label2.pack()                         # 預設從上開始配置控件
label3.pack()                         # 預設從上開始配置控件

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(side=tk.LEFT,fill=tk.Y)         # 從左配置控件fill=tk.Y
label2.pack(fill=tk.X)                   # 預設從上開始配置控件fill=tk.X
label3.pack()                         # 預設從上開始配置控件

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(side=tk.LEFT,fill=tk.Y)         # 從左配置控件fill=tk.Y
label2.pack(fill=tk.X)                   # 預設從上開始配置控件fill=tk.X
label3.pack(fill=tk.X)                   # 預設從上開始配置控件fill=tk.X

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(side=tk.LEFT,fill=tk.Y)         # 從左配置控件fill=tk.Y
label2.pack(fill=tk.X)                   # 預設從上開始配置控件fill=tk.X
label3.pack(fill=tk.BOTH)                # 預設從上開始配置控件fill=tk.BOTH

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.geometry("600x800")
window.title('new all 2')

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

label1 = tk.Label(window,text="歡迎來到美國",bg="lightyellow")
label2 = tk.Label(window,text="歡迎來到美國",bg="lightgreen")
label3 = tk.Label(window,text="歡迎來到美國",bg="lightblue")
label1.pack(side=tk.LEFT,fill=tk.Y)         # 從左配置控件fill=tk.Y
label2.pack(fill=tk.X)                   # 預設從上開始配置控件fill=tk.X
label3.pack(fill=tk.BOTH,expand=True)    # fill=tk.BOTH,expand=True

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個
    
tk.Label(window,text='Mississippi',bg='red',fg='white',
      font='Times 24 bold').pack(fill=tk.X)
tk.Label(window,text='Kentucky',bg='green',fg='white',
      font='Arial 24 bold italic').pack(fill=tk.BOTH,expand=True)  
tk.Label(window,text='Purdue',bg='blue',fg='white',
      font='Times 24 bold').pack(fill=tk.X)

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個
    
tk.Label(window,text='Mississippi',bg='red',fg='white',
      font='Times 20 bold').pack(side=tk.LEFT,fill=tk.Y)
tk.Label(window,text='Kentucky',bg='green',fg='white',
      font='Arial 20 bold italic').pack(side=tk.LEFT,fill=tk.BOTH,expand=True)  
tk.Label(window,text='Purdue',bg='blue',fg='white',
      font='Times 20 bold').pack(side=tk.LEFT,fill=tk.Y)

window.mainloop() 


print('------------------------------------------------------------')	#60個


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



window = tk.Tk()
window.geometry("600x800")
window.title('new all 2')

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


"""

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

print("------------------------------------------------------------")  # 60個

class WidgetsDemo:
    def __init__(self):
        window = tk.Tk()
        window.title("Widgets Demo") # Set a title
        
        # Add a button, a check button, and a radio button to frame1
        frame1 = tk.Frame(window) # Create and add a frame to window
        frame1.pack()      
        self.v1 = tk.IntVar()
        cbtBold = tk.Checkbutton(frame1, text = "Bold", 
            variable = self.v1, command = self.processCheckbutton) 
        self.v2 = tk.IntVar()
        rbRed = tk.Radiobutton(frame1, text = "Red", bg = "red",
                variable = self.v2, value = 1, 
                command = self.processRadiobutton) 
        rbYellow = tk.Radiobutton(frame1, text = "Yellow", 
                bg = "yellow", variable = self.v2, value = 2, 
                command = self.processRadiobutton) 
        cbtBold.grid(row = 1, column = 1)
        rbRed.grid(row = 1, column = 2)
        rbYellow.grid(row = 1, column = 3)
        
        # Add a button, a check button, and a radio button to frame1
        frame2 = tk.Frame(window) # Create and add a frame to window
        frame2.pack()
        label = tk.Label(frame2, text = "Enter your name: ")
        self.name = tk.StringVar()
        entryName = tk.Entry(frame2, textvariable = self.name) 
        btGetName = tk.Button(frame2, text = "Get Name", 
            command = self.processButton)
        message = tk.Message(frame2, text = "It is a widgets demo")
        label.grid(row = 1, column = 1)
        entryName.grid(row = 1, column = 2)
        btGetName.grid(row = 1, column = 3)
        message.grid(row = 1, column = 4)
        
        # Add a text
        text = tk.Text(window) # Create a text add to the window
        text.pack()
        text.insert(tk.END, 
            "Tip\nThe best way to learn Tkinter is to read ")
        text.insert(tk.END, 
            "these carefully designed examples and use them ")
        text.insert(tk.END, "to create your applications.")
        
        window.mainloop() # Create an event loop

    def processCheckbutton(self):
        print("check button is " 
            + ("checked " if self.v1.get() == 1 else "unchecked"))
        
    def processRadiobutton(self):
        print(("Red" if self.v2.get() == 1 else "Yellow") 
            + " is selected " )
    
    def processButton(self):
        print("Your name is " + self.name.get())

WidgetsDemo() # Create GUI

print("------------------------------------------------------------")  # 60個

"""

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個


"""
    
class ChangeLabelDemo:
    def __init__(self):
        window = tk.Tk() # Create a window 
        window.title("Change Label Demo") # Set a title
        
        # Add a label to frame1
        frame1 = tk.Frame(window) # Create and add a frame to window 
        frame1.pack()        
        self.lbl = tk.Label(frame1, text = "Programming is fun")
        self.lbl.pack()
        
        # Add a label, an entry, a button, and two radio buttons to frame2
        frame2 = tk.Frame(window) # Create and add a frame to window 
        frame2.pack()
        label = tk.Label(frame2, text = "Enter text: ")
        self.msg = tk.StringVar()
        entry = tk.Entry(frame2, textvariable = self.msg) 
        btChangeText = tk.Button(frame2, text = "Change Text", command = self.processButton)
        self.v1 = tk.StringVar()
        rbRed = tk.Radiobutton(frame2, text = "Red", bg = "red", variable = self.v1, value = 'R', command = self.processRadiobutton) 
        rbYellow = tk.Radiobutton(frame2, text = "Yellow", bg = "yellow", variable = self.v1, value = 'Y', command = self.processRadiobutton) 
        
        label.grid(row = 1, column = 1)
        entry.grid(row = 1, column = 2)
        btChangeText.grid(row = 1, column = 3)
        rbRed.grid(row = 1, column = 4)
        rbYellow.grid(row = 1, column = 5)
        
        window.mainloop()

    def processRadiobutton(self):
        if self.v1.get() == 'R':
            self.lbl["fg"] = "red"
        elif self.v1.get() == 'Y':
            self.lbl["fg"] = "yellow" 
    
    def processButton(self):
        self.lbl["text"] = self.msg.get() # New text for the label
        
ChangeLabelDemo() # Create GUI 



print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x800")
window.title('new all 2')

separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

wordlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
list1 = tk.Listbox(window, yscrollcommand = scrollbar.set )

for line in range(10):
   list1.insert(tk.END, "字母: " + wordlist[line])

list1.pack( side = tk.LEFT, fill = tk.BOTH )
scrollbar.config( command = list1.yview )


separator = tk.Frame(height = 2, bd = 1, relief = tk.SUNKEN).pack(fill = tk.X, padx = 5, pady = 5)  #分隔線
print("------------------------------------------------------------")  # 60個

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title("Scroll Text Demo")

frame1 = tk.Frame(window)
frame1.pack()

scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

text1 = tk.Text(frame1, width = 40, height = 10, wrap = tk.WORD, yscrollcommand = scrollbar.set)
text1.pack()

scrollbar.config(command = text1.yview)

window.mainloop()

print("------------------------------------------------------------")  # 60個

import calendar

window = tk.Tk()
window.config(background='grey')
window.title("Calender for the year")
window.geometry("550x600")

year = 2024
content = calendar.calendar(year)
calYear = tk.Label(window, text= content, font= "Consolas 10 bold")
calYear.grid(row=5, column=1,padx=20)
window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("600x400")

# Create PhotoImage objects
caImage = tk.PhotoImage(file = "ca.gif")
chinaImage = tk.PhotoImage(file = "china.gif")
leftImage = tk.PhotoImage(file = "left.gif")
rightImage = tk.PhotoImage(file = "right.gif")
usImage = tk.PhotoImage(file = "usIcon.gif")
ukImage = tk.PhotoImage(file = "ukIcon.gif")
crossImage = tk.PhotoImage(file = "x.gif")
circleImage = tk.PhotoImage(file = "o.gif")

# frame1 to contain label and canvas
frame1 = tk.Frame(window)
frame1.pack()
tk.Label(frame1, image = caImage).pack(side = tk.LEFT)
canvas = tk.Canvas(frame1)
canvas.create_image(90, 50, image = chinaImage)
canvas["width"] = 200
canvas["height"] = 100
canvas.pack(side = tk.LEFT)

# frame2 to contain buttons, check buttons, and radio buttons
frame2 = tk.Frame(window)
frame2.pack()
tk.Button(frame2, image = leftImage).pack(side = tk.LEFT)
tk.Button(frame2, image = rightImage).pack(side = tk.LEFT)

tk.Checkbutton(frame2, image = usImage).pack(side = tk.LEFT)
tk.Checkbutton(frame2, image = ukImage).pack(side = tk.LEFT)

tk.Radiobutton(frame2, image = crossImage).pack(side = tk.LEFT)
tk.Radiobutton(frame2, image = circleImage).pack(side = tk.LEFT)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title('my window')
window.geometry('200x100')

var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15,
             height=2)
#l = tk.Label(window, text='OMG! this is TK!', bg='green', font=('Arial', 12), width=15, height=2)
l.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

b = tk.Button(window, text='hit me', width=15,
              height=2, command=hit_me)
b.pack()


window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

tk.Label(window, text='on the window').pack()

frm = tk.Frame(window)
frm.pack()
frm_l = tk.Frame(frm, )
frm_r = tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')

tk.Label(frm_l, text='on the frm_l1').pack()
tk.Label(frm_l, text='on the frm_l2').pack()
tk.Label(frm_r, text='on the frm_r1').pack()

window.mainloop()
'''
print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry("200x200")

# canvas = tk.Canvas(window, height=150, width=500)
# canvas.grid(row=1, column=1)
# image_file = tk.PhotoImage(file='welcome.gif')
# image = canvas.create_image(0, 0, anchor='nw', image=image_file)

# tk.Label(window, text='1').pack(side='top')
# tk.Label(window, text='1').pack(side='bottom')
# tk.Label(window, text='1').pack(side='left')
# tk.Label(window, text='1').pack(side='right')

# for i in range(4):
# for j in range(3):
# tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)

tk.Label(window, text=1).place(x=20, y=10, anchor="nw")

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title("my window")
window.geometry("200x200")

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

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title("my window")
window.geometry("200x200")

var1 = tk.StringVar()
l = tk.Label(window, bg="yellow", width=4, textvariable=var1)
l.pack()


def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)


b1 = tk.Button(
    window, text="print selection", width=15, height=2, command=print_selection
)
b1.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))
lb = tk.Listbox(window, listvariable=var2)
list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert("end", item)
lb.insert(1, "first")
lb.insert(2, "second")
lb.delete(2)
lb.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title("my window")
window.geometry("200x200")

var = tk.StringVar()
l = tk.Label(window, bg="yellow", width=20, text="empty")
l.pack()


def print_selection():
    l.config(text="you have selected " + var.get())


r1 = tk.Radiobutton(
    window, text="Option A", variable=var, value="A", command=print_selection
)
r1.pack()
r2 = tk.Radiobutton(
    window, text="Option B", variable=var, value="B", command=print_selection
)
r2.pack()
r3 = tk.Radiobutton(
    window, text="Option C", variable=var, value="C", command=print_selection
)
r3.pack()


window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title("my window")
window.geometry("200x200")

l = tk.Label(window, bg="yellow", width=20, text="empty")
l.pack()


def print_selection(v):
    l.config(text="you have selected " + v)


s = tk.Scale(
    window,
    label="try me",
    from_=5,
    to=11,
    orient=tk.HORIZONTAL,
    length=200,
    showvalue=0,
    tickinterval=2,
    resolution=0.01,
    command=print_selection,
)
s.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title("my window")
window.geometry("200x200")

l = tk.Label(window, bg="yellow", width=20, text="empty")
l.pack()


def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text="I love only Python ")
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text="I love only C++")
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text="I do not love either")
    else:
        l.config(text="I love both")


var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(
    window, text="Python", variable=var1, onvalue=1, offvalue=0, command=print_selection
)
c2 = tk.Checkbutton(
    window, text="C++", variable=var2, onvalue=1, offvalue=0, command=print_selection
)
c1.pack()
c2.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title("my window")
window.geometry("200x200")

canvas = tk.Canvas(window, bg="blue", height=100, width=200)
image_file = tk.PhotoImage(file="ins.gif")
image = canvas.create_image(10, 10, anchor="nw", image=image_file)
x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill="red")
arc = canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30, start=0, extent=180)
rect = canvas.create_rectangle(100, 30, 100 + 20, 30 + 20)
canvas.pack()


def moveit():
    canvas.move(rect, 0, 2)


b = tk.Button(window, text="move", command=moveit).pack()


window.mainloop()

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


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 定義字符串元組
        books = ("Tkinter庫", "三大布局", "Pack布局", "Grid布局", "Place布局")
        for i in range(len(books)):
            # 生成3個隨機數
            ct = [random.randrange(256) for x in range(3)]
            grayness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
            # 將元組中3個隨機數格式化成16進制數,轉成顏色格式
            bg_color = "#%02x%02x%02x" % tuple(ct)
            # 創建Label，設置背景色和前景色
            lb = tk.Label(
                window,
                text=books[i],
                fg="White" if grayness < 120 else "Black",
                bg=bg_color,
            )
            # 使用place()設置該Label的大小和位置
            lb.place(x=20, y=36 + i * 36, width=180, height=30)


window = tk.Tk()
window.title("Place布局")
# 設置窗口的大小和位置
# width x height + x_offset + y_offset
window.geometry("250x250+30+30")
App(window)
window.mainloop()

print("------------------------------------------------------------")  # 60個


def handler(event, a, b, c):
    # 事件處理函數
    print(event)
    print("handler", a, b, c)


def handlerAdaptor(fun, **kwds):
    # 事件處理函數的適配器，相當于中介，那個event是從那里來的呢，我也納悶，這也許就是python的偉大之處吧
    return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)


window = tk.Tk()

btn = tk.Button(text="按鈕")
# 通過中介函數handlerAdaptor進行事件綁定
btn.bind("<Button-1>", handlerAdaptor(handler, a=1, b=2, c=3))
btn.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

"""自定義函數"""


def init(data):
    # 數據從run函數中預置寬度和高度
    data.circleSize = min(data.width, data.height) / 10
    data.circleX = data.width / 2
    data.circleY = data.height / 2
    data.charText = ""
    data.keysymText = ""


"""跟蹤并響應鼠標點擊"""


def mousePressed(event, data):
    data.circleX = event.x
    data.circleY = event.y


"""跟蹤和響應按鍵"""


def keyPressed(event, data):
    data.charText = event.char
    data.keysymText = event.keysym


"""通常使用redrawAll繪制圖形"""


def redrawAll(canvas, data):
    canvas.create_oval(
        data.circleX - data.circleSize,
        data.circleY - data.circleSize,
        data.circleX + data.circleSize,
        data.circleY + data.circleSize,
    )
    if data.charText != "":
        canvas.create_text(
            data.width / 10, data.height / 3, text="char: " + data.charText
        )
    if data.keysymText != "":
        canvas.create_text(
            data.width / 10, data.height * 2 / 3, text="keysym: " + data.keysymText
        )


"""按原樣使用run函數"""


def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height, fill="white", width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # 設置數據并調用init
    class Struct(object):
        pass

    data = Struct()
    data.width = width
    data.height = height
    window = tk.Tk()
    init(data)
    # 創建根和畫布
    canvas = tk.Canvas(window, width=data.width, height=data.height)
    canvas.pack()
    # 設置事件
    window.bind("<Button-1>", lambda event: mousePressedWrapper(event, canvas, data))
    window.bind("<Key>", lambda event: keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # 然后啟動應用程序
    window.mainloop()  # 塊，直到窗口關閉
    print("bye!")


run(400, 200)

print("------------------------------------------------------------")  # 60個


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
        self.expr = None

    def initWidgets(self):
        # 創建一個輸入組件
        self.show = tk.Label(
            relief=tk.SUNKEN,
            font=("Courier New", 24),
            width=25,
            bg="white",
            anchor=tk.E,
        )
        # 對該輸入組件使用Pack布局，放在容器頂部
        self.show.pack(side=tk.TOP, pady=10)
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
            # 為鼠標左鍵的單擊事件綁定事件處理方法
            b.bind("<Button-1>", self.click)
            # 為鼠標左鍵的雙擊事件綁定事件處理方法
            if b["text"] == "=":
                b.bind("<Double-1>", self.clean)

    def click(self, event):
        # 如果用戶單擊的是數字鍵或點號
        if event.widget["text"] in (
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
            ".",
        ):
            self.show["text"] = self.show["text"] + event.widget["text"]
        # 如果用戶單擊了運算符
        elif event.widget["text"] in ("+", "-", "*", "/"):
            # 如果當前表達式為None，直接用show組件的內容和運算符進行連接
            if self.expr is None:
                self.expr = self.show["text"] + event.widget["text"]
            # 如果當前表達式不為None，用表達式、show組件的內容和運算符進行連接
            else:
                self.expr = self.expr + self.show["text"] + event.widget["text"]
            self.show["text"] = ""
        elif event.widget["text"] == "=" and self.expr is not None:
            self.expr = self.expr + self.show["text"]
            print(self.expr)
            # 使用eval函數計算表達式的值
            self.show["text"] = str(eval(self.expr))
            self.expr = None

    # 雙擊=按鈕時，程序清空計算結果、將表達式設為None
    def clean(self, event):
        self.expr = None
        self.show["text"] = ""


window = tk.Tk()
window.title("計算器")
App(window)
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
from tkinter.messagebox import showinfo

window = tk.Tk()
a = tk.Variable(window, value="123")
e = tk.Entry(window, textvariable=a)
b = tk.Button(window, command=lambda *args: showinfo(message=a.get()), text="獲取")
e.pack()
b.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
tk.Label(window, text="賬號：").grid(row=0, column=0)
tk.Label(window, text="密碼：").grid(row=1, column=0)

v1 = tk.StringVar()  # 輸入框里是字符串類型，因此用Tkinter的StringVar類型來存放
v2 = tk.StringVar()  # 需要兩個變量來存放賬號和密碼

e1 = tk.Entry(window, textvariable=v1)
e2 = tk.Entry(window, textvariable=v2, show="*")  # 想要顯示什么就輸入什么

e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)


def show():
    print("賬號：%s" % e1.get())
    print("密碼：%s" % e2.get())


tk.Button(window, text="獲取信息", width=10, command=show).grid(
    row=3, column=0, sticky=W, padx=10, pady=5
)
tk.Button(window, text="退出", width=10, command=window.quit).grid(
    row=3, column=1, sticky=E, padx=10, pady=5
)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

text1 = tk.Text(window, width=100, height=30)
text1.pack()
photo = PhotoImage(file="bg1.gif")


def show():
    # 添加圖片用image_create
    text1.image_create(tk.END, image=photo)


b1 = tk.Button(text1, text="點我點我", command=show)
# 添加插件用window_create
text1.window_create(tk.INSERT, window=b1)

window.mainloop()

print("------------------------------------------------------------")  # 60個

# 創建容器
tk = tk.Tk()
tk.title("我的GUI界面學習")
# 主界面容器
mainfarm = tk.Frame()
mainfarm.pack()

lab1 = tk.Label(mainfarm, text="你好，這是Checkbutton操作界面")
lab1.pack()


def button1back_handle():
    print("button1 down")


button2val = tk.IntVar()
button2 = tk.Checkbutton(
    mainfarm,
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
tk.Label(mainfarm, textvariable=button2val).pack()
mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

# 單選
LB1 = tk.Listbox(window)
tk.Label(window, text="單選：選擇你的課程").pack()

for item in ["Chinese", "English", "Math"]:
    LB1.insert(tk.END, item)
LB1.pack()

# 多選
LB2 = tk.Listbox(window, selectmode=tk.EXTENDED)
tk.Label(window, text="多選：你會幾種編程語言").pack()

for item in ["python", "C++", "C", "Java", "Php"]:
    LB2.insert(tk.END, item)

LB2.insert(1, "JS", "Go", "R")
LB2.delete(5, 6)
LB2.select_set(0, 3)
LB2.select_clear(0, 1)
print(LB2.size())
print(LB2.get(3))
print(LB2.select_includes(3))
LB2.pack()
window.mainloop()

print("------------------------------------------------------------")  # 60個


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        ttk.Label(self.master, text="指定from、to、increment").pack()
        # 通過指定from_、to、increament選項創建Spinbox
        sb1 = Spinbox(self.master, from_=18, to=50, increment=5)
        sb1.pack(fill=tk.X, expand=tk.YES)
        ttk.Label(self.master, text="指定values").pack()
        # 通過指定values選項創建Spinbox
        self.sb2 = Spinbox(
            self.master, values=("Python", "C++", "Java", "PHY"), command=self.press
        )  # 通過command綁定事件處理方法
        self.sb2.pack(fill=tk.X, expand=tk.YES)
        ttk.Label(self.master, text="綁定變量").pack()
        self.intVar = tk.IntVar()
        # 通過指定values選項創建Spinbox，并為之綁定變量
        sb3 = Spinbox(
            self.master,
            values=list(range(18, 50, -4)),
            textvariable=self.intVar,  # 綁定變量
            command=self.press,
        )
        sb3.pack(fill=tk.X, expand=tk.YES)
        self.intVar.set(33)  # 通過變量改變Spinbox的值

    def press(self):
        print(self.sb2.get())


window = tk.Tk()
window.title("Spinbox測試")

App(window)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()  # 實例化一個窗口
window.title("Scale組件")  # 定義窗口標題
window.geometry("400x600")  # 定義窗口大小

l = tk.Label(window, bg="yellow", width=20, height=2, text="未選擇")
l.pack()


def print_selection(V):
    l.config(text="你已選擇" + V)


s = tk.Scale(
    window,
    label="進行選擇",
    from_=5,
    to=11,
    orient=tk.HORIZONTAL,
    length=200,
    showvalue=1,
    tickinterval=3,
    resolution=0.01,
    command=print_selection,
)
s.pack()  # 顯示名字,條方向;長度（像素），是否直接顯示值，標簽的單位長度，保留精度，定義功能

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


class mybutton:  # 定義按鈕類
    # 類初始化canvas1，label1是MyCanvals，mylabel的實例，因此可以使用類中的方法
    def __init__(self, root, canvas1, label1, type):
        self.root = root  # 保存引用值
        self.canvas1 = canvas1
        self.label1 = label1
        if type == 0:  # 根據類型創建按鈕
            button = tk.Button(root, text="畫線", command=self.DrawLine)
        elif type == 1:
            button = tk.Button(root, text="畫扇形", command=self.DrawArc)
        elif type == 2:
            button = tk.Button(root, text="畫矩形", command=self.DrawRec)
        else:
            button = tk.Button(root, text="畫橢圓", command=self.DrawOval)
        button.pack(side="left")

    def DrawLine(self):  # DrawLine按鈕事件處理函數
        self.label1.text.set("畫直線")
        self.canvas1.SetStatus(0)  # 把status賦值，便于根據status的值進行畫圖

    def DrawArc(self):
        self.label1.text.set("畫弧")
        self.canvas1.SetStatus(1)

    def DrawRec(self):
        self.label1.text.set("畫矩形")
        self.canvas1.SetStatus(2)

    def DrawOval(self):
        self.label1.text.set("畫橢圓")
        self.canvas1.SetStatus(3)


class MyCanvals:
    def __init__(self, root):
        self.status = 0
        self.draw = 0
        self.root = root
        self.canvas = tk.Canvas(root, bg="yellow", width=600, height=480)  # 生成canvas組件
        self.canvas.pack()
        self.canvas.bind("<ButtonRelease-1>", self.Draw)  # 綁定事件到左鍵
        self.canvas.bind("<Button-2>", self.Exit)  # 綁定事件到中鍵
        self.canvas.bind("<Button-3>", self.Del)  # 綁定事件到右鍵
        self.canvas.bind_all("<Delete>", self.Del)  # 綁定事件到delete鍵
        self.canvas.bind_all("<KeyPress-d>", self.Del)  # 綁定事件到d鍵
        self.canvas.bind_all("<KeyPress-e>", self.Exit)  # 綁定事件到e鍵

    def Draw(self, event):  # 繪圖事件處理函數
        if self.draw == 0:  # 判斷是否繪圖，先記錄起始位置
            self.x = event.x
            self.y = event.y
            self.draw = 1
        else:  # 根據self.status繪制不同的圖形
            if self.status == 0:
                self.canvas.create_line(self.x, self.y, event.x, event.y)
                self.draw = 0
            elif self.status == 1:
                self.canvas.create_arc(self.x, self.y, event.x, event.y)
                self.draw = 0
            elif self.status == 2:
                self.canvas.create_rectangle(self.x, self.y, event.x, event.y)
                self.draw = 0
            else:
                self.canvas.create_oval(self.x, self.y, event.x, event.y)
                self.draw = 0

    def Del(self, event):  # 按下右鍵或者d鍵刪除圖形
        items = self.canvas.find_all()
        for i in items:
            self.canvas.delete(i)

    def Exit(self, event):  # 按下中鍵或者e鍵退出
        self.root.quit()

    def SetStatus(self, status):  # 設置繪制的圖形
        self.status = status


class mylabel:  # 定義標簽類
    def __init__(self, root):
        self.root = root
        self.canvas1 = canvas1
        self.text = tk.StringVar()  # 生成標簽引用變量
        self.text.set("畫線")
        self.label = tk.Label(root, textvariable=self.text, fg="blue", width=50)  # 生成標簽
        self.label.pack(side="left")


window = tk.Tk()

canvas1 = MyCanvals(window)  # 生成實例
label1 = mylabel(window)  # 生成實例
mybutton(window, canvas1, label1, 0)
mybutton(window, canvas1, label1, 1)
mybutton(window, canvas1, label1, 2)
mybutton(window, canvas1, label1, 3)

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import messagebox
import threading

GAME_WIDTH = 450
GAME_HEIGHT = 650
BOARD_X = 220
BOARD_Y = 600
BOARD_WIDTH = 80
BALL_RADIUS = 9


class App:
    def __init__(self, master):
        self.master = master
        # 記錄小球動畫的第幾幀
        self.ball_index = 0
        # 記錄游戲是否失敗的旗標
        self.is_lose = False
        # 初始化記錄小球位置的變量
        self.curx = 260
        self.cury = 30
        self.boardx = BOARD_X
        self.init_widgets()
        self.vx = random.randint(3, 6)  # x方向的速度
        self.vy = random.randint(5, 10)  # y方向的速度
        # 通過定時器指定0.1秒之后執行moveball函數
        self.t = threading.Timer(0.1, self.moveball)
        self.t.start()

    # 創建界面組件
    def init_widgets(self):
        self.cv = tk.Canvas(
            root, background="white", width=GAME_WIDTH, height=GAME_HEIGHT
        )
        self.cv.pack()
        # 讓畫布得到焦點，從而可以響應按鍵事件
        self.cv.focus_set()
        self.cv.bms = []
        # 初始化小球的動畫幀
        for i in range(8):
            self.cv.bms.append(PhotoImage(file="images/ball_" + str(i + 1) + ".gif"))
        # 繪制小球
        self.ball = self.cv.create_image(
            self.curx, self.cury, image=self.cv.bms[self.ball_index]
        )
        self.board = self.cv.create_rectangle(
            BOARD_X,
            BOARD_Y,
            BOARD_X + BOARD_WIDTH,
            BOARD_Y + 20,
            width=0,
            fill="lightblue",
        )
        # 為向左箭頭按鍵綁定事件，擋板左移
        self.cv.bind("<Left>", self.move_left)
        # 為向右箭頭按鍵綁定事件，擋板右移
        self.cv.bind("<Right>", self.move_right)

    def move_left(self, event):
        if self.boardx <= 0:
            return
        self.boardx -= 5
        self.cv.coords(
            self.board, self.boardx, BOARD_Y, self.boardx + BOARD_WIDTH, BOARD_Y + 20
        )

    def move_right(self, event):
        if self.boardx + BOARD_WIDTH >= GAME_WIDTH:
            return
        self.boardx += 5
        self.cv.coords(
            self.board, self.boardx, BOARD_Y, self.boardx + BOARD_WIDTH, BOARD_Y + 20
        )

    def moveball(self):
        self.curx += self.vx
        self.cury += self.vy
        # 小球到了右邊墻壁，轉向
        if self.curx + BALL_RADIUS >= GAME_WIDTH:
            self.vx = -self.vx
        # 小球到了左邊墻壁，轉向
        if self.curx - BALL_RADIUS <= 0:
            self.vx = -self.vx
        # 小球到了上邊墻壁，轉向
        if self.cury - BALL_RADIUS <= 0:
            self.vy = -self.vy
        # 小球到了擋板處
        if self.cury + BALL_RADIUS >= BOARD_Y:
            # 如果在擋板范圍內
            if self.boardx <= self.curx <= (self.boardx + BOARD_WIDTH):
                self.vy = -self.vy
            else:
                messagebox.showinfo(title="失敗", message="您已經輸了")
                self.is_lose = True
        self.cv.coords(self.ball, self.curx, self.cury)
        self.ball_index += 1
        self.cv.itemconfig(self.ball, image=self.cv.bms[self.ball_index % 8])
        # 如果游戲還未失敗，讓定時器繼續執行
        if not self.is_lose:
            # 通過定時器指定0.1秒之后執行moveball函數
            self.t = threading.Timer(0.1, self.moveball)
            self.t.start()


window = tk.Tk()
window.title("彈球游戲")
window.geometry("%dx%d" % (GAME_WIDTH, GAME_HEIGHT))
# 禁止改變窗口大小
window.resizable(width=False, height=False)
App(window)
window.mainloop()

print("------------------------------------------------------------")  # 60個


# 定義繼承Frame的Application類
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        # 調用initWidgets()方法初始化界面
        self.initWidgets()

    def initWidgets(self):
        # 創建Label對象，第一個參數指定該Label放入root
        w = tk.Label(self)
        # 創建一個位圖
        bm = PhotoImage(file="images/a.png")
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
        fm2.pack(side=LEFT, padx=10, fill=tk.BOTH, expand=tk.YES)
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
