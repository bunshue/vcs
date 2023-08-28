from tkinter import *
from tkinter import messagebox
import threading
import random
GAME_WIDTH = 450
GAME_HEIGHT = 650
BOARD_X = 220
BOARD_Y = 600
BOARD_WIDTH = 80
BALL_RADIUS = 9
class App:
    def __init__(self, master):
        self.master = master
        #记录小球动画的第几帧
        self.ball_index = 0
        #记录游戏是否失败的旗标
        self.is_lose = False
        #初始化记录小球位置的变量
        self.curx = 260
        self.cury = 30
        self.boardx = BOARD_X
        self.init_widgets()
        self.vx = random.randint(3, 6) #x方向的速度
        self.vy = random.randint(5, 10) #y方向的速度
        #通过定时器指定0.1秒之后执行moveball函数
        self.t = threading.Timer(0.1, self.moveball)
        self.t.start()
    #创建界面组件
    def init_widgets(self):
        self.cv = Canvas(root, background='white',
            width=GAME_WIDTH, height=GAME_HEIGHT)
        self.cv.pack()
        #让画布得到焦点，从而可以响应按键事件
        self.cv.focus_set()
        self.cv.bms = []
        #初始化小球的动画帧
        for i in range(8):
            self.cv.bms.append(PhotoImage(file='images/ball_' + str(i+1) + '.gif'))
        #绘制小球
        self.ball = self.cv.create_image(self.curx, self.cury,
            image=self.cv.bms[self.ball_index])
        self.board = self.cv.create_rectangle(BOARD_X, BOARD_Y,
            BOARD_X + BOARD_WIDTH, BOARD_Y + 20, width=0, fill='lightblue')
        #为向左箭头按键绑定事件，挡板左移
        self.cv.bind('<Left>', self.move_left)
        #为向右箭头按键绑定事件，挡板右移
        self.cv.bind('<Right>', self.move_right)
    def move_left(self, event):
        if self.boardx <= 0:
            return 
        self.boardx -= 5
        self.cv.coords(self.board, self.boardx, BOARD_Y,
            self.boardx + BOARD_WIDTH, BOARD_Y + 20)
    def move_right(self, event):
        if self.boardx + BOARD_WIDTH >= GAME_WIDTH:
            return
        self.boardx += 5
        self.cv.coords(self.board, self.boardx, BOARD_Y,
            self.boardx + BOARD_WIDTH, BOARD_Y + 20)
    def moveball(self):
        self.curx += self.vx
        self.cury += self.vy
        #小球到了右边墙壁，转向
        if self.curx + BALL_RADIUS >= GAME_WIDTH:
            self.vx = -self.vx
        #小球到了左边墙壁，转向
        if self.curx - BALL_RADIUS <= 0:
            self.vx = -self.vx
        #小球到了上边墙壁，转向
        if self.cury - BALL_RADIUS <= 0:
            self.vy = -self.vy
        #小球到了挡板处
        if self.cury + BALL_RADIUS >= BOARD_Y:
            #如果在挡板范围内
            if self.boardx <= self.curx <= (self.boardx + BOARD_WIDTH):
                self.vy = -self.vy
            else:
                messagebox.showinfo(title='失败', message='您已经输了')
                self.is_lose = True
        self.cv.coords(self.ball, self.curx, self.cury)
        self.ball_index += 1
        self.cv.itemconfig(self.ball, image=self.cv.bms[self.ball_index % 8])
        #如果游戏还未失败，让定时器继续执行
        if not self.is_lose:
            #通过定时器指定0.1秒之后执行moveball函数
            self.t = threading.Timer(0.1, self.moveball)
            self.t.start()
root = Tk()
root.title("弹球游戏")
root.geometry('%dx%d' % (GAME_WIDTH, GAME_HEIGHT))  
#禁止改变窗口大小
root.resizable(width=False, height=False)
App(root)
root.mainloop()
