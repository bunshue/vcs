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


