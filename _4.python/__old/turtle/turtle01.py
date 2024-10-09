"""

基本的 turtle 使用


"""


import sys
import time
import random

import turtle

"""
turtle模組方法

screen.setup()

turtle.pensize()

turtle.forward(x)	從目前方向向前走x步
turtle.back(x)		從目前方向向後走x步
turtle.left(x)		從目前方向逆時針向轉x度
turtle.right(x)		從目前方向順時針向轉x度
"""

'''
print("------------------------------------------------------------")  # 60個
print("1. turtle 基本設定")
print("------------------------------------------------------------")  # 60個

turtle.setup(1000, 1000)  # 產生 1000 X 1000 畫布





print("------------------------------------------------------------")  # 60個
print("2. turtle 簡易畫圖")
print("------------------------------------------------------------")  # 60個

print("畫點")
turtle.dot(100, "yellow")  # 畫一個實心圓圈 (直徑, 顏色)
turtle.dot(50, "Red")
turtle.dot(30, "green")
turtle.dot(10, 'green')


print("畫字")

turtle.write("12345", font=("Helvetica", 12, "normal"))

turtle.rt(90)  # 順時針轉N度
turtle.fd(50)
turtle.write("abcde", font=("Helvetica", 12, "normal"))

turtle.fd(50)
turtle.write("ABCDE", font=("Helvetica", 12, "normal"))

turtle.fd(50)
# DisplayUnicode
turtle.write("\u6B22\u8FCE \u03b1 \u03b2 \u03b3")

turtle.fd(50)
turtle.write("Cool Colorful Shapes", font = ("Times", 18, "bold"))


print("畫圓")
turtle.circle(20, 360, 10)

turtle.goto(-200, 200)
turtle.circle(50)  # 繪製第1個左上方圓
turtle.circle(-50)  # 繪製第2個左下方圓
turtle.forward(100)
turtle.circle(50)  # 繪製第3個右上方圓
turtle.circle(-50)  # 繪製第4個右下方圓

turtle.circle(50)  # 繪製第1個左上方圓
turtle.circle(-50)  # 繪製第2個左下方圓
turtle.forward(100)
turtle.circle(50)  # 繪製第3個右上方圓
turtle.circle(-50)  # 繪製第4個右下方圓

turtle.circle(50)  # 繪製第1個左上方圓
turtle.circle(-50, steps=3)  # 繪製第2個左下方三角形
turtle.forward(100)
turtle.circle(50, steps=4)  # 繪製第3個右上方四邊形
turtle.circle(-50, steps=5)  # 繪製第4個右下方五邊形

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

turtle.goto(100, 100)  # 移動畫筆到指定的x、y座標
turtle.goto(100, -100)
turtle.goto(-100, 100)
turtle.goto(-100, -100)
turtle.home()  # 回到原點(x = 0, y = 0)

turtle.forward(50)  # 畫筆前進
turtle.goto(50, 50)  # 畫筆移到座標(50, 50)
turtle.backward(50)  # 畫筆向後
turtle.home()  # 畫筆回到原點


origin = 0, 0  # 設定原點

turtle.speed(2)
turtle.pu()  # 提筆
turtle.goto(origin)
turtle.pd()  # 下筆

turtle.color("black")  # 線色, 字色

# 初始化完成

turtle.pu()  # 提筆
turtle.pd()  # 下筆

turtle.fd(100)
turtle.rt(90)  # 順時針轉N度
turtle.fd(100)
turtle.lt(90)  # 逆時針轉N度
turtle.fd(100)
turtle.forward(100)  # 直走100步
turtle.right(90)  # 右轉90度
turtle.forward(50)  # 直走50步
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)


turtle.pu()  # 提筆

turtle.goto(origin)


#turtle.done()  # 最後用




print("------------------------------------------------------------")  # 60個

turtle.color("red", "yellow")  # 前 : 線色, 字色, 後 : 標記色

turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()
turtle.done()

print("------------------------------------------------------------")  # 60個

# 畫圓
repeats = 0
while repeats <= 360:
    turtle.forward(10)
    turtle.right(10)
    repeats = repeats + 10

print("------------------------------------------------------------")  # 60個


W = 1000
H = 1000
x_st = 200
y_st = 0
turtle.setup(W, H, x_st, y_st)  # 指定畫布的大小與位置

turtle.showturtle()  # 顯示標記
# turtle.hideturtle() # 隱藏標記, 以免遮蔽

origin = 0, 0  # 設定原點
turtle.color("blue")  # 線色
turtle.goto(-W // 2, 0)
turtle.goto(W // 2, 0)
turtle.goto(origin)
turtle.goto(0, -H // 2)
turtle.goto(0, W // 2)
turtle.goto(origin)

turtle.color("red")  # 線色
turtle.pensize(10)

# 空心圓半徑 R, 內接N邊形
turtle.circle(150)
turtle.circle(150, 360, 3)
turtle.circle(150, 360, 5)

print("畫圓, 圓心在turtle的左邊 ??")
r = 100
turtle.circle(r)  # r 正值, 逆時針畫圓

r = -100
turtle.circle(r)  # r 負值, 順時針畫圓

r = 75
turtle.circle(r, 235)  # 畫圓弧 235度

r = 50
N = 5
turtle.circle(r, 360, N)  # 正N邊形


turtle.circle(150)

# 畫中央實心三角形
turtle.begin_fill()
turtle.circle(100, 360, 3)
turtle.end_fill()

turtle.color("red")
turtle.begin_fill()
turtle.color("red")
turtle.circle(40, steps=3)  # Draw a triangle

turtle.color("green")
turtle.circle(100, 270, 10)
turtle.circle(100, 270, 10)

turtle.end_fill()
# turtle.hide()

# 畫右半部直線
turtle.color("blue")  # 線色
turtle.forward(150)

turtle.setheading(270)
turtle.color("red")  # 線色
turtle.pensize(10)

# 回到中心點
turtle.pensize(1)
turtle.color("blue")  # 線色
turtle.setheading(180)
turtle.penup()
turtle.forward(150)
turtle.pendown()

# 畫左半部直線
turtle.forward(150)
turtle.setheading(90)

turtle.color("red")
turtle.pensize(2)

turtle.pensize(1)

# 回到中心點
turtle.setheading(0)
turtle.penup()
turtle.forward(150)

turtle.setheading(180)
turtle.color("green")
turtle.pendown()

print("------------------------------------------------------------")  # 60個

turtle.forward(100)  # 海龜向前繪線移動100
turtle.left(90)  # 海龜方向左轉90度
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

turtle.color("blue")
for angle in range(0, 360, 15):
    turtle.setheading(angle)  # 調整海龜方向
    turtle.circle(100)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個


def drawShape(sides, length):  # 畫多邊形
    angle = 360.0 / sides
    for side in range(sides):
        turtle.forward(length)
        turtle.right(angle)


def moveTurtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def drawSquare(length):  # 畫正方形
    drawShape(4, length)


def drawTriangle(length):  # 畫三角形
    drawShape(3, length)


def drawCircle(length):  # 畫圓形
    drawShape(360, length)


repeats = 0
while repeats < 360:  # 走一步轉一度
    turtle.forward(1)
    turtle.right(1)
    repeats = repeats + 1


length = 0
angle = 90
while length < 200:
    turtle.forward(length)
    turtle.left(angle)
    length = length + 10


# sides = int(input("Enter the number of sides for your shape: "))
# 畫空心八邊形
sides = 8
angle = 360.0 / sides
length = 400.0 / sides

for side in range(sides):
    turtle.forward(length)
    turtle.right(angle)

turtle.done()      #最後再用

print("------------------------------------------------------------")  # 60個


moveTurtle(160, 0)


print("------------------------------------------------------------")  # 60個

# 畫實心八邊形
sides = 8
angle = 360.0 / sides
length = 400.0 / sides

turtle.fillcolor("red")
turtle.begin_fill()

for side in range(sides):
    turtle.forward(length)
    turtle.right(angle)
turtle.end_fill()

turtle.done()      #最後再用

print("------------------------------------------------------------")  # 60個

drawShape(4, 10)
moveTurtle(60, 30)
drawShape(3, 20)

drawShape(4, 10)

drawSquare(30)
drawCircle(1)
drawCircle(2)
drawTriangle(60)

print("------------------------------------------------------------")  # 60個


def moveTurtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


turtle.speed(8)  # speed(速度等級, 1 ~ 10)

turtle.color("black")
turtle.pensize(2)

moveTurtle(-200, 0)
turtle.goto(200, 0)
turtle.goto(200, 200)
turtle.goto(-200, 200)
turtle.goto(-200, -200)
turtle.goto(200, -200)
turtle.goto(200, 0)
moveTurtle(0, 200)
turtle.goto(0, -200)

moveTurtle(0, 0)

turtle.color("blue")
turtle.pensize(6)

turtle.fillcolor("red")

turtle.begin_fill()

turtle.forward(100)  # 直走100步
turtle.right(90)  # 右轉90度
print("目前方位", turtle.heading())
turtle.forward(50)  # 直走50步
turtle.right(90)
print("目前方位", turtle.heading())
turtle.forward(100)
turtle.right(90)
print("目前方位", turtle.heading())
turtle.forward(50)
turtle.right(90)
print("目前方位", turtle.heading())

turtle.end_fill()

turtle.backward(100)


moveTurtle(-100, -100)

# turtle.clear() #清除畫布的所有內容

moveTurtle(-100, -100)

moveTurtle(-100, 100)


time.sleep(1)

angle = 0
while angle < 180:
    angle += 10
    turtle.setheading(angle)
    time.sleep(0.2)

turtle.done()  # 最後用

print("------------------------------------------------------------")  # 60個

x, y, n = 30, 50, 150

t = turtle.Pen()

t.penup()
t.setpos(x + n / 2, y + n / 2)
t.pendown()
t.seth(-180)
t.forward(n)
t.left(90)
t.forward(n)
t.left(90)
t.forward(n)
t.left(90)
t.forward(n)
t.penup()
t.setpos(0, 0)
t.seth(0)

print("------------------------------------------------------------")  # 60個

colorsList = ["green", "blue", "red"]

t = turtle.Pen()
t.ht()  # 隱藏海龜
t.speed(0)
t.penup()
t.setpos(-200, 0)
t.pendown()
r = 100
for i in range(1, 51):
    t.color(random.choice(colorsList))
    t.circle(r)
    t.penup()
    t.fd(5)
    t.pendown()
    r = r - 1

turtle.done()  # 最後用

print("------------------------------------------------------------")  # 60個

turtle.home()

# Draw a square
turtle.speed(1)  # Set a number between 1 to 10, the larger, the faster
turtle.undo()

# 空心星星
t = turtle.Pen()
sides = 5  # 星星的個數
angle = 180 - (180 / sides)  # 每個迴圈海龜轉動角度
size = 100  # 星星長度
for x in range(sides):
    t.forward(size)  # 海龜向前繪線移動100
    t.right(angle)  # 海龜方向左轉的度數

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

# 實心星星
t = turtle.Pen()
sides = 5  # 星星的個數
angle = 180 - (180 / sides)  # 每個迴圈海龜轉動角度
size = 100  # 星星長度
t.begin_fill()
for x in range(sides):
    t.forward(size)  # 海龜向前繪線移動100
    t.right(angle)  # 海龜方向左轉的度數
t.end_fill()

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

# 實心星星

def stars(sides, size, cr, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / sides)  # 每個迴圈海龜轉動角度
    t.color(cr)
    t.begin_fill()
    for x in range(sides):
        t.forward(size)  # 海龜向前繪線移動100
        t.right(angle)  # 海龜方向左轉的度數
    t.end_fill()


t = turtle.Pen()
t.screen.bgcolor("blue")
stars(5, 100, "red", -100, 0)
stars(5, 100, "green", 0, 0)
stars(5, 100, "yellow", 100, 0)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個


def stars(sides, size, cr, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / sides)  # 每個迴圈海龜轉動角度
    t.color(cr)
    t.begin_fill()
    for x in range(sides):
        t.forward(size)  # 海龜向前繪線移動100
        t.right(angle)  # 海龜方向左轉的度數
    t.end_fill()


t = turtle.Pen()
t.screen.bgcolor("blue")
t.ht()
color_list = [
    "yellow",
    "white",
    "gold",
    "pink",
    "gray",
    "red",
    "orange",
    "aqua",
    "green",
]
while True:
    ran_sides = random.randint(2, 5) * 2 + 1  # 限制星星角度是5-11的奇數
    ran_size = random.randint(5, 30)
    ran_color = random.choice(color_list)
    ran_x = random.randint(-250, 250)
    ran_y = random.randint(-250, 250)
    stars(ran_sides, ran_size, ran_color, ran_x, ran_y)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個


def is_inside():
    """測試是否在繪布範圍"""
    left = (-t.screen.window_width() / 2) + 100  # 左邊牆
    right = (t.screen.window_width() / 2) - 100  # 右邊牆
    top = (t.screen.window_height() / 2) - 100  # 上邊牆
    bottom = (-t.screen.window_height() / 2) + 100  # 下邊牆
    x, y = t.pos()  # 海龜座標
    is_inside = (left < x < right) and (bottom < y < top)
    return is_inside


def turtle_move():
    colors = ["blue", "pink", "green", "red", "yellow", "aqua"]
    t.color(random.choice(colors))  # 繪圖顏色
    t.begin_fill()
    if is_inside():  # 如果在繪布範圍
        #t.right(random.randint(320, 350))  # 海龜移動角度
        t.right(random.randint(0, 180))  # 海龜移動角度
        t.forward(length)
    else:
        t.backward(length)
    t.end_fill()


t = turtle.Pen()
length = 100  # 線長
width = 10  # 線寬
t.pensize(width)  # 設定畫筆寬
t.screen.bgcolor("black")  # 畫布背景
while True:
    turtle_move()

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
t.shape("turtle")
firstStamp = t.stamp()  # 蓋章第1隻海龜
t.forward(100)
secondStamp = t.stamp()  # 蓋章第2隻海龜
t.forward(100)
thirdStamp = t.stamp()  # 蓋章第3隻海龜
time.sleep(5)
t.clearstamp(secondStamp)  # 刪除第2隻海龜
time.sleep(5)
t.clearstamps(None)  # 刪除所有海龜

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
t.shape("turtle")
firstStamp = t.stamp()  # 蓋章第1隻海龜
t.forward(100)
secondStamp = t.stamp()  # 蓋章第2隻海龜
t.forward(100)
thirdStamp = t.stamp()  # 蓋章第3隻海龜
time.sleep(5)
t.clearstamp(secondStamp)  # 刪除第2隻海龜
time.sleep(5)
t.clearstamps(None)  # 刪除所有海龜

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
t.shape("turtle")
t.stamp()  # 蓋章第1隻海龜
print("目前有顯示海龜 : ", t.isvisible())
t.forward(100)
secondStamp = t.stamp()  # 蓋章第2隻海龜
time.sleep(3)
print("目前有顯示海龜 : ", t.isvisible())
t.clearstamps(-1)  # 刪除後面1個海龜
time.sleep(3)
print("目前有顯示海龜 : ", t.isvisible())

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
t.shape("turtle")
t.stamp()  # 蓋章第1隻海龜
print("目前有顯示海龜 : ", t.isvisible())
t.forward(100)
secondStamp = t.stamp()  # 蓋章第2隻海龜
time.sleep(3)
print("目前有顯示海龜 : ", t.isvisible())
t.clearstamps(-1)  # 刪除後面1個海龜
time.sleep(3)
print("目前有顯示海龜 : ", t.isvisible())

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
print(t.screen.getshapes())  # 列印海龜游標字串

for cursor in t.screen.getshapes():
    t.shape(cursor)  # 更改海龜游標
    t.stamp()  # 海龜游標蓋章
    t.forward(30)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
print(t.screen.getshapes())  # 列印海龜游標字串

for cursor in t.screen.getshapes():
    t.shape(cursor)  # 更改海龜游標
    t.stamp()  # 海龜游標蓋章
    t.forward(30)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

colorsList = ["green", "yellow", "red"]

t = turtle.Pen()
for i in range(0, 3):
    t.fillcolor(colorsList[i % 3])  # 更改色彩
    t.begin_fill()  # 開始填充
    t.circle(50)  # 繪製左方圓
    t.end_fill()  # 結束填充
    time.sleep(1)  # 每隔3秒執行一次迴圈

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

colorsList = ["green", "yellow", "red"]

t = turtle.Pen()
t.speed(10)  # 加速繪製圖形
t.ht()  # 隱藏海龜游標
for i in range(0, 3):
    t.color("white", colorsList[i % 3])  # 更改色彩
    t.begin_fill()  # 開始填充
    t.circle(50)  # 繪製左方圓
    t.end_fill()  # 結束填充
    time.sleep(1)  # 每隔3秒執行一次迴圈

turtle.mainloop()

print("------------------------------------------------------------")  # 60個


def printStr(x, y):
    print("滑鼠座標 :(", x, y, ")")


t = turtle.Pen()
t.screen.onclick(printStr)
t.screen.mainloop()

turtle.mainloop()

print("------------------------------------------------------------")  # 60個


def drawSignal(x, y):
    if x > 0:
        t.fillcolor("yellow")
    else:
        t.fillcolor("blue")
    t.penup()
    t.setpos(x, y - 50)  # 設定繪圓起點
    t.begin_fill()
    t.circle(50)
    t.end_fill()


t = turtle.Pen()
t.screen.onclick(drawSignal)
t.screen.mainloop()

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

def keyRight():
    t.seth(0)
    t.forward(50)


def keyUp():
    t.seth(90)
    t.forward(50)


def keyLeft():
    t.seth(180)
    t.forward(50)


def keyDown():
    t.seth(270)
    t.forward(50)


t = turtle.Pen()
t.screen.onkey(keyRight, "Right")
t.screen.onkey(keyUp, "Up")
t.screen.onkey(keyLeft, "Left")
t.screen.onkey(keyDown, "Down")
t.screen.listen()
t.screen.mainloop()

turtle.mainloop()
'''
print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
t.penup()
t.setheading(180)  # 海龜往左
t.forward(150)  # 移動往左
t.setheading(0)  # 海龜往右
t.pendown()

