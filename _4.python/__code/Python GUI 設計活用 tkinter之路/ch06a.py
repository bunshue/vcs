import sys

from tkinter import *

print('------------------------------------------------------------')	#60個

def btn_hit():                      # 處理按鈕事件
    global msg_on                   # 這是全域變數
    if msg_on == False:
        msg_on = True
        x.set("I like tkinter")     # 顯示文字
    else:
        msg_on = False
        x.set("")                   # 不顯示文字
   
root = Tk()
root.title("ch6_1")                 # 視窗標題

msg_on = False                      # 全域變數預設是False    
x = StringVar()                     # Label的變數內容

label = Label(root,textvariable=x,          # 設定Label內容是變數x
              fg="blue",bg="lightyellow",   # 淺黃色底藍色字
              font="Verdana 16 bold",       # 字型設定
              width=25,height=2)            # 標籤內容
label.pack()   
btn = Button(root,text="Click Me",command=btn_hit)
btn.pack()                   

root.mainloop()






#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch06\ch6_2.py

# ch6_2.py
from tkinter import *

def btn_hit():                      # 處理按鈕事件
    if x.get() == "":               # 如果目前是空字串
        x.set("I like tkinter")     # 顯示文字
    else:
        x.set("")                   # 不顯示文字
   
root = Tk()
root.title("ch6_2")                 # 視窗標題
    
x = StringVar()                     # Label的變數內容

label = Label(root,textvariable=x,          # 設定Label內容是變數x
              fg="blue",bg="lightyellow",   # 淺黃色底藍色字
              font="Verdana 16 bold",       # 字型設定
              width=25,height=2)            # 標籤內容
label.pack()   
btn = Button(root,text="Click Me",command=btn_hit)
btn.pack()                   

root.mainloop()







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch06\ch6_3.py

# ch6_3.py
from tkinter import *

def callback(*args):
    print("data changed : ",xE.get())   # Python Shell視窗輸出
   
root = Tk()
root.title("ch6_3")                     # 視窗標題
    
xE = StringVar()                        # Entry的變數內容
entry = Entry(root,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)
xE.trace("w",callback)                  # 若是有更改執行callback

root.mainloop()







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch06\ch6_4.py

# ch6_4.py
from tkinter import *

def callback(*args):
    xL.set(xE.get())                    # 更改標籤內容
    print("data changed : ",xE.get())   # Python Shell視窗輸出
   
root = Tk()
root.title("ch6_4")                     # 視窗標題
    
xE = StringVar()                        # Entry的變數內容
entry = Entry(root,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)
xE.trace("w",callback)                  # 若是有更改執行callback

xL = StringVar()                        # Label的變數內容
label = Label(root,textvariable=xL)
xL.set("同步顯示")
label.pack(pady=5,padx=10)   

root.mainloop()







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch06\ch6_5.py

# ch6_5.py
from tkinter import *

def callbackW(*args):                   # 內容被更改時執行
    xL.set(xE.get())                    # 更改標籤內容

def callbackR(*args):                   # 內容被讀取時執行
    print("Warning:資料被讀取!")

def hit():                              # 讀取資料
    print("讀取資料:",xE.get())
  
root = Tk()
root.title("ch6_5")                     # 視窗標題
    
xE = StringVar()                        # Entry的變數內容

entry = Entry(root,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)
xE.trace("w",callbackW)                 # 若是有更改執行callbackW
xE.trace("r",callbackR)                 # 若是有被讀取執行callbackR

xL = StringVar()                        # Label的變數內容
label = Label(root,textvariable=xL)
xL.set("同步顯示")
label.pack(pady=5,padx=10)

btn = Button(root,text="讀取",command=hit)    # 建立讀取按鈕
btn.pack(pady=5)

root.mainloop()







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch06\ch6_6.py

# ch6_6.py
from tkinter import *

def callbackW(name,index,mode):         # 內容被更改時執行
    xL.set(xE.get())                    # 更改標籤內容
    print("name = %r, index = %r, mode = %r" % (name,index,mode)) 
  
root = Tk()
root.title("ch6_5")                     # 視窗標題
    
xE = StringVar()                        # Entry的變數內容

entry = Entry(root,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)
xE.trace("w",callbackW)                 # 若是有更改執行callbackW

xL = StringVar()                        # Label的變數內容
label = Label(root,textvariable=xL)
xL.set("同步顯示")
label.pack(pady=5,padx=10)

root.mainloop()







print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python GUI 設計活用 tkinter之路\ch06\ch6_7.py

# ch6_7.py
from tkinter import *
def calculate():                    # 執行計算並顯示結果
    result = eval(equ.get())
    equ.set(equ.get() + "=\n" + str(result))
    
def show(buttonString):             # 更新顯示區的計算公式
    content = equ.get()
    if content == "0":
        content = ""
    equ.set(content + buttonString)

def backspace():                    # 刪除前一個字元
    equ.set(str(equ.get()[:-1]))

def clear():                        # 清除顯示區,放置0
    equ.set("0")

root = Tk()
root.title("計算器")

equ = StringVar()
equ.set("0")                        # 預設是顯示0

# 設計顯示區
label = Label(root,width=25,height=2,relief="raised",anchor=SE,         
              textvariable=equ)
label.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

# 清除顯示區按鈕
clearButton = Button(root,text="C",fg="blue",width=5,command=clear)   
clearButton.grid(row = 1, column = 0)
# 以下是row1的其它按鈕
Button(root,text="DEL",width=5,command=backspace).grid(row=1,column=1)
Button(root,text="%",width=5,command=lambda:show("%")).grid(row=1,column=2)
Button(root,text="/",width=5,command=lambda:show("/")).grid(row=1,column=3)
# 以下是row2的其它按鈕
Button(root,text="7",width=5,command=lambda:show("7")).grid(row=2,column=0)
Button(root,text="8",width=5,command=lambda:show("8")).grid(row=2,column=1)
Button(root,text="9",width=5,command=lambda:show("9")).grid(row=2,column=2)
Button(root,text="*",width=5,command=lambda:show("*")).grid(row=2,column=3)
# 以下是row3的其它按鈕
Button(root,text="4",width=5,command=lambda:show("4")).grid(row=3,column=0)
Button(root,text="5",width=5,command=lambda:show("5")).grid(row=3,column=1)
Button(root,text="6",width=5,command=lambda:show("6")).grid(row=3,column=2)
Button(root,text="-",width=5,command=lambda:show("-")).grid(row=3,column=3)
# 以下是row4的其它按鈕
Button(root,text="1",width=5,command=lambda:show("1")).grid(row=4,column=0)
Button(root,text="2",width=5,command=lambda:show("2")).grid(row=4,column=1)
Button(root,text="3",width=5,command=lambda:show("3")).grid(row=4,column=2)
Button(root,text="+",width=5,command=lambda:show("+")).grid(row=4,column=3)
# 以下是row5的其它按鈕
Button(root,text="0",width=12,
       command=lambda:show("0")).grid(row=5,column=0,columnspan=2)
Button(root,text=".",width=5,
       command=lambda:show(".")).grid(row=5,column=2)
Button(root,text="=",width=5,bg ="yellow",
       command=lambda:calculate()).grid(row=5,column=3)

root.mainloop()








print('------------------------------------------------------------')	#60個





