import sys

from tkinter import *

def msgShow():
    print('你按了 button')
  

print('------------------------------------------------------------')	#60個
'''
from tkinter.ttk import Separator

root = Tk()

#字 前景 背景 寬 高 字位置預設 字型
label=Label(root,text="Welcome to the United States and have a nice day",
            fg="red",bg="gray",
            height=3,width=15,
            font=("Helvetica",8,"bold"))
label.pack()

#字 前景 背景 寬 高 字位置西北
label=Label(root,text="Welcome to the United States and have a nice day",
            fg="blue",bg="lime",
            height=3,width=15,
            anchor="nw")
label.pack()

#字 前景 背景 寬 高 字位置西北 卷寬度
label=Label(root,text="Welcome to the United States and have a nice day",
            fg="blue",bg="yellow",
            height=3,width=15,
            anchor="nw",
            wraplength = 80,
            justify="left")     #left / center / right
label.pack()

label=Label(root,bitmap="hourglass")
label.pack()  

label=Label(root,bitmap="hourglass",
            compound="left",text="我的天空")
label.pack()  

label=Label(root,bitmap="hourglass",
            compound="top",text="我的天空")
label.pack()  

label=Label(root,bitmap="hourglass",
            compound="center",text="我的天空")
label.pack()  

label=Label(root,text="raised",relief="raised")
label.pack()

label=Label(root,text="raised",relief="raised",
            bg="lightyellow",
            padx=5,pady=10)
label.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

counter = 0                                 # 計數的全域變數
def run_counter(digit):                     # 數字變數內容的更動
    def counting():                         # 更動數字方法
        global counter
        counter += 1                        # 定義這是全域變數
        digit.config(text=str(counter))     # 列出標籤數字內容
        digit.after(1000,counting)          # 隔一秒後呼叫counting
    counting()                              # 啟動呼叫

root = Tk()
digit=Label(root,bg="yellow",fg="blue",     # 黃底藍字
            height=3,width=10,              # 寬10高3
            font="Helvetic 20 bold")        # 字型設定
digit.pack()
run_counter(digit)                          # 呼叫數字更動方法

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

root = Tk()

label=Label(root,text="raised",relief="raised",
            bg="lightyellow",
            padx=5,pady=10,
            cursor="heart")     # 滑鼠外形
label.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

root = Tk()
label=Label(root,text="Welcome to the United States and have a nice day")
label.pack()        # 包裝與定位元件
print(label.keys())

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *
from tkinter.ttk import Separator

root = Tk()

myTitle = "一個人的極境旅行"
myContent = """2016年12月,我一個人訂了機票和船票,
開始我的南極旅行,飛機經杜拜再往阿根廷的烏斯懷雅,
在此我登上郵輪開始我的南極之旅"""

label1 = Label(root,text=myTitle,
             font="Helvetic 20 bold")
label1.pack(padx=10,pady=10)

sep = Separator(root,orient=HORIZONTAL)
sep.pack(fill=X,padx=5)

label2 = Label(root,text=myContent)
label2.pack(padx=10,pady=10)

root.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15

label1.pack(side=BOTTOM)              # 包裝與定位元件
label2.pack(side=BOTTOM)              # 包裝與定位元件
label3.pack(side=BOTTOM)              # 包裝與定位元件

"""
label1.pack(side=LEFT)                # 包裝與定位元件
label2.pack(side=LEFT)                # 包裝與定位元件
label3.pack(side=LEFT)                # 包裝與定位元件
"""

"""
label1.pack()                         # 包裝與定位元件
label2.pack(side=RIGHT)               # 靠右包裝與定位元件
label3.pack(side=LEFT)                # 靠左包裝與定位元件
"""

window.mainloop()

print('------------------------------------------------------------')	#60個

Reliefs = ["flat","groove","raised","ridge","solid","sunken"]

root = Tk()

for Relief in Reliefs:
    Label(root,text=Relief,relief=Relief,
          fg="blue",
          font="Times 20 bold").pack(side=LEFT,padx=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

bitMaps = ["error","hourglass","info","questhead","question",
           "warning","gray12","gray25","gray50","gray75"]

root = Tk()

for bitMap in bitMaps:
    Label(root,bitmap=bitMap).pack(side=LEFT,padx=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(fill=X)                   # 填滿X軸包裝與定位元件
label2.pack(pady=10)                  # y軸增加10像素
label3.pack(fill=X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(fill=X,pady=10)           # 填滿X軸,Y軸增加10像素
label2.pack(pady=10)                  # Y軸增加10像素
label3.pack(fill=X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
label1.pack(padx=50)                  # 左右邊界間距是50像素
label2.pack(padx=50)                  # 左右邊界間距是50像素
label3.pack(padx=50)                  # 左右邊界間距是50像素

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
label1.pack(side=LEFT)                # 包裝與定位元件
label2.pack(side=LEFT,padx=10)        # 左右間距padx=10
label3.pack(side=LEFT)                # 包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack()                         # 包裝與定位元件
label2.pack(ipadx=10)                 # ipadx=10包裝與定位元件
label3.pack()                         # 包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack()                         # 包裝與定位元件
label2.pack(ipadx=10)                 # ipadx=10包裝與定位元件
label3.pack(ipady=10)                 # ipady=10包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()
root.geometry("300x180")            # 設定視窗勘寬300高180

oklabel=Label(root,text="OK",       # 標籤內容是OK
              font="Times 20 bold", # Times字型20粗體
              fg="white",bg="blue") # 藍底白字
oklabel.pack(anchor=S,side=RIGHT,   # 從右開始在南方配置
             padx=10,pady=10)       # x和y軸間距皆是10

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()
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

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(fill=X)                   # 填滿X軸包裝與定位元件
label2.pack()                         # 包裝與定位元件
label3.pack(fill=X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(fill=X)                   # 填滿X軸包裝與定位元件
label2.pack(fill=Y)                   # 填滿Y軸包裝與定位元件
label3.pack(fill=X)                   # 填滿X軸包裝與定位元件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(side=LEFT)                # 從左配置控件
label2.pack()                         # 預設從上開始配置控件
label3.pack()                         # 預設從上開始配置控件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(side=LEFT,fill=Y)         # 從左配置控件fill=Y
label2.pack(fill=X)                   # 預設從上開始配置控件fill=X
label3.pack()                         # 預設從上開始配置控件

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(side=LEFT,fill=Y)         # 從左配置控件fill=Y
label2.pack(fill=X)                   # 預設從上開始配置控件fill=X
label3.pack(fill=X)                   # 預設從上開始配置控件fill=X

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(side=LEFT,fill=Y)         # 從左配置控件fill=Y
label2.pack(fill=X)                   # 預設從上開始配置控件fill=X
label3.pack(fill=BOTH)                # 預設從上開始配置控件fill=BOTH

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow")     # 標籤背景是淺黃色
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen")      # 標籤背景是淺綠色
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue")       # 標籤背景是淺藍色
label1.pack(side=LEFT,fill=Y)         # 從左配置控件fill=Y
label2.pack(fill=X)                   # 預設從上開始配置控件fill=X
label3.pack(fill=BOTH,expand=True)    # fill=BOTH,expand=True

window.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()
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
    
Label(root,text='Mississippi',bg='red',fg='white',
      font='Times 20 bold').pack(side=LEFT,fill=Y)  
Label(root,text='Kentucky',bg='green',fg='white',
      font='Arial 20 bold italic').pack(side=LEFT,fill=BOTH,expand=True)  
Label(root,text='Purdue',bg='blue',fg='white',
      font='Times 20 bold').pack(side=LEFT,fill=Y)  

root.mainloop() 

print('------------------------------------------------------------')	#60個

root = Tk()
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

label1 = Label(window,text="歡迎來到美國",
             bg="lightyellow",      # 標籤背景是淺黃色
             width=15)              # 標籤寬度是15     
label2 = Label(window,text="歡迎來到美國",
             bg="lightgreen",       # 標籤背景是淺綠色
             width=15)              # 標籤寬度是15            
label3 = Label(window,text="歡迎來到美國",
             bg="lightblue",        # 標籤背景是淺藍色
             width=15)              # 標籤寬度是15
label1.grid(row=0,column=0)           # 格狀包裝
label2.grid(row=1,column=0)           # 格狀包裝
label3.grid(row=1,column=1)           # 格狀包裝

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
             bg="lightyellow",      # 標籤背景是淺黃色
             width=15)              # 標籤寬度是15     
label2 = Label(window,text="歡迎來到美國",
             bg="lightgreen",       # 標籤背景是淺綠色
             width=15)              # 標籤寬度是15            
label3 = Label(window,text="歡迎來到美國",
             bg="lightblue",        # 標籤背景是淺藍色
             width=15)              # 標籤寬度是15
label1.grid(row=0,column=0)           # 格狀包裝
label2.grid(row=1,column=2)           # 格狀包裝
label3.grid(row=2,column=1)           # 格狀包裝

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="標籤1",relief="raised")
label2 = Label(window,text="標籤2",relief="raised")
label3 = Label(window,text="標籤3",relief="raised")
label4 = Label(window,text="標籤4",relief="raised")
label5 = Label(window,text="標籤5",relief="raised")
label6 = Label(window,text="標籤6",relief="raised")
label7 = Label(window,text="標籤7",relief="raised")
label8 = Label(window,text="標籤8",relief="raised")
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=0,column=2)
label4.grid(row=0,column=3)
label5.grid(row=1,column=0)
label6.grid(row=1,column=1)
label7.grid(row=1,column=2)
label8.grid(row=1,column=3)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="標籤1",relief="raised")
label2 = Label(window,text="標籤2",relief="raised")
label4 = Label(window,text="標籤4",relief="raised")
label5 = Label(window,text="標籤5",relief="raised")
label6 = Label(window,text="標籤6",relief="raised")
label7 = Label(window,text="標籤7",relief="raised")
label8 = Label(window,text="標籤8",relief="raised")
label1.grid(row=0,column=0)
label2.grid(row=0,column=1,columnspan=2)
label4.grid(row=0,column=3)
label5.grid(row=1,column=0)
label6.grid(row=1,column=1)
label7.grid(row=1,column=2)
label8.grid(row=1,column=3)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="標籤1",relief="raised")
label2 = Label(window,text="標籤2",relief="raised")
label3 = Label(window,text="標籤3",relief="raised")
label4 = Label(window,text="標籤4",relief="raised")
label5 = Label(window,text="標籤5",relief="raised")
label7 = Label(window,text="標籤7",relief="raised")
label8 = Label(window,text="標籤8",relief="raised")
label1.grid(row=0,column=0)
label2.grid(row=0,column=1,rowspan=2)
label3.grid(row=0,column=2)
label4.grid(row=0,column=3)
label5.grid(row=1,column=0)
label7.grid(row=1,column=2)
label8.grid(row=1,column=3)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="標籤1",relief="raised")
label2 = Label(window,text="標籤2",relief="raised")
label4 = Label(window,text="標籤4",relief="raised")
label5 = Label(window,text="標籤5",relief="raised")
label8 = Label(window,text="標籤8",relief="raised")
label1.grid(row=0,column=0)
label2.grid(row=0,column=1,rowspan=2,columnspan=2)
label4.grid(row=0,column=3)
label5.grid(row=1,column=0)
label8.grid(row=1,column=3)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="標籤1",relief="raised")
label2 = Label(window,text="標籤2",relief="raised")
label3 = Label(window,text="標籤3",relief="raised")
label4 = Label(window,text="標籤4",relief="raised")
label5 = Label(window,text="標籤5",relief="raised")
label6 = Label(window,text="標籤6",relief="raised")
label7 = Label(window,text="標籤7",relief="raised")
label8 = Label(window,text="標籤8",relief="raised")
label1.grid(row=0,column=0,padx=5,pady=5)
label2.grid(row=0,column=1,padx=5,pady=5)
label3.grid(row=0,column=2,padx=5,pady=5)
label4.grid(row=0,column=3,padx=5,pady=5)
label5.grid(row=1,column=0,padx=5)
label6.grid(row=1,column=1,padx=5)
label7.grid(row=1,column=2,padx=5)
label8.grid(row=1,column=3,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國")
label2 = Label(window,bg="yellow",width=20)
label3 = Label(window,text="歡迎來到美國")
label4 = Label(window,bg="aqua",width=20)
label1.grid(row=0,column=0,padx=5,pady=5)
label2.grid(row=0,column=1,padx=5,pady=5)
label3.grid(row=1,column=0,padx=5)
label4.grid(row=1,column=1,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國")
label2 = Label(window,bg="yellow",width=20)
label3 = Label(window,text="歡迎來到美國")
label4 = Label(window,bg="aqua",width=20)
label1.grid(row=0,column=0,padx=5,pady=5,sticky=W)
label2.grid(row=0,column=1,padx=5,pady=5)
label3.grid(row=1,column=0,padx=5)
label4.grid(row=1,column=1,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",relief="raised")
label2 = Label(window,bg="yellow",width=20)
label3 = Label(window,text="歡迎來到美國",relief="raised")
label4 = Label(window,bg="aqua",width=20)
label1.grid(row=0,column=0,padx=5,pady=5)
label2.grid(row=0,column=1,padx=5,pady=5)
label3.grid(row=1,column=0,padx=5)
label4.grid(row=1,column=1,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",relief="raised")
label2 = Label(window,bg="yellow",width=20)
label3 = Label(window,text="歡迎來到美國",relief="raised")
label4 = Label(window,bg="aqua",width=20)
label1.grid(row=0,column=0,padx=5,pady=5,sticky=W+E)
label2.grid(row=0,column=1,padx=5,pady=5)
label3.grid(row=1,column=0,padx=5)
label4.grid(row=1,column=1,padx=5)

window.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

Colors = ["red","orange","yellow","green","blue","purple"]

r = 0                               # row編號
for color in Colors:
    Label(root,text=color,relief="groove",width=20).grid(row=r,column=0)
    Label(root,bg=color,relief="ridge",width=20).grid(row=r,column=1)
    r += 1

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

label1 = Label(root,text="Label 1",bg="pink")
label1.grid(row=0,column=0,padx=5,pady=5)

label2 = Label(root,text="Label 2",bg="lightblue")
label2.grid(row=0,column=1,padx=5,pady=5)

label3 = Label(root,bg="yellow")
label3.grid(row=1,column=0,columnspan=2,padx=5,pady=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

label1 = Label(root,text="Label 1",bg="pink")
label1.grid(row=0,column=0,padx=5,pady=5,stick=W)

label2 = Label(root,text="Label 2",bg="lightblue")
label2.grid(row=0,column=1,padx=5,pady=5)

label3 = Label(root,bg="yellow")
label3.grid(row=1,column=0,columnspan=2,padx=5,pady=5,
          sticky=N+S+W+E)

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

label1 = Label(root,text="Label 1",bg="pink")
label1.grid(row=0,column=0,padx=5,pady=5,stick=W+E)

label2 = Label(root,text="Label 2",bg="lightblue")
label2.grid(row=0,column=1,padx=5,pady=5)

label3 = Label(root,bg="yellow")
label3.grid(row=1,column=0,columnspan=2,padx=5,pady=5,
          sticky=N+S+W+E)

root.mainloop()

print('------------------------------------------------------------')	#60個

window = Tk()

label1 = Label(window,text="歡迎來到美國",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
label2 = Label(window,text="歡迎來到美國",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
label3 = Label(window,text="歡迎來到美國",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
label1.place(x=0,y=0)                 # 直接定位
label2.place(x=30,y=50)               # 直接定位
label3.place(x=60,y=100)              # 直接定位

window.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

root = Tk()

btn = Button(root,text="列印訊息",command=msgShow)
btn.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

root = Tk()

btn1 = Button(root,text="列印訊息",width=15,command=msgShow)
btn2 = Button(root,text="結束",width=15,command=root.destroy)
                      
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

counter = 0                                 # 計數的全域變數
def run_counter(digit):                     # 數字變數內容的更動
    def counting():                         # 更動數字方法
        global counter
        counter += 1                        # 定義這是全域變數
        digit.config(text=str(counter))     # 列出標籤數字內容
        digit.after(1000,counting)          # 隔一秒後呼叫counting
    counting()                              # 持續呼叫

root = Tk()

digit=Label(root,bg="yellow",fg="blue",     # 黃底藍字
            height=3,width=10,              # 寬10高3
            font="Helvetica 20 bold")       # 字型設定
digit.pack()
run_counter(digit)                          # 呼叫數字更動方法
Button(root,text="結束",width=15,command=root.destroy).pack(pady=10)

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

def yellow():                   # 設定視窗背景是黃色
    root.config(bg="yellow")
def blue():                     # 設定視窗背景是藍色
    root.config(bg="blue")
    
root = Tk()
root.geometry("300x200")        # 固定視窗大小

# 依次建立3個鈕
exitbtn = Button(root,text="Exit",command=root.destroy)
bluebtn = Button(root,text="Blue",command=blue)
yellowbtn = Button(root,text="Yellow",command=yellow)
# 將3個鈕包裝定位在右下方
exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

def bColor(bgColor):          # 設定視窗背景顏色
    root.config(bg=bgColor)
    
root = Tk()
root.geometry("300x200")        # 固定視窗大小

# 依次建立3個鈕
exitbtn = Button(root,text="Exit",command=root.destroy)
bluebtn = Button(root,text="Blue",command=lambda:bColor("blue"))
yellowbtn = Button(root,text="Yellow",command=lambda:bColor("yellow"))
# 將3個鈕包裝定位在右下方
exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

root = Tk()

lab  = Label(root,text="",bg="yellow",width=20)
btn7 = Button(root,text="7",width=3)
btn8 = Button(root,text="8",width=3)
btn9 = Button(root,text="9",width=3)
btnM = Button(root,text="*",width=3)                # 乘法符號
btn4 = Button(root,text="4",width=3)
btn5 = Button(root,text="5",width=3)
btn6 = Button(root,text="6",width=3)
btnS = Button(root,text="-",width=3)                # 減法符號
btn1 = Button(root,text="1",width=3)
btn2 = Button(root,text="2",width=3)
btn3 = Button(root,text="3",width=3)
btnP = Button(root,text="+",width=3)                # 加法符號
btn0 = Button(root,text="0",width=8)
btnD = Button(root,text=".",width=3)                # 小數點符號
btnE = Button(root,text="=",width=3)                # 等號符號

lab.grid(row=0,column=0,columnspan=4)
btn7.grid(row=1,column=0,padx=5)
btn8.grid(row=1,column=1,padx=5)
btn9.grid(row=1,column=2,padx=5)
btnM.grid(row=1,column=3,padx=5)                    # 乘法符號
btn4.grid(row=2,column=0,padx=5)
btn5.grid(row=2,column=1,padx=5)
btn6.grid(row=2,column=2,padx=5)
btnS.grid(row=2,column=3,padx=5)                    # 減法符號
btn1.grid(row=3,column=0,padx=5)
btn2.grid(row=3,column=1,padx=5)
btn3.grid(row=3,column=2,padx=5)
btnP.grid(row=3,column=3,padx=5)                    # 加法符號
btn0.grid(row=4,column=0,padx=5,columnspan=2)
btnD.grid(row=4,column=2,padx=5)                    # 小數點符號
btnE.grid(row=4,column=3,padx=5)                    # 等號符號

root.mainloop()

print('------------------------------------------------------------')	#60個

root = Tk()

nameL = Label(root,text="Name ")        # name標籤
nameL.grid(row=0)
addressL = Label(root,text="Address")   # address標籤
addressL.grid(row=1)

nameE = Entry(root)                     # 文字方塊name
addressE = Entry(root)                  # 文字方塊address
nameE.grid(row=0,column=1)              # 定位文字方塊name
addressE.grid(row=1,column=1)           # 定位文字方塊address

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

root = Tk()

accountL = Label(root,text="Account")   # account標籤
accountL.grid(row=0)
pwdL = Label(root,text="Password")      # pwd標籤
pwdL.grid(row=1)

accountE = Entry(root)                  # 文字方塊account
pwdE = Entry(root,show="*")             # 文字方塊pwd
accountE.grid(row=0,column=1)           # 定位文字方塊account
pwdE.grid(row=1,column=1)               # 定位文字方塊pwd

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

def cal():                          # 執行數學式計算
    out.configure(text = "結果 : " + str(eval(equ.get())))
    
root = Tk()

label = Label(root, text="請輸入數學表達式:")
label.pack()

equ = Entry(root)                   # 在此輸入表達式
equ.pack(pady=5)                    

out = Label(root)                   # 存放計算結果
out.pack()                          

btn = Button(root,text="計算",command=cal)    # 計算按鈕
btn.pack(pady=5)

root.mainloop()

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

print('------------------------------------------------------------')	#60個

from tkinter import *

def btn_hit():                      # 處理按鈕事件
    if x.get() == "":               # 如果目前是空字串
        x.set("I like tkinter")     # 顯示文字
    else:
        x.set("")                   # 不顯示文字
   
root = Tk()
    
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

from tkinter import *

def callback(*args):
    print("data changed : ",xE.get())   # Python Shell視窗輸出
   
root = Tk()
    
xE = StringVar()                        # Entry的變數內容
entry = Entry(root,textvariable=xE)     # 設定Label內容是變數x
entry.pack(pady=5,padx=10)
xE.trace("w",callback)                  # 若是有更改執行callback

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

def callback(*args):
    xL.set(xE.get())                    # 更改標籤內容
    print("data changed : ",xE.get())   # Python Shell視窗輸出
   
root = Tk()
    
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

from tkinter import *

def callbackW(*args):                   # 內容被更改時執行
    xL.set(xE.get())                    # 更改標籤內容

def callbackR(*args):                   # 內容被讀取時執行
    print("Warning:資料被讀取!")

def hit():                              # 讀取資料
    print("讀取資料:",xE.get())
  
root = Tk()
    
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

from tkinter import *

def callbackW(name,index,mode):         # 內容被更改時執行
    xL.set(xE.get())                    # 更改標籤內容
    print("name = %r, index = %r, mode = %r" % (name,index,mode)) 
  
root = Tk()
    
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

'''
print('------------------------------------------------------------')	#60個