t.penup()
t.forward(100)  # 移動往右
t.pendown()
t.setheading(0)
step = 5  # 每次增加距離
for r in range(10, 100 + step, step):
    t.penup()  # 將筆提起
    t.setpos(150, -100)  # 海龜到點(150,100)
    t.setheading(0)
    t.pendown()  # 將筆放下準備繪製
    t.circle(r, 90 + r * 2)  # 繪製圓

turtle.mainloop()


sys.exit()


print("------------------------------------------------------------")  # 60個

'''
print('turtle.circle 測試 空心圓')
t = turtle.Pen()
r = 30  # 半徑
t.penup()
t.setheading(180)  # 海龜往左
t.forward(270)  # 移動往左
t.setheading(0)  # 海龜往右

for edge in range(3, 13, 1):  # 繪3 - 12邊圖
    t.pendown()
    t.circle(r, steps=edge)
    t.penup()
    t.forward(60)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print('turtle.circle 測試 實心圓')
t = turtle.Pen()
t.color("white")
r = 30  # 半徑
t.penup()
t.setheading(180)  # 海龜往左
t.forward(270)  # 移動往左
t.setheading(0)  # 海龜往右
colorsList = ["red", "orange", "yellow", "green", "blue", "cyan", "purple", "violet"]
for edge in range(3, 13, 1):  # 繪3 - 12邊圖
    t.pendown()
    t.fillcolor(colorsList[edge % 8])
    t.begin_fill()
    t.circle(r, steps=edge)
    t.end_fill()
    t.penup()
    t.forward(60)
'''
print("------------------------------------------------------------")  # 60個

