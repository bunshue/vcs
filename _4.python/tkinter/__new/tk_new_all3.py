from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
x_center, y_center, r = 320, 240, 100
x, y = [], []
for i in range(12):         # 建立圓外圍12個點
    x.append(x_center + r * math.cos(30*i*math.pi/180))
    y.append(y_center + r * math.sin(30*i*math.pi/180))
for i in range(12):         # 執行12個點彼此連線
    for j in range(12):
        canvas.create_line(x[i],y[i],x[j],y[j])


print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_2.py

from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_line(100,100,500,100)
canvas.create_line(100,125,500,125,width=5)
canvas.create_line(100,150,500,150,width=10,fill='blue')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_3.py

from tkinter import *
from random import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
for i in range(50):                 # 隨機繪50個不同位置與大小的矩形
    x1, y1 = randint(1, 640), randint(1, 480)
    x2, y2 = randint(1, 640), randint(1, 480)
    if x1 > x2: x1,x2 = x2,x1       # 確保左上角x座標小於右下角x座標
    if y1 > y2: y1,y2 = y2,y1       # 確保左上角y座標小於右下角y座標
    canvas.create_rectangle(x1, y1, x2, y2)














print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_4.py

from tkinter import *
from random import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_rectangle(10, 10, 120, 60, fill='red')
canvas.create_rectangle(130, 10, 200, 80, fill='yellow', outline='blue')
canvas.create_rectangle(210, 10, 300, 60, fill='green', outline='grey')












print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_5.py

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
# 以下以圓形為基礎
canvas.create_arc(10, 10, 110, 110, extent=45, style=ARC)
canvas.create_arc(210, 10, 310, 110, extent=90, style=ARC)
canvas.create_arc(410, 10, 510, 110, extent=180, fill='yellow')
canvas.create_arc(10, 110, 110, 210, extent=270, style=ARC)
canvas.create_arc(210, 110, 310, 210, extent=359, style=ARC, width=5)
# 以下以橢圓形為基礎
canvas.create_arc(10, 250, 310, 350, extent=90, style=ARC, start=90)
canvas.create_arc(320, 250, 620, 350, extent=180, style=ARC)
canvas.create_arc(10, 360, 310, 460, extent=270, style=ARC, outline='blue')
canvas.create_arc(320, 360, 620, 460, extent=359, style=ARC)










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_6.py

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
# 以下是圓形
canvas.create_oval(10, 10, 110, 110)
canvas.create_oval(150, 10, 300, 160, fill='yellow')
# 以下是橢圓形
canvas.create_oval(10, 200, 310, 350)
canvas.create_oval(350, 200, 550, 300, fill='aqua', outline='blue', width=5)











print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_7.py

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
canvas.create_polygon(10,10, 100,10, 50,80, fill='', outline='black')
canvas.create_polygon(120,10, 180,30, 250,100, 200,90, 130,80)
canvas.create_polygon(200,10, 350,30, 420,70, 360,90, fill='aqua')
canvas.create_polygon(400,10,600,10,450,80,width=5,outline='blue',fill='yellow')






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_8.py

from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
#canvas = Canvas(tk, width=640, height=240, bg='yellow')
canvas.pack()

canvas.create_text(200, 50, text='Ming-Chi Institute of Technology')
canvas.create_text(200, 80, text='Ming-Chi Institute of Technology', fill='blue')
canvas.create_text(300, 120, text='Ming-Chi Institute of Technology', fill='blue',
                   font=('Old English Text MT',20))
canvas.create_text(300, 160, text='Ming-Chi Institute of Technology', fill='blue',
                   font=('華康新綜藝體 Std W7',20))
canvas.create_text(300, 200, text='明志科技大學', fill='blue',
                   font=('華康新綜藝體 Std W7',20))


print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_10.py

from tkinter import *
def bgUpdate(source):
    ''' 更改畫布背景顏色 '''
    red = rSlider.get()                                 # 讀取red值
    green = gSlider.get()                               # 讀取green值
    blue = bSlider.get( )                               # 讀取blue值
    print("R=%d, G=%d, B=%d" % (red, green, blue))      # 列印色彩數值
    myColor = "#%02x%02x%02x" % (red, green, blue)      # 將顏色轉成16進位字串
    canvas.config(bg=myColor)                           # 設定畫布背景顏色
    
tk = Tk()
canvas = Canvas(tk, width=640, height=240)              # 初始化背景
rSlider = Scale(tk, from_=0, to=255, command=bgUpdate)
gSlider = Scale(tk, from_=0, to=255, command=bgUpdate)
bSlider = Scale(tk, from_=0, to=255, command=bgUpdate)
gSlider.set(125)                                        # 設定green是125
rSlider.grid(row=1, column=1)                           # 第一行第一欄
gSlider.grid(row=1, column=2)                           # 第一行第二欄
bSlider.grid(row=1, column=3)                           # 第一行第三欄
canvas.grid(row=2, column=1, columnspan=3)              # 第二行全部
mainloop()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_11.move.py

# ch19_11.py
from tkinter import *
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

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_12.move.py

from tkinter import *
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

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_13.move.py

from tkinter import *
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

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_14.py

# ch19_14.py
from tkinter import *
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

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_15.py

# ch19_15.py
from tkinter import *
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

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_16.py

# ch19_16.py 
from tkinter import *
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
tk.title("Bouncing Ball")                       # 遊戲視窗標題
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

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_17.py

# ch19_17.py
from tkinter import *

tk = Tk()
canvas= Canvas(tk, width=500, height=150)
canvas.pack()
id = canvas.create_oval(10,50,60,100,fill='yellow', outline='lightgray')
ballPos = canvas.coords(id)
print(ballPos)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_18.py

# ch19_18.py 
from tkinter import *
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
tk.title("Bouncing Ball")                       # 遊戲視窗標題
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

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_19.py

# ch19_19.py 
from tkinter import *
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
tk.title("Bouncing Ball")                       # 遊戲視窗標題
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

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_20.py

# ch19_20.py 
from tkinter import *
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
tk.title("Bouncing Ball")                       # 遊戲視窗標題
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

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_21.py

# ch19_21.py 
from tkinter import *
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
tk.title("Bouncing Ball")                       # 遊戲視窗標題
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

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_22.py

# ch19_22.py 
from tkinter import *
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
tk.title("Bouncing Ball")                       # 遊戲視窗標題
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

#檔案 : C:\_git\vcs\_4.python\tkinter\__new\new4\ch19_23.py

# ch19_23.py 
from tkinter import *
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
tk.title("Bouncing Ball")                       # 遊戲視窗標題
tk.wm_attributes('-topmost', 1)                 # 確保遊戲視窗在螢幕最上層
canvas = Canvas(tk, width=winW, height=winH)
canvas.pack()
tk.update()

racket = Racket(canvas, 'purple')               # 定義紫色球拍
ball = Ball(canvas,'yellow',winW,winH,racket)   # 定義球物件

while ball.notTouchBottom:                      # 如果球未接觸畫布底端                   
    try:
        ball.ballMove()
    except:
        print("按關閉紐終止程式執行")
        break
    racket.racketMove()
    tk.update()
    time.sleep(speed)                           # 可以控制移動速度


    







print("------------------------------------------------------------")  # 60個










