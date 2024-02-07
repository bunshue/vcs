import sys

# ch18_1.py
from tkinter import *

window = Tk()
window.mainloop()







#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_2.py

# ch18_2.py
from tkinter import *

window = Tk()
window.title("MyWindow")    # 視窗標題
window.geometry("300x160")  # 視窗大小

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_3.py

# ch18_3.py
from tkinter import *

window = Tk()
window.title("ch18_3")          # 視窗標題
label = Label(window,text="I like tkinter")
label.pack()                    # 包裝與定位元件

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_3_1.py

# ch18_3_1.py
from tkinter import *

window = Tk()
window.title("ch18_3_1")          # 視窗標題
label = Label(window,text="I like tkinter").pack()

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_4.py

# ch18_4.py
from tkinter import *

window = Tk()
window.title("ch18_4")              # 視窗標題
label = Label(window,text="I like tkinter",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label.pack()                        # 包裝與定位元件

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_4_1.py

# ch18_4_1.py
from tkinter import *

window = Tk()
window.title("ch18_4_1")            # 視窗標題
label = Label(window,text="I like tkinter",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15,             # 標籤寬度是15
              font="Helvetica 16 bold italic")
label.pack()                        # 包裝與定位元件

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_5.py

# ch18_5.py
from tkinter import *

window = Tk()
window.title("ch18_5")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack()                         # 包裝與定位元件
lab2.pack()                         # 包裝與定位元件
lab3.pack()                         # 包裝與定位元件

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_6.py

# ch18_6.py
from tkinter import *

window = Tk()
window.title("ch18_6")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=BOTTOM)              # 包裝與定位元件
lab2.pack(side=BOTTOM)              # 包裝與定位元件
lab3.pack(side=BOTTOM)              # 包裝與定位元件

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_6_1.py

# ch18_6_1.py
from tkinter import *

window = Tk()
window.title("ch18_6")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=BOTTOM)              # 包裝與定位元件
lab2.pack(side=BOTTOM,pady=5)       # 包裝與定位元件,增加y軸間距
lab3.pack(side=BOTTOM)              # 包裝與定位元件

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_7.py

# ch18_7.py
from tkinter import *

window = Tk()
window.title("ch18_7")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=LEFT)                # 包裝與定位元件
lab2.pack(side=LEFT)                # 包裝與定位元件
lab3.pack(side=LEFT)                # 包裝與定位元件

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_7_1.py

# ch18_7_1.py
from tkinter import *

window = Tk()
window.title("ch18_7")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(side=LEFT)                # 包裝與定位元件
lab2.pack(side=LEFT,padx=5)         # 包裝與定位元件,增加x軸間距
lab3.pack(side=LEFT)                # 包裝與定位元件

window.mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_8.py

# ch18_8.py
from tkinter import *

window = Tk()
window.title("ch18_8")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack()                         # 包裝與定位元件
lab2.pack(side=RIGHT)               # 包裝與定位元件
lab3.pack(side=LEFT)                # 包裝與定位元件

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_9.py

# ch18_9.py
from tkinter import *

window = Tk()
window.title("ch18_9")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=1,column=0)           # 格狀包裝
lab3.grid(row=1,column=1)           # 格狀包裝

window.mainloop()







print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_10.py

# ch18_10.py
from tkinter import *

window = Tk()
window.title("ch18_10")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=1,column=2)           # 格狀包裝
lab3.grid(row=2,column=1)           # 格狀包裝

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_10_1.py

# ch18_10_1.py
from tkinter import *

window = Tk()
window.title("ch18_10_1")              # 視窗標題
lab1 = Label(window,text="標籤1",relief="raised")
lab2 = Label(window,text="標籤2",relief="raised")
lab3 = Label(window,text="標籤3",relief="raised")
lab4 = Label(window,text="標籤4",relief="raised")
lab5 = Label(window,text="標籤5",relief="raised")
lab6 = Label(window,text="標籤6",relief="raised")
lab7 = Label(window,text="標籤7",relief="raised")
lab8 = Label(window,text="標籤8",relief="raised")
lab1.grid(row=0,column=0)
lab2.grid(row=0,column=1)
lab3.grid(row=0,column=2)
lab4.grid(row=0,column=3)
lab5.grid(row=1,column=0)
lab6.grid(row=1,column=1)
lab7.grid(row=1,column=2)
lab8.grid(row=1,column=3)

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_10_2.py

