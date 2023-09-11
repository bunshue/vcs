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




