import sys

import tkinter as tk

from tkinter import ttk
from PIL import ImageTk, Image

import random

W = 200
H = 200
w = 12
h = 2

'''
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

from tkinter import * # Import tkinter
    
class WidgetsDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Widgets Demo") # Set a title
        
        # Add a button, a check button, and a radio button to frame1
        frame1 = Frame(window) # Create and add a frame to window
        frame1.pack()      
        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1, text = "Bold", 
            variable = self.v1, command = self.processCheckbutton) 
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text = "Red", bg = "red",
                variable = self.v2, value = 1, 
                command = self.processRadiobutton) 
        rbYellow = Radiobutton(frame1, text = "Yellow", 
                bg = "yellow", variable = self.v2, value = 2, 
                command = self.processRadiobutton) 
        cbtBold.grid(row = 1, column = 1)
        rbRed.grid(row = 1, column = 2)
        rbYellow.grid(row = 1, column = 3)
        
        # Add a button, a check button, and a radio button to frame1
        frame2 = Frame(window) # Create and add a frame to window
        frame2.pack()
        label = Label(frame2, text = "Enter your name: ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name) 
        btGetName = Button(frame2, text = "Get Name", 
            command = self.processButton)
        message = Message(frame2, text = "It is a widgets demo")
        label.grid(row = 1, column = 1)
        entryName.grid(row = 1, column = 2)
        btGetName.grid(row = 1, column = 3)
        message.grid(row = 1, column = 4)
        
        # Add a text
        text = Text(window) # Create a text add to the window
        text.pack()
        text.insert(END, 
            "Tip\nThe best way to learn Tkinter is to read ")
        text.insert(END, 
            "these carefully designed examples and use them ")
        text.insert(END, "to create your applications.")
        
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



from tkinter import * # Import tkinter
    
class ChangeLabelDemo:
    def __init__(self):
        window = Tk() # Create a window 
        window.title("Change Label Demo") # Set a title
        
        # Add a label to frame1
        frame1 = Frame(window) # Create and add a frame to window 
        frame1.pack()        
        self.lbl = Label(frame1, text = "Programming is fun")
        self.lbl.pack()
        
        # Add a label, an entry, a button, and two radio buttons to frame2
        frame2 = Frame(window) # Create and add a frame to window 
        frame2.pack()
        label = Label(frame2, text = "Enter text: ")
        self.msg = StringVar()
        entry = Entry(frame2, textvariable = self.msg) 
        btChangeText = Button(frame2, text = "Change Text", command = self.processButton)
        self.v1 = StringVar()
        rbRed = Radiobutton(frame2, text = "Red", bg = "red", variable = self.v1, value = 'R', command = self.processRadiobutton) 
        rbYellow = Radiobutton(frame2, text = "Yellow", bg = "yellow", variable = self.v1, value = 'Y', command = self.processRadiobutton) 
        
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

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/SpongeBob.gif'

tkimage = tk.PhotoImage(file = filename)

canvas = tk.Canvas(window, width = 600, height = 600)
canvas.pack()
canvas.create_image(256, 256, image = tkimage)

window.mainloop()

print("------------------------------------------------------------")  # 60個

#只能用gif
filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/SpongeBob.gif'
   
window = tk.Tk() # Create a root window

photo = tk.PhotoImage(file = filename)
tk.Label(window, text = "Blue", image = photo, bg = "blue").pack(fill = tk.BOTH, expand = 1)

window.mainloop() # Create an event loop

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
canvas = tk.Canvas(window,
			width = 600,					# 指定Canvas元件的寬度
			height = 480,					# 指定Canvas元件的高度
			bg = 'white')					# 指定Canvas元件的背景色

#只能開啟 gif 檔
filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/brown.gif'
im = tk.PhotoImage(file=filename)				# 使用PhotoImage開啟圖片
canvas.create_image(300,250,image = im)					# 使用create_image將圖片新增到Canvas元件中

canvas.pack()								# 將Canvas新增到主視窗

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

import tkinter as tk

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

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit_me():
    #tk.messagebox.showinfo(title='Hi', message='hahahaha')
    #tk.messagebox.showwarning(title='Hi', message='nononono')
    #tk.messagebox.showerror(title='Hi', message='No!! never')
    #print(tk.messagebox.askquestion(title='Hi', message='hahahaha'))   # return 'yes' , 'no'
    #print(tk.messagebox.askyesno(title='Hi', message='hahahaha'))   # return True, False
    print(tk.messagebox.asktrycancel(title='Hi', message='hahahaha'))   # return True, False
    print(tk.messagebox.askokcancel(title='Hi', message='hahahaha'))   # return True, False
    print(tk.messagebox.askyesnocancel(title="Hi", message="haha"))     # return, True, False, None

tk.Button(window, text='hit me', command=hit_me).pack()
window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.geometry('200x200')

#canvas = tk.Canvas(window, height=150, width=500)
#canvas.grid(row=1, column=1)
#image_file = tk.PhotoImage(file='welcome.gif')
#image = canvas.create_image(0, 0, anchor='nw', image=image_file)

#tk.Label(window, text='1').pack(side='top')
#tk.Label(window, text='1').pack(side='bottom')
#tk.Label(window, text='1').pack(side='left')
#tk.Label(window, text='1').pack(side='right')

#for i in range(4):
    #for j in range(3):
        #tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10)

tk.Label(window, text=1).place(x=20, y=10, anchor='nw')

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# e = tk.Entry(window, show="*")
e = tk.Entry(window, show="1")
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert', var)
def insert_end():
    var = e.get()
    # t.insert('end', var)
    t.insert(2.2, var)

b1 = tk.Button(window, text='insert point', width=15,
              height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert end',
               command=insert_end)
b2.pack()
t = tk.Text(window, height=2)
t.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=4, textvariable=var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

b1 = tk.Button(window, text='print selection', width=15,
              height=2, command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44))
lb = tk.Listbox(window, listvariable=var2)
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var = tk.StringVar()
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_selection():
    l.config(text='you have selected ' + var.get())

r1 = tk.Radiobutton(window, text='Option A',
                    variable=var, value='A',
                    command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B',
                    variable=var, value='B',
                    command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C',
                    variable=var, value='C',
                    command=print_selection)
r3.pack()


window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_selection(v):
    l.config(text='you have selected ' + v)

s = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')

var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
                    command=print_selection)
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0,
                    command=print_selection)
c1.pack()
c2.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

canvas = tk.Canvas(window, bg='blue', height=100, width=200)
image_file = tk.PhotoImage(file='ins.gif')
image = canvas.create_image(10, 10, anchor='nw', image=image_file)
x0, y0, x1, y1= 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=180)
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)
canvas.pack()

def moveit():
    canvas.move(rect, 0, 2)

b = tk.Button(window, text='move', command=moveit).pack()


window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window, text='', bg='yellow')
l.pack()
counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter+=1

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label="Submenu1", command=do_job)

window.config(menu=menubar)

window.mainloop()

'''
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


