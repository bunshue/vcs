import sys

from tkinter import *

print('------------------------------------------------------------')	#60個

def printSelection():
    num = var.get()
    if num == 1:
        label.config(text="你是男生")
    else:
        label.config(text="你是女生")

root = Tk()
root.title("ch7_1")                             # 視窗標題

var = IntVar()                                  # 選項紐綁定的變數
var.set(1)                                      # 預設選項是男生
                       
label = Label(root,text="這是預設,尚未選擇", bg="lightyellow",width=30)
label.pack()

rbman = Radiobutton(root,text="男生",           # 男生選項鈕
                    variable=var,value=1,
                    command=printSelection)
rbman.pack()
rbwoman = Radiobutton(root,text="女生",         # 女生選項鈕
                      variable=var,value=2,
                      command=printSelection)
rbwoman.pack()

root.mainloop()







#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch07\ch7_2.py

# ch7_2.py
from tkinter import *
def printSelection():
    label.config(text="你是"+var.get())

root = Tk()
root.title("ch7_2")                             # 視窗標題

var = StringVar()                               # 選項紐綁定的變數
var.set("男生")                                 # 預設選項是男生
                       
label = Label(root,text="這是預設,尚未選擇", bg="lightyellow",width=30)
label.pack()

rbman = Radiobutton(root,text="男生",           # 男生選項鈕
                    variable=var,value="男生",
                    command=printSelection)
rbman.pack()
rbwoman = Radiobutton(root,text="女生",         # 女生選項鈕
                      variable=var,value="女生",
                      command=printSelection)
rbwoman.pack()

root.mainloop()







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch07\ch7_3.py

# ch7_3.py
from tkinter import *
def printSelection():
    print(cities[var.get()])            # 列出所選城市

root = Tk()
root.title("ch7_3")                     # 視窗標題
cities = {0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"香港"}

var = IntVar()
var.set(0)                              # 預設選項                       
label = Label(root,text="選擇最喜歡的城市",
              fg="blue",bg="lightyellow",width=30).pack()

for val, city in cities.items():        # 建立選項紐    
    Radiobutton(root,
                text=city,
                variable=var,value=val, 
                command=printSelection).pack()

root.mainloop()







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch07\ch7_4.py

# ch7_4.py
from tkinter import *
def printSelection():
    print(cities[var.get()])            # 列出所選城市

root = Tk()
root.title("ch7_4")                     # 視窗標題
cities = {0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"香港"}

var = IntVar()
var.set(0)                              # 預設選項                       
label = Label(root,text="選擇最喜歡的城市",
              fg="blue",bg="lightyellow",width=30).pack()

for val, city in cities.items():        # 建立選項紐    
    Radiobutton(root,
                text=city,
                indicatoron = 0,        # 用盒子取代選項紐
                width=30,
                variable=var,value=val,
                command=printSelection).pack()

root.mainloop()







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch07\ch7_5.py

# ch7_5.py
from tkinter import *
def printSelection():
    label.config(text="你選的是"+var.get())

root = Tk()
root.title("ch7_5")                             # 視窗標題

imgStar = PhotoImage(file="star.gif")
imgMoon = PhotoImage(file="moon.gif")
imgSun = PhotoImage(file="sun.gif")

var = StringVar()                               # 選項紐綁定的變數
var.set("星星")                                 # 預設選項是男生
                       
label = Label(root,text="這是預設,尚未選擇", bg="lightyellow",width=30)
label.pack()

rbStar = Radiobutton(root,image=imgStar,        # 星星選項鈕
                     variable=var,value="星星",
                     command=printSelection)
rbStar.pack()
rbMoon = Radiobutton(root,image=imgMoon,        # 月亮選項鈕
                     variable=var,value="月亮",
                     command=printSelection)
rbMoon.pack()
rbSun = Radiobutton(root,image=imgSun,          # 太陽選項鈕
                    variable=var,value="太陽",
                    command=printSelection)
rbSun.pack()

root.mainloop()







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch07\ch7_6.py

# ch7_6.py
from tkinter import *
def printSelection():
    label.config(text="你選的是"+var.get())

root = Tk()
root.title("ch7_6")                             # 視窗標題

