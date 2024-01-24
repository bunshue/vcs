import sys

print("------------------------------------------------------------")  # 60個

print("turtle 01")

import turtle

t = turtle.Pen()
sides = 5                       # 星星的個數
angle = 180 - (180 / sides)     # 每個迴圈海龜轉動角度
size = 100                      # 星星長度
for x in range(sides):
    t.forward(size)             # 海龜向前繪線移動100
    t.right(angle)              # 海龜方向左轉的度數

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 02")

import turtle

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


turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 03")

import turtle

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
stars(5, 60, 'yellow', 0, 0)


turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 04")

import turtle
import random

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


turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 05")

import turtle
import random

def is_inside():
    ''' 測試是否在繪布範圍 '''
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


turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 06")

import turtle

t = turtle.Pen()
t.color('blue')
t.shape('turtle')
for angle in range(0, 361, 15):
    t.forward(100)
    t.stamp()
    t.home()                # 海龜返回原點
    t.seth(angle)           # 調整海龜方向


turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 07")

import turtle
import time

t = turtle.Pen()
t.color('blue')
t.shape('turtle')
firstStamp = t.stamp()      # 蓋章第1隻海龜
t.forward(100)
secondStamp = t.stamp()     # 蓋章第2隻海龜
t.forward(100)
thirdStamp = t.stamp()      # 蓋章第3隻海龜
t.hideturtle()              # 隱藏目前海龜
time.sleep(5)
t.clearstamp(secondStamp)   # 刪除第2隻海龜
time.sleep(5)
t.clearstamps(None)         # 刪除所有海龜


turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 08")

import turtle
import time

t = turtle.Pen()
t.color('blue')
t.shape('turtle')
t.stamp()                   # 蓋章第1隻海龜
print("目前有顯示海龜 : ", t.isvisible())
t.forward(100)
secondStamp = t.stamp()     # 蓋章第2隻海龜
time.sleep(3)
t.hideturtle()              # 隱藏目前海龜
print("目前有顯示海龜 : ", t.isvisible())
t.clearstamps(-1)           # 刪除後面1個海龜
time.sleep(3)
t.showturtle()              # 顯示海龜
print("目前有顯示海龜 : ", t.isvisible())


turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 09")

import turtle
import time

t = turtle.Pen()
t.color('blue')
print(t.screen.getshapes())             # 列印海龜游標字串

for cursor in t.screen.getshapes():
    t.shape(cursor)                     # 更改海龜游標
    t.stamp()                           # 海龜游標蓋章
    t.forward(30)


turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 10")

import turtle
import time

colorsList = ['green', 'yellow', 'red']

t = turtle.Pen()
for i in range(0,3):
    t.fillcolor(colorsList[i%3])    # 更改色彩
    t.begin_fill()                  # 開始填充
    t.circle(50)                    # 繪製左方圓
    t.end_fill()                    # 結束填充
    time.sleep(3)                   # 每隔3秒執行一次迴圈
    

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 11")

import turtle
import time

colorsList = ['green', 'yellow', 'red']

t = turtle.Pen()
t.speed(10)                             # 加速繪製圖形
t.ht()                                  # 隱藏海龜游標
for i in range(0,3):
    t.color('white', colorsList[i%3])   # 更改色彩
    t.begin_fill()                      # 開始填充
    t.circle(50)                        # 繪製左方圓
    t.end_fill()                        # 結束填充
    time.sleep(3)                       # 每隔3秒執行一次迴圈
    

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 12")

import turtle

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
    

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 13")

import turtle

t = turtle.Pen()
t.shape('turtle')
# 繪製時鐘中間顏色
t.color('white', 'aqua')
t.setpos(0, -120)
t.begin_fill()
t.circle(120)           # 繪時鐘內圓盤
t.end_fill()
t.penup()               # 畫筆關閉
t.home()
t.pendown()             # 畫筆打開
t.color('black')
t.pensize(5)
# 繪製時鐘刻度
for i in range(1, 13):
    t.penup()           # 畫筆關閉
    t.seth(-30*i+90)    # 設定刻度的角度
    t.forward(180)
    t.pendown()         # 畫筆打開
    t.forward(30)       # 畫時間軸
    t.penup()
    t.forward(20)
    t.write(str(i), align="left") # 寫上刻度
    t.home()