# ch18_10_2.py
from tkinter import *

window = Tk()
window.title("ch18_10_2")              # 視窗標題
lab1 = Label(window,text="標籤1",relief="raised")
lab2 = Label(window,text="標籤2",relief="raised")
lab4 = Label(window,text="標籤4",relief="raised")
lab5 = Label(window,text="標籤5",relief="raised")
lab6 = Label(window,text="標籤6",relief="raised")
lab7 = Label(window,text="標籤7",relief="raised")
lab8 = Label(window,text="標籤8",relief="raised")
lab1.grid(row=0,column=0)
lab2.grid(row=0,column=1,columnspan=2)
lab4.grid(row=0,column=3)
lab5.grid(row=1,column=0)
lab6.grid(row=1,column=1)
lab7.grid(row=1,column=2)
lab8.grid(row=1,column=3)

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_10_3.py

# ch18_10_3.py
from tkinter import *

window = Tk()
window.title("ch18_10_3")              # 視窗標題
lab1 = Label(window,text="標籤1",relief="raised")
lab2 = Label(window,text="標籤2",relief="raised")
lab3 = Label(window,text="標籤3",relief="raised")
lab4 = Label(window,text="標籤4",relief="raised")
lab5 = Label(window,text="標籤5",relief="raised")
lab7 = Label(window,text="標籤7",relief="raised")
lab8 = Label(window,text="標籤8",relief="raised")
lab1.grid(row=0,column=0)
lab2.grid(row=0,column=1,rowspan=2)
lab3.grid(row=0,column=2)
lab4.grid(row=0,column=3)
lab5.grid(row=1,column=0)
lab7.grid(row=1,column=2)
lab8.grid(row=1,column=3)

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_11.py

# ch18_11.py
from tkinter import *

window = Tk()
window.title("ch18_11")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.place(x=0,y=0)                 # 直接定位
lab2.place(x=30,y=50)               # 直接定位
lab3.place(x=60,y=100)              # 直接定位

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_12.py

# ch18_12.py
from tkinter import *

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
window = Tk()
window.title("ch18_12")             # 視窗標題
label = Label(window)               # 標籤內容             
btn = Button(window,text="Message",command=msgShow)

label.pack()                      
btn.pack()

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_13.py

# ch18_13.py
from tkinter import *

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
window = Tk()
window.title("ch18_13")             # 視窗標題
label = Label(window)               # 標籤內容             
btn1 = Button(window,text="Message",width=15,command=msgShow)
btn2 = Button(window,text="Exit",width=15,command=window.destroy)
label.pack()                      
btn1.pack(side=LEFT)                # 按鈕1
btn2.pack(side=RIGHT)               # 按鈕2

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_13_1.py

# ch18_13_1.py
from tkinter import *

def yellow():                   # 設定視窗背景是黃色
    window.config(bg="yellow")
def blue():                     # 設定視窗背景是藍色
    window.config(bg="blue")
    
window = Tk()
window.title("ch18_13_1")
window.geometry("300x200")        # 固定視窗大小
# 依次建立3個鈕
exitbtn = Button(window,text="Exit",command=window.destroy)
bluebtn = Button(window,text="Blue",command=blue)
yellowbtn = Button(window,text="Yellow",command=yellow)
# 將3個鈕包裝定位在右下方
exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

window.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_13_2.py

# ch18_13_2.py
from tkinter import *

def bColor(bgColor):          # 設定視窗背景顏色
    window.config(bg=bgColor)
    
window = Tk()
window.title("ch18_13_2")
window.geometry("300x200")        # 固定視窗大小
# 依次建立3個鈕
exitbtn = Button(window,text="Exit",command=window.destroy)
bluebtn = Button(window,text="Blue",command=lambda:bColor("blue"))
yellowbtn = Button(window,text="Yellow",command=lambda:bColor("yellow"))
# 將3個鈕包裝定位在右下方
exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

window.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_13_3.py

# ch18_13_3.py
from tkinter import *

window = Tk()
window.title("ch18_13_2")
window.geometry("300x200")        # 固定視窗大小
# 依次建立3個鈕
exitbtn = Button(window,text="Exit",command=window.destroy)
bluebtn = Button(window,text="Blue",command=lambda:window.config(bg="blue"))
yellowbtn = Button(window,text="Yellow",command=lambda:window.config(bg="yellow"))
# 將3個鈕包裝定位在右下方
exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