'''
turtle.width(5)  # 輪廓寬度

turtle.fillcolor("yellow")  # 設定填充顏色

turtle.begin_fill()  # 開始填充

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.end_fill()  # 結束填充

turtle.mainloop()
'''
print("------------------------------------------------------------")  # 60個

'''
# 畫星號
for x in range(1, 6):
    turtle.forward(100)  # 海龜向前繪線移動100
    turtle.left(144)  # 海龜方向左轉144度

turtle.mainloop()
'''
print("------------------------------------------------------------")  # 60個
'''
for x in range(1, 20):
    turtle.forward(100)  # 海龜向前繪線移動100
    turtle.right(170)  # 海龜方向右轉170度

turtle.mainloop()
'''
print("------------------------------------------------------------")  # 60個
'''
for x in range(1, 40):
    turtle.forward(200)  # 海龜向前繪線移動200
    turtle.right(95)  # 海龜方向右轉95度

turtle.mainloop()
'''
print("------------------------------------------------------------")  # 60個
'''
for x in range(1, 500):
    turtle.forward(x)  # 海龜向前繪線移動x
    turtle.right(91)  # 海龜方向右轉91度

turtle.mainloop()
'''
print("------------------------------------------------------------")  # 60個
'''
for x in range(1, 37):
    turtle.forward(100)  # 海龜向前繪線移動100
    turtle.left(90)  # 海龜方向左轉90度
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(100)  # 海龜方向左轉100度

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

turtle.pensize(5)  # 畫筆寬度
colorValue = 1.0
colorStep = colorValue / 36
for x in range(1, 37):
    colorValue -= colorStep
    turtle.color(0.5, 1, colorValue)  # 色彩調整
    turtle.forward(100)  # 海龜向前繪線移動100
    turtle.left(90)  # 海龜方向左轉90度
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(100)  # 海龜方向左轉100度

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

step = 5  # 每次增加距離
for r in range(10, 50, step):
    turtle.circle(r)  # 繪製圓
    turtle.penup()  # 將筆提起
    turtle.right(90)  # 方向往下
    turtle.forward(step)  # 移動海龜位置起繪點
    turtle.right(270)  # 方向往右
    turtle.pendown()  # 將筆放下準備繪製

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
step = 5  # 每次增加距離
for r in range(10, 90, step):
    turtle.circle(r, 90 + r * 2)  # 繪製圓
    turtle.penup()  # 將筆提起
    turtle.home()  # 海龜回到原點(0,0)
    turtle.pendown()  # 將筆放下準備繪製

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
colors = ["red", "orange", "yellow", "green", "blue"]
step = 10  # 每次增加距離
twidth = 0  # 最初寬度0
for r in range(1, 11):
    turtle.color(colors[r % 5])  # 選畫筆顏色
    twidth += 1  # 每次迴圈寬度加1
    turtle.width(twidth)  # 設定寬度
    turtle.circle(r * step)  # 繪製圓
    turtle.penup()  # 將筆關閉
    turtle.right(90)  # 方向往下
    turtle.forward(step)  # 移動海龜位置起繪點
    turtle.right(270)  # 方向往右
    turtle.pendown()  # 將筆開啟準備繪製

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
t.screen.title("歡迎來到美國")
t.screen.bgcolor("yellow")

turtle.mainloop()
'''
print("------------------------------------------------------------")  # 60個
'''
t = turtle.Pen()
width = t.screen.window_width()
height = t.screen.window_height()
print("視窗width  = ", width)
print("視窗height = ", height)
time.sleep(3)
t.screen.setup(600, 480)  # 更改視窗寬和高
width = t.screen.window_width()
height = t.screen.window_height()
print("新視窗width  = ", width)
print("新視窗height = ", height)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
t.screen.setworldcoordinates(0, 0, 800, 800)
print("列印海龜位置  = ", t.pos())
t.left(45)
t.forward(300)
print("列印新海龜位置  = ", t.pos())

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

pen = turtle.Turtle()  # 建立畫布物件
pen.penup()  # 畫筆懸空
pen.goto(-50, 50)  # 移向指定座標
pen.pendown()  # 落下畫筆
pen.forward(100)  # 前進100像素
pen.right(90)  # 畫筆右轉90度
pen.fd(100)  # forward()方法簡寫
pen.right(135)
pen.fd(140)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

show = turtle.Turtle()  # 建立畫布物件
turtle.colormode(255)  # 變更色彩以數值表示
show.pencolor(255, 0, 0)  # 設定畫筆顏色
show.pensize(10)  # 設定畫筆大小
show.speed(1)  # 畫筆速度為慢

show.penup()  # 畫筆懸空
show.goto(-50, 50)  # 移向指定座標

show.pendown()  # 落下畫筆
show.forward(100)  # 前進100像素
show.right(90)  # 畫筆右轉90度
show.fd(100)  # forward()方法簡寫
show.right(135)
show.fd(140)

turtle.mainloop()
'''
print("------------------------------------------------------------")  # 60個
'''
pen = turtle.Turtle()
pen.pencolor("Red")
pen.pensize(2)

# X軸
pen.up()  # 抬起畫筆
pen.goto(-300, 0)  # 前進指定座標
pen.down()  # 放下畫筆
pen.forward(600)  # 畫筆前進
pen.left(90)  # 畫筆左轉

# Y軸
pen.up()  # 抬起畫筆
pen.goto(0, -300)  # 前進指定座標
pen.down()  # 放下畫筆
pen.forward(600)  # 畫筆前進
pen.left(90)  # 畫筆左轉
pen.home()  # 畫筆回到原點

# 繪製兩個三角形
pen.pencolor("Yellow")
pen.pensize(10)
pen.left(45)
pen.forward(100)
pen.left(135)
pen.forward(140)
pen.home()

pen.right(45)
pen.forward(100)
pen.right(135)
pen.forward(140)
pen.right(135)
pen.forward(100)

turtle.mainloop()
'''
print("------------------------------------------------------------")  # 60個
'''
show = turtle.Turtle()  # 建立畫布物件
show.pencolor("Yellow")  # 畫筆為黃色
show.pensize(10)  # 畫筆大小
show.speed(1)  # 畫筆速度為慢

# 畫一個簡單矩形
show.forward(70)  # 前進70像素
show.right(90)  # 畫筆右轉90度
show.fd(70)  # forward()方法簡寫
show.right(90)
show.fd(70)
show.right(90)
show.home()

turtle.mainloop()
'''
print("------------------------------------------------------------")  # 60個
'''
show = turtle.Turtle()  # 建立畫布物件
show.color("Blue", "Gold")  # 設畫筆為藍色，塗滿金黃色
show.pensize(10)  # 畫筆大小
show.speed(1)  # 畫筆速度為慢
show.pu()  # 抬起畫筆
show.goto(-50, 50)  # 前往指定位置

# 畫一個簡單矩形
show.begin_fill()  # 開始進行塗色
show.pd()  # pendown()方法簡寫，放下畫筆
show.forward(100)  # 前進100像素
show.right(90)  # 畫筆右轉90度
show.fd(100)  # forward()方法簡寫
show.right(90)
show.fd(100)
show.right(90)
show.fd(100)
show.end_fill()  # 結束塗色動作

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

turtle.colormode(255)  # 色彩以數值表示
show = turtle.Turtle()  # 建立畫布物件
show.pensize(10)  # 畫筆大小
show.speed(1)  # 畫筆速度為慢

show.color((255, 0, 255), (255, 215, 0))  # 設畫筆為洋紅色，塗滿金黃色
show.pu()  # 抬起畫筆
show.goto(-50, 50)  # 前往指定位置

# 畫一個簡單三角形
show.begin_fill()  # 開始塗色
show.pd()  # pendown()方法簡寫
show.forward(100)  # 前進100像素
show.right(120)  # 畫筆右轉120度
show.fd(100)  # forward()方法簡寫
show.right(120)
show.forward(100)
show.end_fill()  # 結束塗色

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

# 填滿正5邊形
show = turtle.Turtle()  # 建立畫布物件
show.pensize(10)  # 畫筆大小
show.speed(1)  # 畫筆速度為慢

show.color((1.0, 0, 1.0), (1.0, 0.84, 0.0))  # 設畫筆為洋紅色，塗滿金黃色
show.pu()  # 抬起畫筆
show.goto(-60, 80)  # 前往指定位置

# 畫一個簡單五邊形
show.begin_fill()  # 開始進行塗色
show.pd()  # pendown()方法簡寫
show.forward(100)  # 前進100像素
show.right(72)  # 畫筆右轉72度
show.fd(100)  # forward()方法簡寫
show.right(72)
show.forward(100)
show.right(72)
show.fd(100)
show.right(72)
show.fd(100)
show.end_fill()  # 結束塗色動作

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

pen = turtle.Turtle()  # 建立畫布物件
pen.pensize(10)  # 畫筆大小
pen.speed(1)  # 畫筆速度為慢
pen.pencolor("#FF0000")  # 設畫筆為紅色
pen.shape("turtle")  # 設畫筆形狀是海龜
pen.pu()  # 抬起畫筆
pen.goto(-10, 70)
pen.pd()  # 放下畫筆
pen.circle(-60, 360, 6)  # 畫出一個六邊形

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

show = turtle.Turtle()  # 建立畫布物件
show.pencolor("Yellow")  # 畫筆為黃色
show.pensize(10)  # 畫筆大小
show.speed(1)  # 畫筆速度為慢

# 畫一個簡單矩形
for item in range(4):
    show.fd(70)  # 前進70像素
    show.right(90)  # 畫筆右轉90度

show.up()  # 抬起畫筆
show.goto(-50, 10)  # 畫筆移向指定位置

show.write("正方形", font=("微軟正黑體", 40))

turtle.mainloop()  # 開始主事件的循環

print("------------------------------------------------------------")  # 60個

show = turtle.Turtle()  # 建立畫布物件
show.pencolor("Red")  # 畫筆為紅色
show.pensize(2)  # 畫筆大小
show.speed(1)  # 畫筆速度為慢

# 畫一個連續矩形
for item in range(16):
    show.fd(item * 3)  # 依值前進
    # print(item * 3)
    show.right(90)  # 畫筆右轉90度

turtle.mainloop()  # 開始主事件的循環

print("------------------------------------------------------------")  # 60個

show = turtle.Turtle()  # 建立畫布物件
show.pencolor("Red")  # 畫筆為紅色
show.pensize(1)  # 畫筆大小

# 畫一個螺旋圖
for item in range(20):
    show.fd(item * 2)  # 依值前進
    show.right(91)  # 畫筆右轉91度

turtle.mainloop()  # 開始主事件的循環

print("------------------------------------------------------------")  # 60個

show = turtle.Turtle()  # 建立畫布物件
show.pencolor("Red")  # 畫筆為紅色
show.pensize(1)  # 畫筆大小

# 畫一個螺旋圖
for item in range(20):
    show.fd(item * 5)  # 依值前進
    show.right(121)  # 畫筆右轉121度

turtle.mainloop()  # 開始主事件的循環
'''
print("------------------------------------------------------------")  # 60個
'''
pen = turtle.Turtle()  # 建立畫布物件
pen.pencolor("Red")  # 畫筆為紅色
pen.speed(1)

# 第一層for/in廻圈輸出4列
for r1 in range(5):
    # 第二層for/in廻圈，依r1值遞減
    for r2 in range(5 - r1):
        pen.pu()  # 抬起畫筆
        p1, p2 = -50, -50  # 設起始座標 x, y(-50, -50)
        p1 = p1 + r1 * 30  # X軸
        p2 = p2 + r2 * 30  # Y軸
        pen.goto(p1, p2)  # 畫筆移向座標
        pen.pd()  # 放下畫筆
        pen.dot(15, "Blue")  # 畫白色圓點
        print(f"座標(x = {p1}, y = {p2})")  # 查看畫圓點的座標位置
    print()  # 換新行

turtle.mainloop()  # 開始主事件的循環

print("------------------------------------------------------------")  # 60個

ps = turtle.Turtle()  # 產生一支畫筆

colors = ("Red", "LightGreen", "Yellow", "Blue")
ps.pensize(2)  # 設畫筆大小

# 以矩形為底的4色螺旋圖
for num in range(20):
    # %運算子取餘數來獲得色彩
    ps.pencolor(colors[num % 4])
    ps.forward(num * 3)
    ps.left(91)

turtle.mainloop()  # 開始主事件的循環

print("------------------------------------------------------------")  # 60個

"""
colors = ['Magenta', 'Gold', 'Cyan', 'PaleGreen',
          'LemonChiffon', 'Orange', 'Pink']   # List

pen = turtle.Turtle()   # 建立畫布物件
weeks = []              # 存放輸入字串
count = 0               # 計數器
wk = turtle.textinput(f'一週七天 <{count}>，按0離開',
                      '請輸入星期前三個字母：')

while count <= 6:
   weeks.append(wk)
   #print(count, wk)
   wk = turtle.textinput(f'一週七天 <{count}>，按0離開',
                         '請輸入星期前三個字母：')
   count += 1
   
# 畫一個螺旋形
for item in range(120):
   pen.pencolor(colors [item % len(weeks)]) # 依餘數取色彩值   
   pen.pu()   # 抬起畫筆
   pen.fd(item * 2)   # forward()方法簡寫
   pen.pd()   # 放下畫筆
   # 在畫布秀出星期名稱，並逐漸把字型放大
   pen.write(weeks[item % len(weeks)],
             font = ('Arial', int((item + 4) / 4)))
   pen.left(360 / len(weeks) + 2)   # 依所得外角左轉

turtle.done()

turtle.mainloop()    # 開始主事件的循環

"""

print("------------------------------------------------------------")  # 60個


tines = ["Red", "Yellow", "Orange", "Purple", "Cyan", "Pink", "LightGreen", "Bisque"]

pen = turtle.Turtle()  # 建立畫布物件
pen.speed(0)


# 隨機產生螺旋圖
def haphazardTwist():
    # 方法choice()讓畫筆色彩隨機變
    pen.pencolor(random.choice(tines))
    # 隨機產生 8~40 的大小不一的值來作為螺旋圖大小的依據
    size = random.randint(8, 40)

    # x, y座標為視窗寬度的一半
    w1 = -turtle.window_width() // 2
    w2 = turtle.window_width() // 2
    h1 = -turtle.window_height() // 2
    h2 = turtle.window_height() // 2

    posX = random.randrange(w1, w2)
    posY = random.randrange(h1, h2)

    pen.penup()  # 抬畫筆
    pen.goto(posX, posY)
    pen.pendown()
    for item in range(size):
        pen.forward(item * 2)
        pen.left(91)


for num in range(10):
    haphazardTwist()


turtle.mainloop()  # 開始主事件的循環

print("------------------------------------------------------------")  # 60個


"""
def moveTurtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def drawStar(length):       #畫星形
    turtle.right(108)       #右轉 ? 度
    turtle.forward(length)  #直走length步
    turtle.left(144)    #右轉 ? 度
    turtle.forward(length)  #直走length步
    turtle.left(144)    #右轉 ? 度
    turtle.forward(length)  #直走length步
    turtle.left(144)    #右轉 ? 度
    turtle.forward(length)  #直走length步
    turtle.left(144)    #右轉 ? 度
    turtle.forward(length)  #直走length步

def drawStar2(length):       #畫星形
    turtle.right(108)       #右轉 ? 度
    drawDashline(length)
    turtle.left(144)    #右轉 ? 度
    drawDashline(length)
    turtle.left(144)    #右轉 ? 度
    drawDashline(length)
    turtle.left(144)    #右轉 ? 度
    drawDashline(length)
    turtle.left(144)    #右轉 ? 度
    drawDashline(length)

def drawDashline(length):       #畫dashline
    length2 = length / 9
    turtle.forward(length2)
    turtle.penup()
    turtle.forward(length2)
    turtle.pendown()
    turtle.forward(length2)
    turtle.penup()
    turtle.forward(length2)
    turtle.pendown()
    turtle.forward(length2)
    turtle.penup()
    turtle.forward(length2)
    turtle.pendown()
    turtle.forward(length2)
    turtle.penup()
    turtle.forward(length2)
    turtle.pendown()
    turtle.forward(length2)
   
    

moveTurtle(0, 0)

turtle.fillcolor('red')
turtle.begin_fill()

turtle.pensize(5)
turtle.color('blue')
#drawStar(200)

turtle.end_fill()

moveTurtle(100, 100)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.goto(100, 100)
turtle.goto(200, 0)
turtle.penup()

turtle.done()       #最後用
"""

turtle.Turtle()
turtle.shape("turtle")  # 設定畫筆形狀, 預設為箭頭
"""
6種
arrow, turtle, circle, square, triangle, classic(預設)

"""

"""
w = W / 3
h = H / 3
turtle.goto(w, 0)
turtle.goto(w, h)
turtle.goto(-w, h)
turtle.goto(-w, -h)
turtle.goto(w, -h)
turtle.home()   #畫筆回到原點
"""


turtle.forward(50)  # 前進=fd  vs backward後退
turtle.left(90)  # 左轉
turtle.forward(50)
turtle.right(90)  # 右轉
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

turtle.penup()  # 舉起畫筆 不畫 = pu
turtle.pendown()  # 放下畫筆 畫 = pd

turtle.pensize(width=5)  # 設定畫筆大小
turtle.width(width=5)  # 同上

"""
turtle.speed()  #設定畫筆移動速度
fastest  0  最快
fast     10 快
normal   6 正常
slow     3 慢
slowest  1 最慢

"""

"""
#畫筆上色
#turtle.color(colorstring)
turtle.color((r,g,b))   #浮點數
turtle.color(r,g,b)     #16進制表示
turtle.color('#FF0000') #紅色
"""

# 塗上顏色
turtle.begin_fill()  # 開始塗色
turtle.end_fill()  # 結束塗色
turtle.fillcolor()  # 指定塗滿的色彩
turtle.color("Blue", "Gold")  # 畫筆為Blue, 塗滿為Gold

turtle.penup()
turtle.home()  # 畫筆回到原點

turtle.begin_fill()  # 開始塗色
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.end_fill()  # 結束塗色

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


"""
新進暫存



t.left(65) 試左轉65度

互補的指令
t.left()	t.right()
t.forwared()	t.backward

print("------------------------------------------------------------")  # 60個

wd = turtle.Screen()  #建立名為wd的screen實體
pen = turtle.Turtle()    # 建立一個名為tu的海龜turtle實體
pen.forward(50)   #tu往前50pixels
pen.right(90)  #tu往右轉90度
pen.forward(150)   #tu往前150pixels
wd.exitonclick()      #在視窗任一位置按下滑鼠左鍵關閉視窗

print("------------------------------------------------------------")  # 60個

wd = turtle.Screen()  #建立turtle screen實體
wd.setup(width=.5, height=200) #視窗大小與位置
wd.title("turtle繪圖真有趣，簡單又易學")
tu = turtle.Turtle()    # 建立海龜turtle實體
tu.color('green')
tu.pensize(5)
tu.penup()
tu.setx(-100)
tu.pendown()
for x in range(10):
	tu.circle(30)
	tu.right(360/10)

tu2 = turtle.Turtle()    # 建立第二個海龜名為tu2
tu2.color('#FF00FF', '#55CCBB')
tu2.penup() 
tu2.goto(120,-120)
tu2.pendown()
tu2.begin_fill()
for x in range(10):
	tu2.forward(100)
	tu2.left(720/5)
tu2.end_fill()  

wd.exitonclick()
turtle.done()

print("------------------------------------------------------------")  # 60個

wd = turtle.Screen()  #建立turtle screen實體
wd.setup(width=.3, height=200, startx=None, starty=None) #視窗大小與位置
wd.bgcolor("green")  #設定底色
pen = turtle.Turtle()    # 建立一個海龜turtle實體
pen.shape("arrow")     #海龜樣式
pen.color("yellow","#ff00ff")  #海龜線條顏色與填色顏色
pen.pensize(10)   #線條寬度
pen.speed(3)     #海龜繪圖速度
pen.forward(50)   
pen.right(90) 
pen.forward(50)
pen.right(90)
pen.forward(50)
wd.exitonclick()      
turtle.done() #結束tutle繪圖

print("------------------------------------------------------------")  # 60個

"""


def main():
    initTurtle()
    drawSquare()
    drawRectangle()
    drawCircle()
    drawStar()


######################################################


def initTurtle():
    turtle.shape("turtle")
    turtle.bgcolor("#87CEEB")


######################################################


def drawSquare():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.reset()


######################################################


def drawRectangle():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(60)
    turtle.reset()


######################################################


def drawCircle():
    turtle.circle(90)
    turtle.reset()


######################################################


def drawTriangle():
    turtle.left(180)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.reset()


######################################################


def drawStar():
    turtle.color("red", "yellow")
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    turtle.exitonclick()


######################################################


def drawOlympicLogo(radius):
    positions = [
        (60, 0, "blue"),
        (-60, 0, "purple"),
        (120, 60, "red"),
        (0, 60, "yellow"),
        (-120, 60, "green"),
    ]

    for position in positions:
        drawOlympicCircle(position[0], position[1], position[2], radius)


######################################################


def drawOlympicCircle(x, y, color, radius):
    turtle.pensize(10)
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(radius)


######################################################


def drawSquareLoop():
    for num in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.reset()


######################################################

if __name__ == "__main__":
    main()


print("------------------------------------------------------------")  # 60個

"""
turtle.pensize(3)
turtle.penup()
turtle.goto(-180, 150)
turtle.pencolor('red')
turtle.fillcolor('yellow')
turtle.pendown()
turtle.begin_fill()
for _ in range(36):
    turtle.forward(200)
    turtle.right(170)
turtle.end_fill()
turtle.mainloop()
"""

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


screen = turtle.Screen()
screen.setup(500, 400)

turtle.forward(100)
turtle.left(90)
turtle.forward(100)

screen.exitonclick()

print("------------------------------------------------------------")  # 60個

screen = turtle.Screen()
screen.setup(500, 400)

turtle.color("blue")
turtle.shape("turtle")
turtle.forward(100)

screen.exitonclick()

print("------------------------------------------------------------")  # 60個

screen = turtle.Screen()
screen.setup(500, 400)

turtle.pensize(5)
turtle.pencolor("blue")
turtle.forward(100)
turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()
turtle.left(90)
turtle.forward(100)

screen.exitonclick()

print("------------------------------------------------------------")  # 60個

screen = turtle.Screen()
screen.setup(500, 400, startx=20, starty=50)

turtle.pensize(5)
turtle.pencolor("blue")
turtle.forward(100)

screen.exitonclick()

print("------------------------------------------------------------")  # 60個

screen = turtle.Screen()
screen.setup(500, 400)

for i in range(1, 5):
    turtle.forward(100)
    turtle.left(90)

screen.exitonclick()

print("------------------------------------------------------------")  # 60個

screen = turtle.Screen()
screen.setup(500, 400)

for i in range(1, 7):
    turtle.forward(100)
    turtle.left(60)

screen.exitonclick()

print("------------------------------------------------------------")  # 60個

screen = turtle.Screen()
screen.setup(500, 400)

for i in range(1, 4):
    turtle.forward(100)
    turtle.left(120)

screen.exitonclick()

print("------------------------------------------------------------")  # 60個

screen = turtle.Screen()
screen.setup(500, 400)

for i in range(1, 6):
    turtle.forward(150)
    turtle.left(144)

screen.exitonclick()

print("------------------------------------------------------------")  # 60個

screen = turtle.Screen()

for i in range(360):
    turtle.forward(2)
    turtle.left(1)

screen.exitonclick()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


def draw_spiral_matrix(size):
    # 初始化海龜
    turtle.speed(0)
    turtle.color("black")
    turtle.penup()
    turtle.goto(-size//2, size//2)
    turtle.pendown()

    # 繪製螺旋矩陣
    for i in range(size//2):
        for direction in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            dx, dy = direction
            for j in range(i*2 + 1):
                turtle.forward(20)
                turtle.left(90)
                if j == i:
                    turtle.penup()
                    turtle.forward(20)
                    turtle.pendown()
            turtle.penup()
            turtle.goto(turtle.xcor()+dx*20, turtle.ycor()+dy*20)
            turtle.pendown()

    # 隱藏海龜
    turtle.hideturtle()

# 畫出螺旋矩陣
draw_spiral_matrix(10)
turtle.done()

print("------------------------------------------------------------")  # 60個

def draw_hexagon_spiral(size):
    # 初始化海龜
    turtle.speed(0)
    turtle.color("black")
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    # 繪製六邊形螺旋
    side_length = 10
    for i in range(size):
        for j in range(6):
            turtle.forward(side_length*(i+1))
            turtle.right(60)
        turtle.right(60)

    # 隱藏海龜
    turtle.hideturtle()

# 畫出六邊形螺旋
draw_hexagon_spiral(10)
turtle.done()

print("------------------------------------------------------------")  # 60個

wd = turtle.Screen()  #建立名為wd的screen實體
pen = turtle.Turtle()    # 建立一個名為tu的海龜turtle實體
pen.forward(50)   #tu往前50pixels
pen.right(90)  #tu往右轉90度
pen.forward(150)   #tu往前150pixels
wd.exitonclick()      #在視窗任一位置按下滑鼠左鍵關閉視窗

print("------------------------------------------------------------")  # 60個

from time import perf_counter
import statistics

screen = turtle.Screen()
print(type(screen))
print(screen)

ANGLES = (0, 3.695220532)  # 直線和斜線的角度
NUM_RUNS = 20
SPEED = 0

for angle in ANGLES:
    times = []
    for _ in range(NUM_RUNS):
        line = turtle.Turtle()
        line.speed(SPEED)  
        line.hideturtle()
        line.penup()
        line.lt(angle)
        line.setpos(-470, 0)
        line.pendown()
        line.showturtle()
        start_time = perf_counter()
        line.fd(962)
        end_time = perf_counter()
        times.append(end_time - start_time)
        
    line_ave = statistics.mean(times)
    print("Angle {} degrees: average time for {} runs at speed {} = {:.5f}"
          .format(angle, NUM_RUNS, SPEED, line_ave))

print("------------------------------------------------------------")  # 60個

# 繪製池塘
pond = turtle.Screen()
pond.setup(600, 400)
pond.bgcolor('light blue')
pond.title("Yertle's Pond")

# 繪製小島
mud = turtle.Turtle('circle')
mud.shapesize(stretch_wid=5, stretch_len=5, outline=None)
mud.pencolor('tan')
mud.fillcolor('tan')

# 繪製樹幹
SIDE = 80
ANGLE = 90
log = turtle.Turtle()
log.hideturtle()
log.pencolor('peru')
log.fillcolor('peru')
log.speed(0) # 最快的移動速度
log.penup()
log.setpos(215, -30)
log.lt(45)
log.begin_fill()
for _ in range(2):
    log.fd(SIDE)
    log.lt(ANGLE)
    log.fd(SIDE / 4)
    log.lt(ANGLE)
log.end_fill()

# 繪製樹洞
knot = turtle.Turtle()
knot.hideturtle()
knot.speed(0) # 最快的移動速度
knot.penup()
knot.setpos(245, 5)
knot.begin_fill()
knot.circle(5)
knot.end_fill()

# 繪製鱷龜 Yertle
yertle = turtle.Turtle('turtle')
yertle.color('green')
yertle.speed(1)  # 最慢的移動速度
yertle.fd(200)
yertle.lt(180)
yertle.fd(200)
yertle.rt(176)
yertle.fd(205)

print("------------------------------------------------------------")  # 60個

wd = turtle.Screen()  #建立turtle screen實體
wd.setup(width=.5, height=200) #視窗大小與位置
wd.title("turtle繪圖真有趣，簡單又易學")
tu = turtle.Turtle()    # 建立海龜turtle實體
tu.color('green')
tu.pensize(5)
tu.penup()
tu.setx(-100)
tu.pendown()
for x in range(10):
	tu.circle(30)
	tu.right(360/10)

tu2 = turtle.Turtle()    # 建立第二個海龜名為tu2
tu2.color('#FF00FF', '#55CCBB')
tu2.penup() 
tu2.goto(120,-120)
tu2.pendown()
tu2.begin_fill()
for x in range(10):
	tu2.forward(100)
	tu2.left(720/5)
tu2.end_fill()  

wd.exitonclick()
turtle.done()

print("------------------------------------------------------------")  # 60個

wd = turtle.Screen()  #建立turtle screen實體
wd.setup(width=.3, height=200, startx=None, starty=None) #視窗大小與位置
wd.bgcolor("green")  #設定底色
pen = turtle.Turtle()    # 建立一個海龜turtle實體
pen.shape("arrow")     #海龜樣式
pen.color("yellow","#ff00ff")  #海龜線條顏色與填色顏色
pen.pensize(10)   #線條寬度
pen.speed(3)     #海龜繪圖速度
pen.forward(50)   
pen.right(90) 
pen.forward(50)
pen.right(90)
pen.forward(50)
wd.exitonclick()      
turtle.done() #結束tutle繪圖

print("------------------------------------------------------------")  # 60個

# Draw chess board borders
turtle.pensize(3) # Set pen thickness to 3 pixels
turtle.penup() # Pull the pen up
turtle.goto(-120, -120)
turtle.pendown() # Pull the pen down
turtle.color("red")

for i in range(4):
    turtle.forward(240) # Draw a line
    turtle.left(90) # Turn left 90 degrees

# Draw chess board inside
turtle.color("black")
for j in range(-120, 90, 60): 
    for i in range(-120, 120, 60):
        turtle.penup()
        turtle.goto(i, j)
        turtle.pendown()

       # Draw a small rectangle        
        turtle.begin_fill()
        for k in range(4):
            turtle.forward(30) # Draw a line
            turtle.left(90) # Turn left 90 degrees
        turtle.end_fill()

for j in range(-90, 120, 60): 
    for i in range(-90, 120, 60):
        turtle.penup()
        turtle.goto(i, j)
        turtle.pendown()

       # Draw a small rectangle        
        turtle.begin_fill()
        for k in range(4):
            turtle.forward(30) # Draw a line
            turtle.left(90) # Turn left 90 degrees
        turtle.end_fill()

turtle.hideturtle()

turtle.done() 

print("------------------------------------------------------------")  # 60個

turtle.pensize(3) # Set pen thickness to 3 pixels
turtle.penup() # Pull the pen up
turtle.goto(-200, -50)
turtle.pendown() # Pull the pen down
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("red")
turtle.circle(40, steps = 3) # Draw a triangle
turtle.end_fill() # Fill the shape

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("blue")
turtle.circle(40, steps = 4) # Draw a square
turtle.end_fill() # Fill the shape

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("green")
turtle.circle(40, steps = 5) # Draw a pentagon
turtle.end_fill() # Fill the shape

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("yellow")
turtle.circle(40, steps = 6) # Draw a hexagon
turtle.end_fill() # Fill the shape

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("purple")
turtle.circle(40) # Draw a circle
turtle.end_fill() # Fill the shape

turtle.color("green")
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.hideturtle()

turtle.done() 

print("------------------------------------------------------------")  # 60個

# Prompt the user for inputing two points
x1, y1 = eval(input("Enter x1 and y1 for Point 1: "))
x2, y2 = eval(input("Enter x2 and y2 for Point 2: "))
              
# Compute the distance
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Display two points and the connecting line
turtle.penup()
turtle.goto(x1, y1) # Move to (x1, y1)
turtle.pendown()



turtle.goto(x2, y2) # draw a line to (x2, y2)


# Move to the center point of the line
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2) 
turtle.write(distance)

turtle.done() 

print("------------------------------------------------------------")  # 60個

turtle.circle(50)

turtle.done() 

print("------------------------------------------------------------")  # 60個

turtle.color("red", "yellow")

turtle.backward(100)
turtle.begin_fill()
for i in range(22):
    turtle.forward(200)
    turtle.left(125)
turtle.end_fill()
turtle.done()

print("------------------------------------------------------------")  # 60個

turtle.ondrag(turtle.goto)

turtle.done() 

print("------------------------------------------------------------")  # 60個

# HandleMouseClick

def displayMousePoint(x, y):
    turtle.write("Mouse click at (" + str(x) + ", " +
        str(y) + ")")

def displayCircle(x, y):
    turtle.circle(50)

def main():
    # Bind handlers with the mouse-click event
    turtle.onclick(displayMousePoint)
    turtle.onclick(displayCircle, add = True)
 
    turtle.done() 

main()

print("------------------------------------------------------------")  # 60個

# HandleMouseRelease.py

def displaySqaure(x, y):
    turtle.penup()
    turtle.goto(x - 100, y - 100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50, steps = 4)
    turtle.end_fill()

def main(): 
    # Bind a handler with the mouse-release event
    turtle.onrelease(displaySqaure)
 
    turtle.done() 

main()

print("------------------------------------------------------------")  # 60個

# Histogram.py

def main():
    # Create a list of numbers 
    list = [32, 23, 45, 34, 4, 90, 23, 25]
    drawHistogram(list)

    turtle.done() 

def drawHistogram(list):
    WIDTH = 400 # Width of the histogram
    HEIGHT = 300 # Height of the histogram

    # Draw a base line
    turtle.penup()
    turtle.goto(-WIDTH / 2, -HEIGHT / 2)
    turtle.pendown()
    turtle.forward(WIDTH)

    widthOfBar = WIDTH / len(list) # Width of each bar

    for i in range(len(list)):     
        height = list[i] * HEIGHT / max(list) 
        drawABar(-WIDTH / 2 + i * widthOfBar, 
            -HEIGHT / 2, widthOfBar, height)     

    turtle.hideturtle()

def drawABar(i, j, widthOfBar, height):
    turtle.penup()
    turtle.goto(i, j)
    turtle.setheading(90) # Set orientation to north
    turtle.pendown()

    # turtle.left(90) # Turn left 90 degrees
    turtle.forward(height) # Draw a vertical line
    turtle.right(90) # Turn right 90 degrees
    turtle.forward(widthOfBar) # Draw a horizontal line
    turtle.right(90) # Turn right 90 degrees
    turtle.forward(height) # Draw a vertical line

main()

print("------------------------------------------------------------")  # 60個

# OlympicSymbol.py

turtle.color("blue")
turtle.penup()
turtle.goto(-110, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("red")
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.circle(45)

turtle.color("yellow")
turtle.penup()
turtle.goto(-55, -75)
turtle.pendown()
turtle.circle(45)

turtle.color("green")
turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.circle(45)

turtle.done() 

print("------------------------------------------------------------")  # 60個

# PointInCircle.py

x1, y1 = eval(input("Enter the center of a circle x, y: "))
radius = eval(input("Enter the radius of the circle: "))
x2, y2 = eval(input("Enter a point x, y: "))

# Draw the circle
turtle.penup() # Pull the pen up
turtle.goto(x1, y1 - radius)
turtle.pendown() # Pull the pen down
turtle.circle(radius)

# Draw the point
turtle.penup() # Pull the pen up
turtle.goto(x2, y2)
turtle.pendown() # Pull the pen down
turtle.begin_fill() # Begin to fill color in a shape
turtle.color("red")
turtle.circle(3) 
turtle.end_fill() # Fill the shape

# Display the status
turtle.penup() # Pull the pen up
turtle.goto(x1 - 70, y1 - radius - 20)
turtle.pendown() 

d = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5
if d <= radius:
    turtle.write("The point is inside the circle") 
else:
    turtle.write("The point is outside the circle") 

turtle.hideturtle()

turtle.done() 

print("------------------------------------------------------------")  # 60個

# RandomWalk.py

from random import randint

turtle.speed(1) # Set turtle speed to slowest

# Draw 16 by 16 lattices
turtle.color("gray") # Color for lattice
x = -80 
for y in range(-80, 80 + 1, 10):
    turtle.penup()
    turtle.goto(x, y) # Draw a horizontal line
    turtle.pendown()
    turtle.forward(160)

y = 80
turtle.right(90)
for x in range(-80, 80 + 1, 10):
    turtle.penup()
    turtle.goto(x, y) # Draw a vertical line
    turtle.pendown()
    turtle.forward(160)
    
turtle.pensize(3)
turtle.color("red")

turtle.penup()
turtle.goto(0, 0) # Go to the center
turtle.pendown()

x = y = 0 # Current pen location at the center of lattice
while abs(x) < 80 and abs(y) < 80:    
    r = randint(0, 3)
    if r == 0:
        x += 10  # Walk east
        turtle.setheading(0)
        turtle.forward(10)      
    elif r == 1:
        y -= 10 # Walk south
        turtle.setheading(270)
        turtle.forward(10)      
    elif r == 2:
        x -= 10 # Walk west
        turtle.setheading(180)
        turtle.forward(10)      
    elif r == 3:
        y += 10 # Walk north
        turtle.setheading(90)
        turtle.forward(10)      

turtle.done() 

print("------------------------------------------------------------")  # 60個

# SimpleShapes.py

turtle.pensize(3)
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
turtle.circle(40, steps = 3) # Draw a triangle

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.circle(40, steps = 4) # Draw a square

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(40, steps = 5) # Draw a pentagon

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.circle(40, steps = 6) # Draw a hexagon

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.circle(40) # Draw a circle

turtle.done() 

print("------------------------------------------------------------")  # 60個

# TwoChessBoard.py

def main():
    drawChessboard(-260, -20, -120, 120) # Draw first chess board
    drawChessboard(20, 260, -120, 120) # Draw second chess board

    turtle.hideturtle()
    turtle.done() 

# Draw one chess board
def drawChessboard(startx, endx, starty, endy):
    # Draw chess board borders
    turtle.pensize(3) # Set pen thickness to 3 pixels
    turtle.penup() # Pull the pen up
    turtle.goto(startx, starty)
    turtle.pendown() # Pull the pen down
    turtle.color("red")

    for i in range(4):
        turtle.forward(240) # Draw a line
        turtle.left(90) # Turn left 90 degrees

    # Draw chess board inside
    drawMultipleRectangle(startx, endx, starty, endy)
    drawMultipleRectangle(startx + 30, endx, starty + 30, endy)

# Draw multiple rectangles
def drawMultipleRectangle(startx, endx, starty, endy):
    turtle.color("black")
    for j in range(starty, endy, 60): 
        for i in range(startx, endx, 60):
            fillRectangle(i, j)

# Draw a small rectangle  
def fillRectangle(i, j):      
    turtle.penup()
    turtle.goto(i, j)
    turtle.pendown()
    turtle.begin_fill()
    for k in range(4):
        turtle.forward(30) # Draw a line
        turtle.left(90) # Turn left 90 degrees
    turtle.end_fill()

main()

print("------------------------------------------------------------")  # 60個

# UseCustomTurtleFunctions.py

from UsefulTurtleFunctions import *

# Draw a line from (-50, -50) to (50, 50)
drawLine(-50, -50, 50, 50)

# Write a text at (-50, -60)
writeText("Testing useful Turtle functions", -50, -60)

# Draw a point at (0, 0)
drawPoint(0, 0)

# Draw a circle at (0, 0) with radius 80
drawCircle(0, 0, 80)
    
# Draw a rectangle at (0, 0) with width 60 and height 40
drawRectangle(0, 0, 60, 40)

turtle.hideturtle()
turtle.done() 

print("------------------------------------------------------------")  # 60個

# UsefulTurtleFunctions.py

# Draw a line from (x1, y1) to (x2, y2)
def drawLine(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

# Write a text at the specified location (x, y)
def writeText(s, x, y): 
    turtle.penup() # Pull the pen up
    turtle.goto(x, y)
    turtle.pendown() # Pull the pen down
    turtle.write(s) # Write a string

# Draw a point at the specified location (x, y)
def drawPoint(x, y): 
    turtle.penup() # Pull the pen up
    turtle.goto(x, y)
    turtle.pendown() # Pull the pen down
    turtle.begin_fill() # Begin to fill color in a shape
    turtle.circle(3) 
    turtle.end_fill() # Fill the shape

# Draw a circle at centered at (x, y) with the specified radius
def drawCircle(x, y, radius): 
    turtle.penup() # Pull the pen up
    turtle.goto(x, y - radius)
    turtle.pendown() # Pull the pen down
    turtle.circle(radius) 
    
# Draw a rectangle at (x, y) with the specified width and height
def drawRectangle(x, y, width, height): 
    turtle.penup() # Pull the pen up
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown() # Pull the pen down
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


""" 新進

turtle.bk(30)

turtle.bk(30)
turtle.bk(4)

turtle.Screen().reset()


"""

turtle.bgcolor("black")
turtle.bgcolor("#708090")  # 背景為深灰色 RGB(190, 190, 190)
turtle.bgcolor("Skyblue")  # 設定背景色
turtle.bgcolor("Gray21")  # 背景為深灰
turtle.bgcolor("#363636")  # 設背景為深灰
turtle.bgcolor("#BEBEBE")  # 背景為灰色 RGB(190, 190, 190)

#單項完整的

print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
t.pensize(5)  # 畫筆寬度
colorValue = 1.0
colorStep = colorValue / 36
for x in range(1, 37):
    colorValue -= colorStep
    t.color(0.5, 1, colorValue)  # 色彩調整
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

turtle.shape("turtle")
# 繪製時鐘中間顏色
turtle.color("white", "aqua")
turtle.setpos(0, -120)
turtle.begin_fill()
turtle.circle(120)  # 繪時鐘內圓盤
turtle.end_fill()
turtle.penup()  # 畫筆關閉
turtle.home()
turtle.pendown()  # 畫筆打開
turtle.color("black")
turtle.pensize(5)

# 繪製時鐘刻度
for i in range(1, 13):
    turtle.penup()  # 畫筆關閉
    turtle.seth(-30 * i + 90)  # 設定刻度的角度
    turtle.forward(180)
    turtle.pendown()  # 畫筆打開
    turtle.forward(30)  # 畫時間軸
    turtle.penup()
    turtle.forward(20)
    turtle.write(str(i), align="left")  # 寫上刻度
    turtle.home()

# 繪製時鐘外框
turtle.home()
turtle.setpos(0, -270)
turtle.pendown()
turtle.pensize(10)
turtle.pencolor("blue")
turtle.circle(270)
# 寫上名字
turtle.penup()
turtle.setpos(0, 320)
turtle.pendown()
turtle.write("歡迎來到美國", align="center", font=("新細明體", 24))
turtle.ht()  # 隱藏游標

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

turtle.tracer(0, 0)  # 終止追蹤

colorsList = ["red", "green", "blue"]
for line in range(400):
    turtle.color(colorsList[line % 3])
    turtle.forward(line)
    turtle.right(119)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個
'''

