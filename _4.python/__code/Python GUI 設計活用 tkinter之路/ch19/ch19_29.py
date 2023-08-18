# ch19_29.py
from tkinter import * # Import tkinter
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
tk.title("ch19_29")                     
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