window.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_14.py

# ch18_14.py
from tkinter import *

def btn_hit():                      # 處理按鈕事件
    global msg_on                   # 這是全域變數
    if msg_on == False:
        msg_on = True
        x.set("I like tkinter")     # 顯示文字
    else:
        msg_on = False
        x.set("")                   # 不顯示文字
   
window = Tk()
window.title("ch18_14")             # 視窗標題

msg_on = False                      # 全域變數預設是False    
x = StringVar()                     # Label的變數內容

label = Label(window,textvariable=x,      # 設定Label內容是變數x
              fg="blue",bg="lightyellow", # 淺黃色底藍色字
              font="Verdana 16 bold",     # 字型設定
              width=25,height=2).pack()   # 標籤內容
btn = Button(window,text="Hit",command=btn_hit).pack()                   

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_15.py

# ch18_15.py
from tkinter import *

window = Tk()
window.title("ch18_15")         # 視窗標題

lab1 = Label(window,text="Account ").grid(row=0)
lab2 = Label(window,text="Password").grid(row=1)

e1 = Entry(window)              # 文字方塊1
e2 = Entry(window,show='*')     # 文字方塊2
e1.grid(row=0,column=1)         # 定位文字方塊1
e2.grid(row=1,column=1)         # 定位文字方塊2

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_16.py

# ch18_16.py
from tkinter import *
def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
          
window = Tk()
window.title("ch18_16")             # 視窗標題

lab1 = Label(window,text="Account ").grid(row=0)
lab2 = Label(window,text="Password").grid(row=1)

e1 = Entry(window)                  # 文字方塊1
e2 = Entry(window,show='*')         # 文字方塊2
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = Button(window,text="Print",command=printInfo)
btn1.grid(row=2,column=0)
btn2 = Button(window,text="Quit",command=window.quit)
btn2.grid(row=2,column=1)

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_17.py

# ch18_17.py
from tkinter import *
def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
          
window = Tk()
window.title("ch18_17")             # 視窗標題

lab1 = Label(window,text="Account ").grid(row=0)
lab2 = Label(window,text="Password").grid(row=1)

e1 = Entry(window)                  # 文字方塊1
e2 = Entry(window,show='*')         # 文字方塊2
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = Button(window,text="Print",command=printInfo)
# sticky=W可以設定物件與上面的Label切齊, pady設定上下間距是10
btn1.grid(row=2,column=0,sticky=W,pady=10)  
btn2 = Button(window,text="Quit",command=window.quit)
# sticky=W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2,column=1,sticky=W,pady=10)

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_18.py

# ch18_18.py
from tkinter import *
def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
          
window = Tk()
window.title("ch18_18")             # 視窗標題

lab1 = Label(window,text="Account ").grid(row=0)
lab2 = Label(window,text="Password").grid(row=1)

e1 = Entry(window)                  # 文字方塊1
e2 = Entry(window,show='*')         # 文字方塊2
e1.insert(1,"Kevin")                # 預設文字方塊1內容
e2.insert(1,"pwd")                  # 預設文字方塊2內容
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = Button(window,text="Print",command=printInfo)
# sticky=W可以設定物件與上面的Label切齊, pady設定上下間距是10
btn1.grid(row=2,column=0,sticky=W,pady=10)  
btn2 = Button(window,text="Quit",command=window.quit)
# sticky=W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2,column=1,sticky=W,pady=10)

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_19.py

# ch18_19.py
from tkinter import *
def printInfo():                    # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (e1.get(),e2.get()))
    e1.delete(0,END)                # 刪除文字方塊1
    e2.delete(0,END)                # 刪除文字方塊2
          
window = Tk()
window.title("ch18_19")             # 視窗標題

lab1 = Label(window,text="Account ").grid(row=0)
lab2 = Label(window,text="Password").grid(row=1)