from tkinter import *

root = Tk();root.geometry("700x220")
root.title('制作钢琴按键布局') 
#Frame 是一个矩形区域， 就是用来防止其他子组件
f1 = Frame(root)
f1.pack()
f2 = Frame(root);f2.pack()
btnText = ("流行风","中国风","伦敦风","古典风","轻音乐")
for txt in btnText:
	Button(f1,text=txt).pack(side="left",padx="10")
	for i in range(1,20):
		Button(f2,width=5,height=10,bg="black" if i%2==0 else "white").pack(side="left")
root.mainloop()





#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_2.py

from tkinter import *

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 创建一个输入组件
        e = Entry(relief=SUNKEN, font=('Courier New', 24), width=25)
        # 对该输入组件使用Pack布局，放在容器顶部
        e.pack(side=TOP, pady=10)
        p = Frame(self.master)
        p.pack(side=TOP)
        # 定义字符串的元组
        names = ("0" , "1" , "2" , "3" 
            , "4" , "5" , "6" , "7" , "8" , "9"
            , "+" , "-" , "*" , "/" , ".", "=")
        # 遍历字符串元组
        for i in range(len(names)):
            # 创建Button，将Button放入p组件中
            b = Button(p, text=names[i], font=('Verdana', 20), width=6)
            b.grid(row=i // 4, column=i % 4)
root = Tk()
root.title("Grid布局")
App(root)
root.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_3.py

from tkinter import *
from tkinter import messagebox
import random
class Application(Frame):
	def __init__(self, master=None):
		super().__init__(master) # super()代表的是父类的定义， 而不是父类对象
		self.master = master
		self.pack()
		self.createWidget()
	
	def createWidget(self):
		"""通过 grid 布局实现登录界面"""
		self.label01 = Label(self,text="用户名")
		self.label01.grid(row=0,column=0)
		self.entry01 = Entry(self)
		self.entry01.grid(row=0,column=1)
		Label(self,text="用户名为手机号").grid(row=0,column=2)
		Label(self, text="密码").grid(row=1, column=0)
		Entry(self, show="*").grid(row=1, column=1)
		Button(self, text="登录").grid(row=2, column=1, sticky=EW)
		Button(self, text="取消").grid(row=2, column=2, sticky=E)
	
if __name__ == '__main__':
	root = Tk()
	root.geometry("400x90+200+300")
	app = Application(master=root)
root.title("Grid布局")
root.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_4.py

from tkinter import *
import random
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        #定义字符串元组
        books = ('Tkinter库', '三大布局','Pack布局', 'Grid布局',\
            'Place布局')
        for i in range(len(books)):
            # 生成3个随机数
            ct = [random.randrange(256) for x in range(3)]
            grayness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
            # 将元组中3个随机数格式化成16进制数,转成颜色格式
            bg_color = "#%02x%02x%02x" % tuple(ct)
            # 创建Label，设置背景色和前景色
            lb = Label(root,
                text=books[i], 
                fg = 'White' if grayness < 120 else 'Black',
                bg = bg_color)
            # 使用place()设置该Label的大小和位置
            lb.place(x = 20, y = 36 + i*36, width=180, height=30) 
root = Tk()
root.title("Place布局")
# 设置窗口的大小和位置
# width x height + x_offset + y_offset
root.geometry("250x250+30+30")   
App(root)
root.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_5.py

#coding=utf-8
 import tkinter
def handler(event, a, b, c):
    '''事件处理函数'''
    print(event)
    print ("handler", a, b, c) 
def handlerAdaptor(fun, **kwds):
    '''事件处理函数的适配器，相当于中介，那个event是从那里来的呢，我也纳闷，这也许就是python的伟大之处吧'''
    return lambda event,fun=fun,kwds=kwds: fun(event, **kwds) 
if __name__=='__main__':
    root = tkinter.Tk()
    btn = tkinter.Button(text=u'按钮') 
    # 通过中介函数handlerAdaptor进行事件绑定
    btn.bind("<Button-1>", handlerAdaptor(handler, a=1, b=2, c=3)) 
    btn.pack()
    root.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_6.py

import tkinter as tk
# 事件
def sys_out(even):
    from tkinter import messagebox
    if messagebox.askokcancel('Exit','Confirm to exit?'):
        root.destroy()
root = tk.Tk()
root.geometry('300x200')
#绑定事件到Esc键，当按下Esc键就会调用sys_out函数，弹出对话框
root.bind('<Escape>',sys_out)
root.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_7.py

from tkinter import *
"""自定义函数"""
def init(data):
    # 数据从run函数中预置宽度和高度
    data.circleSize = min(data.width, data.height)/10
    data.circleX = data.width/2
    data.circleY = data.height/2
    data.charText = ""
    data.keysymText = "" 
"""跟踪并响应鼠标点击"""
def mousePressed(event, data):
    data.circleX = event.x
    data.circleY = event.y 
"""跟踪和响应按键"""
def keyPressed(event, data):
    data.charText = event.char
    data.keysymText = event.keysym 
"""通常使用redrawAll绘制图形"""
def redrawAll(canvas, data):
    canvas.create_oval(data.circleX - data.circleSize, 
                       data.circleY - data.circleSize,
                       data.circleX + data.circleSize,
                       data.circleY + data.circleSize)
    if data.charText != "":
        canvas.create_text(data.width/10, data.height/3,
                           text="char: " + data.charText)
    if data.keysymText != "":
        canvas.create_text(data.width/10, data.height*2/3, 
                           text="keysym: " + data.keysymText)
"""按原样使用run函数""" 
def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()     
    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data) 
    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data) 
    #设置数据并调用init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    init(data) 
    #创建根和画布
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack() 
    #设置事件
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data) 
    #然后启动应用程序
    root.mainloop()  #块，直到窗口关闭
    print("bye!") 
