from tkinter import *  
#创建Tk对象，Tk代表窗口
root = Tk()
#设置窗口标题
root.title('窗口标题')
#创建Label对象，第一个参数指定该Label放入root
w = Label(root, text="Hello Tkinter!")
#调用pack进行布局
w.pack()
#启动主窗口的消息循环
root.mainloop()
