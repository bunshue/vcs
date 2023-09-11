import sys

from tkinter import *

print('------------------------------------------------------------')	#60個

window = Tk()

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

'''
lab1.pack(side=LEFT)                # 包裝與定位元件
lab2.pack(side=LEFT)                # 包裝與定位元件
lab3.pack(side=LEFT)                # 包裝與定位元件
'''

'''
lab1.pack()                         # 包裝與定位元件
lab2.pack(side=RIGHT)               # 靠右包裝與定位元件
lab3.pack(side=LEFT)                # 靠左包裝與定位元件
'''

window.mainloop()

print('------------------------------------------------------------')	#60個

Reliefs = ["flat","groove","raised","ridge","solid","sunken"]

root = Tk()
root.title("ch3_5")

for Relief in Reliefs:
    Label(root,text=Relief,relief=Relief,
          fg="blue",
          font="Times 20 bold").pack(side=LEFT,padx=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

bitMaps = ["error","hourglass","info","questhead","question",
           "warning","gray12","gray25","gray50","gray75"]

root = Tk()
root.title("ch3_5_1")

for bitMap in bitMaps:
    Label(root,bitmap=bitMap).pack(side=LEFT,padx=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_6")               # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow")     # 標籤背景是淺黃色
lab2 = Label(window,text="長庚大學",
              bg="lightgreen")      # 標籤背景是淺綠色
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue")       # 標籤背景是淺藍色
lab1.pack(fill=X)                   # 填滿X軸包裝與定位元件
lab2.pack(pady=10)                  # y軸增加10像素
lab3.pack(fill=X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_7")               # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow")     # 標籤背景是淺黃色
lab2 = Label(window,text="長庚大學",
              bg="lightgreen")      # 標籤背景是淺綠色
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue")       # 標籤背景是淺藍色
lab1.pack(fill=X,pady=10)           # 填滿X軸,Y軸增加10像素
lab2.pack(pady=10)                  # Y軸增加10像素
lab3.pack(fill=X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_8")               # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="長庚大學",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab1.pack(padx=50)                  # 左右邊界間距是50像素
lab2.pack(padx=50)                  # 左右邊界間距是50像素
lab3.pack(padx=50)                  # 左右邊界間距是50像素

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_9")               # 視窗標題
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
lab2.pack(side=LEFT,padx=10)        # 左右間距padx=10
lab3.pack(side=LEFT)                # 包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_10")               # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow")     # 標籤背景是淺黃色
lab2 = Label(window,text="長庚大學",
              bg="lightgreen")      # 標籤背景是淺綠色
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue")       # 標籤背景是淺藍色
lab1.pack()                         # 包裝與定位元件
lab2.pack(ipadx=10)                 # ipadx=10包裝與定位元件
lab3.pack()                         # 包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_11")               # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow")     # 標籤背景是淺黃色
lab2 = Label(window,text="長庚大學",
              bg="lightgreen")      # 標籤背景是淺綠色
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue")       # 標籤背景是淺藍色
lab1.pack()                         # 包裝與定位元件
lab2.pack(ipadx=10)                 # ipadx=10包裝與定位元件
lab3.pack(ipady=10)                 # ipady=10包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()
root.title("ch3_12")
root.geometry("300x180")            # 設定視窗勘寬300高180
oklabel=Label(root,text="OK",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="blue") # 藍底白字
oklabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             padx=10,pady=10)       # x和y軸間距皆是10

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()
root.title("ch3_13")
root.geometry("300x180")            # 設定視窗勘寬300高180
oklabel=Label(root,text="OK",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="blue") # 藍底白字
oklabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             padx=10,pady=10)       # x和y軸間距皆是10
nolabel=Label(root,text="NO",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="red")  # 藍底白字
nolabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             pady=10)               # y軸間距皆是10

