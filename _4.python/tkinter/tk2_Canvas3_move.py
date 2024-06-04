"""
# 會動的tk範例

"""

import sys
import time
import random
import tkinter as tk
import tkinter.ttk as ttk

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

canvas= tk.Canvas(window, width=500, height=150)
canvas.pack()
canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
for x in range(0, 80):
    canvas.move(1, 5, 0)        # ID=1 x軸移動5像素, y軸不變
    window.update()                 # 強制tkinter重繪
    time.sleep(0.05)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

canvas= tk.Canvas(window, width=500, height=300)
canvas.pack()
canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
for x in range(0, 80):
    canvas.move(1, 5, 2)        # ID=1 x軸移動5像素, y軸移動2像素
    window.update()                 # 強制tkinter重繪
    time.sleep(0.05)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

canvas= tk.Canvas(window, width=500, height=300)
canvas.pack()
canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
for x in range(0, 80):
    canvas.move(1, 5, 2)        # ID=1 x軸移動5像素, y軸移動2像素
    window.update()                 # 強制tkinter重繪
    canvas.after(50)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

canvas= tk.Canvas(window, width=500, height=250)
canvas.pack()
id1 = canvas.create_oval(10,50,60,100,fill='yellow')
id2 = canvas.create_oval(10,150,60,200,fill='aqua')
for x in range(0, 80):
    canvas.move(id1, 5, 0)      # id1 x軸移動5像素, y軸移動0像素
    canvas.move(id2, 5, 0)      # id2 x軸移動5像素, y軸移動0像素
    window.update()                 # 強制tkinter重繪
    time.sleep(0.05)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

canvas= tk.Canvas(window, width=500, height=250)
canvas.pack()
id1 = canvas.create_oval(10,50,60,100,fill='yellow')
id2 = canvas.create_oval(10,150,60,200,fill='aqua')
for x in range(0, 100):
    if random.randint(1,100) > 70:
        canvas.move(id2, 5, 0)  # id2 x軸移動5像素, y軸移動0像素
    else:
        canvas.move(id1, 5, 0)  # id1 x軸移動5像素, y軸移動0像素    
    window.update()                 # 強制tkinter重繪
    time.sleep(0.05)

window.mainloop()

print("------------------------------------------------------------")  # 60個

def ballMove(event):
    if event.keysym == 'Left':  # 左移
        canvas.move(1, -5, 0)
    if event.keysym == 'Right': # 右移
        canvas.move(1, 5, 0)
    if event.keysym == 'Up':    # 上移
        canvas.move(1, 0, -5)
    if event.keysym == 'Down':  # 下移
        canvas.move(1, 0, 5)

window = tk.Tk()

canvas= tk.Canvas(window, width=500, height=300)
canvas.pack()
canvas.create_oval(225,125,275,175,fill='red')
canvas.bind_all('<KeyPress-Left>', ballMove)
canvas.bind_all('<KeyPress-Right>', ballMove)
canvas.bind_all('<KeyPress-Up>', ballMove)
canvas.bind_all('<KeyPress-Down>', ballMove)

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

window.title("draw oval")  

xWidth = 400
yHeight = 250
canvas = tk.Canvas(window, width=xWidth, height=yHeight)
canvas.pack()
        
for i in range(20):
    canvas.create_oval(10+i*5, 10+i*5, xWidth-10-i*5, yHeight-10-i*5)
        
window.mainloop() 

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

window.title("ex19_4.py") 
        
xWidth = 300
yHeight = 100
canvas = tk.Canvas(window, width=xWidth, height=yHeight)
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

"""
使用tkinter创建GUI
- 在窗口上制作动画
"""

# 播放动画效果的函数
def play_animation():
    canvas.move(oval, 2, 2)
    canvas.update()
    window.after(50, play_animation)


x = 10
y = 10

window = tk.Tk()