imgStar = PhotoImage(file="star.gif")
imgMoon = PhotoImage(file="moon.gif")
imgSun = PhotoImage(file="sun.gif")

var = StringVar()                               # 選項紐綁定的變數
var.set("星星")                                 # 預設選項是男生
                       
label = Label(root,text="這是預設,尚未選擇", bg="lightyellow",width=30)
label.pack()

rbStar = Radiobutton(root,image=imgStar,        # 星星選項鈕
                     text="星星",compound=RIGHT,
                     variable=var,value="星星",
                     command=printSelection)
rbStar.pack()
rbMoon = Radiobutton(root,image=imgMoon,        # 月亮選項鈕
                     text="月亮",compound=RIGHT,
                     variable=var,value="月亮",
                     command=printSelection)
rbMoon.pack()
rbSun = Radiobutton(root,image=imgSun,          # 太陽選項鈕
                    text="太陽",compound=RIGHT,
                    variable=var,value="太陽",
                    command=printSelection)
rbSun.pack()

root.mainloop()







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch07\ch7_7.py

# ch7_7.py
from tkinter import *

root = Tk()
root.title("ch7_7")                   # 視窗標題

lab = Label(root,text="請選擇喜歡的運動",fg="blue",bg="lightyellow",width=30)
lab.grid(row=0)

var1 = IntVar()                      
cbtnNFL = Checkbutton(root,text="美式足球",variable=var1)
cbtnNFL.grid(row=1,sticky=W)

var2 = IntVar()
cbtnMLB = Checkbutton(root,text="棒球",variable=var2)
cbtnMLB.grid(row=2,sticky=W)

var3 = IntVar()
cbtnNBA = Checkbutton(root,text="籃球",variable=var3)
cbtnNBA.grid(row=3,sticky=W)   

root.mainloop()







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch07\ch7_8.py

# ch7_8.py
from tkinter import *

def printInfo():
    selection = ''
    for i in checkboxes:                    # 檢查此字典
        if checkboxes[i].get() == True:     # 被選取則執行
            selection = selection + sports[i] + "\t"
    print(selection)

root = Tk()
root.title("ch7_8")                         # 視窗標題

Label(root,text="請選擇喜歡的運動",
      fg="blue",bg="lightyellow",width=30).grid(row=0)

sports = {0:"美式足球",1:"棒球",2:"籃球",3:"網球"}    # 運動字典
checkboxes = {}                             # 字典存放被選取項目
for i in range(len(sports)):                # 將運動字典轉成核取方塊
    checkboxes[i] = BooleanVar()            # 布林變數物件
    Checkbutton(root,text=sports[i],
                variable=checkboxes[i]).grid(row=i+1,sticky=W)
  
btn = Button(root,text="確定",width=10,command=printInfo)
btn.grid(row=i+2)

root.mainloop()







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch07\ch7_9.py

# ch7_9.py
from tkinter import *
# 以下是callback方法
def selAll():                               # 選取全部字串
    entry.select_range(0,END)
def deSel():                                # 取消選取
    entry.select_clear()
def clr():                                  # 刪除文字
    entry.delete(0,END)
def readonly():                             # 設定Entry狀態
    if var.get() == True:
        entry.config(state=DISABLED)        # 設為DISABLED
    else:
        entry.config(state=NORMAL)          # 設為NORMAL

root = Tk()
root.title("ch7_9")                         # 視窗標題

# 以下row=0建立Entry
entry = Entry(root)
entry.grid(row=0,column=0,columnspan=4,
           padx=5,pady=5,sticky=W)
# 以下row=1建立Button
btnSel = Button(root,text="選取",command=selAll)
btnSel.grid(row=1,column=0,padx=5,pady=5,sticky=W)
btnDesel = Button(root,text="取消選取",command=deSel)
btnDesel.grid(row=1,column=1,padx=5,pady=5,sticky=W)
btnClr = Button(root,text="刪除",command=clr)
btnClr.grid(row=1,column=2,padx=5,pady=5,sticky=W)
btnQuit = Button(root,text="結束",command=root.destroy)
btnQuit.grid(row=1,column=3,padx=5,pady=5,sticky=W)
# 以下row=2建立Checkboxes
var = BooleanVar()
var.set(False)
chkReadonly = Checkbutton(root,text="唯讀",variable=var,
                          command=readonly)
