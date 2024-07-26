"""
# 會動的tk範例 after

"""

import sys
import time
import random
import datetime
import tkinter as tk
from tkinter import ttk

print("------------------------------------------------------------")  # 60個

running = True

def stop_running_and_exit():
    global running
    running = False
    window.destroy()

def stop_running_and_exit2():
    global running
    running = False

print('------------------------------------------------------------')	#60個


def run_digital_clock(label1):                     # 數字變數內容的更動
    def counting():                         # 更動數字方法
        now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        label1.config(text=str(now))     # 列出標籤數字內容
        label1.after(1000,counting)          # 隔一秒後呼叫counting
    counting()                              # 啟動呼叫

window = tk.Tk()
label1=tk.Label(window,bg="yellow",fg="blue",     # 黃底藍字
            height=3,width=18,              # 寬10高3
            font="Helvetica 20 bold")        # 字型設定
label1.pack()
run_digital_clock(label1)                          # 呼叫數字更動方法

window.mainloop()

print('------------------------------------------------------------')	#60個

#同上 但多了 按鈕

def run_digital_clock(label1):                     # 數字變數內容的更動
    def counting():                         # 更動數字方法
        now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        label1.config(text=str(now))     # 列出標籤數字內容
        label1.after(1000,counting)          # 隔一秒後呼叫counting
    counting()                              # 啟動呼叫

window = tk.Tk()
label1=tk.Label(window,bg="yellow",fg="blue",     # 黃底藍字
            height=3,width=18,              # 寬10高3
            font="Helvetica 20 bold")       # 字型設定
label1.pack()
run_digital_clock(label1)                          # 呼叫數字更動方法
tk.Button(window,text="結束",width=15,command=window.destroy).pack(pady=10)

window.mainloop()

print('------------------------------------------------------------')	#60個

window = tk.Tk()
window.title('秒數計算中...')
window.geometry("300x150")

counter = 0 #儲存數值

# 顯示訊息於label上
def display():
   counter = 0
   
   # 自訂函式二
   def count():
      global counter #全域變數
      counter += 1
      lb_mesg1.config(text = str(counter),
         bg = 'pink', width = 20, height = 2)
      lb_mesg1.after(1000, count)
   count()
   
lb_mesg1 = tk.Label(window, fg = 'gray')
lb_mesg1.pack()
display()

# 設定離開按鈕
tk.Button(window, text = '結束', width = 20, command = window.destroy).pack()

window.mainloop()

print("------------------------------------------------------------")  # 60個

number = 1
def update_data():
    global number
    # 更新標籤顯示
    lb_mesg2.config(text=str(number))
    # 每200毫秒後再次調用update_data函數更新數據
    window.after(200, update_data)
    number += 17

window = tk.Tk()

# 建立一個標籤用於顯示數據, 初始值為0, 字體設置為Helvetica, 大小為48
lb_mesg2 = tk.Label(window, text="0",
                    bg="yellow",fg="blue",     # 黃底藍字
                    width=6,height=3,              # 寬6高3
                    #font=("Helvetica", 48))
                    font="Helvetica 48 bold")
lb_mesg2.pack()                           # 將標籤添加到視窗中
update_data()           # 呼叫update_data( )函數以開始數據更新過程

window.mainloop()

print("------------------------------------------------------------")  # 60個


def load():                         # 啟動Prograssbar
    global download_bytes
    download_bytes = 0
    progressbar1["value"] = 0                 # Prograssbar初始值
    progressbar1["maximum"] = maxbytes        # Prograddbar最大值
    loading()


def loading():                      # 模擬下載資料
    global download_bytes
    download_bytes += 500                    # 模擬每次下在500bytes
    progressbar1["value"] = download_bytes             # 設定指針
    if download_bytes < maxbytes:
        progressbar1.after(50,loading)        # 經過0.05秒繼續執行loading
 
window = tk.Tk()

download_bytes = 0                           # 設定初值
maxbytes = 10000                    # 假設下載檔案大小    

