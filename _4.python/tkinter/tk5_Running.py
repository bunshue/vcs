"""
# 會動的tk範例

"""

import sys

print("------------------------------------------------------------")  # 60個

import tkinter as tk
import tkinter.ttk as ttk



print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.title('秒數計算中...')
window.geometry('100x100+150+150')

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
show = tk.Label(window, fg = 'gray')
show.pack()
display(show)

# 設定按鈕
btnStop = tk.Button(window, text = 'Stop',
    width = 20, command = window.destroy)
btnStop.pack()

window.mainloop()


print("------------------------------------------------------------")  # 60個

import random           

def update_data():
    # 更新標籤顯示的數據為1到100的隨機數
    label_data.config(text=str(random.randint(1, 100)))
    # 每1000毫秒(即1秒)後再次調用update_data函數更新數據
    window.after(1000, update_data)

window = tk.Tk()
window.title("數據監控")                      # 視窗標題
# 建立一個標籤用於顯示數據, 初始值為0, 字體設置為Helvetica, 大小為48
label_data = tk.Label(window, text="0", font=("Helvetica", 48))
label_data.pack()                           # 將標籤添加到視窗中
update_data()           # 呼叫update_data( )函數以開始數據更新過程

window.mainloop()


print("------------------------------------------------------------")  # 60個

import time

tk = Tk()
canvas= Canvas(tk, width=500, height=150)
canvas.pack()
canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
for x in range(0, 80):
    canvas.move(1, 5, 0)        # ID=1 x軸移動5像素, y軸不變
    tk.update()                 # 強制tkinter重繪
    time.sleep(0.05)

print("------------------------------------------------------------")  # 60個

import time

tk = Tk()
canvas= Canvas(tk, width=500, height=300)
canvas.pack()
canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
for x in range(0, 80):
    canvas.move(1, 5, 2)        # ID=1 x軸移動5像素, y軸移動2像素
    tk.update()                 # 強制tkinter重繪
    time.sleep(0.05)

print("------------------------------------------------------------")  # 60個

tk = Tk()
canvas= Canvas(tk, width=500, height=300)
canvas.pack()
canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
for x in range(0, 80):
    canvas.move(1, 5, 2)        # ID=1 x軸移動5像素, y軸移動2像素
    tk.update()                 # 強制tkinter重繪
    canvas.after(50)

print("------------------------------------------------------------")  # 60個

import time

tk = Tk()
canvas= Canvas(tk, width=500, height=250)
canvas.pack()
id1 = canvas.create_oval(10,50,60,100,fill='yellow')
id2 = canvas.create_oval(10,150,60,200,fill='aqua')
for x in range(0, 80):
    canvas.move(id1, 5, 0)      # id1 x軸移動5像素, y軸移動0像素
    canvas.move(id2, 5, 0)      # id2 x軸移動5像素, y軸移動0像素
    tk.update()                 # 強制tkinter重繪
    time.sleep(0.05)

print("------------------------------------------------------------")  # 60個

from random import *
import time

tk = Tk()
canvas= Canvas(tk, width=500, height=250)
canvas.pack()
id1 = canvas.create_oval(10,50,60,100,fill='yellow')
id2 = canvas.create_oval(10,150,60,200,fill='aqua')
for x in range(0, 100):
    if randint(1,100) > 70:
        canvas.move(id2, 5, 0)  # id2 x軸移動5像素, y軸移動0像素
    else:
        canvas.move(id1, 5, 0)  # id1 x軸移動5像素, y軸移動0像素    
    tk.update()                 # 強制tkinter重繪
    time.sleep(0.05)

print("------------------------------------------------------------")  # 60個

import time
def ballMove(event):
    if event.keysym == 'Left':  # 左移
        canvas.move(1, -5, 0)
    if event.keysym == 'Right': # 右移
        canvas.move(1, 5, 0)
    if event.keysym == 'Up':    # 上移
        canvas.move(1, 0, -5)
    if event.keysym == 'Down':  # 下移
        canvas.move(1, 0, 5)