'''
# 依據特定階級數繪製Sierpinski三角形
def sierpinski(order, p1, p2, p3):
    if order == 0:  # 階級數為0
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
def drawLine(p1, p2):
    turtle.penup()
    turtle.setpos(p1[0], p1[1])
    turtle.pendown()
    turtle.setpos(p2[0], p2[1])
    turtle.penup()
    turtle.seth(0)


# 傳回2點的中間值
def midpoint(p1, p2):
    p = [0, 0]  # 初值設定
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p


p1 = [0, 866//4]
p2 = [-1000//4, -866//4]
p3 = [1000//4, -866//4]
#order = eval(input("輸入階級數 : "))
order = 4
sierpinski(order, p1, p2, p3)

turtle.mainloop()
'''
print("------------------------------------------------------------")  # 60個

n = 300
step = 10
t = turtle.Pen()
for i in range(0, n + step, step):
    t.penup()
    t.setpos(i, 0)
    t.pendown()
    t.setpos(0, n - i)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

n = 300
step = 10
t = turtle.Pen()
colorsList = ["red", "orange", "yellow", "green", "blue", "cyan", "purple", "violet"]
for i in range(0, n + step, step):
    t.color(random.choice(colorsList))  # 使用不同顏色
    t.setpos(i, 0)
    t.setpos(0, n - i)
    t.setpos(-i, 0)
    t.setpos(0, i - n)
    t.setpos(i, 0)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