window.geometry('600x600')
window.title('动画效果')
window.resizable(False, False)
#fail window.wm_attributes('-topmost', 1)
canvas = tk.Canvas(window, width=600, height=600, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, 600, 600, fill='gray')
oval = canvas.create_oval(10, 10, 60, 60, fill='red')
canvas.pack()
window.update()
play_animation()

window.mainloop()

# 请思考如何让小球碰到屏幕的边界就弹回
# 请思考如何用面向对象的编程思想对上面的代码进行封装

print("------------------------------------------------------------")  # 60個

import math

# 建立主視窗
window = tk.Tk()

# 設定主視窗大小
w = 800
h = 800
x_st = 100
y_st = 100
#size = str(w)+'x'+str(h)
#size = str(w)+'x'+str(h)+'+'+str(x_st)+'+'+str(y_st)
#window.geometry(size)
window.geometry("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))
#print("{0:d}x{1:d}+{2:d}+{3:d}".format(w, h, x_st, y_st))

# 設定主視窗標題
title = "移動測試"
window.title(title)

#公用變數
width = 300
height = 300
canvas = tk.Canvas(window, bg = 'pink', width = width, height = height)
canvas.pack()

radius = 20
x1 = 0 # Starting x position
y1 = 100
sleepTime = 100 #Sleep 一段時間(msec)
canvas.create_oval(x1 - radius, y1 - radius, x1 + radius, y1 + radius, fill = 'red', tags = 'moving1')

x2 = x1
y2 = 200
canvas.create_oval(x2 - radius, y2 - radius, x2 + radius, y2 + radius, fill = 'red', tags = 'moving2')

dx = 10

count = 0
msg = tk.StringVar()
msg.set('')

label1 = tk.Label(window, textvariable = msg, fg = 'red', font=("新細明體", 20))
label1.pack() 

while True:
    #移動法
    canvas.move('moving1', dx, 0) #移動那個被畫上去的移動物件
    canvas.after(sleepTime) #Sleep 一段時間(msec)
    canvas.update() # Update canvas
    count = count + 1
    msg.set(count)
    
    if x1 < width:
        x1 += dx  # Set new position 
    else:
        x1 = 0
        canvas.delete('moving1') #刪除所有移動物件
        #畫 移動物件
        canvas.create_oval(x1 - radius, y1 - radius, x1 + radius, y1 + radius, fill = 'red', tags = 'moving1')

    #重畫法
    canvas.delete('moving2') #刪除所有移動物件
    y2 = 200 + 50 * math.sin(count / 5)
    x2 = x1
    canvas.create_oval(x2 - radius, y2 - radius, x2 + radius, y2 + radius, fill = 'red', tags = 'moving2')

window.mainloop()

print("------------------------------------------------------------")  # 60個

import sys
import time
import random
import tkinter as tk

print("------------------------------------------------------------")  # 60個

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

window = tk.Tk()
window.title("Bouncing Ball")                       # 遊戲視窗標題
window.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = tk.Canvas(window, width=winW, height=winH)
canvas.pack()
window.update()

ball = Ball(canvas, 'yellow', winW, winH)       # 定義球物件

while True:
    ball.ballMove()
    window.update()
    time.sleep(speed)                           # 可以控制移動速度

window.mainloop()

print("------------------------------------------------------------")  # 60個


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

window = tk.Tk()

window.title("Bouncing Ball")                       # 遊戲視窗標題
window.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = tk.Canvas(window, width=winW, height=winH)
canvas.pack()
window.update()
 
ball = Ball(canvas, 'yellow', winW, winH)       # 定義球物件

while True:
    ball.ballMove()
    window.update()
    time.sleep(speed)                           # 可以控制移動速度

window.mainloop()

print("------------------------------------------------------------")  # 60個


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

window = tk.Tk()

window.title("Bouncing Ball")                       # 遊戲視窗標題
window.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = tk.Canvas(window, width=winW, height=winH)
canvas.pack()
window.update()

ball = Ball(canvas, 'yellow', winW, winH)       # 定義球物件

while True:
    ball.ballMove()
    window.update()
    time.sleep(speed)                           # 可以控制移動速度

window.mainloop()

print("------------------------------------------------------------")  # 60個

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

window = tk.Tk()

window.title("Bouncing Ball")                       # 遊戲視窗標題
window.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = tk.Canvas(window, width=winW, height=winH)
canvas.pack()
window.update()

racket = Racket(canvas, 'purple')               # 定義紫色球拍
ball = Ball(canvas, 'yellow', winW, winH)       # 定義球物件

while True:
    ball.ballMove()
    window.update()
    time.sleep(speed)                           # 可以控制移動速度

window.mainloop()

print("------------------------------------------------------------")  # 60個


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

window = tk.Tk()

window.title("Bouncing Ball")                       # 遊戲視窗標題
window.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = tk.Canvas(window, width=winW, height=winH)
canvas.pack()
window.update()

racket = Racket(canvas, 'purple')               # 定義紫色球拍
ball = Ball(canvas, 'yellow', winW, winH)       # 定義球物件

while True:
    ball.ballMove()
    racket.racketMove()
    window.update()
    time.sleep(speed)                           # 可以控制移動速度

window.mainloop()

print("------------------------------------------------------------")  # 60個


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

window = tk.Tk()

window.title("Bouncing Ball")                       # 遊戲視窗標題
window.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = tk.Canvas(window, width=winW, height=winH)
canvas.pack()
window.update()

racket = Racket(canvas, 'purple')               # 定義紫色球拍
ball = Ball(canvas,'yellow',winW,winH,racket)   # 定義球物件

while True:
    ball.ballMove()
    racket.racketMove()
    window.update()
    time.sleep(speed)                           # 可以控制移動速度

window.mainloop()

print("------------------------------------------------------------")  # 60個


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

window = tk.Tk()

window.title("Bouncing Ball")                       # 遊戲視窗標題
window.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = tk.Canvas(window, width=winW, height=winH)
canvas.pack()
window.update()

racket = Racket(canvas, 'purple')               # 定義紫色球拍
ball = Ball(canvas,'yellow',winW,winH,racket)   # 定義球物件

while ball.notTouchBottom:                      # 如果球未接觸畫布底端                   
    try:
        ball.ballMove()
    except:
        print("按關閉紐終止程式執行")
        break
    racket.racketMove()
    window.update()
    time.sleep(speed)                           # 可以控制移動速度

window.mainloop()

print("------------------------------------------------------------")  # 60個

import pygame

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
        if self.hitRacket(ballPos) == True:     # 偵測是否撞到球拍
            soundObj = pygame.mixer.Sound(r'C:\Windows\Media\notify.wav')  # 建立聲音物件
            soundObj.play()                     # 發出聲音
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

pygame.mixer.init()                             # 初始化聲音       
winW = 640                                      # 定義畫布寬度
winH = 480                                      # 定義畫布高度
step = 3                                        # 定義速度可想成位移步伐
speed = 0.01                                    # 設定移動速度

window = tk.Tk()

window.title("Bouncing Ball")                       # 遊戲視窗標題
window.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = tk.Canvas(window, width=winW, height=winH)
canvas.pack()
window.update()

racket = Racket(canvas, 'purple')               # 定義紫色球拍
ball = Ball(canvas,'yellow',winW,winH,racket)   # 定義球物件

while ball.notTouchBottom:                      # 如果球未接觸畫布底端                   
    try:
        ball.ballMove()
    except:
        print("按關閉紐終止程式執行")
        break
    racket.racketMove()
    window.update()
    time.sleep(speed)                           # 可以控制移動速度

window.mainloop()

print("------------------------------------------------------------")  # 60個

import pygame

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
        pygame.mixer.music.load(r'C:\Windows\Media\town.mid') # 下載mp3音樂檔案
        pygame.mixer.music.play(-1)                 # 永遠播放mp3音樂檔案
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
        if self.hitRacket(ballPos) == True:     # 偵測是否撞到球拍
            pygame.mixer.music.pause()          # 暫停播放背景音樂
            soundObj = pygame.mixer.Sound(r'C:\Windows\Media\notify.wav')  # 建立碰撞聲音物件            
            soundObj.play()                     # 發出碰撞聲音
            pygame.mixer.music.unpause()        # 恢復播放背景音樂
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

pygame.mixer.init()                             # 初始化聲音       
winW = 640                                      # 定義畫布寬度
winH = 480                                      # 定義畫布高度
step = 3                                        # 定義速度可想成位移步伐
speed = 0.01                                    # 設定移動速度

window = tk.Tk()

window.title("Bouncing Ball")                       # 遊戲視窗標題
window.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = tk.Canvas(window, width=winW, height=winH)
canvas.pack()
window.update()

racket = Racket(canvas, 'purple')               # 定義紫色球拍
ball = Ball(canvas,'yellow',winW,winH,racket)   # 定義球物件

while ball.notTouchBottom:                      # 如果球未接觸畫布底端                   
    try:
        ball.ballMove()
    except:
        print("按關閉紐終止程式執行")
        break
    racket.racketMove()
    window.update()
    time.sleep(speed)                           # 可以控制移動速度

window.mainloop()

print("------------------------------------------------------------")  # 60個

# Return a random color string in the form #RRGGBB
def getRandomColor():
    color = "#"
    for j in range(6):
        color += toHexChar(random.randint(0, 15)) # Add a random digit
    return color

# Convert an integer to a single hex digit in a character 
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))
        