tk = Tk()
canvas= Canvas(tk, width=500, height=300)
canvas.pack()
canvas.create_oval(225,125,275,175,fill='red')
canvas.bind_all('<KeyPress-Left>', ballMove)
canvas.bind_all('<KeyPress-Right>', ballMove)
canvas.bind_all('<KeyPress-Up>', ballMove)
canvas.bind_all('<KeyPress-Down>', ballMove)
mainloop()

print("------------------------------------------------------------")  # 60個

window = Tk() 
        
xWidth = 300
yHeight = 100
canvas = Canvas(window, width=xWidth, height=yHeight)
canvas.pack()
        
x = 0
yMsg = 45
canvas.create_text(x, yMsg, text="王者歸來", tags="msg")
        
dx = 5
while True:
    canvas.move("msg", dx, 0)  
    canvas.after(100)       
    canvas.update()         
    if x < xWidth:
        x += dx             
    else:
        x = 0               
        canvas.delete("msg")                             
        canvas.create_text(x, yMsg, text = "王者歸來", tags = "msg")
                
window.mainloop() 

print("------------------------------------------------------------")  # 60個


def up(event):
    global y
    canvas.create_line(x, y, x, y - 5)
    y -= 5       
def down(event):
    global y
    canvas.create_line(x, y, x, y + 5)
    y += 5       
def left(event):
    global x
    canvas.create_line(x, y, x - 5, y)
    x -= 5  
def right(event):
    global x
    canvas.create_line(x, y, x + 5, y)
    x += 5

xWidth = 200
yHeight = 200

window = Tk() 

canvas = Canvas(window, width=xWidth, height=yHeight)
canvas.pack()

x = xWidth / 2
y = yHeight / 2
       
canvas.bind("<Up>", up)
canvas.bind("<Down>", down)
canvas.bind("<Left>", left)
canvas.bind("<Right>", right)
canvas.focus_set()
        
window.mainloop() 

print("------------------------------------------------------------")  # 60個


def displayFan(startingAngle):
    canvas.delete("fan")    
    canvas.create_arc(xWidth / 2 - r, yHeight / 2 - r, xWidth / 2 + r, yHeight / 2 + r,
            start = startAngle + 0, extent = 60, fill = "green", tags = "fan")        
    canvas.create_arc(xWidth / 2 - r, yHeight / 2 - r, xWidth / 2 + r, yHeight / 2 + r,
            start = startAngle + 120, extent = 60, fill = "green", tags = "fan")        
    canvas.create_arc(xWidth / 2 - r, yHeight / 2 - r, xWidth / 2 + r, yHeight / 2 + r,
            start = startAngle + 240, extent = 60, fill = "green", tags = "fan")        

xWidth = 300
yHeight = 300
r = 120

window = Tk() 
        
canvas = Canvas(window,width=xWidth, height=yHeight)
canvas.pack()

startAngle = 0
while True:
    startAngle += 5
    displayFan(startAngle)
    canvas.after(50) 
    canvas.update()
            
window.mainloop() 

print("------------------------------------------------------------")  # 60個

from random import *

def display():
    if Flag:       
        if ball.get() == "1":
            raceResult.set("恭喜你贏了, Ball 1勝利")
        else:
            raceResult.set("抱歉你輸了, Ball 1勝利")
    else:
        if ball.get() == "1":
            raceResult.set("抱歉你輸了, Ball 2勝利")
        else:
            raceResult.set("恭喜你贏了, Ball 2勝利")
    startBtn.set("重置")