root.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_14")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow")     # 標籤背景是淺黃色
lab2 = Label(window,text="長庚大學",
              bg="lightgreen")      # 標籤背景是淺綠色
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue")       # 標籤背景是淺藍色
lab1.pack(fill=X)                   # 填滿X軸包裝與定位元件
lab2.pack()                         # 包裝與定位元件
lab3.pack(fill=X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_15")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow")     # 標籤背景是淺黃色
lab2 = Label(window,text="長庚大學",
              bg="lightgreen")      # 標籤背景是淺綠色
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue")       # 標籤背景是淺藍色
lab1.pack(fill=X)                   # 填滿X軸包裝與定位元件
lab2.pack(fill=Y)                   # 填滿Y軸包裝與定位元件
lab3.pack(fill=X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_16")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow")     # 標籤背景是淺黃色
lab2 = Label(window,text="長庚大學",
              bg="lightgreen")      # 標籤背景是淺綠色
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue")       # 標籤背景是淺藍色
lab1.pack(side=LEFT)                # 從左配置控件
lab2.pack()                         # 預設從上開始配置控件
lab3.pack()                         # 預設從上開始配置控件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_17")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow")     # 標籤背景是淺黃色
lab2 = Label(window,text="長庚大學",
              bg="lightgreen")      # 標籤背景是淺綠色
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue")       # 標籤背景是淺藍色
lab1.pack(side=LEFT,fill=Y)         # 從左配置控件fill=Y
lab2.pack(fill=X)                   # 預設從上開始配置控件fill=X
lab3.pack()                         # 預設從上開始配置控件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_18")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow")     # 標籤背景是淺黃色
lab2 = Label(window,text="長庚大學",
              bg="lightgreen")      # 標籤背景是淺綠色
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue")       # 標籤背景是淺藍色
lab1.pack(side=LEFT,fill=Y)         # 從左配置控件fill=Y
lab2.pack(fill=X)                   # 預設從上開始配置控件fill=X
lab3.pack(fill=X)                   # 預設從上開始配置控件fill=X

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_19")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow")     # 標籤背景是淺黃色
lab2 = Label(window,text="長庚大學",
              bg="lightgreen")      # 標籤背景是淺綠色
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue")       # 標籤背景是淺藍色
lab1.pack(side=LEFT,fill=Y)         # 從左配置控件fill=Y
lab2.pack(fill=X)                   # 預設從上開始配置控件fill=X
lab3.pack(fill=BOTH)                # 預設從上開始配置控件fill=BOTH

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_20")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
              bg="lightyellow")     # 標籤背景是淺黃色
lab2 = Label(window,text="長庚大學",
              bg="lightgreen")      # 標籤背景是淺綠色
lab3 = Label(window,text="長庚科技大學",
              bg="lightblue")       # 標籤背景是淺藍色
lab1.pack(side=LEFT,fill=Y)         # 從左配置控件fill=Y
lab2.pack(fill=X)                   # 預設從上開始配置控件fill=X
lab3.pack(fill=BOTH,expand=True)    # fill=BOTH,expand=True

window.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()
root.title("ch3_21")               # 視窗標題
root.geometry("300x200")
    
Label(root,text='Mississippi',bg='red',fg='white',
      font='Times 24 bold').pack(fill=X)  
Label(root,text='Kentucky',bg='green',fg='white',
      font='Arial 24 bold italic').pack(fill=BOTH,expand=True)  
Label(root,text='Purdue',bg='blue',fg='white',
      font='Times 24 bold').pack(fill=X)  

root.mainloop() 

print('------------------------------------------------------------')	#60個

root = Tk()
root.title("ch3_22")               # 視窗標題
    
Label(root,text='Mississippi',bg='red',fg='white',
      font='Times 20 bold').pack(side=LEFT,fill=Y)  
Label(root,text='Kentucky',bg='green',fg='white',
      font='Arial 20 bold italic').pack(side=LEFT,fill=BOTH,expand=True)  
Label(root,text='Purdue',bg='blue',fg='white',
      font='Times 20 bold').pack(side=LEFT,fill=Y)  

root.mainloop() 