progressbar1 = ttk.Progressbar(window,length=200,mode="determinate",orient=tk.HORIZONTAL)
progressbar1.pack(padx=10,pady=10)
progressbar1["value"] = 0                     # Prograssbar初始值
 
btn = tk.Button(window,text="Load",command=load)
btn.pack(pady=10)

window.mainloop()

print("------------------------------------------------------------")  # 60個


def displayFan(startingAngle):
    canvas.delete("fan")    
    canvas.create_arc(W / 2 - r, H / 2 - r, W / 2 + r, H / 2 + r,
            start = startAngle + 0, extent = 60, fill = "green", tags = "fan")        
    canvas.create_arc(W / 2 - r, H / 2 - r, W / 2 + r, H / 2 + r,
            start = startAngle + 120, extent = 60, fill = "green", tags = "fan")        
    canvas.create_arc(W / 2 - r, H / 2 - r, W / 2 + r, H / 2 + r,
            start = startAngle + 240, extent = 60, fill = "green", tags = "fan")        

W = 300
H = 300
r = 120

window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", stop_running_and_exit)  # 更改協定綁定

canvas = tk.Canvas(window,width=W, height=H)
canvas.pack()

running = True

startAngle = 0
while running == True:
    startAngle += 5
    displayFan(startAngle)
    canvas.after(20) 
    canvas.update()
            
window.mainloop()

print("------------------------------------------------------------")  # 60個

print('移動一個球範例')

window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", stop_running_and_exit)  # 更改協定綁定

canvas= tk.Canvas(window, width=500, height=300)
canvas.pack()

item1 = canvas.create_oval(20,50,70,100,fill='yellow')

running = True

while running == True:
    canvas.delete('all') #重來, 刪除全部畫件
    item1 = canvas.create_oval(20,50,70,100,fill='yellow')
    for x in range(0, 50):# 最多 N 次
        if running == False:
            break
        canvas.move(item1, 5, 1)      # item1 x軸移動5像素, y軸移動1像素
        window.update()                 # 強制tkinter重繪
        canvas.after(50)
        #time.sleep(0.05) # 等同於 canvas.after(50)
        
window.mainloop()

print("------------------------------------------------------------")  # 60個

print('移動一個球範例')

window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", stop_running_and_exit)  # 更改協定綁定

canvas= tk.Canvas(window, width=500, height=300)
canvas.pack()

item1 = canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray', tags = 'running_ball')

""" 物件資訊
ballPos = canvas.coords(item1)
print(ballPos)
"""

running = True
while running == True:
    if running == False:
        print('break')
        break
   
    canvas.move(item1, 5, 1)      # item1 x軸移動5像素, y軸移動1像素
    ballPos = canvas.coords(item1)
    #print(ballPos)
    if ballPos[0] > 300:
        canvas.delete('running_ball') #刪除所有移動物件
        item1 = canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray', tags = 'running_ball')
    window.update()                 # 強制tkinter重繪
    time.sleep(0.1) # 等同於 canvas.after(100)
        

window.mainloop()

print("------------------------------------------------------------")  # 60個

"""
使用tkinter創建GUI
- 在窗口上制作動畫
"""

count = 0
# 播放動畫效果的函數, 每隔 0.1 秒呼叫自己一次
def play_animation():
    global count
    if count < 50:
        canvas.move(item1, 5, 1)      # item1 x軸移動5像素, y軸移動1像素
        canvas.update()
        window.after(100, play_animation)
    count += 1

x = 20
y = 20

window = tk.Tk()
window.geometry("600x400")
window.title('動畫效果')
window.resizable(False, False)
#fail window.wm_attributes('-topmost', 1)

canvas = tk.Canvas(window, width=600, height=600, bd=0, highlightthickness=0)
canvas.pack()

canvas.create_rectangle(0, 0, 600, 400, fill='gray')
item1 = canvas.create_oval(10, 10, 60, 60, fill='red')

window.update()
play_animation()

window.mainloop()

print("------------------------------------------------------------")  # 60個

window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", stop_running_and_exit)  # 更改協定綁定
window.geometry("600x400")
window.title("移動測試")

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

running = True
    