def running():
    global Flag
    if startBtn.get() == "重置":
        startBtn.set("開始")
        raceResult.set("")
        canvas.delete('all')
        canvas.create_text(10,50,text="1")
        id1 = canvas.create_oval(20,50,70,100,fill='yellow')
        canvas.create_text(10,150,text="2")
        id2 = canvas.create_oval(20,150,70,200,fill='aqua')
        return
    canvas.delete('all')
    canvas.create_text(10,50,text="1")
    id1 = canvas.create_oval(20,50,70,100,fill='yellow')
    canvas.create_text(10,150,text="2")
    id2 = canvas.create_oval(20,150,70,200,fill='aqua')
    id1Loc, id2Loc = 0, 0
    for x in range(0, 100):
        if ball.get() == '1':
            weight = 40
            raceResult.set("")
        elif ball.get() == '2':
            weight = 60
            raceResult.set("")
        else:
            raceResult.set("輸入錯誤!")
            return
        if randint(1,100) > weight:
            canvas.move(id2, 5, 0)  # id2 x軸移動5像素, y軸移動0像素
            id2Loc += 1
        else:
            canvas.move(id1, 5, 0)  # id1 x軸移動5像素, y軸移動0像素
            id1Loc += 1
        tk.update()                 # 強制tkinter重繪
        canvas.after(50)
    if id1Loc > id2Loc:
        Flag = True
    else:
        Flag = False
    display()

tk = Tk()
canvas= Canvas(tk, width=500, height=250)
canvas.pack()
canvas.create_text(10,50,text="1")
canvas.create_oval(20,50,70,100,fill='yellow')
canvas.create_text(10,150,text="2")
canvas.create_oval(20,150,70,200,fill='aqua')

Flag = True                         # 判斷那一球勝利

frame = Frame(tk)                   # 建立框架
frame.pack(padx=5, pady=5)
# 在框架Frame內建立標籤Label, 輸入獲勝的球, 按鈕Button
Label(frame, text="那一個球獲勝 : ").pack(side=LEFT)
ball = StringVar()
ball.set("1or2")
entry = Entry(frame, textvariable=ball).pack(side=LEFT,padx=3)
startBtn = StringVar()
startBtn.set("開始")
Button(frame, textvariable=startBtn,command=running).pack(side=LEFT)
raceResult = StringVar()

Label(frame,width=16,textvariable=raceResult).pack(side=LEFT,padx=3)

tk.mainloop()

print("------------------------------------------------------------")  # 60個

from random import *
import time

class Ball:
    def __init__(self, canvas, color, winW, winH):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)  # 建立球物件
        self.canvas.move(self.id, winW/2, winH/2)   # 設定球最初位置
    def ballMove(self):
        self.canvas.move(self.id, 0, step)      # step是正值表示往下移動

winW = 640                                      # 定義畫布寬度
winH = 480                                      # 定義畫布高度
step = 3                                        # 定義速度可想成位移步伐
speed = 0.03                                    # 設定移動速度

tk = Tk()
tk.title("Bouncing Ball")

tk.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = Canvas(tk, width=winW, height=winH)
canvas.pack()
tk.update()

ball = Ball(canvas, 'yellow', winW, winH)       # 定義球物件

while True:
    ball.ballMove()
    tk.update()
    time.sleep(speed)                           # 可以控制移動速度

print("------------------------------------------------------------")  # 60個

tk = Tk()
canvas= Canvas(tk, width=500, height=150)
canvas.pack()
id = canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
ballPos = canvas.coords(id)
print(ballPos)

print("------------------------------------------------------------")  # 60個

from random import *
import time

class Ball:
    def __init__(self, canvas, color, winW, winH):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)  # 建立球物件
        self.canvas.move(self.id, winW/2, winH/2)   # 設定球最初位置
        self.x = 0                                  # 水平不移動
        self.y = step                               # 垂直移動單位
    def ballMove(self):
        self.canvas.move(self.id, self.x, self.y)   # step是正值表示往下移動
        ballPos = self.canvas.coords(self.id)
        if ballPos[1] <= 0:                     # 偵測球是否超過畫布上方
            self.y = step
        if ballPos[3] >= winH:                  # 偵測球是否超過畫布下方
            self.y = -step
        
winW = 640                                      # 定義畫布寬度
winH = 480                                      # 定義畫布高度
step = 3                                        # 定義速度可想成位移步伐
speed = 0.01                                    # 設定移動速度

tk = Tk()
tk.title("Bouncing Ball")

tk.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = Canvas(tk, width=winW, height=winH)
canvas.pack()
tk.update()