print('------------------------------------------------------------')	#60個

root = Tk()
root.title("ch3_23")
root.geometry("300x180")            # 設定視窗勘寬300高180
print("執行前",root.pack_slaves())
oklabel=Label(root,text="OK",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="blue") # 藍底白字
oklabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             padx=10,pady=10)       # x和y軸間距皆是10
nolabel=Label(root,text="NO",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="red")  # 藍底白字
nolabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             pady=10)               # y軸間距皆是10
print("執行後",root.pack_slaves())

root.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_24")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
             bg="lightyellow",      # 標籤背景是淺黃色
             width=15)              # 標籤寬度是15     
lab2 = Label(window,text="長庚大學",
             bg="lightgreen",       # 標籤背景是淺綠色
             width=15)              # 標籤寬度是15            
lab3 = Label(window,text="長庚科技大學",
             bg="lightblue",        # 標籤背景是淺藍色
             width=15)              # 標籤寬度是15
lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=1,column=0)           # 格狀包裝
lab3.grid(row=1,column=1)           # 格狀包裝

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_25")              # 視窗標題
lab1 = Label(window,text="明志科技大學",
             bg="lightyellow",      # 標籤背景是淺黃色
             width=15)              # 標籤寬度是15     
lab2 = Label(window,text="長庚大學",
             bg="lightgreen",       # 標籤背景是淺綠色
             width=15)              # 標籤寬度是15            
lab3 = Label(window,text="長庚科技大學",
             bg="lightblue",        # 標籤背景是淺藍色
             width=15)              # 標籤寬度是15