run(400, 200)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_8.py

from tkinter import *

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
        self.expr = None
    def initWidgets(self):
        #创建一个输入组件
        self.show = Label(relief=SUNKEN, font=('Courier New', 24),\
            width=25, bg='white', anchor=E)
        #对该输入组件使用Pack布局，放在容器顶部
        self.show.pack(side=TOP, pady=10)
        p = Frame(self.master)
        p.pack(side=TOP)
        #定义字符串的元组
        names = ("0" , "1" , "2" , "3" 
            , "4" , "5" , "6" , "7" , "8" , "9"
            , "+" , "-" , "*" , "/" , ".", "=")
        #遍历字符串元组
        for i in range(len(names)):
            #创建Button，将Button放入p组件中
            b = Button(p, text=names[i], font=('Verdana', 20), width=6)
            b.grid(row=i // 4, column=i % 4)
            #为鼠标左键的单击事件绑定事件处理方法
            b.bind('<Button-1>', self.click)
            #为鼠标左键的双击事件绑定事件处理方法
            if b['text'] == '=': b.bind('<Double-1>', self.clean)
    def click(self, event):
        #如果用户单击的是数字键或点号
        if(event.widget['text'] in ('0', '1', '2', '3',\
            '4', '5', '6', '7', '8', '9', '.')):
            self.show['text'] = self.show['text'] + event.widget['text']
        #如果用户单击了运算符
        elif(event.widget['text'] in ('+', '-', '*', '/')):
            #如果当前表达式为None，直接用show组件的内容和运算符进行连接
            if self.expr is None:
                self.expr = self.show['text'] + event.widget['text']
            #如果当前表达式不为None，用表达式、show组件的内容和运算符进行连接
            else:
                self.expr = self.expr + self.show['text'] + event.widget['text']
            self.show['text'] = ''
        elif(event.widget['text'] == '=' and self.expr is not None):
            self.expr = self.expr + self.show['text']
            print(self.expr)
            #使用eval函数计算表达式的值
            self.show['text'] = str(eval(self.expr))
            self.expr = None
    #双击=按钮时，程序清空计算结果、将表达式设为None
    def clean(self, event):
        self.expr = None
        self.show['text'] = ''
root = Tk()
root.title("计算器")
App(root)
root.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_9.py

import tkinter as tk
from tkinter import ttk
 
win = tk.Tk()
win.title("Python图形界面") #添加标题 
label1=ttk.Label(win, text="选择数字")
label1.grid(column=1, row=0)    #添加一个标签，并将其列设置为1，行设置为0
 
#button被点击之后会被执行
def clickMe(): #当acction被点击时,该函数则生效"显示当前选择的数"
 
    print(numberChosen.current())#输出下所选的索引
 
    if numberChosen.current()==0 :#判断列表当前所选~~~~~~~~~~~
        label1.config(text="选了1")#注意，上面的label1如果直接.grid会出错
    if numberChosen.current()==1 :
        label1.config(text="选了6")
    if numberChosen.current()==2 :
        label1.config(text="选了第"+ str(numberChosen.current()+1)+"个") 
#按钮
action = ttk.Button(win, text="单击我", command=clickMe)  #创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.grid(column=2, row=1) #设置其在界面中出现的位置,column代表列,row代表行 
# 创建一个下拉列表
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = (1, 6, 3)     #设置下拉列表的值
numberChosen.grid(column=1, row=1)  #设置其在界面中出现的位置,column代表列,row代表行
numberChosen.current(0)    #设置下拉列表默认显示的值，0为numberChosen['values']的下标值 
win.mainloop()      #当调用mainloop()时,窗口才会显示出来

print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_10.py

from tkinter import Tk, Variable, Entry, Button
from tkinter.messagebox import showinfo

tk = Tk()
a = Variable(tk, value='123')
e = Entry(tk, textvariable=a)
b = Button(tk, command=lambda *args: showinfo(message=a.get()),
          text="获取")
e.pack()
b.pack()

tk.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_12.py

from tkinter import * 

root = Tk() 
Label(root, text='账号：').grid(row=0, column=0)
Label(root, text='密码：').grid(row=1, column=0) 

v1 = StringVar()  #输入框里是字符串类型，因此用Tkinter的StringVar类型来存放
v2 = StringVar()  #需要两个变量来存放账号和密码 

e1 = Entry(root, textvariable=v1)
e2 = Entry(root, textvariable=v2, show='*') #想要显示什么就输入什么

e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5) 