while running == True:
    #移動法
    canvas.move('moving1', dx, 0) #移動那個被畫上去的移動物件
    canvas.after(sleepTime) #Sleep 一段時間(msec)
    canvas.update() # Update canvas
    
    if x1 < width:
        x1 += dx  # Set new position 
    else:
        x1 = 0
        canvas.delete('moving1') #刪除所有移動物件
        #畫 移動物件
        canvas.create_oval(x1 - radius, y1 - radius, x1 + radius, y1 + radius, fill = 'red', tags = 'moving1')

    if running == False:
        break

    #重畫法
    canvas.delete('moving2') #刪除所有移動物件
    if x2 < width:
        x2 += dx  # Set new position 
    else:
        x2 = 0
    canvas.create_oval(x2 - radius, y2 - radius, x2 + radius, y2 + radius, fill = 'green', tags = 'moving2')

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










print('bouncing ball ST')



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
    if ball.x > W or ball.x < 0:
        ball.dx = -ball.dx
            
    if ball.y > H or ball.y < 0:
        ball.dy = -ball.dy
    
    ball.x += ball.dx
    ball.y += ball.dy
    canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius, ball.x + ball.radius, ball.y + ball.radius, fill = ball.color, tags = "ball")


ballList = [] # Create a list for balls

window = tk.Tk()
window.title("Bouncing Ball 9")

W = 350 # Width of the canvas
H = 150 # Width of the canvas
canvas = tk.Canvas(window, bg = "white", width = W, height = H)
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
        self.x = W / 2              # 發球的x軸座標 
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
    if ball.x > W or ball.x < 0:
        ball.dx = -ball.dx            
    if ball.y > H or ball.y < 0:
        ball.dy = -ball.dy   
    ball.x += ball.dx
    ball.y += ball.dy
    canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius,
                       ball.x + ball.radius, ball.y + ball.radius,
                       fill = ball.color, tags = "ball")
     
window = tk.Tk()

ballList = []                           # 建立球的串列
W, H = 400, 260
canvas = tk.Canvas(window, width=W, height=H)
canvas.pack()
        
frame = tk.Frame(window)                       # 建立下方功能紐
frame.pack()

btnStop = tk.Button(frame, text = "暫停", command = stop)
btnStop.pack(side = tk.LEFT)
btnResume = tk.Button(frame, text = "恢復",command = resume)
btnResume.pack(side = tk.LEFT)
btnAdd = tk.Button(frame, text = "增加球", command = addBall)
btnAdd.pack(side = tk.LEFT)
btnRemove = tk.Button(frame, text = "減少球", command = removeBall)
btnRemove.pack(side = tk.LEFT)
btnExit = tk.Button(frame, text = "結束", command=window.destroy)
btnExit.pack(side = tk.LEFT)
        
sleepTime = 50                          # 動畫速度 
ballRunning = False
animate()
        
window.mainloop()

print("------------------------------------------------------------")  # 60個

print("文字移動")

window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", stop_running_and_exit)  # 更改協定綁定

W = 300
H = 100
canvas = tk.Canvas(window, bg="white", width=W, height=H)
canvas.pack()

x_st = 0
y_st = 45
canvas.create_text(x_st, y_st, text="Welcome to the US", tags="text")

running = True

dx = 3
dy = 0
while running == True:
    canvas.move("text", dx, dy)  # 移動dx, dy
    canvas.after(100)  # 100 msec
    canvas.update()
    if x_st < W:
        x_st += dx
    else:#若超過, 砍掉重畫
        x_st = 0
        canvas.delete("text")
        canvas.create_text(x_st, y_st, text="Welcome to the US", tags="text")

window.mainloop()

print("------------------------------------------------------------")  # 60個


# Return a random color string in the form #RRGGBB
def getRandomColor():
    color = "#"
    for j in range(6):
        color += toHexChar(random.randint(0, 15))  # Add a random digit
    return color


# Convert an integer to a single hex digit in a character
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord("0"))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord("A"))