chkReadonly.grid(row=2,column=0)

root.mainloop()







print('------------------------------------------------------------')	#60個




import sys

from tkinter import Tk
from tkinter.ttk import Frame, Style
from tkinter import *

print('------------------------------------------------------------')	#60個

root = Tk()

for fm in ["red","green","blue"]:    # 建立3個不同底色的框架
    Frame(root,bg=fm,height=50,width=250).pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

for fm in ["red","green","blue"]:    # 建立3個不同底色的框架
    Frame(bg=fm,height=50,width=250).pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

# 用字典儲存框架顏色與游標外形
fms = {'red':'cross','green':'boat','blue':'clock'}
for fmColor in fms:         # 建立3個不同底色的框架與游標外形
    Frame(root,bg=fmColor,cursor=fms[fmColor],
          height=50,width=200).pack(side=LEFT)

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

frameUpper = Frame(root,bg="lightyellow")   # 建立上層框架
frameUpper.pack()
btnRed = Button(frameUpper,text="Red",fg="red")
btnRed.pack(side=LEFT,padx=5,pady=5)
btnGreen = Button(frameUpper,text="Green",fg="green")
btnGreen.pack(side=LEFT,padx=5,pady=5)
btnBlue = Button(frameUpper,text="Blue",fg="blue")
btnBlue.pack(side=LEFT,padx=5,pady=5)