ball = Ball(canvas, 'yellow', winW, winH)       # 定義球物件

while True:
    ball.ballMove()
    tk.update()
    time.sleep(speed)                           # 可以控制移動速度

print("------------------------------------------------------------")  # 60個

from random import *
import time

class Ball:
    def __init__(self, canvas, color, winW, winH):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)  # 建立球物件
        self.canvas.move(self.id, winW/2, winH/2)   # 設定球最初位置
        startPos = [-4, -3, -2, -1, 1, 2, 3, 4]     # 球最初x軸位移的隨機數
        shuffle(startPos)                           # 打亂排列
        self.x = startPos[0]                        # 球最初水平移動單位
        self.y = step                               # 垂直移動單位
    def ballMove(self):
        self.canvas.move(self.id, self.x, self.y)   # step是正值表示往下移動
        ballPos = self.canvas.coords(self.id)
        if ballPos[0] <= 0:                     # 偵測球是否超過畫布左方
            self.x = step
        if ballPos[1] <= 0:                     # 偵測球是否超過畫布上方
            self.y = step
        if ballPos[2] >= winW:                  # 偵測球是否超過畫布右方
            self.x = -step
        if ballPos[3] >= winH:                  # 偵測球是否超過畫布下方
            self.y = -step
        
winW = 640                                      # 定義畫布寬度
winH = 480                                      # 定義畫布高度
step = 3                                        # 定義速度可想成位移步伐
speed = 0.01                                    # 設定移動速度

tk = Tk()
tk.title("Bouncing Ball")

tk.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = Canvas(tk, width=winW, height=winH)
canvas.pack()
tk.update()

ball = Ball(canvas, 'yellow', winW, winH)       # 定義球物件

while True:
    ball.ballMove()
    tk.update()
    time.sleep(speed)                           # 可以控制移動速度

print("------------------------------------------------------------")  # 60個

from random import *
import time

class Ball:
    def __init__(self, canvas, color, winW, winH):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)  # 建立球物件
        self.canvas.move(self.id, winW/2, winH/2)   # 設定球最初位置
        startPos = [-4, -3, -2, -1, 1, 2, 3, 4]     # 球最初x軸位移的隨機數
        shuffle(startPos)                           # 打亂排列
        self.x = startPos[0]                        # 球最初水平移動單位
        self.y = step                               # 垂直移動單位
    def ballMove(self):
        self.canvas.move(self.id, self.x, self.y)   # step是正值表示往下移動
        ballPos = self.canvas.coords(self.id)
        if ballPos[0] <= 0:                     # 偵測球是否超過畫布左方
            self.x = step
        if ballPos[1] <= 0:                     # 偵測球是否超過畫布上方
            self.y = step
        if ballPos[2] >= winW:                  # 偵測球是否超過畫布右方
            self.x = -step
        if ballPos[3] >= winH:                  # 偵測球是否超過畫布下方
            self.y = -step
class Racket:                                                       
    def __init__(self, canvas, color):                              
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,15, fill=color)   # 球拍物件
        self.canvas.move(self.id, 270, 400)                         # 球拍位置
        
winW = 640                                      # 定義畫布寬度
winH = 480                                      # 定義畫布高度
step = 3                                        # 定義速度可想成位移步伐
speed = 0.01                                    # 設定移動速度

tk = Tk()
tk.title("Bouncing Ball")

tk.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = Canvas(tk, width=winW, height=winH)
canvas.pack()
tk.update()

racket = Racket(canvas, 'purple')               # 定義紫色球拍
ball = Ball(canvas, 'yellow', winW, winH)       # 定義球物件

while True:
    ball.ballMove()
    tk.update()
    time.sleep(speed)                           # 可以控制移動速度

print("------------------------------------------------------------")  # 60個

from random import *
import time