def show():
    print("账号：%s" % e1.get())
    print("密码：%s" % e2.get()) 

Button(root, text='获取信息', width=10, command=show)\
             .grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text='退出', width=10, command=root.quit)\
             .grid(row=3, column=1, sticky=E, padx=10, pady=5) 

mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_13.py

from tkinter import *
root = Tk()
text1 = Text(root,width=100,height=30)
text1.pack()
photo = PhotoImage(file='bg1.gif')
def show():
     #添加图片用image_create
     text1.image_create(END,image=photo)
b1 = Button(text1,text='点我点我',command=show)
     #添加插件用window_create
text1.window_create(INSERT,window=b1)
mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_15.py

from tkinter import *
#创建容器
tk=Tk()
tk.title("我的GUI界面学习")
#主界面容器
mainfarm=Frame()
mainfarm.pack()

lab1=Label(mainfarm,text="你好，这是Checkbutton操作界面")
lab1.pack()
def button1back_handle():
    print("button1 down")
button2val=IntVar()
button2=Checkbutton(mainfarm,
                    text='BUTTON2',
                    variable=button2val,  #variable为按键的状态值
                    anchor="n",  # 按键文本位置为n
                    bd=5,  # 将borderwidth（边框宽度）设置为5
                    command=button1back_handle,  # 传入回调函数
                    justify="left",  # 按键文本为左对齐
                    cursor="right_ptr",  # 将光标移动至按键时的显示修改为
                    font=("宋体", 15, "bold", "italic"),  # 设置按键的字体、大小、加粗、斜体
                    padx=5, pady=5,  # 指定按键文本或图像距离边框的距离
                    relief=RAISED,  # 指定按键的样式
                    state=ACTIVE,  # 指定按键的状态
                    width=10, height=5,  # 制定按键的宽、高
                    )
button2.pack()
#为了看到按键值使用Lable控件显示下按键的值
Label(mainfarm,textvariable=button2val).pack()
mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_17.py

from tkinter import *
root=Tk() 
#单选
LB1=Listbox(root) 
Label(root,text='单选：选择你的课程').pack()
for item in ['Chinese','English','Math']:
    LB1.insert(END,item)
LB1.pack() 
#多选
LB2=Listbox(root,selectmode=EXTENDED)
Label(root,text='多选：你会几种编程语言').pack()
for item in ['python','C++','C','Java','Php']:
    LB2.insert(END,item)
