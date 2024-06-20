"""
# 會動的tk範例 after

"""

import sys
import time
import random
import datetime
import tkinter as tk
from tkinter import ttk
'''
print("------------------------------------------------------------")  # 60個


def run_digital_clock(label1):                     # 數字變數內容的更動
    def counting():                         # 更動數字方法
        now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        label1.config(text=str(now))     # 列出標籤數字內容
        label1.after(1000,counting)          # 隔一秒後呼叫counting
    counting()                              # 啟動呼叫

window = tk.Tk()
label1=tk.Label(window,bg="yellow",fg="blue",     # 黃底藍字
            height=3,width=18,              # 寬10高3
            font="Helvetic 20 bold")        # 字型設定
label1.pack()
run_digital_clock(label1)                          # 呼叫數字更動方法

window.mainloop()

print('------------------------------------------------------------')	#60個

def run_digital_clock(label1):                     # 數字變數內容的更動
    def counting():                         # 更動數字方法
        now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        label1.config(text=str(now))     # 列出標籤數字內容
        label1.after(1000,counting)          # 隔一秒後呼叫counting
    counting()                              # 持續呼叫

window = tk.Tk()
label1=tk.Label(window,bg="yellow",fg="blue",     # 黃底藍字
            height=3,width=18,              # 寬10高3
            font="Helvetica 20 bold")       # 字型設定
label1.pack()
run_digital_clock(label1)                          # 呼叫數字更動方法
tk.Button(window,text="結束",width=15,command=window.destroy).pack(pady=10)

window.mainloop()

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
 
window = tk.Tk()

bytes = 0                           # 設定初值
maxbytes = 10000                    # 假設下載檔案大小    

pb = ttk.Progressbar(window,length=200,mode="determinate",orient=tk.HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["value"] = 0                     # Prograssbar初始值
 
btn = tk.Button(window,text="Load",command=load)
btn.pack(pady=10)

window.mainloop()

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

number = 1
def update_data():
    global number
    # 更新標籤顯示
    label_data.config(text=str(number))
    # 每200毫秒後再次調用update_data函數更新數據
    window.after(200, update_data)
    number += 17

window = tk.Tk()

# 建立一個標籤用於顯示數據, 初始值為0, 字體設置為Helvetica, 大小為48
label_data = tk.Label(window, text="0", font=("Helvetica", 48))
label_data.pack()                           # 將標籤添加到視窗中
update_data()           # 呼叫update_data( )函數以開始數據更新過程

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
        
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

window = tk.Tk() 
        
canvas = tk.Canvas(window,width=xWidth, height=yHeight)
canvas.pack()

startAngle = 0
while True:
    startAngle += 5
    displayFan(startAngle)
    canvas.after(50) 
    canvas.update()
            
window.mainloop() 

print("------------------------------------------------------------")  # 60個

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
        if random.randint(1,100) > weight:
            canvas.move(id2, 5, 0)  # id2 x軸移動5像素, y軸移動0像素
            id2Loc += 1
        else:
            canvas.move(id1, 5, 0)  # id1 x軸移動5像素, y軸移動0像素
            id1Loc += 1
        window.update()                 # 強制tkinter重繪
        canvas.after(50)
    if id1Loc > id2Loc:
        Flag = True
    else:
        Flag = False
    display()

window = tk.Tk()
canvas= tk.Canvas(window, width=500, height=250)
canvas.pack()
canvas.create_text(10,50,text="1")
canvas.create_oval(20,50,70,100,fill='yellow')
canvas.create_text(10,150,text="2")
canvas.create_oval(20,150,70,200,fill='aqua')

Flag = True                         # 判斷那一球勝利

frame = tk.Frame(window)                   # 建立框架
frame.pack(padx=5, pady=5)

# 在框架Frame內建立標籤Label, 輸入獲勝的球, 按鈕Button
tk.Label(frame, text="那一個球獲勝 : ").pack(side=tk.LEFT)
ball = tk.StringVar()
ball.set("1or2")
entry = tk.Entry(frame, textvariable=ball).pack(side=tk.LEFT,padx=3)
startBtn = tk.StringVar()
startBtn.set("開始")
tk.Button(frame, textvariable=startBtn,command=running).pack(side=tk.LEFT)
raceResult = tk.StringVar()

tk.Label(frame,width=16,textvariable=raceResult).pack(side=tk.LEFT,padx=3)

window.mainloop() 

print("------------------------------------------------------------")  # 60個

window = tk.Tk()

canvas= tk.Canvas(window, width=500, height=150)
canvas.pack()

id = canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
ballPos = canvas.coords(id)
print(ballPos)

window.mainloop() 

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
    time.sleep(0.05) # 等同於 canvas.after(50)

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

print('用上下左右鍵控制紅球移動')

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

"""
print('文字移動')

window = tk.Tk()

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
"""

print("------------------------------------------------------------")  # 60個

"""
使用tkinter创建GUI
- 在窗口上制作动画
"""

# 播放动画效果的函数
def play_animation():
    canvas.move(oval, 2, 2)
    canvas.update()
    window.after(30, play_animation)


x = 20
y = 20

window = tk.Tk()
window.geometry("600x800")
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

window = tk.Tk()
window.geometry("600x800")
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


class Ball:
    def __init__(self, canvas, color, winW, winH, racket):
        self.canvas = canvas
        self.racket = racket
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color)  # 建立球物件
        self.canvas.move(self.id, winW/2, winH/2)   # 設定球最初位置
        startPos = [-4, -3, -2, -1, 1, 2, 3, 4]     # 球最初x軸位移的隨機數
        random.shuffle(startPos)                           # 打亂排列
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
window.title("Bouncing Ball 8")                       # 遊戲視窗標題
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

window = tk.Tk()
window.title("Bouncing Ball 9")

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

window = tk.Tk()
window.title("Animation Demo")
        
width = 250 # Width of the canvas
canvas = tk.Canvas(window, bg = "white", width = 250, height = 50)
canvas.pack()
        
x = 0 # Starting x position
canvas.create_text(x, 30, text = "Message moving?", tags = "text")
        
dx = 3
while True:
    canvas.move("text", dx, 0) # Move text dx unit
    canvas.after(100) # Sleep for 100 milliseconds
    canvas.update() # Update canvas
    if x < width:
        x += dx  # Get the current position for string
    else:
        x = 0 # Reset string position to the beginning
        canvas.delete("text") 
        # Redraw text at the beginning
        canvas.create_text(x, 30, text = "Message moving?", tags = "text")
                
window.mainloop() # Create an event loop



print("------------------------------------------------------------")  # 60個

from tkinter import * # Import tkinter
from random import randint

# Return a random color string in the form #RRGGBB
def getRandomColor():
    color = "#"
    for j in range(6):
        color += toHexChar(randint(0, 15)) # Add a random digit
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

class BounceBalls:
    def __init__(self):
        self.ballList = [] # Create a list for balls
        
        window = Tk()
        window.title("Bouncing Balls")
        
        self.width = 350 # Width of the self.canvas
        self.height = 150 # Width of the self.canvas
        self.canvas = Canvas(window, bg = "white", 
            width = self.width, height = self.height)
        self.canvas.pack()
        
        frame = Frame(window)
        frame.pack()
        btStop = Button(frame, text = "Stop", command = self.stop)
        btStop.pack(side = LEFT)
        btResume = Button(frame, text = "Resume",
            command = self.resume)
        btResume.pack(side = LEFT)
        btAdd = Button(frame, text = "+", command = self.add)
        btAdd.pack(side = LEFT)
        btRemove = Button(frame, text = "-", command = self.remove)
        btRemove.pack(side = LEFT)
        
        self.sleepTime = 100 # Set a sleep time 
        self.isStopped = False
        self.animate()
        
        window.mainloop() # Create an event loop
           
    def stop(self): # Stop animation
        self.isStopped = True
    
    def resume(self): # Resume animation
        self.isStopped = False   
        self.animate()
    
    def add(self): # Add a new ball
        self.ballList.append(Ball())
    
    def remove(self): # Remove the last ball 
        self.ballList.pop()
                                
    def animate(self): # Move the message
        while not self.isStopped:
            self.canvas.after(self.sleepTime) # Sleep 
            self.canvas.update() # Update self.canvas
            self.canvas.delete("ball") 
            
            for ball in self.ballList:
                self.redisplayBall(ball)
    
    def redisplayBall(self, ball):
        if ball.x > self.width or ball.x < 0:
            ball.dx = -ball.dx
            
        if ball.y > self.height or ball.y < 0:
            ball.dy = -ball.dy
    
        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - ball.radius, 
            ball.y - ball.radius, ball.x + ball.radius, 
            ball.y + ball.radius, fill = ball.color, tags = "ball")
                                             
BounceBalls() # Create GUI
'''
print("------------------------------------------------------------")  # 60個