print('把圖片顯示在Label上')
filename = 'C:/_git/vcs/_4.python/_data/lena_color.png'

root = Tk()
root.geometry("800x600")

night = PhotoImage(file=filename)
label1 = Label(root,image=night)
label1.place(x=0,y=0,width=512,height=512)

label2=Label(root,image=night)
label2.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

root.mainloop()

print('------------------------------------------------------------')	#60個

print('把圖片顯示在Label上')

filename = 'C:/_git/vcs/_4.python/_data/lena_color.png'

root = Tk()
root.geometry("640x480")

night = PhotoImage(file=filename)
label=Label(root,image=night)
label.place(relx=0.1,rely=0.1,relheight=0.8)

print('把圖片顯示在Button上')

sunGif = PhotoImage(file="sun.gif")                 # Image物件
btn = Button(root,image=sunGif,command=msgShow)     # 含影像的按鈕
btn.pack()

root.mainloop()

print('------------------------------')	#60個

from tkinter import *
      
root = Tk()

sunGif = PhotoImage(file="sun.gif")                 # Image物件
btn = Button(root,image=sunGif,command=msgShow,     # 含文字與影像的按鈕
             text="Click Me",compound=TOP)          

btn.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

root = Tk()

sunGif = PhotoImage(file="sun.gif")                 # Image物件
btn = Button(root,image=sunGif,command=msgShow,     # 含文字與影像的按鈕
             text="Click Me",compound=CENTER)          
