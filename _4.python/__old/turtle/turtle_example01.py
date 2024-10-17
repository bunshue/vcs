import sys
import time
import random

import turtle

turtle.speed(0)

print("------------------------------------------------------------")  # 60個


def is_inside():
    # 測試是否在繪布範圍
    left = (-t.screen.window_width() / 2) + 100  # 左邊牆
    right = (t.screen.window_width() / 2) - 100  # 右邊牆
    top = (t.screen.window_height() / 2) - 100  # 上邊牆
    bottom = (-t.screen.window_height() / 2) + 100  # 下邊牆
    x, y = t.pos()  # 海龜座標
    is_inside = (left < x < right) and (bottom < y < top)
    return is_inside


def t_move():
    colors = ["blue", "pink", "green", "red", "yellow", "aqua"]
    t.color(random.choice(colors))  # 繪圖顏色
    t.begin_fill()  # 開始塗色
    if is_inside():  # 如果在繪布範圍
        # t.right(random.randint(320, 350))  # 海龜移動角度
        t.right(random.randint(0, 180))  # 海龜移動角度
        t.forward(length)
    else:
        t.backward(length)
    t.end_fill()  # 結束塗色


length = 100  # 線長
width = 10  # 線寬
t = turtle.Pen()
t.pensize(width)  # 設定畫筆大小
t.screen.bgcolor("black")  # 畫布背景
while True:
    t_move()

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

turtle.shape("turtle")

# 繪製時鐘中間顏色
turtle.color("white", "aqua")
turtle.setpos(0, -120)
turtle.begin_fill()  # 開始塗色
turtle.circle(120)  # 繪時鐘內圓盤
turtle.end_fill()  # 結束塗色
turtle.penup()  # 提筆
turtle.home()  # 畫筆回到原點
turtle.pendown()  # 下筆
turtle.color("black")
turtle.pensize(5)  # 設定畫筆大小

# 繪製時鐘刻度
for i in range(1, 13):
    turtle.penup()  # 提筆
    turtle.setheading(-30 * i + 90)  # 設定海龜方向  # 設定刻度的角度
    turtle.forward(180)
    turtle.pendown()  # 下筆
    turtle.forward(30)  # 畫時間軸
    turtle.penup()  # 提筆
    turtle.forward(20)
    turtle.write(str(i), align="left")  # 寫上刻度
    turtle.home()  # 畫筆回到原點

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("特殊完整turtle範例")
turtle.tracer(0, 0)  # 終止追蹤

colorsList = ["red", "green", "blue"]
for line in range(400):
    turtle.color(colorsList[line % 3])
    turtle.forward(line)
    turtle.right(119)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("特殊完整turtle範例")


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
    turtle.penup()  # 提筆
    turtle.setpos(p1[0], p1[1])
    turtle.pendown()  # 下筆
    turtle.setpos(p2[0], p2[1])
    turtle.penup()  # 提筆
    turtle.setheading(0)  # 設定海龜方向


# 傳回2點的中間值
def midpoint(p1, p2):
    p = [0, 0]  # 初值設定
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p


p1 = [0, 866 // 4]
p2 = [-1000 // 4, -866 // 4]
p3 = [1000 // 4, -866 // 4]
# 階級數
order = 4
sierpinski(order, p1, p2, p3)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("特殊完整turtle範例")
n = 300
step = 10
colorsList = ["red", "orange", "yellow", "green", "blue", "cyan", "purple", "violet"]
for i in range(0, n + step, step):
    turtle.color(random.choice(colorsList))  # 使用不同顏色
    turtle.setpos(i, 0)
    turtle.setpos(0, n - i)
    turtle.setpos(-i, 0)
    turtle.setpos(0, i - n)
    turtle.setpos(i, 0)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個


def draw_spiral_matrix(size):
    # 初始化海龜
    turtle.color("black")
    turtle.penup()  # 提筆
    turtle.goto(-size // 2, size // 2)
    turtle.pendown()  # 下筆

    # 繪製螺旋矩陣
    for i in range(size // 2):
        for direction in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            dx, dy = direction
            for j in range(i * 2 + 1):
                turtle.forward(20)
                turtle.left(90)
                if j == i:
                    turtle.penup()  # 提筆
                    turtle.forward(20)
                    turtle.pendown()  # 下筆
            turtle.penup()  # 提筆
            turtle.goto(turtle.xcor() + dx * 20, turtle.ycor() + dy * 20)
            turtle.pendown()  # 下筆

    turtle.hideturtle()  # 隱藏海龜


# 畫出螺旋矩陣
draw_spiral_matrix(10)
turtle.done()

print("------------------------------------------------------------")  # 60個


def draw_hexagon_spiral(size):
    # 初始化海龜
    turtle.color("black")
    turtle.penup()  # 提筆
    turtle.goto(0, 0)
    turtle.pendown()  # 下筆

    # 繪製六邊形螺旋
    side_length = 10
    for i in range(size):
        for j in range(6):
            turtle.forward(side_length * (i + 1))
            turtle.right(60)
        turtle.right(60)

    turtle.hideturtle()  # 隱藏海龜


# 畫出六邊形螺旋
draw_hexagon_spiral(10)
turtle.done()

print("------------------------------------------------------------")  # 60個


# 繪製池塘
pond = turtle.Screen()
pond.setup(600, 400)
pond.bgcolor("light blue")
pond.title("Yertle's Pond")

# 繪製小島
mud = turtle.Turtle("circle")
mud.shapesize(stretch_wid=5, stretch_len=5, outline=None)
mud.pencolor("tan")
mud.fillcolor("tan")

# 繪製樹幹
SIDE = 80
ANGLE = 90
log = turtle.Turtle()
log.hideturtle()  # 隱藏海龜
log.pencolor("peru")
log.fillcolor("peru")
log.penup()  # 提筆
log.setpos(215, -30)
log.left(45)
log.begin_fill()  # 開始塗色
for _ in range(2):
    log.forward(SIDE)
    log.left(ANGLE)
    log.forward(SIDE / 4)
    log.left(ANGLE)
log.end_fill()  # 結束塗色

# 繪製樹洞
knot = turtle.Turtle()
knot.hideturtle()  # 隱藏海龜
knot.penup()  # 提筆
knot.setpos(245, 5)
knot.begin_fill()  # 開始塗色
knot.circle(5)
knot.end_fill()  # 結束塗色

# 繪製鱷龜 Yertle
yertle = turtle.Turtle("turtle")
yertle.color("green")
yertle.forward(200)
yertle.left(180)
yertle.forward(200)
yertle.right(176)
yertle.forward(205)

print("------------------------------------------------------------")  # 60個

turtle.color("red", "yellow")
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()

turtle.done()

print("------------------------------------------------------------")  # 60個