class ControlAnimation:
    def __init__(self):
        window = tk.Tk()
        window.title("Control Animation Demo")
        
        self.width = 250 # Width of the self.canvas
        self.canvas = tk.Canvas(window, bg = "white", 
            width = self.width, height = 50)
        self.canvas.pack()
        
        frame = tk.Frame(window)
        frame.pack()
        btStop = tk.Button(frame, text = "Stop", command = self.stop)
        btStop.pack(side = tk.LEFT)
        btResume = tk.Button(frame, text = "Resume", command = self.resume)
        btResume.pack(side = tk.LEFT)
        btFaster = tk.Button(frame, text = "Faster", command = self.faster)
        btFaster.pack(side = tk.LEFT)
        btSlower = tk.Button(frame, text = "Slower", command = self.slower)
        btSlower.pack(side = tk.LEFT)
        
        self.x = 0 # Starting x position
        self.sleepTime = 100 # Set a sleep time 
        self.canvas.create_text(self.x, 30, text = "Message moving?", tags = "text")
        
        self.dx = 3
        self.isStopped = False
        self.animate()
        
        window.mainloop() # Create an event loop
        
    def stop(self): # Stop animation
        self.isStopped = True
    
    def resume(self): # Resume animation
        self.isStopped = False   
        self.animate()
    
    def faster(self): # Speed up the animation
        if self.sleepTime > 5:
            self.sleepTime -= 20
               
    def slower(self): # Slow down the animation
        self.sleepTime += 20
                                
    def animate(self): # Move the message
        while not self.isStopped:
            self.canvas.move("text", self.dx, 0) # Move text 
            self.canvas.after(self.sleepTime) # Sleep 
            self.canvas.update() # Update self.canvas
            if self.x < self.width:
                self.x += self.dx  # Set new position 
            else:
                self.x = 0 # Reset string position to the beginning
                self.canvas.delete("text") 
                # Redraw text at the beginning
                self.canvas.create_text(self.x, 30, 
                    text = "Message moving?", tags = "text")    
                                       
ControlAnimation() # Create GUI

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