btn.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

root = Tk()

sunGif = PhotoImage(file="sun.gif")                 # Image物件
btn = Button(root,image=sunGif,command=msgShow,     # 含文字與影像的按鈕
             text="Click Me",compound=LEFT)          
btn.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

root = Tk()

sunGif = PhotoImage(file="sun.gif")                 # Image物件
btn = Button(root,image=sunGif,command=msgShow,     # 含影像的按鈕
             cursor="star")                         # star外形   
btn.pack()

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

root = Tk()

msg = "歡迎進入Silicon Stone Educaiton系統"
sseGif = PhotoImage(file="sse.gif")     # Logo影像檔
logo = Label(root,image=sseGif,text=msg,compound=BOTTOM)
accountL = Label(root,text="Account")   # account標籤
accountL.grid(row=1)
pwdL = Label(root,text="Password")      # pwd標籤
pwdL.grid(row=2)

logo.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
accountE = Entry(root)                  # 文字方塊account
pwdE = Entry(root,show="*")             # 文字方塊pwd
accountE.grid(row=1,column=1)           # 定位文字方塊account
pwdE.grid(row=2,column=1,pady=10)       # 定位文字方塊pwd

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *
def printInfo():                        # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (accountE.get(),pwdE.get()))
    
root = Tk()

msg = "歡迎進入Silicon Stone Educaiton系統"
sseGif = PhotoImage(file="sse.gif")     # Logo影像檔
logo = Label(root,image=sseGif,text=msg,compound=BOTTOM)
accountL = Label(root,text="Account")   # account標籤
accountL.grid(row=1)
pwdL = Label(root,text="Password")      # pwd標籤
pwdL.grid(row=2)