# Define a Ball class
class Ball:
    def __init__(self):
        self.x = 0 # Starting center position
        self.y = 0 
        self.dx = 2 # Move right by default
        self.dy = 2 # Move down by default
        self.radius = 3 # The radius is fixed
        self.color = getRandomColor() # Get random color

def add(): # Add a new ball
    ballList.append(Ball())

def animate(): # Move the message
    while True:
        canvas.after(sleepTime) # Sleep 
        canvas.update() # Update canvas
        canvas.delete("ball") 
            
        for ball in ballList:
            redisplayBall(ball)
    
def redisplayBall(ball):
    if ball.x > width or ball.x < 0:
        ball.dx = -ball.dx
            
    if ball.y > height or ball.y < 0:
        ball.dy = -ball.dy
    
    ball.x += ball.dx
    ball.y += ball.dy
    canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius, ball.x + ball.radius, ball.y + ball.radius, fill = ball.color, tags = "ball")


ballList = [] # Create a list for balls

window = tk.Tk() # Create a window
window.title("Bouncing Balls") # Set a title

width = 350 # Width of the canvas
height = 150 # Width of the canvas
canvas = tk.Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

frame = tk.Frame(window)
frame.pack()
button1 = tk.Button(frame, text = "+", command = add)
button1.pack(side = tk.LEFT)

add()
sleepTime = 100 # Set a sleep time, in msec
animate()

window.mainloop()

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
     
window = tk.Tk()

ballList = []                           # 建立球的串列
width, height = 400, 260
canvas = tk.tk.Canvas(window, width=width, height=height)
canvas.pack()
        
frame = tk.Frame(tk)                       # 建立下方功能紐
frame.pack()
btnStop = tk.Button(frame, text = "暫停", command = stop)
btnStop.pack(side = tk.LEFT)
btnResume = tk.Button(frame, text = "恢復",command = resume)
btnResume.pack(side = tk.LEFT)
btnAdd = tk.Button(frame, text = "增加球", command = addBall)
btnAdd.pack(side = tk.LEFT)
btnRemove = tk.Button(frame, text = "減少球", command = removeBall)
btnRemove.pack(side = tk.LEFT)
btnExit = tk.Button(frame, text = "結束", command=tk.destroy)
btnExit.pack(side = tk.LEFT)
        
sleepTime = 50                          # 動畫速度 
ballRunning = False
animate()
        
window.mainloop()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
