import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext #导入滚动文本框的模块
win = tk.Tk()
win.title("Python GUI") # 加标题
#创建一个容器,
monty = ttk.LabelFrame(win, text=" Monty Python ") #创建一个容器，其父容器为win
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
        win.configure(background=colors[0])#设置整个界面的背景颜色
        print(radVar.get())
    elif radSel == 1:
        win.configure(background=colors[1])
    elif radSel == 2:
        win.configure(background=colors[2])
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
win.mainloop()#当调用mainloop()时,窗口才会显示出来