logo.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
accountE = Entry(root)                  # 文字方塊account
pwdE = Entry(root,show="*")             # 文字方塊pwd
accountE.grid(row=1,column=1)           # 定位文字方塊account
pwdE.grid(row=2,column=1,pady=10)       # 定位文字方塊pwd
# 以下建立Login和Quit案鈕
loginbtn = Button(root,text="Login",command=printInfo)
loginbtn.grid(row=3,column=0)
quitbtn = Button(root,text="Quit",command=root.quit)
quitbtn.grid(row=3,column=1)

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

def printInfo():                        # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (accountE.get(),pwdE.get()))
    
root = Tk()

msg = "歡迎進入Silicon Stone Educaiton系統"
sseGif = PhotoImage(file="sse.gif")     # Logo影像檔
logo = Label(root,image=sseGif,text=msg,compound=BOTTOM)
accountL = Label(root,text="Account")   # account標籤
accountL.grid(row=1)
pwdL = Label(root,text="Password")      # pwd標籤
pwdL.grid(row=2)

logo.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
accountE = Entry(root)                  # 文字方塊account
pwdE = Entry(root,show="*")             # 文字方塊pwd
accountE.grid(row=1,column=1)           # 定位文字方塊accou
pwdE.grid(row=2,column=1,pady=10)       # 定位文字方塊pwd
# 以下建立Login和Quit案鈕
loginbtn = Button(root,text="Login",command=printInfo)
loginbtn.grid(row=3,column=0,sticky=W,pady=5)
quitbtn = Button(root,text="Quit",command=root.quit)
quitbtn.grid(row=3,column=1,sticky=W,pady=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *
def printInfo():                        # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (accountE.get(),pwdE.get()))
    
root = Tk()

msg = "歡迎進入Silicon Stone Educaiton系統"
sseGif = PhotoImage(file="sse.gif")     # Logo影像檔
logo = Label(root,image=sseGif,text=msg,compound=BOTTOM)
accountL = Label(root,text="Account")   # account標籤
accountL.grid(row=1)
pwdL = Label(root,text="Password")      # pwd標籤
pwdL.grid(row=2)

logo.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
accountE = Entry(root)                  # 文字方塊account
pwdE = Entry(root,show="*")             # 文字方塊pwd
accountE.insert(0,"Kevin")              # 預設Account內容
pwdE.insert(0,"pwd")                    # 預設pwd內容
accountE.grid(row=1,column=1)           # 定位文字方塊accou
pwdE.grid(row=2,column=1,pady=10)       # 定位文字方塊pwd
# 以下建立Login和Quit案鈕
loginbtn = Button(root,text="Login",command=printInfo)
loginbtn.grid(row=3,column=0,sticky=W,pady=5)
quitbtn = Button(root,text="Quit",command=root.quit)
quitbtn.grid(row=3,column=1,sticky=W,pady=5)

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter import *

def printInfo():                        # 列印輸入資訊
    print("Account: %s\nPassword: %s" % (accountE.get(),pwdE.get()))
    accountE.delete(0,END)              # 刪除account文字方塊的帳號內容
    pwdE.delete(0,END)                  # 刪除pwd文字方塊的密碼內容
    
root = Tk()

msg = "歡迎進入Silicon Stone Educaiton系統"
sseGif = PhotoImage(file="sse.gif")     # Logo影像檔
logo = Label(root,image=sseGif,text=msg,compound=BOTTOM)
accountL = Label(root,text="Account")   # account標籤
accountL.grid(row=1)
pwdL = Label(root,text="Password")      # pwd標籤
pwdL.grid(row=2)

logo.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
accountE = Entry(root)                  # 文字方塊account
pwdE = Entry(root,show="*")             # 文字方塊pwd
accountE.insert(1,"Kevin")              # 預設Account內容
pwdE.insert(1,"pwd")                    # 預設pwd內容
accountE.grid(row=1,column=1)           # 定位文字方塊accou
pwdE.grid(row=2,column=1,pady=10)       # 定位文字方塊pwd
# 以下建立Login和Quit案鈕
loginbtn = Button(root,text="Login",command=printInfo)
loginbtn.grid(row=3,column=0,sticky=W,pady=5)
quitbtn = Button(root,text="Quit",command=root.quit)
quitbtn.grid(row=3,column=1,sticky=W,pady=5)

root.mainloop()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


