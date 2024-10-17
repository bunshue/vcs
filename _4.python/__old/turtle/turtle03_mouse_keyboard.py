"""

基本的 turtle 使用


"""


import sys
import time
import random

import turtle

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("turtle測試 視窗相關 鍵鼠控制")
print("------------------------------------------------------------")  # 60個

print("在視窗任一位置按下滑鼠左鍵關閉視窗")
turtle.exitonclick()  # 在視窗任一位置按下滑鼠左鍵關閉視窗

print("------------------------------------------------------------")  # 60個

print("取得滑鼠座標")


def drawPoint(x, y):
    print("滑鼠座標 :(", x, y, ")")
    turtle.goto(x, y)
    turtle.dot(50, "Red")


t = turtle.Pen()
t.screen.onclick(drawPoint)
t.screen.mainloop()

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

# HandleMouseClick


def drawPoint(x, y):
    print("滑鼠座標 :(", x, y, ")")
    turtle.goto(x, y)
    turtle.dot(50, "Red")


def drawPoint2(x, y):
    turtle.circle(30)


# Bind handlers with the mouse-click event
t = turtle.Pen()
t.screen.onclick(drawPoint)
t.screen.onclick(drawPoint2, add=True)  # 附加另一個事件

turtle.done()

print("------------------------------------------------------------")  # 60個


def fxn1(x, y):
    print("滑鼠按下")
    turtle.fillcolor("red")


def fxn2(x, y):
    print("滑鼠放開")
    turtle.fillcolor("black")


# set screen and turtle
sc = turtle.Screen()
sc.setup(400, 300)

turtle.shape("turtle")
turtle.turtlesize(2)

# 滑鼠按下事件
turtle.onclick(fxn1)

# 滑鼠放開事件
turtle.onrelease(fxn2)

print("------------------------------------------------------------")  # 60個

# HandleMouseRelease.py


def displaySqaure(x, y):
    turtle.penup()  # 提筆
    turtle.goto(x - 100, y - 100)
    turtle.pendown()  # 下筆
    turtle.begin_fill()  # 開始塗色
    turtle.circle(50)
    turtle.end_fill()  # 結束塗色


# Bind a handler with the mouse-release event
turtle.onrelease(displaySqaure)
turtle.done()

print("------------------------------------------------------------")  # 60個


def keyRight():
    turtle.setheading(0)  # 設定海龜方向
    turtle.forward(50)


def keyUp():
    turtle.setheading(90)  # 設定海龜方向
    turtle.forward(50)


def keyLeft():
    turtle.setheading(180)  # 設定海龜方向
    turtle.forward(50)


def keyDown():
    turtle.setheading(270)  # 設定海龜方向
    turtle.forward(50)


t = turtle.Pen()
t.screen.onkey(keyRight, "Right")
t.screen.onkey(keyUp, "Up")
t.screen.onkey(keyLeft, "Left")
t.screen.onkey(keyDown, "Down")
t.screen.listen()
t.screen.mainloop()

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

wk = turtle.textinput(f"一週七天，按0離開", "請輸入星期前三個字母：")

if wk == None:
    print("你按了取消")
else:
    print("輸入資料 :", wk)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個