class Ball:
    def __init__(self, canvas, color, winW, winH):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)  # 建立球物件
        self.canvas.move(self.id, winW/2, winH/2)   # 設定球最初位置
        startPos = [-4, -3, -2, -1, 1, 2, 3, 4]     # 球最初x軸位移的隨機數
        shuffle(startPos)                           # 打亂排列
        self.x = startPos[0]                        # 球最初水平移動單位
        self.y = step                               # 垂直移動單位
    def ballMove(self):
        self.canvas.move(self.id, self.x, self.y)   # step是正值表示往下移動
        ballPos = self.canvas.coords(self.id)
        if ballPos[0] <= 0:                     # 偵測球是否超過畫布左方
            self.x = step
        if ballPos[1] <= 0:                     # 偵測球是否超過畫布上方
            self.y = step
        if ballPos[2] >= winW:                  # 偵測球是否超過畫布右方
            self.x = -step
        if ballPos[3] >= winH:                  # 偵測球是否超過畫布下方
            self.y = -step
class Racket:                                                       
    def __init__(self, canvas, color):                              
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,15, fill=color)   # 球拍物件
        self.canvas.move(self.id, 270, 400)                         # 球拍位置
        self.x = 0
        self.canvas.bind_all('<KeyPress-Right>', self.moveRight)    # 綁定按往右鍵
        self.canvas.bind_all('<KeyPress-Left>', self.moveLeft)      # 綁定按往左鍵        
    def racketMove(self):                       # 設計球拍移動
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:                         # 移動時是否碰到畫布左邊
            self.x = 0
        elif pos[2] >= winW:                    # 移動時是否碰到畫布右邊
            self.x = 0
    def moveLeft(self, event):                 # 球拍每次向左移動的單位數
        self.x = -3
    def moveRight(self, event):                # 球拍每次向右移動的單位數
        self.x = 3
       
winW = 640                                      # 定義畫布寬度
winH = 480                                      # 定義畫布高度
step = 3                                        # 定義速度可想成位移步伐
speed = 0.01                                    # 設定移動速度

tk = Tk()
tk.title("Bouncing Ball")

tk.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = Canvas(tk, width=winW, height=winH)
canvas.pack()
tk.update()

racket = Racket(canvas, 'purple')               # 定義紫色球拍
ball = Ball(canvas, 'yellow', winW, winH)       # 定義球物件

while True:
    ball.ballMove()
    racket.racketMove()
    tk.update()
    time.sleep(speed)                           # 可以控制移動速度

print("------------------------------------------------------------")  # 60個

from random import *
import time

class Ball:
    def __init__(self, canvas, color, winW, winH, racket):
        self.canvas = canvas
        self.racket = racket
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)  # 建立球物件
        self.canvas.move(self.id, winW/2, winH/2)   # 設定球最初位置
        startPos = [-4, -3, -2, -1, 1, 2, 3, 4]     # 球最初x軸位移的隨機數
        shuffle(startPos)                           # 打亂排列
        self.x = startPos[0]                        # 球最初水平移動單位
        self.y = step                               # 垂直移動單位
    def hitRacket(self, ballPos):                                       
        racketPos = self.canvas.coords(self.racket.id)
        if ballPos[2] >= racketPos[0] and ballPos[0] <= racketPos[2]:
            if ballPos[3] >= racketPos[1] and ballPos[3] <= racketPos[3]:
                return True
        return False
    def ballMove(self):
        self.canvas.move(self.id, self.x, self.y)   # step是正值表示往下移動
        ballPos = self.canvas.coords(self.id)
        if ballPos[0] <= 0:                     # 偵測球是否超過畫布左方
            self.x = step
        if ballPos[1] <= 0:                     # 偵測球是否超過畫布上方
            self.y = step
        if ballPos[2] >= winW:                  # 偵測球是否超過畫布右方
            self.x = -step
        if ballPos[3] >= winH:                  # 偵測球是否超過畫布下方
            self.y = -step
        if self.hitRacket(ballPos) == True:     # 偵測是否撞到球拍
            self.y = -step    