# Define a Ball class
class Ball:
    def __init__(self):
        self.x = 0  # Starting center position
        self.y = 0
        self.dx = 2  # Move right by default
        self.dy = 2  # Move down by default
        self.radius = 3  # The radius is fixed
        self.color = getRandomColor()  # Get random color


class BounceBalls:
    def __init__(self):
        self.ballList = []  # Create a list for balls

        window = tk.Tk()
        window.title("Bouncing Balls")

        self.width = 350  # Width of the self.canvas
        self.height = 150  # Width of the self.canvas
        self.canvas = tk.Canvas(window, bg="white", width=self.width, height=self.height)
        self.canvas.pack()

        frame = tk.Frame(window)
        frame.pack()
        btStop = tk.Button(frame, text="Stop", command=self.stop)
        btStop.pack(side=tk.LEFT)
        btResume = tk.Button(frame, text="Resume", command=self.resume)
        btResume.pack(side=tk.LEFT)
        btAdd = tk.Button(frame, text="+", command=self.add)
        btAdd.pack(side=tk.LEFT)
        btRemove = tk.Button(frame, text="-", command=self.remove)
        btRemove.pack(side=tk.LEFT)

        self.sleepTime = 100  # Set a sleep time
        self.isStopped = False
        self.animate()

        window.mainloop()

    def stop(self):  # Stop animation
        self.isStopped = True

    def resume(self):  # Resume animation
        self.isStopped = False
        self.animate()

    def add(self):  # Add a new ball
        self.ballList.append(Ball())

    def remove(self):  # Remove the last ball
        self.ballList.pop()

    def animate(self):  # Move the message
        while not self.isStopped:
            self.canvas.after(self.sleepTime)  # Sleep
            self.canvas.update()  # Update self.canvas
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
        self.canvas.create_oval(
            ball.x - ball.radius,
            ball.y - ball.radius,
            ball.x + ball.radius,
            ball.y + ball.radius,
            fill=ball.color,
            tags="ball",
        )

"""
print('目前無法移動中關閉視窗')
BounceBalls()  # Create GUI
"""
print("------------------------------------------------------------")  # 60個


class ControlAnimation:
    def __init__(self):
        window = tk.Tk()
        window.title("Control Animation Demo")

        self.width = 250  # Width of the self.canvas
        self.canvas = tk.Canvas(window, bg="white", width=self.width, height=50)
        self.canvas.pack()

        frame = tk.Frame(window)
        frame.pack()
        btStop = tk.Button(frame, text="Stop", command=self.stop)
        btStop.pack(side=tk.LEFT)
        btResume = tk.Button(frame, text="Resume", command=self.resume)
        btResume.pack(side=tk.LEFT)
        btFaster = tk.Button(frame, text="Faster", command=self.faster)
        btFaster.pack(side=tk.LEFT)
        btSlower = tk.Button(frame, text="Slower", command=self.slower)
        btSlower.pack(side=tk.LEFT)

        self.x = 0  # Starting x position
        self.sleepTime = 100  # Set a sleep time
        self.canvas.create_text(self.x, 30, text="Message moving?", tags="text")

        self.dx = 3
        self.isStopped = False
        self.animate()

        window.mainloop()

    def stop(self):  # Stop animation
        self.isStopped = True

    def resume(self):  # Resume animation
        self.isStopped = False
        self.animate()

    def faster(self):  # Speed up the animation
        if self.sleepTime > 5:
            self.sleepTime -= 20

    def slower(self):  # Slow down the animation
        self.sleepTime += 20

    def animate(self):  # Move the message
        while not self.isStopped:
            self.canvas.move("text", self.dx, 0)  # Move text
            self.canvas.after(self.sleepTime)  # Sleep
            self.canvas.update()  # Update self.canvas
            if self.x < self.width:
                self.x += self.dx  # Set new position
            else:
                self.x = 0  # Reset string position to the beginning
                self.canvas.delete("text")
                # Redraw text at the beginning
                self.canvas.create_text(self.x, 30, text="Message moving?", tags="text")

"""
print('目前無法移動中關閉視窗')
ControlAnimation()  # Create GUI
"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