e1 = Entry(window)                  # 文字方塊1
e2 = Entry(window,show='*')         # 文字方塊2
e1.insert(1,"Kevin")                # 預設文字方塊1內容
e2.insert(1,"pwd")                  # 預設文字方塊2內容
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn1 = Button(window,text="Print",command=printInfo)
# sticky=W可以設定物件與上面的Label切齊, pady設定上下間距是10
btn1.grid(row=2,column=0,sticky=W,pady=10)  
btn2 = Button(window,text="Quit",command=window.quit)
# sticky=W可以設定物件與上面的Entry切齊, pady設定上下間距是10
btn2.grid(row=2,column=1,sticky=W,pady=10)

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_20.py

# ch18_20.py
from tkinter import *
def add():                                  # 加法運算
    n3.set(n1.get()+n2.get())
    
window = Tk()
window.title("ch18_20")                     # 視窗標題

n1 = IntVar()                   
n2 = IntVar()
n3 = IntVar()

e1 = Entry(window,width=8,textvariable=n1)  # 文字方塊1
label = Label(window,width=3,text='+')      # 加號
e2 = Entry(window,width=8,textvariable=n2)  # 文字方塊2
btn = Button(window,width=5,text='=',command=add)   # =按鈕
e3 = Entry(window,width=8,textvariable=n3)  # 儲存結果文字方塊

e1.grid(row=0,column=0)                     # 定位文字方塊1
label.grid(row=0,column=1,padx=5)           # 定位加號
e2.grid(row=0,column=2)                     # 定位文字方塊2
btn.grid(row=1,column=1,pady=5)             # 定位=按鈕
e3.grid(row=2,column=1)                     # 定位儲存結果

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_21.py

# ch18_21.py
from tkinter import *
          
window = Tk()
window.title("ch18_21")             # 視窗標題

text = Text(window,height=2,width=30)
text.insert(END,"我懷念\n我的明志工專生活點滴")
text.pack()

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_22.py

# ch18_22.py
from tkinter import *
          
window = Tk()
window.title("ch18_22")             # 視窗標題

text = Text(window,height=2,width=30)
text.insert(END,"我懷念\n一個人的極境旅行")
str = """2016年12月,我一個人訂了機票和船票,
開始我的南極旅行,飛機經杜拜再往阿根廷的烏斯懷雅,
在此我登上郵輪開始我的南極之旅"""
text.insert(END,str)
text.pack()

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_23.py

# ch18_23.py
from tkinter import *
          
window = Tk()
window.title("ch18_23")                 # 視窗標題
scrollbar = Scrollbar(window)           # 卷軸物件
text = Text(window,height=2,width=30)   # 文字區域物件
scrollbar.pack(side=RIGHT,fill=Y)       # 靠右安置與父物件高度相同
text.pack(side=LEFT,fill=Y)             # 靠左安置與父物件高度相同
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)
text.insert(END,"我懷念\n一個人的極境旅行")
str = """2016年12月,我一個人訂了機票和船票,
開始我的南極旅行,飛機經杜拜再往阿根廷的烏斯懷雅,
在此我登上郵輪開始我的南極之旅"""
text.insert(END,str)

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_24.py

# ch18_24.py
from tkinter import *
def printSelection():
    label.config(text="你是" + var.get())

window = Tk()
window.title("ch18_24")                   # 視窗標題

var = StringVar()
var.set("男生")                           # 預設選項                       
label = Label(window,text="尚未選擇", bg="lightyellow",width=30)
label.pack()

rb1 = Radiobutton(window,text="男生",
                  variable=var,value='男生',
                  command=printSelection).pack()
rb2 = Radiobutton(window,text="女生",
                  variable=var,value='女生',
                  command=printSelection).pack()

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_25.py

# ch18_25.py
from tkinter import *
def printSelection():
    print(cities[var.get()])            # 列出所選城市

window = Tk()
window.title("ch18_25")                 # 視窗標題
cities = {0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"香港"}

var = IntVar()
var.set(0)                              # 預設選項                       
label = Label(window,text="選擇最喜歡的城市",
              fg="blue",bg="lightyellow",width=30).pack()

for val, city in cities.items():        # 建立選項紐    
    Radiobutton(window,
                text=city,
                variable=var,value=val,
                command=printSelection).pack()

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_26.py

# ch18_26.py
from tkinter import *
def printSelection():
    print(cities[var.get()])            # 列出所選城市

window = Tk()
window.title("ch18_26")                 # 視窗標題
cities = {0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"香港"}

var = IntVar()
var.set(0)                              # 預設選項                       
label = Label(window,text="選擇最喜歡的城市",
              fg="blue",bg="lightyellow",width=30).pack()