colorsList = ["red", "orange", "yellow", "green", "blue", "cyan", "purple", "violet"]
tWidth = 1  # 最初畫筆寬度
for x in range(1, 41):
    t.color(colorsList[x % 8])  # 選擇畫筆顏色
    t.forward(2 + x * 5)  # 每次移動距離
    t.right(45)  # 每次旋轉角度
    tWidth += x * 0.05  # 每次畫筆寬度遞增
    t.width(tWidth)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

colorsList = ["red", "orange", "yellow", "green", "blue", "cyan", "purple", "violet"]
tWidth = 1  # 最初畫筆寬度
for x in range(1, 41):
    turtle.color(colorsList[x % 8])  # 選擇畫筆顏色
    turtle.forward(2 + x * 5)  # 每次移動距離
    turtle.right(45)  # 每次旋轉角度
    tWidth += x * 0.05  # 每次畫筆寬度遞增
    turtle.width(tWidth)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
colorsList = ["red", "orange", "yellow", "green", "blue", "cyan", "purple", "violet"]
for line in range(200):
    t.color(colorsList[line % 8])
    t.forward(line * 2)
    t.left(91)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
for angle in range(0, 360, 15):
    turtle.setheading(angle)  # 調整海龜方向
    turtle.circle(100)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
turtle.shape("turtle")
for angle in range(0, 361, 15):
    turtle.forward(100)
    turtle.stamp()
    turtle.home()
    turtle.seth(angle)  # 調整海龜方向

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
t.shape("turtle")
for angle in range(0, 361, 15):
    t.forward(100)
    t.stamp()
    t.home()  # 海龜返回原點
    t.seth(angle)  # 調整海龜方向

