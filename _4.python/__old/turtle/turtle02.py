# 一大堆turtle範例

import sys

import turtle
import random

import turtle as tu
'''
print("------------------------------------------------------------")  # 60個
"""
pos_list = list()
print("請問要畫幾邊形？")
n = 7
tu.color('red')
tu.speed(8)
tu.penup()
tu.goto(0,-200)
for i in range(n):
    tu.left(360//n)
    tu.forward(100)
    pos_list.append(tu.pos())
for i in range(len(pos_list)):
    for point in pos_list:
        tu.penup()
        tu.goto(pos_list[i])
        tu.pendown()
        tu.goto(point)
tu.done()

print('------------------------------------------------------------')	#60個

tu.speed(0)
tu.color('blue')
tu.pensize(3)
for i in range(150):
    tu.left(i//10)
    tu.forward(6)
tu.penup()
tu.home()
tu.pendown()
for i in range(150):
    tu.right(i//10)
    tu.forward(6)
tu.penup()
tu.home()
tu.pendown()
for i in range(150):
    tu.right(i//10)
    tu.backward(6)
tu.penup()
tu.home()
tu.pendown()
for i in range(150):
    tu.left(i//10)
    tu.backward(6)
tu.done()
"""
print("------------------------------------------------------------")  # 60個

import math

tu.speed(8)
tu.penup()
tu.goto(-200, 0)
tu.pendown()
for d in range(0, 361, 5):
    tu.goto(d - 200, 100 * math.sin(d * math.pi / 180))
tu.done()

print("------------------------------------------------------------")  # 60個

import math

tu.speed(8)
tu.pensize(3)
tu.penup()
tu.goto(-200, 0)
tu.color("red")
tu.pendown()
for d in range(0, 361, 5):
    tu.goto(d - 200, 100 * math.sin(d * math.pi / 180))
tu.penup()
tu.goto(-200, 100)
tu.color("blue")
tu.pendown()
for d in range(0, 361, 5):
    tu.goto(d - 200, 100 * math.cos(d * math.pi / 180))
tu.done()

print("------------------------------------------------------------")  # 60個

import math

tu.speed(8)

tu.pensize(3)
tu.penup()
tu.goto(150, 0)
tu.color("red")
tu.pendown()
for d in range(0, 361, 2):
    x = 150 * math.cos(3 * d * math.pi / 180)
    y = 150 * math.sin(7 * d * math.pi / 180)
    tu.goto(x, y)
tu.done()

print("------------------------------------------------------------")  # 60個

import math


def th(degree):
    return degree * math.pi / 180


r = 100
tu.speed(8)
tu.pensize(3)
tu.penup()
tu.color("red")
for d in range(0, 361, 2):
    x = 2 * r * (math.cos(th(d)) - 0.5 * math.cos(2 * th(d)))
    y = 2 * r * (math.sin(th(d)) - 0.5 * math.sin(2 * th(d)))
    if d:
        tu.pendown()
    tu.goto(x, y)
tu.done()

print("------------------------------------------------------------")  # 60個

import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
pg.display.set_caption("Richard's pygame!")
bk = pg.Surface(screen.get_size())
bk.fill((255, 255, 255))
screen.blit(bk, (0, 0))
pg.display.update()
quit = False
while not quit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit = True
pg.quit()

print("------------------------------------------------------------")  # 60個

import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
pg.display.set_caption("Richard's pygame!")
bk = pg.Surface(screen.get_size())
bk.fill((255, 255, 255))
pg.draw.rect(bk, (255, 0, 0), (100, 100, 300, 300), 2)
screen.blit(bk, (0, 0))
pg.display.update()
quit = False
while not quit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit = True
pg.quit()

print("------------------------------------------------------------")  # 60個

import pygame as pg
import math

pg.init()
screen = pg.display.set_mode((640, 480))
pg.display.set_caption("Richard's pygame!")
bk = pg.Surface(screen.get_size())
bk.fill((255, 255, 255))
lines = list()
for th in range(0, 361):
    y = 250 - 200 * math.sin(th * math.pi / 180)
    lines.append((th + 140, y))
pg.draw.lines(bk, (0, 0, 255), False, lines, 2)

screen.blit(bk, (0, 0))
pg.display.update()
quit = False
while not quit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit = True
pg.quit()

"""
print('------------------------------------------------------------')	#60個
print('畫一個五角星形 空心')
t = turtle.Pen()
sides = 5                       # 星星的個數
angle = 180 - (180 / sides)     # 每個迴圈海龜轉動角度
size = 100                      # 星星長度
for x in range(sides):
    t.forward(size)             # 海龜向前繪線移動100
    t.right(angle)              # 海龜方向左轉的度數

print('------------------------------------------------------------')	#60個

t = turtle.Pen()
t.pensize(5)                        # 畫筆寬度
colorValue = 1.0
colorStep = colorValue / 36
for x in range(1, 37):
    colorValue -= colorStep
    t.color(0.5, 1, colorValue)     # 色彩調整
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(100)
"""

"""
print('------------------------------------------------------------')	#60個
print('畫八卦形')

t = turtle.Pen()
colorsList = ['red','orange','yellow','green','blue','cyan','purple','violet']
tWidth = 1                          # 最初畫筆寬度
for x in range(1, 41):
    t.color(colorsList[x % 8])      # 選擇畫筆顏色
    t.forward(2 + x * 5)            # 每次移動距離
    t.right(45)                     # 每次旋轉角度
    tWidth += x * 0.05              # 每次畫筆寬度遞增    
    t.width(tWidth)

print('------------------------------------------------------------')	#60個

print('畫二維平面連線')
n = 300
step = 10
t = turtle.Pen()
t.color('blue')
for i in range(0, n+step, step):
    t.penup()
    t.setpos(i,0)
    t.pendown()
    t.setpos(0, n-i)

print('------------------------------------------------------------')	#60個


print('畫二維平面連線')

n = 300
step = 10
t = turtle.Pen()
colorsList = ['red','orange','yellow','green','blue','cyan','purple','violet']
for i in range(0, n+step, step):
    t.color(random.choice(colorsList))      # 使用不同顏色
    t.setpos(i, 0)
    t.setpos(0, n-i)
    t.setpos(-i, 0)
    t.setpos(0, i-n)
    t.setpos(i, 0)

print('------------------------------------------------------------')	#60個


print('畫一些圓形 1')

t = turtle.Pen()
t.color('blue')
t.penup()
t.setheading(180)                   # 海龜往左
t.forward(150)                      # 移動往左
t.setheading(0)                     # 海龜往右
t.pendown()
t.circle(50)                        # 繪製第1個左上方圓
t.circle(-50)                       # 繪製第2個左下方圓
t.forward(100)
t.circle(50)                        # 繪製第3個右上方圓
t.circle(-50)                       # 繪製第4個右下方圓

t.penup()
t.forward(100)                      # 移動往右
t.pendown()
t.setheading(0)
step = 5                            # 每次增加距離
for r in range(10, 100+step, step):
    t.penup()                       # 將筆提起
    t.setpos(150, -100)             # 海龜到點(150,100)
    t.setheading(0)                 
    t.pendown()                     # 將筆放下準備繪製
    t.circle(r, 90 + r*2)           # 繪製圓      


print('------------------------------------------------------------')	#60個

print('畫一些圓形 2')

t = turtle.Pen()
t.color('blue')
for angle in range(0, 360, 15):
    t.setheading(angle)         # 調整海龜方向
    t.circle(100)

print('------------------------------------------------------------')	#60個


print('畫一些多邊形 空心')
t = turtle.Pen()
t.color('blue')
r = 30                              # 半徑
t.penup()
t.setheading(180)                   # 海龜往左
t.forward(270)                      # 移動往左
t.setheading(0)                     # 海龜往右

for edge in range(3, 13, 1):        # 繪3 - 12邊圖
    t.pendown()
    t.circle(r, steps=edge)
    t.penup()
    t.forward(60)

print('------------------------------------------------------------')	#60個

print('畫一些多邊形 實心')
t = turtle.Pen()
t.color('white')
r = 30                              # 半徑
t.penup()
t.setheading(180)                   # 海龜往左
t.forward(270)                      # 移動往左
t.setheading(0)                     # 海龜往右
colorsList = ['red','orange','yellow','green','blue','cyan','purple','violet']
for edge in range(3, 13, 1):        # 繪3 - 12邊圖
    t.pendown()
    t.fillcolor(colorsList[edge % 8])
    t.begin_fill()
    t.circle(r, steps=edge)
    t.end_fill()
    t.penup()
    t.forward(60)

print('------------------------------------------------------------')	#60個

print('畫一個五角星形 實心')
t = turtle.Pen()
sides = 5                       # 星星的個數
angle = 180 - (180 / sides)     # 每個迴圈海龜轉動角度
size = 100                      # 星星長度
t.color('blue')
t.begin_fill()
for x in range(sides):
    t.forward(size)             # 海龜向前繪線移動100
    t.right(angle)              # 海龜方向左轉的度數
t.end_fill()

print('------------------------------------------------------------')	#60個

print('畫一個五角星形 實心')

def stars(sides, size, cr, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / sides)     # 每個迴圈海龜轉動角度
    t.color(cr)
    t.begin_fill()
    for x in range(sides):
        t.forward(size)             # 海龜向前繪線移動100
        t.right(angle)              # 海龜方向左轉的度數
    t.end_fill()
t = turtle.Pen()
t.screen.bgcolor('blue')    #設定畫面的背景色
stars(5, 60, 'yellow', 0, 0)

print('------------------------------------------------------------')	#60個

print('畫任意五角星形 實心')

def stars(sides, size, cr, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / sides)     # 每個迴圈海龜轉動角度
    t.color(cr)
    t.begin_fill()
    for x in range(sides):
        t.forward(size)             # 海龜向前繪線移動100
        t.right(angle)              # 海龜方向左轉的度數
    t.end_fill()
t = turtle.Pen()
t.screen.bgcolor('blue')
t.ht()
color_list = ['yellow','white','gold','pink','gray',
              'red','orange','aqua','green']
while True:
    ran_sides = random.randint(2, 5) * 2 + 1   # 限制星星角度是5-11的奇數
    ran_size = random.randint(5, 30)
    ran_color = random.choice(color_list)
    ran_x = random.randint(-250,250)
    ran_y = random.randint(-250,250)
    stars(ran_sides,ran_size,ran_color,ran_x,ran_y)

print('------------------------------------------------------------')	#60個

print('畫random walk')

def is_inside():
    #測試是否在繪布範圍
    left = (-t.screen.window_width() / 2) + 100             # 左邊牆
    right = (t.screen.window_width() / 2) - 100             # 右邊牆
    top = (t.screen.window_height() / 2) - 100              # 上邊牆
    bottom = (-t.screen.window_height() / 2) + 100          # 下邊牆
    x, y = t.pos()                                          # 海龜座標
    is_inside = (left < x < right) and (bottom < y < top)
    return is_inside

def turtle_move():
    colors = ['blue', 'pink', 'green', 'red', 'yellow', 'aqua']
    t.color(random.choice(colors))              # 繪圖顏色
    t.begin_fill()
    if is_inside():                             # 如果在繪布範圍
        t.right(random.randint(0, 180))         # 海龜移動角度
        t.forward(length)
    else:
        t.backward(length)
    t.end_fill()
    
t = turtle.Pen()
length = 100                                    # 線長
width = 10                                      # 線寬
t.pensize(width)                                # 設定畫筆寬
t.screen.bgcolor('black')                       # 畫布背景
while True:
    turtle_move()

print('------------------------------------------------------------')	#60個

print('畫不同色筆連線')
t = turtle.Pen()
colorsList = ['red','orange','yellow','green','blue','cyan','purple','violet']
for line in range(200):            
    t.color(colorsList[line % 8])
    t.forward(line*2)
    t.left(91)
    
print('------------------------------------------------------------')	#60個

"""
print("畫不同色筆連線")

turtle.tracer(0, 0)  # 終止追蹤
t = turtle.Pen()

colorsList = ["red", "green", "blue"]
for line in range(400):
    t.color(colorsList[line % 3])
    t.forward(line)
    t.right(119)

print("------------------------------------------------------------")  # 60個

'''

