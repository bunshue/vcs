# ch19_23.py 
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


    