class Racket:                                                       
    def __init__(self, canvas, color):                              
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,15, fill=color)   # 球拍物件
        self.canvas.move(self.id, 270, 400)                         # 球拍位置
        self.x = 0
        self.canvas.bind_all('<KeyPress-Right>', self.moveRight)    # 綁定按往右鍵
        self.canvas.bind_all('<KeyPress-Left>', self.moveLeft)      # 綁定按往左鍵        
    def racketMove(self):                       # 設計球拍移動
        self.canvas.move(self.id, self.x, 0)
        racketPos = self.canvas.coords(self.id)
        if racketPos[0] <= 0:                   # 移動時是否碰到畫布左邊
            self.x = 0
        elif racketPos[2] >= winW:              # 移動時是否碰到畫布右邊
            self.x = 0
    def moveLeft(self, event):                  # 球拍每次向左移動的單位數
        self.x = -3
    def moveRight(self, event):                 # 球拍每次向右移動的單位數
        self.x = 3
       
winW = 640                                      # 定義畫布寬度
winH = 480                                      # 定義畫布高度
step = 3                                        # 定義速度可想成位移步伐
speed = 0.01                                    # 設定移動速度

tk = Tk()
tk.title("Bouncing Ball")

tk.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = Canvas(tk, width=winW, height=winH)
canvas.pack()
tk.update()

racket = Racket(canvas, 'purple')               # 定義紫色球拍
ball = Ball(canvas,'yellow',winW,winH,racket)   # 定義球物件

while True:
    ball.ballMove()
    racket.racketMove()
    tk.update()
    time.sleep(speed)                           # 可以控制移動速度

print("------------------------------------------------------------")  # 60個

from random import *
import time

class Ball:
    def __init__(self, canvas, color, winW, winH, racket):
        self.canvas = canvas
        self.racket = racket
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)  # 建立球物件
        self.canvas.move(self.id, winW/2, winH/2)   # 設定球最初位置
        startPos = [-4, -3, -2, -1, 1, 2, 3, 4]     # 球最初x軸位移的隨機數
        shuffle(startPos)                           # 打亂排列
        self.x = startPos[0]                        # 球最初水平移動單位
        self.y = -step                              # 球先往上垂直移動單位
        self.notTouchBottom = True                  # 未接觸畫布底端
    def hitRacket(self, ballPos):                                       
        racketPos = self.canvas.coords(self.racket.id)
        if ballPos[2] >= racketPos[0] and ballPos[0] <= racketPos[2]:
            if ballPos[3] >= racketPos[1] and ballPos[3] <= racketPos[3]:
                return True
        return False
    def ballMove(self):
        self.canvas.move(self.id, self.x, self.y)   # step是正值表示往下移動
        ballPos = self.canvas.coords(self.id)
        if ballPos[0] <= 0:                     # 偵測球是否超過畫布左方
            self.x = step
        if ballPos[1] <= 0:                     # 偵測球是否超過畫布上方
            self.y = step
        if ballPos[2] >= winW:                  # 偵測球是否超過畫布右方
            self.x = -step
        if ballPos[3] >= winH:                  # 偵測球是否超過畫布下方
            self.y = -step
        if self.hitRacket(ballPos) == True:     # 偵測是否撞到球拍
            self.y = -step
        if ballPos[3] >= winH:                  # 如果球接觸到畫布底端
            self.notTouchBottom = False
class Racket:                                                       
    def __init__(self, canvas, color):                              
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,15, fill=color)   # 球拍物件
        self.canvas.move(self.id, 270, 400)                         # 球拍位置
        self.x = 0
        self.canvas.bind_all('<KeyPress-Right>', self.moveRight)    # 綁定按往右鍵
        self.canvas.bind_all('<KeyPress-Left>', self.moveLeft)      # 綁定按往左鍵        
    def racketMove(self):                       # 設計球拍移動
        self.canvas.move(self.id, self.x, 0)
        racketPos = self.canvas.coords(self.id)
        if racketPos[0] <= 0:                   # 移動時是否碰到畫布左邊
            self.x = 0
        elif racketPos[2] >= winW:              # 移動時是否碰到畫布右邊
            self.x = 0
    def moveLeft(self, event):                  # 球拍每次向左移動的單位數
        self.x = -3
    def moveRight(self, event):                 # 球拍每次向右移動的單位數
        self.x = 3
       