LB2.insert(1,'JS','Go','R')
LB2.delete(5,6)
LB2.select_set(0,3)
LB2.select_clear(0,1)
print (LB2.size())
print (LB2.get(3))
print(LB2.select_includes(3))
LB2.pack() 
root.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_18.py

from tkinter import *
# 导入ttk
from tkinter import ttk
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        ttk.Label(self.master, text='指定from、to、increment').pack()
        # 通过指定from_、to、increament选项创建Spinbox
        sb1 = Spinbox(self.master, from_ = 18,
            to = 50,
            increment = 5)
        sb1.pack(fill=X, expand=YES)
        ttk.Label(self.master, text='指定values').pack()
        # 通过指定values选项创建Spinbox
        self.sb2 = Spinbox(self.master, 
            values=('Python', 'C++', 'Java', 'PHY'),
            command = self.press) # 通过command绑定事件处理方法
        self.sb2.pack(fill=X, expand=YES)
        ttk.Label(self.master, text='绑定变量').pack()
        self.intVar = IntVar()
        # 通过指定values选项创建Spinbox，并为之绑定变量
        sb3 = Spinbox(self.master, 
            values=list(range(18, 50, -4)),
            textvariable = self.intVar, # 绑定变量
            command = self.press)
        sb3.pack(fill=X, expand=YES)
        self.intVar.set(33) # 通过变量改变Spinbox的值
    def press(self):
        print(self.sb2.get())
root = Tk()
root.title("Spinbox测试")
App(root)
root.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_19.py

import tkinter as tk
window=tk.Tk()              #实例化一个窗口
window.title('Scale组件')   #定义窗口标题
window.geometry('400x600')  #定义窗口大小 
l=tk.Label(window,bg='yellow',width=20,height=2,text='未选择')
l.pack() 
def print_selection(V):
    l.config(text='你已选择'+V) 
s=tk.Scale(window,label='进行选择',from_=5,to=11,orient=tk.HORIZONTAL,length=200,showvalue=1,tickinterval=3,resolution=0.01,command=print_selection)
s.pack() #显示名字,条方向;长度（像素），是否直接显示值，标签的单位长度，保留精度，定义功能
window.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_20.py

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext #导入滚动文本框的模块

window = tk.Tk()
window.title("Python GUI") # 加标题

#创建一个容器,
monty = ttk.LabelFrame(window, text=" Monty Python ") #创建一个容器，其父容器为win
monty.grid(column=0, row=0, padx=10, pady=10) #该容器外围需要留出的空余空间
aLabel = ttk.Label(monty, text="A Label")
ttk.Label(monty, text="Chooes a number").grid(column=1, row=0) #添加一个标签，并将其列设置为1，行设置为0
ttk.Label(monty, text="Enter a name:").grid(column=0, row=0, sticky='W') #设置其在界面中出现的位置,column代表列,row代表行
#button被点击之后会被执行
def clickMe():   #当acction被点击时,该函数则生效
  action.configure(text='Hello ' + name.get() + ' ' + numberChosen.get()) #设置button显示的内容
  print('check3 is %s %s' % (type(chvarEn.get()), chvarEn.get()))
#创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action = ttk.Button(monty, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)#设置其在界面中出现的位置,column代表列,row 代表行
#文本框
name = tk.StringVar()#StringVar是Tk库内部定义的字符串变量类型
nameEntered = ttk.Entry(monty, width=12, textvariable=name) #创建一个文本框，定义长度为12个字符长度
nameEntered.grid(column=0, row=1, sticky=tk.W) #设置其在界面中出现的位置,column代表列,row代表行
nameEntered.focus()     #当程序运行时,光标默认会出现在该文本框中
#创建一个下拉列表
number = tk.StringVar()
numberChosen = ttk.Combobox(monty, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 42, 100)#设置下拉列表的值
numberChosen.grid(column=1, row=1)      #设置其在界面中出现的位置,column代表列,row 代表行
numberChosen.current(0)    #设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
#复选框
chVarDis = tk.IntVar()#用来获取复选框是否被勾选，其状态值为int类型,勾选为1,未勾选为0
#text为该复选框后面显示的名称, variable将该复选框的状态赋值给一个变量，当state='disabled'时，该复选框为灰色，不能点的状态
check1 = tk.Checkbutton(monty, text="Disabled", variable=chVarDis, state='disabled')
check1.select()     #该复选框是否勾选,select为勾选, deselect为不勾选
check1.grid(column=0, row=4, sticky=tk.W)       #sticky=tk.W(N：北/上对齐,S：南/下对齐,W：西/左对齐,E：东/右对齐)
chvarUn = tk.IntVar()
check2 = tk.Checkbutton(monty, text="UnChecked", variable=chvarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)
chvarEn = tk.IntVar()
check3 = tk.Checkbutton(monty, text="Enabled", variable=chvarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)
#单选按钮
#定义几个颜色的全局变量
colors = ["Blue", "Gold", "Red"]
#单选按钮回调函数,就是当单选按钮被点击会执行该函数
def radCall():
    radSel = radVar.get()
    if radSel == 0:
        window.configure(background=colors[0])#设置整个界面的背景颜色
        print(radVar.get())
    elif radSel == 1:
        window.configure(background=colors[1])
    elif radSel == 2:
        window.configure(background=colors[2])
