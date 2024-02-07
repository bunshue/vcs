from tkinter import Tk, Frame, Button
from datetime import date #滙入datetime模組的date類別

#宣告類別
class wndApp(Frame):
    
    #方法一：初始化物件，加入主視窗版面
    def __init__(self, ruler = None):
        Frame.__init__(self, ruler)
        # 呼叫主視窗物件以pack()方法將自己加入
        self.pack()
        self.makeComponent()
        
    #方法二：定義按鈕元件的相關屬性值
    def makeComponent(self):
        self.day_is = Button(self)
        
        #按鈕上欲顯示的文字
        self.day_is['text'] = '我是 按鈕\n(Click Me..)'
        
        #按下按鈕由command執行動作，此處呼叫方法display()
        self.day_is['command'] = self.display
        
        # 設定按鈕在主視窗左側，藍色文字，被按下後，關閉主視窗並做資源的釋放
        self.day_is.pack(side = 'left')
        self.QUIT = Button(self, text = 'QUIT',
                fg = 'blue', command = wnd.destroy)
        # 設定按鈕在主視窗右側
        self.QUIT.pack(side = 'right')
        
    #方法三：按下按鈕後會以date類別呼叫today()顯示今天的日期
    def display(self):
        today = date.today()
        print('Day is', today)
        
# 呼叫Tk()建構函式產生主視窗
wnd = Tk()
# 實體化wndApp類別，以主視窗物件為引數做初始化動作
# 然後加入Frame元件，再由Frame加入兩個按鈕
work = wndApp(ruler = wnd)
# 讓視窗程式開始做訊息化輸出
work.mainloop()





print('------------------------------------------------------------')	#60個


from tkinter import *

#建立Frame子類別
class appWork(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()

#產生Frame子類別物件
work = appWork()

# 顯示於視窗標題列
work.master.title('Python GUI')
work.master.maxsize(500, 250)

# 視窗訊息初始化
work.mainloop()


print('------------------------------------------------------------')	#60個



from tkinter import *

# 呼叫Tk()建構式產生主視窗
wnd = Tk()

# 顯示主視窗標題列的文字
wnd.title('Button state...')

#Button屬性state的常數值
state = ['normal', 'active', 'disabled']

#for廻圈配合state參數值顯示按鈕狀態
for item in state:
    btn = Button(wnd, text = item, state = item)
    btn.pack()    #以元件加入主視窗
wnd.mainloop()



print('------------------------------------------------------------')	#60個


from tkinter import *

# 呼叫Tk()建構式產生主視窗
root = Tk()
# 方法title()顯示主視窗標題列的文字
root.title('秒數計算中...')
# 呼叫geometry()設視窗大小
root.geometry('100x100+150+150')

counter = 0 #儲存數值

# 自訂函式一：顯示標籤(Label)元件
def display(label):
   counter = 0
   
   # 自訂函式二
   def count():
      global counter #全域變數
      counter += 1
      label.config(text = str(counter),
         bg = 'pink', width = 20, height = 2)
      label.after(1000, count)
   count()
   
#設定標籤並把它放入主視窗
show = Label(root, fg = 'gray')
show.pack()
display(show)

# 設定按鈕
btnStop = Button(root, text = 'Stop',
    width = 20, command = root.destroy)
btnStop.pack()
root.mainloop()





print('------------------------------------------------------------')	#60個


"""
使用tkinter创建GUI
- 顶层窗口
- 控件
- 布局
- 事件回调

"""
import tkinter
import tkinter.messagebox

def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('240x160')
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()

if __name__ == '__main__':
    main()



print('------------------------------------------------------------')	#60個

"""
使用tkinter创建GUI
- 使用画布绘图
- 处理鼠标事件

"""
import tkinter

def mouse_evt_handler(evt=None):
    row = round((evt.y - 20) / 40)
    col = round((evt.x - 20) / 40)
    pos_x = 40 * col
    pos_y = 40 * row
    canvas.create_oval(pos_x, pos_y, 40 + pos_x, 40 + pos_y, fill='black')

top = tkinter.Tk()
# 设置窗口尺寸
top.geometry('620x620')
# 设置窗口标题
top.title('五子棋')
# 设置窗口大小不可改变
top.resizable(False, False)
# 设置窗口置顶
top.wm_attributes('-topmost', 1)
canvas = tkinter.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
canvas.bind('<Button-1>', mouse_evt_handler)
canvas.create_rectangle(0, 0, 600, 600, fill='yellow', outline='white')
for index in range(15):
    canvas.create_line(20, 20 + 40 * index, 580, 20 + 40 * index, fill='black')
    canvas.create_line(20 + 40 * index, 20, 20 + 40 * index, 580, fill='black')
canvas.create_rectangle(15, 15, 585, 585, outline='black', width=4)
canvas.pack()
tkinter.mainloop()

# 请思考如何用面向对象的编程思想对上面的代码进行封装



print('------------------------------------------------------------')	#60個



"""

使用tkinter创建GUI
- 在窗口上制作动画

"""

import tkinter
import time

# 播放动画效果的函数
def play_animation():
    canvas.move(oval, 2, 2)
    canvas.update()
    top.after(50, play_animation)


x = 10
y = 10
top = tkinter.Tk()
top.geometry('600x600')
top.title('动画效果')
top.resizable(False, False)
top.wm_attributes('-topmost', 1)
canvas = tkinter.Canvas(top, width=600, height=600, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, 600, 600, fill='gray')
oval = canvas.create_oval(10, 10, 60, 60, fill='red')
canvas.pack()
top.update()
play_animation()
tkinter.mainloop()

# 请思考如何让小球碰到屏幕的边界就弹回
# 请思考如何用面向对象的编程思想对上面的代码进行封装


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個