winW = 640                                      # 定義畫布寬度
winH = 480                                      # 定義畫布高度
step = 3                                        # 定義速度可想成位移步伐
speed = 0.01                                    # 設定移動速度

tk = Tk()
tk.title("Bouncing Ball")

tk.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = Canvas(tk, width=winW, height=winH)
canvas.pack()
tk.update()

racket = Racket(canvas, 'purple')               # 定義紫色球拍
ball = Ball(canvas,'yellow',winW,winH,racket)   # 定義球物件

while ball.notTouchBottom:                      # 如果球未接觸畫布底端                   
    ball.ballMove()
    racket.racketMove()
    tk.update()
    time.sleep(speed)                           # 可以控制移動速度

print("------------------------------------------------------------")  # 60個

import random

# 傳回球的隨機顏色
def getColor():
    colorlist = ['red', 'green', 'blue', 'aqua', 'gold', 'purple']
    return random.choice(colorlist)
        
# 定義Ball類別
class Ball:
    def __init__(self):
        self.x = width / 2              # 發球的x軸座標 
        self.y = 0                      # 發球的y軸座標 
        self.dx = 3                     # 每次移動x距離
        self.dy = 3                     # 每次移動y距離
        self.radius = 5                 # 求半徑
        self.color = getColor()         # 隨機取得球的顏色

def addBall():                          # 增加球
    ballList.append(Ball())

def removeBall():                       # 刪除串列最後一個球 
    ballList.pop()

def stop():                             # 動畫停止
    global ballRunning
    ballRunning = True
    
def resume():                           # 恢復動畫
    global ballRunning
    ballRunning = False
    animate()   
                                
def animate():                          # 球體移動
    global ballRunning
    while not ballRunning:
        canvas.after(sleepTime)         
        canvas.update()                 # 更新
        canvas.delete("ball")             
        for ball in ballList:           # 更新所有球
            redisplayBall(ball)
    
def redisplayBall(ball):                # 重新顯示球
    if ball.x > width or ball.x < 0:
        ball.dx = -ball.dx            
    if ball.y > height or ball.y < 0:
        ball.dy = -ball.dy   
    ball.x += ball.dx
    ball.y += ball.dy
    canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius,
                       ball.x + ball.radius, ball.y + ball.radius,
                       fill = ball.color, tags = "ball")
     
tk = Tk()

ballList = []                           # 建立球的串列
width, height = 400, 260
canvas = Canvas(tk, width=width, height=height)
canvas.pack()
        
frame = Frame(tk)                       # 建立下方功能紐
frame.pack()
btnStop = Button(frame, text = "暫停", command = stop)
btnStop.pack(side = LEFT)
btnResume = Button(frame, text = "恢復",command = resume)
btnResume.pack(side = LEFT)
btnAdd = Button(frame, text = "增加球", command = addBall)
btnAdd.pack(side = LEFT)
btnRemove = Button(frame, text = "減少球", command = removeBall)
btnRemove.pack(side = LEFT)
btnExit = Button(frame, text = "結束", command=tk.destroy)
btnExit.pack(side = LEFT)
        
sleepTime = 50                          # 動畫速度 
ballRunning = False
animate()
        
tk.mainloop() 



print("------------------------------------------------------------")  # 60個

import tkinter.messagebox
import random 
        
def reset():
    # 重設長條圖
    global i
    i = 0                               # 重設索引
    random.shuffle(mylist)
    newBar()

def go():                               
    # 執行排序
    global i
    if i > len(mylist) - 1:
        tkinter.messagebox.showinfo("showinfo", "排序完成")
        return              
# 將mylist[i]插入mylist[0 .. i-1]
    currentValue = mylist[i]
    k = i - 1
# 找尋mylist[i]適當位置
    while k >= 0 and mylist[k] > currentValue:      
        mylist[k + 1] = mylist[k]
        k -= 1            