radVar = tk.IntVar()  #通过tk.IntVar(),获取单选按钮value参数对应的值
radVar.set(99)
for col in range(3):
  #当该单选按钮被点击时，会触发参数command对应的函数
  curRad = tk.Radiobutton(monty, text=colors[col], variable=radVar, value=col, command=radCall)
  curRad.grid(column=col, row=5, sticky=tk.W)     #参数sticky对应的值参考复选框的解释
#滚动文本框
scrolW = 30 #设置文本框的长度
scrolH = 3 #设置文本框的高度
#wrap=tk.WORD这个值表示在行的末尾如果有一个单词跨行，会将该单词放到下一行显示
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)     
scr.grid(column=0, columnspan=3)

window.mainloop()#当调用mainloop()时,窗口才会显示出来


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_21.py

"""
测试OptionMenu(选择项)
用来做多选一，选中的项在顶部显
"""
import tkinter
def show():
    varLabel.set(var.get())
root = tkinter.Tk()
tupleVar = ('python', 'java', 'C', 'C++', 'C#')
var = tkinter.StringVar()
var.set(tupleVar[0])
optionMenu = tkinter.OptionMenu(root, var, *tupleVar)
optionMenu.pack()
varLabel = tkinter.StringVar()
label = tkinter.Label(root, textvariable=varLabel, width=20, height=3, bg='lightblue', fg='red')
label.pack()
button = tkinter.Button(root, text='打印', command=show)
button.pack()
root.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_22.py

import tkinter as tk 
window = tk.Tk()
window.title('窗口菜单')
window.geometry('200x200') 
l = tk.Label(window, text='', bg='blue')
l.pack()
counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter+=1
 
#创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
menubar = tk.Menu(window)
#定义一个空菜单单元
filemenu = tk.Menu(menubar, tearoff=0)
#将上面定义的空菜单命名为`File`，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='文件', menu=filemenu)
#在`File`中加入`New`的小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
#如果点击这些单元, 就会触发`do_job`的功能
filemenu.add_command(label='新建', command=do_job)
filemenu.add_command(label='打开', command=do_job)#同样的在`文件`中加入`打开`小菜单
filemenu.add_command(label='保存', command=do_job)#同样的在`文件`中加入`保存`小菜单
filemenu.add_separator()#这里就是一条分割线
#同样的在`文件`中加入`编辑`小菜单,此处对应命令为`window.quit`
filemenu.add_command(label='编辑', command=window.quit)
 
editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='编辑', menu=editmenu)
editmenu.add_command(label='剪切', command=do_job)
editmenu.add_command(label='复制', command=do_job)
editmenu.add_command(label='粘贴', command=do_job)
#和上面定义菜单一样，不过此处实在`文件`上创建一个空的菜单
submenu = tk.Menu(filemenu)
#给放入的菜单`子菜单`命名为`导入`
filemenu.add_cascade(label='导入', menu=submenu, underline=0)
#这里和上面也一样，在`导入`中加入一个小菜单命令`子菜单1`
submenu.add_command(label="子菜单1", command=do_job)
window.config(menu=menubar) 
window.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_23.py

from tkinter import *
abc = Tk()
abc.title('创建文本框右键菜单')
abc.resizable(False, False)
abc.geometry("300x100+200+20")
Label(abc, text='被生成的文本框').pack(side="top")
Label(abc).pack(side="top")
show = StringVar()
Entry = Entry(abc, textvariable=show, width="30")
Entry.pack() 
class section:
    def onPaste(self):
        try:
            self.text = abc.clipboard_get()
        except TclError:
            pass
        show.set(str(self.text))
 
    def onCopy(self):
        self.text = Entry.get()
        abc.clipboard_append(self.text)
 
    def onCut(self):
        self.onCopy()
        try:
            Entry.delete('sel.first', 'sel.last')
        except TclError:
            pass 
section = section()
menu = Menu(abc, tearoff=0)
menu.add_command(label="复制", command=section.onCopy)
menu.add_separator()
menu.add_command(label="粘贴", command=section.onPaste)
menu.add_separator()
menu.add_command(label="剪切", command=section.onCut) 
 
def popupmenu(event):
    menu.post(event.x_root, event.y_root)
Entry.bind("<Button-3>", popupmenu)
abc.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_24.py

