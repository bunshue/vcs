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






print('------------------------------------------------------------')	#60個