# 正式執行插入list[k + 1]
    mylist[k + 1] = currentValue

    newBar()                            # 繪製新的長條圖   
    i += 1                              # 增加串列指標
        
def newBar():
    global i, gap
    canvas.delete("line")               # 刪除bar
    canvas.delete("text")               # 刪除bar上方數字
    canvas.create_line(10, ht-gap, wd-10, ht-gap, tag="line")
    barWd = (wd - 20) / len(mylist)
        
    maxC = int(max(mylist))
    for j in range(len(mylist)):
        canvas.create_rectangle(j*barWd+10, (ht-gap)*(1-mylist[j]/(maxC+4)), 
                                (j+1)*barWd+10, ht-gap, tag="line")       
                         
        canvas.create_text(j*barWd+10+barWd/2, (ht-gap)*(1-mylist[j]/(maxC+4))-8, 
                           text=str(mylist[j]), tag = "text")

    if i >= 0:
        canvas.create_rectangle(i*barWd+10, (ht-gap)*(1-mylist[i]/(maxC+4)), 
                                (i + 1)*barWd+10, ht-gap, fill="blue", tag="line")


wd = 400                                # 視窗寬度
ht = 200                                # 視窗高度
gap = 20                                # 長條圖與視窗的間距
i = 0                                   # 這是目前排序指標

tk = Tk()                           

canvas = Canvas(tk, width = wd, height = ht)
canvas.pack()
        
frame = Frame(tk)
frame.pack()
        
btnStep = Button(frame, text = "執行", command = go)
btnStep.pack(side = LEFT)
btnReset = Button(frame, text = "重置", command = reset)
btnReset.pack(side = LEFT)
btnReset = Button(frame, text = "結束", command = tk.destroy)
btnReset.pack(side = LEFT)

mylist = [ x for x in range(1, 20) ]
reset()
newBar()
       
tk.mainloop()



print("------------------------------------------------------------")  # 60個


import datetime

def run_digital_clock(label1):                     # 數字變數內容的更動
    def counting():                         # 更動數字方法
        now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        label1.config(text=str(now))     # 列出標籤數字內容
        label1.after(1000,counting)          # 隔一秒後呼叫counting
    counting()                              # 啟動呼叫

root = Tk()
label1=Label(root,bg="yellow",fg="blue",     # 黃底藍字
            height=3,width=18,              # 寬10高3
            font="Helvetic 20 bold")        # 字型設定
label1.pack()
run_digital_clock(label1)                          # 呼叫數字更動方法

root.mainloop()

print('------------------------------------------------------------')	#60個

def run_digital_clock(label1):                     # 數字變數內容的更動
    def counting():                         # 更動數字方法
        now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        label1.config(text=str(now))     # 列出標籤數字內容
        label1.after(1000,counting)          # 隔一秒後呼叫counting
    counting()                              # 持續呼叫

root = Tk()
label1=Label(root,bg="yellow",fg="blue",     # 黃底藍字
            height=3,width=18,              # 寬10高3
            font="Helvetica 20 bold")       # 字型設定
label1.pack()
run_digital_clock(label1)                          # 呼叫數字更動方法
Button(root,text="結束",width=15,command=root.destroy).pack(pady=10)

root.mainloop()

print('------------------------------------------------------------')	#60個

from tkinter.ttk import *
 
def load():                         # 啟動Prograssbar
    pb["value"] = 0                 # Prograssbar初始值
    pb["maximum"] = maxbytes        # Prograddbar最大值
    loading()
def loading():                      # 模擬下載資料
    global bytes
    bytes += 500                    # 模擬每次下在500bytes
    pb["value"] = bytes             # 設定指針
    if bytes < maxbytes:
        pb.after(50,loading)        # 經過0.05秒繼續執行loading
 
root = Tk()

bytes = 0                           # 設定初值
maxbytes = 10000                    # 假設下載檔案大小    

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["value"] = 0                     # Prograssbar初始值
 
btn = Button(root,text="Load",command=load)
btn.pack(pady=10)

root.mainloop()

print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


