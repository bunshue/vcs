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