# 繪製時鐘外框
t.home()
t.setpos(0, -270)
t.pendown()
t.pensize(10)
t.pencolor('blue')
t.circle(270)
# 寫上名字
t.penup()
t.setpos(0, 320)
t.pendown()
t.write('Python王者歸來', align="center", font=('新細明體', 24))
t.ht()                  # 隱藏游標


turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 14")

import turtle

def printStr(x, y):
    print(x, y)

t = turtle.Pen()
t.screen.onclick(printStr)
t.screen.mainloop()

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 15")

import turtle
    
def drawSignal(x, y):
    if x > 0:
        t.fillcolor('yellow')
    else:
        t.fillcolor('blue')
    t.penup()
    t.setpos(x,y-50)            # 設定繪圓起點      
    t.begin_fill()
    t.circle(50)
    t.end_fill()

t = turtle.Pen()
t.screen.onclick(drawSignal)
t.screen.mainloop()

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 16")

import turtle
    
def keyUp():
    t.seth(90)
    t.forward(50)
def keyDn():
    t.seth(270)
    t.forward(50)
    
t = turtle.Pen()
t.screen.onkey(keyUp, 'Up')
t.screen.onkey(keyDn, 'Down')
t.screen.listen()
t.screen.mainloop()

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 17")

import turtle

t = turtle.Pen()
colorsList = ['red','orange','yellow','green','blue','cyan','purple','violet']
for line in range(200):            
    t.color(colorsList[line % 8])
    t.forward(line*2)
    t.left(91)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 18")

import turtle

turtle.tracer(0,0)                      # 終止追蹤
t = turtle.Pen()

colorsList = ['red','green','blue']
for line in range(400):            
    t.color(colorsList[line % 3])
    t.forward(line)
    t.right(119)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 19")

import turtle

# 依據特定階級數繪製Sierpinski三角形
def sierpinski(order, p1, p2, p3):
    if order == 0:      # 階級數為0
        # 將3個點連接繪製成三角形
        drawLine(p1, p2)
        drawLine(p2, p3)
        drawLine(p3, p1)
    else:    
        # 取得三角形各邊長的中點
        p12 = midpoint(p1, p2)
        p23 = midpoint(p2, p3)
        p31 = midpoint(p3, p1)
        # 遞迴呼叫處理繪製三角形
        sierpinski(order - 1, p1, p12, p31)
        sierpinski(order - 1, p12, p2, p23)
        sierpinski(order - 1, p31, p23, p3)   
# 繪製p1和p2之間的線條
def drawLine(p1,p2):
    t.penup()
    t.setpos(p1[0],p1[1])
    t.pendown()
    t.setpos(p2[0],p2[1])
    t.penup()
    t.seth(0)  
# 傳回2點的中間值
def midpoint(p1, p2):
    p = [0,0]                       # 初值設定
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p

# main
t = turtle.Pen()
p1 = [0, 86.6]
p2 = [-100, -86.6]
p3 = [100, -86.6]
order = eval(input("輸入階級數 : "))
sierpinski(order, p1, p2, p3)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 20")

import turtle

t = turtle.Pen()
colorsList = ['red','orange','yellow','green','blue','cyan','purple','violet']
tWidth = 1                          # 最初畫筆寬度
for x in range(1, 41):
    t.color(colorsList[x % 8])      # 選擇畫筆顏色
    t.forward(2 + x * 5)            # 每次移動距離
    t.right(45)                     # 每次旋轉角度
    tWidth += x * 0.05              # 每次畫筆寬度遞增    
    t.width(tWidth)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 21")

import turtle

n = 300
step = 10
t = turtle.Pen()
t.color('blue')
for i in range(0, n+step, step):
    t.penup()
    t.setpos(i,0)
    t.pendown()
    t.setpos(0, n-i)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 22")

import turtle
import random

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

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 23")

import turtle

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

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 24")

import turtle

t = turtle.Pen()
t.color('blue')
for angle in range(0, 360, 15):
    t.setheading(angle)         # 調整海龜方向
    t.circle(100)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 25")

import turtle

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

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 26")

import turtle

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
    
   


print("------------------------------------------------------------")  # 60個