turtle.mainloop()

print("------------------------------------------------------------")  # 60個


t = turtle.Pen()
t.fillcolor("yellow")  # 設定填充顏色
t.begin_fill()  # 開始填充
t.circle(50)  # 繪製左方圓
t.end_fill()  # 結束填充
t.forward(100)
t.color("red", "aqua")  # 設定輪廓顏色是red, 填充顏色是aqua
t.begin_fill()  # 開始填充
t.circle(50)  # 繪製第2個右方圓
t.end_fill()  # 結束填充

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

length = 10
angle = 90
turtle.forward(length)
turtle.left(angle)
length = length + 10

turtle.forward(length)
turtle.left(angle)
length = length + 10

turtle.forward(length)
turtle.left(angle)
length = length + 10

turtle.forward(length)
turtle.left(angle)
length = length + 10

turtle.forward(length)
turtle.left(angle)
length = length + 10

turtle.forward(length)
turtle.left(angle)
length = length + 10

turtle.forward(length)
turtle.left(angle)
length = length + 10

turtle.forward(length)
turtle.left(angle)
length = length + 10

turtle.forward(length)
turtle.left(angle)
length = length + 10

turtle.forward(length)
turtle.left(angle)
length = length + 10

turtle.forward(length)
turtle.left(angle)
length = length + 10