for val, city in cities.items():        # 建立選項紐    
    Radiobutton(window,
                text=city,
                indicatoron = 0,        # 用盒子取代選項紐
                width=30,
                variable=var,value=val,
                command=printSelection).pack()

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_27.py

# ch18_27.py
from tkinter import *

window = Tk()
window.title("ch18_27")                   # 視窗標題

Label(window,text="請選擇喜歡的運動",
      fg="blue",bg="lightyellow",width=30).grid(row=0)

var1 = IntVar()                      
Checkbutton(window,text="美式足球",
                  variable=var1).grid(row=1,sticky=W)
var2 = IntVar()
Checkbutton(window,text="棒球",
                  variable=var2).grid(row=2,sticky=W)                
var3 = IntVar()
Checkbutton(window,text="籃球",
                  variable=var3).grid(row=3,sticky=W)   

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_28.py

# ch18_28.py
from tkinter import *

def printInfo():
    selection = ''
    for i in checkboxes:                    # 檢查此字典
        if checkboxes[i].get() == True:     # 被選取則執行
            selection = selection + sports[i] + "\t"
    print(selection)

window = Tk()
window.title("ch18_28")                     # 視窗標題

Label(window,text="請選擇喜歡的運動",
      fg="blue",bg="lightyellow",width=30).grid(row=0)

sports = {0:"美式足球",1:"棒球",2:"籃球",3:"網球"}    # 運動字典
checkboxes = {}                             # 字典存放被選取項目
for i in range(len(sports)):                # 將運動字典轉成核取方塊
    checkboxes[i] = BooleanVar()            # 布林變數物件
    Checkbutton(window,text=sports[i],
                variable=checkboxes[i]).grid(row=i+1,sticky=W)
  
Button(window,text="確定",width=10,command=printInfo).grid(row=i+2)

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_29.py

# ch18_29.py
from tkinter import *
from tkinter import messagebox

def myMsg():                    # 按Good Morning按鈕時執行
    messagebox.showinfo("My Message Box","Python tkinter早安")
    
window = Tk()
window.title("ch18_29")         # 視窗標題
window.geometry("300x160")      # 視窗寬300高160

Button(window,text="Good Morning",command=myMsg).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_30.py

# ch18_30.py
from tkinter import *
    
window = Tk()
window.title("ch18_30")         # 視窗標題

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/brown.gif'

html_gif = PhotoImage(file=filename)
Label(window,image=html_gif).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_31.py

# ch18_31.py
from tkinter import *
    
window = Tk()
window.title("ch18_31")         # 視窗標題

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/brown.gif'

sselogo = PhotoImage(file=filename)
lab1 = Label(window,image=sselogo).pack(side="right")

sseText = """
功蓋三分國，
名成八陣圖。
江流石不轉，
遺恨失吞吳。
"""
lab2 = Label(window,text=sseText,bg="lightyellow",
             padx=10).pack(side="left")

window.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_32.py

# ch18_32.py
from tkinter import *
    
window = Tk()
window.title("ch18_32")         # 視窗標題

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/brown.gif'

sselogo = PhotoImage(file=filename)
lab1 = Label(window,image=sselogo).pack(side="right")

sseText = """
功蓋三分國，
名成八陣圖。
江流石不轉，
遺恨失吞吳。
"""
lab2 = Label(window,text=sseText,bg="lightyellow",
             justify=LEFT,padx=10).pack(side="left")

window.mainloop()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_33.py

# ch18_33.py
from tkinter import *

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
window = Tk()
window.title("ch18_33")             # 視窗標題
label = Label(window)               # 標籤內容

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/brown.gif'

sun_gif = PhotoImage(file=filename)
btn = Button(window,image=sun_gif,command=msgShow)

label.pack()                      
btn.pack()

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_33_1.py

#ch18_33_1.py
from tkinter import *

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
window = Tk()
window.title("ch18_33_1")           # 視窗標題
label = Label(window)               # 標籤內容

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/brown.gif'

sun_gif = PhotoImage(file=filename)
btn = Button(window,image=sun_gif,command=msgShow,
             text="Click me",compound=TOP)

label.pack()                      
btn.pack()

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_33_2.py

#ch18_33_2.py
from tkinter import *