lab1.grid(row=0,column=0)           # 格狀包裝
lab2.grid(row=1,column=2)           # 格狀包裝
lab3.grid(row=2,column=1)           # 格狀包裝

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_26")              # 視窗標題
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

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_27")              # 視窗標題
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

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_28")              # 視窗標題
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

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_29")              # 視窗標題
lab1 = Label(window,text="標籤1",relief="raised")
lab2 = Label(window,text="標籤2",relief="raised")
lab4 = Label(window,text="標籤4",relief="raised")
lab5 = Label(window,text="標籤5",relief="raised")
lab8 = Label(window,text="標籤8",relief="raised")
lab1.grid(row=0,column=0)
lab2.grid(row=0,column=1,rowspan=2,columnspan=2)
lab4.grid(row=0,column=3)
lab5.grid(row=1,column=0)
lab8.grid(row=1,column=3)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_30")              # 視窗標題
lab1 = Label(window,text="標籤1",relief="raised")
lab2 = Label(window,text="標籤2",relief="raised")
lab3 = Label(window,text="標籤3",relief="raised")
lab4 = Label(window,text="標籤4",relief="raised")
lab5 = Label(window,text="標籤5",relief="raised")
lab6 = Label(window,text="標籤6",relief="raised")
lab7 = Label(window,text="標籤7",relief="raised")
lab8 = Label(window,text="標籤8",relief="raised")
lab1.grid(row=0,column=0,padx=5,pady=5)
lab2.grid(row=0,column=1,padx=5,pady=5)
lab3.grid(row=0,column=2,padx=5,pady=5)
lab4.grid(row=0,column=3,padx=5,pady=5)
lab5.grid(row=1,column=0,padx=5)
lab6.grid(row=1,column=1,padx=5)
lab7.grid(row=1,column=2,padx=5)
lab8.grid(row=1,column=3,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_31")              # 視窗標題
lab1 = Label(window,text="明志工專")
lab2 = Label(window,bg="yellow",width=20)
lab3 = Label(window,text="明志科技大學")
lab4 = Label(window,bg="aqua",width=20)
lab1.grid(row=0,column=0,padx=5,pady=5)
lab2.grid(row=0,column=1,padx=5,pady=5)
lab3.grid(row=1,column=0,padx=5)
lab4.grid(row=1,column=1,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_32")              # 視窗標題
lab1 = Label(window,text="明志工專")
lab2 = Label(window,bg="yellow",width=20)
lab3 = Label(window,text="明志科技大學")
lab4 = Label(window,bg="aqua",width=20)
lab1.grid(row=0,column=0,padx=5,pady=5,sticky=W)
lab2.grid(row=0,column=1,padx=5,pady=5)
lab3.grid(row=1,column=0,padx=5)
lab4.grid(row=1,column=1,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_33")              # 視窗標題
lab1 = Label(window,text="明志工專",relief="raised")
lab2 = Label(window,bg="yellow",width=20)
lab3 = Label(window,text="明志科技大學",relief="raised")
lab4 = Label(window,bg="aqua",width=20)
lab1.grid(row=0,column=0,padx=5,pady=5)
lab2.grid(row=0,column=1,padx=5,pady=5)
lab3.grid(row=1,column=0,padx=5)
lab4.grid(row=1,column=1,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_34")              # 視窗標題
lab1 = Label(window,text="明志工專",relief="raised")
lab2 = Label(window,bg="yellow",width=20)
lab3 = Label(window,text="明志科技大學",relief="raised")
lab4 = Label(window,bg="aqua",width=20)
lab1.grid(row=0,column=0,padx=5,pady=5,sticky=W+E)
lab2.grid(row=0,column=1,padx=5,pady=5)
lab3.grid(row=1,column=0,padx=5)
lab4.grid(row=1,column=1,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()
root.title("ch3_35")                # 視窗標題
Colors = ["red","orange","yellow","green","blue","purple"]

r = 0                               # row編號
for color in Colors:
    Label(root,text=color,relief="groove",width=20).grid(row=r,column=0)
    Label(root,bg=color,relief="ridge",width=20).grid(row=r,column=1)
    r += 1

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()
root.title("ch3_35_1")

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

lab1 = Label(root,text="Label 1",bg="pink")
lab1.grid(row=0,column=0,padx=5,pady=5)

lab2 = Label(root,text="Label 2",bg="lightblue")
lab2.grid(row=0,column=1,padx=5,pady=5)

lab3 = Label(root,bg="yellow")
lab3.grid(row=1,column=0,columnspan=2,padx=5,pady=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()
root.title("ch3_35_2")

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

lab1 = Label(root,text="Label 1",bg="pink")
lab1.grid(row=0,column=0,padx=5,pady=5,stick=W)

lab2 = Label(root,text="Label 2",bg="lightblue")
lab2.grid(row=0,column=1,padx=5,pady=5)

lab3 = Label(root,bg="yellow")
lab3.grid(row=1,column=0,columnspan=2,padx=5,pady=5,
          sticky=N+S+W+E)

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()
root.title("ch3_35_3")

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

lab1 = Label(root,text="Label 1",bg="pink")
lab1.grid(row=0,column=0,padx=5,pady=5,stick=W+E)

lab2 = Label(root,text="Label 2",bg="lightblue")
lab2.grid(row=0,column=1,padx=5,pady=5)

lab3 = Label(root,bg="yellow")
lab3.grid(row=1,column=0,columnspan=2,padx=5,pady=5,
          sticky=N+S+W+E)

root.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()
window.title("ch3_36")              # 視窗標題
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

print('------------------------------------------------------------')	#60個

root = Tk()
root.title("ch3_37")
root.geometry("640x480")

night = PhotoImage(file="night.png")    # 影像night
lab1 = Label(root,image=night)
lab1.place(x=20,y=30,width=200,height=120)
snow = PhotoImage(file="snow.png")      # 影像snow
lab2 = Label(root,image=snow)
lab2.place(x=200,y=200,width=400,height=240)

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()
root.title("ch3_38")
root.geometry("640x480")

night = PhotoImage(file="night.png")
label=Label(root,image=night)
label.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()
root.title("ch3_39")
root.geometry("640x480")

night = PhotoImage(file="night.png")
label=Label(root,image=night)
label.place(relx=0.1,rely=0.1,relheight=0.8)

root.mainloop()





print('------------------------------------------------------------')	#60個