import tkinter
class mybutton:#定义按钮类
	#类初始化canvas1，label1是MyCanvals，mylabel的实例，因此可以使用类中的方法
	def __init__(self,root,canvas1,label1,type):
		self.root=root#保存引用值
		self.canvas1=canvas1
		self.label1=label1
		if type==0:#根据类型创建按钮
			button=tkinter.Button(root,text='画线',command=self.DrawLine)
		elif type==1:
			button=tkinter.Button(root,text='画扇形',command=self.DrawArc)
		elif type==2:
			button=tkinter.Button(root,text='画矩形',command=self.DrawRec)
		else:
			button=tkinter.Button(root,text='画椭圆',command=self.DrawOval)
		button.pack(side='left')
	def DrawLine(self):#DrawLine按钮事件处理函数
		self.label1.text.set('画直线')
		self.canvas1.SetStatus(0)#把status赋值，便于根据status的值进行画图
	def DrawArc(self):
		self.label1.text.set('画弧')
		self.canvas1.SetStatus(1)
	def DrawRec(self):
		self.label1.text.set('画矩形')
		self.canvas1.SetStatus(2)
	def DrawOval(self):
		self.label1.text.set('画椭圆')
		self.canvas1.SetStatus(3)
class MyCanvals:
	def __init__(self,root):
		self.status=0
		self.draw=0
		self.root=root
		self.canvas=tkinter.Canvas(root,bg='yellow',width=600,height=480)#生成canvas组件
		self.canvas.pack()
		self.canvas.bind('<ButtonRelease-1>',self.Draw)#绑定事件到左键
		self.canvas.bind('<Button-2>',self.Exit)#绑定事件到中键
		self.canvas.bind('<Button-3>',self.Del)#绑定事件到右键
		self.canvas.bind_all('<Delete>',self.Del)#绑定事件到delete键
		self.canvas.bind_all('<KeyPress-d>',self.Del)#绑定事件到d键
		self.canvas.bind_all('<KeyPress-e>',self.Exit)#绑定事件到e键
	def Draw(self,event):#绘图事件处理函数
		if self.draw==0:#判断是否绘图，先记录起始位置
			self.x=event.x
			self.y=event.y
			self.draw=1
		else:#根据self.status绘制不同的图形
			if self.status==0:
				self.canvas.create_line(self.x,self.y,event.x,event.y)
				self.draw=0
			elif self.status==1:
				self.canvas.create_arc(self.x,self.y,event.x,event.y)
				self.draw=0
			elif self.status==2:
				self.canvas.create_rectangle(self.x,self.y,event.x,event.y)
				self.draw=0
			else:
				self.canvas.create_oval(self.x,self.y,event.x,event.y)
				self.draw=0
	def Del(self,event):#按下右键或者d键删除图形
		items=self.canvas.find_all()
		for i in items:
			self.canvas.delete(i)
	def Exit(self,event):#按下中键或者e键退出
		self.root.quit()
	def SetStatus(self,status):#设置绘制的图形
		self.status=status
class mylabel:#定义标签类
	def __init__(self,root):
		self.root=root
		self.canvas1=canvas1
		self.text=tkinter.StringVar()#生成标签引用变量
		self.text.set('画线')
		self.label=tkinter.Label(root,textvariable=self.text,fg='blue',width=50)#生成标签
		self.label.pack(side='left')
root=tkinter.Tk()#生成主窗口
canvas1=MyCanvals(root)#生成实例
label1=mylabel(root)#生成实例
mybutton(root,canvas1,label1,0)
mybutton(root,canvas1,label1,1)
mybutton(root,canvas1,label1,2)
mybutton(root,canvas1,label1,3)
root.mainloop()#进入消息循环

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\p18_25.py

