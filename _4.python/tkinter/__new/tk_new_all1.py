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
'''



print("------------------------------------------------------------")  # 60個

from tkinter import * # Import tkinter
    
class PopupMenuDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Popup Menu Demo") # Set title

        # Create a popup menu
        self.menu = Menu(window, tearoff = 0)
        self.menu.add_command(label = "Draw a line", 
            command = self.displayLine)
        self.menu.add_command(label = "Draw an oval", 
            command = self.displayOval)
        self.menu.add_command(label = "Draw a rectangle", 
            command = self.displayRect)
        self.menu.add_command(label = "Clear", 
            command = self.clearCanvas)
        
        # Place canvas in window
        self.canvas = Canvas(window, width = 200, 
            height = 100, bg = "white")
        self.canvas.pack()
        
        # Bind popup to canvas
        self.canvas.bind("<Button-3>", self.popup)
        
        window.mainloop() # Create an event loop
        
    # Display a rectangle
    def displayRect(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect")
        
    # Display an oval
    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 90, tags = "oval")
    
    # Display a line
    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 90, tags = "line")
        self.canvas.create_line(10, 90, 190, 10, tags = "line")
    
    # Clear drawings
    def clearCanvas(self):
        self.canvas.delete("rect", "oval", "line")

    def popup(self, event):
        self.menu.post(event.x_root, event.y_root)

print('右鍵選單')    
PopupMenuDemo() # Create GUI


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