turtle.forward(length)
turtle.left(angle)
length = length + 10

turtle.forward(length)
turtle.left(angle)
length = length + 10
turtle.forward(length)
turtle.left(angle)
length = length + 10

turtle.forward(length)
turtle.left(angle)
length = length + 10

turtle.forward(length)
turtle.left(angle)
length = length + 10

turtle.forward(length)
turtle.left(angle)
length = length + 10

print("------------------------------------------------------------")  # 60個

length = 20
angle = 90
turtle.forward(length)
turtle.right(angle)
turtle.forward(length)
turtle.left(angle)
turtle.forward(length)
turtle.right(angle)
turtle.forward(length)
turtle.left(angle)
turtle.forward(length)
turtle.right(angle)
turtle.forward(length)
turtle.left(angle)
turtle.forward(length)
turtle.right(angle)
turtle.forward(length)
turtle.left(angle)
turtle.forward(length)
turtle.right(angle)
turtle.forward(length)
turtle.left(angle)

print("------------------------------------------------------------")  # 60個

import math


def moveTurtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


turtle.color("black")
turtle.pensize = 10

moveTurtle(0, 0)
turtle.goto(400, 0)

moveTurtle(0, 0)
turtle.goto(0, 300)

moveTurtle(0, 0)
for x in range(360):
    y = math.sin(2 * math.pi * x / 360)
    turtle.goto(x * 1, y * 250)
    turtle.dot(3, "green")


print("------------------------------------------------------------")  # 60個

#sides = int(input("Enter the number of sides for your shape: "))

print('正N邊形')

N = 6


angle = 360.0 / N
length = 400.0 / N

for side in range(N):
    turtle.forward(length)
    turtle.right(angle)

turtle.done()

print("------------------------------------------------------------")  # 60個

#sides = int(input("Enter the number of sides for your shape: "))
print('正N邊形')

N = 6

angle = 360.0 / N
length = 400.0 / N

turtle.fillcolor("blue")
turtle.begin_fill()

for side in range(N):
    turtle.forward(length)
    turtle.right(angle)
turtle.end_fill()
turtle.done()

print("------------------------------------------------------------")  # 60個

length = 0
angle = 90
while length < 200:
    turtle.forward(length)
    turtle.left(angle)
    length = length + 10

print("------------------------------------------------------------")  # 60個

turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)