from tkinter import *
from tkinter import messagebox
import threading
import random
GAME_WIDTH = 450
GAME_HEIGHT = 650
BOARD_X = 220
BOARD_Y = 600
BOARD_WIDTH = 80
BALL_RADIUS = 9
class App:
    def __init__(self, master):
        self.master = master
        #记录小球动画的第几帧
        self.ball_index = 0
        #记录游戏是否失败的旗标
        self.is_lose = False
        #初始化记录小球位置的变量
        self.curx = 260
        self.cury = 30
        self.boardx = BOARD_X
        self.init_widgets()
        self.vx = random.randint(3, 6) #x方向的速度
        self.vy = random.randint(5, 10) #y方向的速度
        #通过定时器指定0.1秒之后执行moveball函数
        self.t = threading.Timer(0.1, self.moveball)
        self.t.start()
    #创建界面组件
    def init_widgets(self):
        self.cv = Canvas(root, background='white',
            width=GAME_WIDTH, height=GAME_HEIGHT)
        self.cv.pack()
        #让画布得到焦点，从而可以响应按键事件
        self.cv.focus_set()
        self.cv.bms = []
        #初始化小球的动画帧
        for i in range(8):
            self.cv.bms.append(PhotoImage(file='images/ball_' + str(i+1) + '.gif'))
        #绘制小球
        self.ball = self.cv.create_image(self.curx, self.cury,
            image=self.cv.bms[self.ball_index])
        self.board = self.cv.create_rectangle(BOARD_X, BOARD_Y,
            BOARD_X + BOARD_WIDTH, BOARD_Y + 20, width=0, fill='lightblue')
        #为向左箭头按键绑定事件，挡板左移
        self.cv.bind('<Left>', self.move_left)
        #为向右箭头按键绑定事件，挡板右移
        self.cv.bind('<Right>', self.move_right)
    def move_left(self, event):
        if self.boardx <= 0:
            return 
        self.boardx -= 5
        self.cv.coords(self.board, self.boardx, BOARD_Y,
            self.boardx + BOARD_WIDTH, BOARD_Y + 20)
    def move_right(self, event):
        if self.boardx + BOARD_WIDTH >= GAME_WIDTH:
            return
        self.boardx += 5
        self.cv.coords(self.board, self.boardx, BOARD_Y,
            self.boardx + BOARD_WIDTH, BOARD_Y + 20)
    def moveball(self):
        self.curx += self.vx
        self.cury += self.vy
        #小球到了右边墙壁，转向
        if self.curx + BALL_RADIUS >= GAME_WIDTH:
            self.vx = -self.vx
        #小球到了左边墙壁，转向
        if self.curx - BALL_RADIUS <= 0:
            self.vx = -self.vx
        #小球到了上边墙壁，转向
        if self.cury - BALL_RADIUS <= 0:
            self.vy = -self.vy
        #小球到了挡板处
        if self.cury + BALL_RADIUS >= BOARD_Y:
            #如果在挡板范围内
            if self.boardx <= self.curx <= (self.boardx + BOARD_WIDTH):
                self.vy = -self.vy
            else:
                messagebox.showinfo(title='失败', message='您已经输了')
                self.is_lose = True
        self.cv.coords(self.ball, self.curx, self.cury)
        self.ball_index += 1
        self.cv.itemconfig(self.ball, image=self.cv.bms[self.ball_index % 8])
        #如果游戏还未失败，让定时器继续执行
        if not self.is_lose:
            #通过定时器指定0.1秒之后执行moveball函数
            self.t = threading.Timer(0.1, self.moveball)
            self.t.start()
root = Tk()
root.title("弹球游戏")
root.geometry('%dx%d' % (GAME_WIDTH, GAME_HEIGHT))  
#禁止改变窗口大小
root.resizable(width=False, height=False)
App(root)
root.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\Frame_test.py

from tkinter import * 
#定义继承Frame的Application类
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        #调用initWidgets()方法初始化界面
        self.initWidgets()
    def initWidgets(self):
        #创建Label对象，第一个参数指定该Label放入root
        w = Label(self)
        #创建一个位图
        bm = PhotoImage(file = 'images/a.png')
        #必须用一个不会被释放的变量引用该图片，否则该图片会被回收
        w.x = bm
        # 设置显示的图片是bm
        w['image'] = bm
        w.pack()
        #创建Button对象，第一个参数指定该Button放入root
        okButton = Button(self, text="确定")
        okButton.configure(background='red')
        okButton.pack()
#创建Application对象
app = Application()
#Frame有个默认的master属性，该属性值是Tk对象（窗口）
print(type(app.master))
#通过master属性来设置窗口标题
app.master.title('窗口标题')
#启动主窗口的消息循环
app.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\一本書秒殺電腦視覺最新應用：80個Python大師級實例(第二版)\18\Frame_test2.py

from tkinter import *  
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 创建第一个容器
        fm1 = Frame(self.master)
        # 该容器放在左边排列
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)
        # 向fm1中添加3个按钮
        # 设置按钮从顶部开始排列，且按钮只能在垂直（X）方向填充
        Button(fm1, text='第一个').pack(side=TOP, fill=X, expand=YES)
        Button(fm1, text='第二个').pack(side=TOP, fill=X, expand=YES)
        Button(fm1, text='第三个').pack(side=TOP,  fill=X, expand=YES)
        # 创建第二个容器
        fm2 = Frame(self.master)
        # 该容器放在左边排列，就会挨着fm1
#        fm2.pack(side=LEFT, padx=10, expand=YES)
        fm2.pack(side=LEFT, padx=10, fill=BOTH, expand=YES)
        # 向fm2中添加3个按钮
        # 设置按钮从右边开始排列
        Button(fm2, text='第一个').pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text='第二个').pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text='第三个').pack(side=RIGHT, fill=Y, expand=YES)        
        # 创建第三个容器
        fm3 = Frame(self.master)
        # 该容器放在右边排列，就会挨着fm1
        fm3.pack(side=RIGHT, padx=10, fill=BOTH, expand=YES)
        # 向fm3中添加3个按钮
        # 设置按钮从底部开始排列，且按钮只能在垂直（Y）方向填充
        Button(fm3, text='第一个').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='第二个').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='第三个').pack(side=BOTTOM, fill=Y, expand=YES) 
root = Tk()
root.title("Pack布局")
display = App(root)
root.mainloop()

print("------------------------------------------------------------")  # 60個