frameLower = Frame(root,bg="lightblue")     # 建立下層框架
frameLower.pack()
btnPurple = Button(frameLower,text="Purple",fg="purple")
btnPurple.pack(side=LEFT,padx=5,pady=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

fm1 = Frame(width=150,height=80,relief=GROOVE, borderwidth=5)
fm1.pack(side=LEFT,padx=5,pady=10)

fm2 = Frame(width=150,height=80,relief=RAISED, borderwidth=5)
fm2.pack(side=LEFT,padx=5,pady=10)

fm3 = Frame(width=150,height=80,relief=RIDGE, borderwidth=5)
fm3.pack(side=LEFT,padx=5,pady=10)

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

fm = Frame(width=150,height=80,relief=RAISED,borderwidth=5) # 建立框架
lab = Label(fm,text="請複選常用的程式語言")     # 建立標籤
lab.pack()
python = Checkbutton(fm,text="Python")          # 建立phthon核取方塊          
python.pack(anchor=W)
java = Checkbutton(fm,text="Java")              # 建立java核取方塊
java.pack(anchor=W)
ruby = Checkbutton(fm,text="Ruby")              # 建立ruby核取方塊
ruby.pack(anchor=W)
fm.pack(padx=10,pady=10)                        # 包裝框架

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

style = Style()                 # 改用Style
style.theme_use("alt")          # 改用alt支援Style

fm1 = Frame(root,width=150,height=80,relief="flat")
fm1.grid(row=0,column=0,padx=5,pady=5)

fm2 = Frame(root,width=150,height=80,relief="groove")
fm2.grid(row=0,column=1,padx=5,pady=5)

fm3 = Frame(root,width=150,height=80,relief="raised")
fm3.grid(row=0,column=2,padx=5,pady=5)

fm4 = Frame(root,width=150,height=80,relief="ridge")
fm4.grid(row=1,column=0,padx=5,pady=5)

fm5 = Frame(root,width=150,height=80,relief="solid")
fm5.grid(row=1,column=1,padx=5,pady=5)

fm6 = Frame(root,width=150,height=80,relief="sunken")
fm6.grid(row=1,column=2,padx=5,pady=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

msg = "歡迎進入Silicon Stone Educaiton系統"
sseGif = PhotoImage(file="sse.gif")         # Logo影像檔
logo = Label(root,image=sseGif,text=msg,compound=BOTTOM)
logo.pack()

# 以下是LabelFrame標籤框架
labFrame = LabelFrame(root,text="資料驗證") # 建立標籤框架
accountL = Label(labFrame,text="Account")   # account標籤
accountL.grid(row=0,column=0)
pwdL = Label(labFrame,text="Password")      # pwd標籤
pwdL.grid(row=1,column=0)

accountE = Entry(labFrame)                  # 文字方塊account
accountE.grid(row=0,column=1)               # 定位文字方塊account
pwdE = Entry(labFrame,show="*")             # 文字方塊pwd
pwdE.grid(row=1,column=1,pady=10)           # 定位文字方塊pwd
labFrame.pack(padx=10,pady=5,ipadx=5,ipady=5)   # 包裝與定位標籤框架

root.mainloop()

print('------------------------------------------------------------')	#60個

def printInfo():
    selection = ''
    for i in checkboxes:                    # 檢查此字典
        if checkboxes[i].get() == True:     # 被選取則執行
            selection = selection + sports[i] + "\t"
    print(selection)

root = Tk()

root.geometry("400x220")
# 以下建立標籤框架與和曲方塊
labFrame = LabelFrame(root,text="選擇最喜歡的運動")
sports = {0:"美式足球",1:"棒球",2:"籃球",3:"網球"}    # 運動字典
checkboxes = {}                             # 字典存放被選取項目
for i in range(len(sports)):                # 將運動字典轉成核取方塊
    checkboxes[i] = BooleanVar()            # 布林變數物件
    Checkbutton(labFrame,text=sports[i],
                variable=checkboxes[i]).grid(row=i+1,sticky=W)
labFrame.pack(ipadx=5,ipady=5,pady=10)      # 包裝定位標籤框架

btn = Button(root,text="確定",width=10,command=printInfo)
btn.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

tl = Toplevel()
Label(tl,text = 'I am a Toplevel').pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

tl = Toplevel()
tl.title("Toplevel")
tl.geometry("300x180")
Label(tl,text = 'I am a Toplevel').pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

import random

root = Tk()

msgYes, msgNo, msgExit = 1,2,3
def MessageBox():                   # 建立對話方塊
    msgType = random.randint(1,3)   # 隨機數產生對話方塊方式
    if msgType == msgYes:           # 產生Yes字串
        labTxt = 'Yes'
    elif msgType == msgNo:          # 產生No字串
        labTxt = 'No'
    elif msgType == msgExit:        # 產生Exit字串
        labTxt = 'Exit'    
    tl = Toplevel()                 # 建立Toplevel視窗
    tl.geometry("300x180")          # 建立對話方塊大小
    tl.title("Message Box")
    Label(tl,text=labTxt).pack(fill=BOTH,expand=True)

btn = Button(root,text='Click Me',command = MessageBox)
btn.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

import math

def paintTree(depth, x1, y1, length, angle):
    if depth >= 0:
        depth -= 1
        x2 = x1 + int(math.cos(angle) * length)
        y2 = y1 - int(math.sin(angle) * length)
        # 繪線
        drawLine(x1, y1, x2, y2)
        # 繪左邊
        paintTree(depth,x2, y2, length*sizeRatio, angle+angleValue)
        # 繪右邊
        paintTree(depth, x2, y2, length*sizeRatio, angle-angleValue)
        
# 繪製p1和p2之間的線條
def drawLine(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2,tags="myline")

# 顯示
def show():
    canvas.delete("myline")
    myDepth = depth.get()
    paintTree(myDepth, myWidth/2, myHeight, myHeight/3, math.pi/2)
    
# main
tk = Tk()
myWidth = 400
myHeight = 400
canvas = Canvas(tk, width=myWidth, height=myHeight) # 建立畫布
canvas.pack()

frame = Frame(tk)                               # 建立框架
frame.pack(padx=5, pady=5)
# 在框架Frame內建立標籤Label, 輸入depth數Entry, 按鈕Button
Label(frame, text="輸入depth : ").pack(side=LEFT)
depth = IntVar()
depth.set(0)
entry = Entry(frame, textvariable=depth).pack(side=LEFT,padx=3)
Button(frame, text="Recursive Tree",
       command=show).pack(side=LEFT)
angleValue = math.pi / 4                       # 設定角度
sizeRatio = 0.6                                 # 設定下一層的長度與前一層的比率是0.6

tk.mainloop()



print('------------------------------------------------------------')	#60個



import sys

from tkinter import *

print('------------------------------------------------------------')	#60個

root = Tk()
root.title("ch10_1")

myText = "2016年12月,我一個人訂了機票和船票,開始我的南極旅行"
msg = Message(root,bg="yellow",text=myText,
              font="times 12 italic")
msg.pack(padx=10,pady=10)

root.mainloop()





#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch10\ch10_2.py

# ch10_2.py
from tkinter import *

root = Tk()
root.title("ch10_2")

var = StringVar()
msg = Message(root,textvariable=var,relief=RAISED)
var.set("2016年12月,我一個人訂了機票和船票,開始我的南極旅行")
msg.pack(padx=10,pady=10)

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch10\ch10_3.py

# ch10_3.py
from tkinter import *

root = Tk()
root.title("ch10_3")

var = StringVar()
msg = Message(root,textvariable=var,relief=RAISED)
var.set("2016年12月,我一個人訂了機票和船票,開始我的南極旅行")
msg.config(bg="yellow")
msg.pack(padx=10,pady=10)

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch10\ch10_4.py

# ch10_4.py
from tkinter import *
from tkinter import messagebox

def myMsg():                    # 按Good Morning按鈕時執行
    messagebox.showinfo("My Message Box","Python tkinter早安")
    
window = Tk()
window.title("ch10_4")          # 視窗標題
window.geometry("300x160")      # 視窗寬300高160

Button(window,text="Good Morning",command=myMsg).pack()

window.mainloop()







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch10\ch10_5.py

# ch10_5.py
from tkinter import *
from tkinter import messagebox

def myMsg1():
    ret = messagebox.askretrycancel("Test1","安裝失敗,再試一次?")
    print("安裝失敗",ret)
def myMsg2():
    ret = messagebox.askyesnocancel("Test2","編輯完成,是或否或取消?")
    print("編輯完成",ret)
root = Tk()
root.title("ch10_5")          # 視窗標題

Button(root,text="安裝失敗",command=myMsg1).pack()
Button(root,text="編輯完成",command=myMsg2).pack()

root.mainloop()







print('------------------------------------------------------------')	#60個



import sys

from tkinter import *

print('------------------------------------------------------------')	#60個

from tkinter import *
def pythonClicked():            # Python核取方塊事件處理程式     
    if varPython.get():
        lab.config(text="選取Python")
    else:
        lab.config(text="取消選取Python")
def javaClicked():              # Java核取方塊事件處理程式
    if varJava.get():
        lab.config(text="選取Java")
    else:
        lab.config(text="取消選取Java")
def buttonClicked():            # Button按鈕事件處理程式
    lab.config(text="Button clicked")
    
root = Tk()
root.title("ch11_1")            # 視窗標題
root.geometry("300x180")        # 視窗寬300高160

btn = Button(root,text="Click me",command=buttonClicked)
btn.pack(anchor=W)
varPython = BooleanVar()
cbnPython = Checkbutton(root,text="Python",variable=varPython,
                        command=pythonClicked)
cbnPython.pack(anchor=W)
varJava = BooleanVar()
cbnJava = Checkbutton(root,text="Java",variable=varJava,
                      command=javaClicked)
cbnJava.pack(anchor=W)
lab = Label(root,bg="yellow",fg="blue",
            height=2,width=12,
            font="Times 16 bold")
lab.pack()

root.mainloop()





#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_1_1.py

# ch11_1_1.py
from tkinter import *
def pythonClicked():            # Python核取方塊事件處理程式     
    if varPython.get():
        lab.config(text="選取Python")
    else:
        lab.config(text="取消選取Python")
def javaClicked():              # Java核取方塊事件處理程式
    if varJava.get():
        lab.config(text="選取Java")
    else:
        lab.config(text="取消選取Java")
def buttonClicked(event):       # Button按鈕事件處理程式
    lab.config(text="Button clicked")
    
root = Tk()
root.title("ch11_1_1")          # 視窗標題
root.geometry("300x180")        # 視窗寬300高160

btn = Button(root,text="Click me")
btn.pack(anchor=W)
btn.bind("<Button-1>",buttonClicked)  # 按一下Click me綁定buttonClicked方法

varPython = BooleanVar()
cbnPython = Checkbutton(root,text="Python",variable=varPython,
                        command=pythonClicked)
cbnPython.pack(anchor=W)
varJava = BooleanVar()
cbnJava = Checkbutton(root,text="Java",variable=varJava,
                      command=javaClicked)
cbnJava.pack(anchor=W)
lab = Label(root,bg="yellow",fg="blue",
            height=2,width=12,
            font="Times 16 bold")
lab.pack()

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_2.py

# ch11_2.py
from tkinter import *
def callback(event):                        # 事件處理程式
    print("Clicked at", event.x, event.y)   # 列印座標
    
root = Tk()
root.title("ch11_2")
frame = Frame(root,width=300,height=180)
frame.bind("<Button-1>",callback)           # 按一下綁定callback
frame.pack()

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_2_1.py

# ch11_2_1.py
from tkinter import *
def mouseMotion(event):             # Mouse移動
    x = event.x
    y = event.y
    textvar = "Mouse location - x:{}, y:{}".format(x,y)
    var.set(textvar)
    
root = Tk()
root.title("ch11_2_1")              # 視窗標題
root.geometry("300x180")            # 視窗寬300高180

x, y = 0, 0                         # x,y座標
var = StringVar()
text = "Mouse location - x:{}, y:{}".format(x,y)
var.set(text)

lab = Label(root,textvariable=var)  # 建立標籤
lab.pack(anchor=S,side=RIGHT,padx=10,pady=10)

root.bind("<Motion>",mouseMotion)   # 增加事件處理程式

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_3.py

# ch11_3.py
from tkinter import *
def enter(event):                       # Enter事件處理程式
    x.set("滑鼠進入Exit功能鈕")   
def leave(event):                       # Leave事件處理程式
    x.set("滑鼠離開Exit功能鈕")
    
root = Tk()
root.title("ch11_3")
root.geometry("300x180")

btn = Button(root,text="離開",command=root.destroy)
btn.pack(pady=30)
btn.bind("<Enter>",enter)               # 進入綁定enter
btn.bind("<Leave>",leave)               # 離開綁定leave

x = StringVar()
lab = Label(root,textvariable=x,        # 標籤區域
            bg="yellow",fg="blue",
            height = 4, width=15,
            font="Times 12 bold")
lab.pack(pady=30)

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_4.py

# ch11_4.py
from tkinter import *
from tkinter import messagebox

def leave(event):                       # <Esc>事件處理程式
    ret = messagebox.askyesno("ch11_4","是否離開?")
    if ret == True:
        root.destroy()                  # 結束程式
    else:
        return
   
root = Tk()
root.title("ch11_4")

root.bind("<Escape>",leave)             # Esc鍵綁定leave函數
lab = Label(root,text="測試Esc鍵",      # 標籤區域
            bg="yellow",fg="blue",
            height = 4, width=15,
            font="Times 12 bold")
lab.pack(padx=30,pady=30)

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_5.py

# ch11_5.py
from tkinter import *
def key(event):                     # 處理鍵盤按a ... z
    print("按了 " + repr(event.char) + " 鍵") 
   
root = Tk()
root.title("ch11_5")

root.bind("<Key>",key)              # <Key>鍵綁定key函數

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_6.py

# ch11_6.py
from tkinter import *
def key(event):                     # 列出所按的鍵
    print("按了 " + repr(event.char) + " 鍵")

def coordXY(event):                 # 列出滑鼠座標
    frame.focus_set()               # frame物件取得焦點
    print("滑鼠座標 : ", event.x, event.y)
    
root = Tk()
root.title("ch11_6")

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)            # frame物件的<Key>綁定key
frame.bind("<Button-1>", coordXY)   # frame物件按一下綁定coordXY
frame.pack()

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_7.py

# ch11_7.py
from tkinter import *
def buttonClicked(event):           # Button按鈕事件處理程式
    print("I like tkinter")

# 所傳遞的物件onoff是btn物件    
def toggle(onoff):                  # 切換綁定
    if var.get() == True:           # 如果True綁定
        onoff.bind("<Button-1>",buttonClicked)
    else:                           # 如果False不綁定
        onoff.unbind("<Button-1>")
    
root = Tk()
root.title("ch11_7")                # 視窗標題
root.geometry("300x180")            # 視窗寬300高180

btn = Button(root,text="tkinter")   # 建立按鈕tkinter
btn.pack(anchor=W,padx=10,pady=10)

var = BooleanVar()                  # 建立核取方塊
cbtn = Checkbutton(root,text="bind/unbind",variable=var,
                   command=lambda:toggle(btn))
cbtn.pack(anchor=W,padx=10)

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_8.py

# ch11_8.py
from tkinter import *
def btnClicked1():                  # Button按鈕事件處理程式1
    print("Command event handler, I like tkinter")
def btnClicked2(event):             # Button按鈕事件處理程式2
    print("Bind event handler, I like tkinter")
    
root = Tk()
root.title("ch11_8")                # 視窗標題
root.geometry("300x180")            # 視窗寬300高180

btn = Button(root,text="tkinter",   # 建立按鈕tkinter
             command=btnClicked1)
btn.pack(anchor=W,padx=10,pady=10)
btn.bind("<Button-1>",btnClicked2,add="+")  # 增加事件處理程式

root.mainloop()









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch11\ch11_9.py

# ch11_9.py
from tkinter import *
from tkinter import messagebox

def callback():
    res = messagebox.askokcancel("OKCANCEL","結束或取消?")
    if res == True:
        root.destroy()
    else:
        return
    
root = Tk()
root.title("ch11_9")
root.geometry("300x180")
root.protocol("WM_DELETE_WINDOW",callback)  # 更改協定綁定

root.mainloop()









print('------------------------------------------------------------')	#60個




"""
使用 PanedWindow()

"""
import sys

from tkinter import *

print('------------------------------------------------------------')	#60個

pw = PanedWindow(orient=VERTICAL)       # 建立PanedWindow物件
pw.pack(fill=BOTH,expand=True)

top = Label(pw,text="Top Pane")         # 建立標籤Top Pane
pw.add(top)                             # top標籤插入PanedWindow

bottom = Label(pw,text="Bottom Pane")   # 建立標籤Bottom Pane
pw.add(bottom)                          # bottom標籤插入PanedWindow

pw.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

root = Tk()
root.title("")

pw = PanedWindow(orient=HORIZONTAL)     # 建立PanedWindow物件

leftframe = LabelFrame(pw,text="Left Pane",width=120,height=150)
pw.add(leftframe)                       # 插入左邊LabelFrame
middleframe = LabelFrame(pw,text="Middle Pane",width=120)
pw.add(middleframe)                     # 插入中間LabelFrame
rightframe = LabelFrame(pw,text="Right Pane",width=120)
pw.add(rightframe)                      # 插入右邊LabelFrame

pw.pack(fill=BOTH,expand=True,padx=10,pady=10)     

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("")

pw = PanedWindow(orient=HORIZONTAL)     # 建立PanedWindow物件

leftframe = LabelFrame(pw,text="Left Pane",width=120,height=150)
pw.add(leftframe,weight=1)              # 插入左邊LabelFrame
middleframe = LabelFrame(pw,text="Middle Pane",width=120)
pw.add(middleframe,weight=1)            # 插入中間LabelFrame
rightframe = LabelFrame(pw,text="Right Pane",width=120)
pw.add(rightframe,weight=1)             # 插入右邊LabelFrame

pw.pack(fill=BOTH,expand=True,padx=10,pady=10)     

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("")

pw = PanedWindow(orient=HORIZONTAL)     # 建立PanedWindow物件

leftframe = LabelFrame(pw,text="Left Pane",width=120,height=150)
pw.add(leftframe,weight=2)              # 插入左邊LabelFrame
middleframe = LabelFrame(pw,text="Middle Pane",width=120)
pw.add(middleframe,weight=2)            # 插入中間LabelFrame
rightframe = LabelFrame(pw,text="Right Pane",width=120)
pw.add(rightframe,weight=1)             # 插入右邊LabelFrame

pw.pack(fill=BOTH,expand=True,padx=10,pady=10)     

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

pw = PanedWindow(orient=HORIZONTAL)     # 建立外層PanedWindow
pw.pack(fill = BOTH,expand=True)

entry = Entry(pw,bd=3)                  # 建立entry            
pw.add(entry)                           # 這是外層PanedWindow的子物件

# 建立PanedWindow物件pwin,這是外層PanedWindow的子物件
pwin = PanedWindow(pw,orient=VERTICAL)  
pw.add(pwin)                            
# 建立Scale,這是pwin物件的子物件
scale = Scale(pwin,orient=HORIZONTAL)   
pwin.add(scale)                         

pw.mainloop()

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個




import sys

from tkinter import *

print('------------------------------------------------------------')	#60個

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("300x140")
root.title("ch15_1")

# 使用預設建立進度條
pb1 = Progressbar(root)
pb1.pack(pady=20)
pb1["maximum"] = 100
pb1["value"] = 50

# 使用各參數設定方式建立進度條
pb2 = Progressbar(root,orient=HORIZONTAL,length=200,mode ="determinate")
pb2.pack(pady=20)
pb2["maximum"] = 100
pb2["value"] = 50

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *
from tkinter.ttk import *
import time
 
def running():                      # 開始Progressbar動畫
    for i in range(100):
        pb["value"] = i+1           # 每次更新1
        root.update()               # 更新畫面
        time.sleep(0.05)
 
root = Tk()
root.title("ch15_2")

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["maximum"] = 100
pb["value"] = 0
 
btn = Button(root,text="Running",command=running)
btn.pack(pady=10)

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *
from tkinter.ttk import *
 
def load():                         # 啟動Prograssbar
    pb["value"] = 0                 # Prograssbar初始值
    pb["maximum"] = maxbytes        # Prograddbar最大值
    loading()
def loading():                      # 模擬下載資料
    global bytes
    bytes += 500                    # 模擬每次下在500bytes
    pb["value"] = bytes             # 設定指針
    if bytes < maxbytes:
        pb.after(50,loading)        # 經過0.05秒繼續執行loading
 
root = Tk()
root.title("ch15_3")
bytes = 0                           # 設定初值
maxbytes = 10000                    # 假設下載檔案大小    

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["value"] = 0                     # Prograssbar初始值
 
btn = Button(root,text="Load",command=load)
btn.pack(pady=10)

root.mainloop()


print('------------------------------------------------------------')	#60個

from tkinter import *
from tkinter.ttk import *
import time
 
def running():                      # 開始Progressbar動畫
    while pb.cget("value") <= pb["maximum"]:        
        pb.step(2)
        root.update()               # 更新畫面
        print(pb.cget("value"))     # 列印指針值
        time.sleep(0.05)
 
root = Tk()
root.title("ch15_4")

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["maximum"] = 100
pb["value"] = 0
 
btn = Button(root,text="Running",command=running)
btn.pack(pady=10)

root.mainloop()


print('------------------------------------------------------------')	#60個

from tkinter import *
from tkinter.ttk import *
 
def run():                                      # 開始Progressbar動畫
    pb.start()                                  # 指針每次移動1
def stop():                                     # 中止Progressbar動畫
    pb.stop()                                   # 中止pb物件動畫
 
root = Tk()
root.title("ch15_5")

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=5,pady=10)
pb["maximum"] = 100
pb["value"] = 0
 
btnRun = Button(root,text="Run",command=run)    # 建立Run按鈕
btnRun.pack(side=LEFT,padx=5,pady=10)

btnStop = Button(root,text="Stop",command=stop) # 建立Stop按鈕
btnStop.pack(side=LEFT,padx=5,pady=10)

root.mainloop()


print('------------------------------------------------------------')	#60個

from tkinter import *
from tkinter.ttk import *
 
def run():                                      # 開始Progressbar動畫
    pb.start()                                  # 指針每次移動1
def stop():                                     # 中止Progressbar動畫
    pb.stop()                                   # 中止pb物件動畫
 
root = Tk()
root.title("aaaa")

pb = Progressbar(root,length=200,mode="indeterminate",orient=HORIZONTAL)
pb.pack(padx=5,pady=10)
pb["maximum"] = 100
pb["value"] = 0
 
btnRun = Button(root,text="Run",command=run)    # 建立Run按鈕
btnRun.pack(side=LEFT,padx=5,pady=10)

btnStop = Button(root,text="Stop",command=stop) # 建立Stop按鈕
btnStop.pack(side=LEFT,padx=5,pady=10)

root.mainloop()

print('------------------------------------------------------------')	#60個








print('------------------------------------------------------------')	#60個