"""
print('滑鼠點擊離開視窗')
turtle.Screen().exitonclick()
"""
'''
import time

# Pendulum motion

bar = turtle.Turtle(visible=False)
pen = turtle.Turtle(visible=False)

pen.speed(20)
bar.speed(20)

pen.color("red")
bar.color("red")

bar.fd(40)
bar.back(80)
pen.right(90)


def left(rounds):
    for i in range(rounds):
        pen.fd(120)
        pen.right(90)
        pen.fd(3)
        pen.circle(10)
        pen.back(3)
        pen.left(90)
        pen.back(120)
        pen.right(3)
        time.sleep(0.2)
        pen.clear()


def right(rounds):
    for j in range(rounds):
        pen.fd(120)
        pen.right(90)
        pen.fd(3)
        pen.circle(10)
        pen.back(3)
        pen.left(90)
        pen.back(120)
        pen.left(3)
        time.sleep(0.2)
        pen.clear()

N = 1  # 次數
m = 13
for k in range(N):
    print(k)
    left(m)
    right(m)
    right(m)
    left(m)
    m -= 4
pen.fd(120)
pen.right(90)
pen.fd(3)
pen.circle(10)

print("------------------------------------------------------------")  # 60個
'''

# writing the labels for simulation
text = turtle.Turtle(visible=False)
text.goto(200, 300)
text.write("Trajectory of motion", font=("Ariel", 16, "normal"))
text.rt(90)
text.fd(100)
text.write("Radial Acceleration", font=("Ariel", 16, "normal"))
text.fd(100)
text.write("Tangential acceleration", font=("Ariel", 16, "normal"))
text.fd(100)
text.write("Object in motion", font=("Ariel", 16, "normal"))

# text.reset()

print("------------------------------------------------------------")  # 60個


import turtle
import time

turtle1 = turtle.Turtle(visible=False)
turtle2 = turtle.Turtle(visible=False)
turtle3 = turtle.Turtle(visible=False)

turtle1.speed(20)
turtle2.speed(20)
turtle3.speed(20)

turtle1.color("red")
turtle2.color("green")
turtle3.color("blue")

turtle1.pensize(5)
turtle2.pensize(5)
turtle3.pensize(5)

turtle1.goto(-200,100)
turtle2.goto(-200,0)
turtle3.goto(-200,-100)

for i in range(16):
    turtle1.forward(30)
    turtle2.forward(30)
    turtle3.forward(30)

    time.sleep(0.1)

"""
time.sleep(3)

# 清除單一海龜 reset
turtle1.reset()
# turtle2.reset()
# turtle3.reset()

time.sleep(3)
# 清除單一海龜 clear
#turtle1.clear()
#turtle2.clear()
turtle3.clear()


# 清除全部海龜
turtle.Screen().clear()
"""



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