def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    
window = Tk()
window.title("ch18_33_2")           # 視窗標題
label = Label(window)               # 標籤內容

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/brown.gif'

sun_gif = PhotoImage(file=filename)
btn = Button(window,image=sun_gif,command=msgShow,
             text="Click me",compound=CENTER)

label.pack()                      
btn.pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *
    
window = Tk()
window.title("ch18_34")             # 視窗標題

slider1 = Scale(window,from_=0,to=10).pack()
slider2 = Scale(window,from_=0,to=10,
                length=300,orient=HORIZONTAL).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

from tkinter import *

def printInfo():
    print(slider1.get(),slider2.get())
    
window = Tk()
window.title("ch18_35")             # 視窗標題

slider1 = Scale(window,from_=0,to=10)
slider1.pack()
slider2 = Scale(window,from_=0,to=10,
                length=300,orient=HORIZONTAL)
slider2.set(3)                      # 設定水平尺度值
slider2.pack()
Button(window,text="Print",command=printInfo).pack()

window.mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_36.py

# ch18_36.py
from tkinter import *
from tkinter import messagebox

def newfile():
    messagebox.showinfo("開新檔案","可在此撰寫開新檔案程式碼")
    
def savefile():
    messagebox.showinfo("儲存檔案","可在此撰寫儲存檔案程式碼")
   
def about():
    messagebox.showinfo("程式說明","作者:洪錦魁")

window = Tk()
window.title("ch18_36")
window.geometry("300x160")          # 視窗寬300高160

menu = Menu(window)                 # 建立功能表物件
window.config(menu=menu)

filemenu = Menu(menu)               # 建立檔案功能表
menu.add_cascade(label="檔案",menu=filemenu)
filemenu.add_command(label="開新檔案",command=newfile)
filemenu.add_separator()            # 增加分隔線
filemenu.add_command(label="儲存檔案",command=savefile)
filemenu.add_separator()            # 增加分隔線
filemenu.add_command(label="結束",command=window.destroy)

helpmenu = Menu(menu)               # 建立說明功能表
menu.add_cascade(label="說明",menu=helpmenu)
helpmenu.add_command(label="程式說明",command=about)

mainloop()







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_36_1.py

# ch18_36_1.py
from tkinter import *

root = Tk()
root.title("ch18_36_1")
label=Label(root,text="I like tkinter",
            fg="blue",bg="yellow",
            height=3,width=15,
            anchor="se")
label.pack()  

root.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_37.py

# ch18_37.py
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








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_38.py

# ch18_38.py
import tkinter as tk
from tkinter.filedialog import asksaveasfilename    # 導入文件保存對話框函數
 
def generate_report():
    # 生成報告的函數, 從文本框中獲取報告內容
    report_content = text_report.get("1.0", tk.END)
    # 打開一個對話框讓使用者選擇保存報告的路徑
    file_path = asksaveasfilename(
        defaultextension=".txt",                    # 預設副檔名為.txt
        filetypes=[("Text documents", ".txt")],     # 文件類型過濾
    )
    # 如果使用者選擇了文件路徑, 則將報告內容寫入文件
    if file_path:
        with open(file_path, "w") as file:
            file.write(report_content)

root = tk.Tk()
root.title("報告生成器")                             # 視窗標題
text_report = tk.Text(root)                 # 建立文字區域用於編輯報告內容
text_report.pack()                          # 將文本區域添加到視窗中
# 建一個按鈕，點擊時會呼叫generate_report()函數
button_generate = tk.Button(root, text="生成報告", command=generate_report)
button_generate.pack()                      # 將按鈕添加到視窗中
root.mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new5\ch18_39.py

# ch18_39.py
import tkinter as tk
import random           

def update_data():
    # 更新標籤顯示的數據為1到100的隨機數
    label_data.config(text=str(random.randint(1, 100)))
    # 每1000毫秒(即1秒)後再次調用update_data函數更新數據
    root.after(1000, update_data)

root = tk.Tk()
root.title("數據監控")                      # 視窗標題
# 建立一個標籤用於顯示數據, 初始值為0, 字體設置為Helvetica, 大小為48
label_data = tk.Label(root, text="0", font=("Helvetica", 48))
label_data.pack()                           # 將標籤添加到視窗中
update_data()           # 呼叫update_data( )函數以開始數據更新過程
root.mainloop()


print("------------------------------------------------------------")  # 60個



