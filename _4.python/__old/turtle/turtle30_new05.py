import sys

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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import turtle

screen = turtle.Screen()
screen.setup(500, 400)

turtle.forward(100)
turtle.left(90)
turtle.forward(100)

screen.exitonclick()

print("------------------------------------------------------------")  # 60個

import turtle

screen = turtle.Screen()
screen.setup(500, 400)

turtle.color("blue")
turtle.shape("turtle")
turtle.forward(100)

screen.exitonclick()

print("------------------------------------------------------------")  # 60個

import turtle

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

import turtle

screen = turtle.Screen()
screen.setup(500, 400, startx=20, starty=50)

turtle.pensize(5)
turtle.pencolor("blue")
turtle.forward(100)

screen.exitonclick()

print("------------------------------------------------------------")  # 60個

import turtle

screen = turtle.Screen()
screen.setup(500, 400)

for i in range(1, 5):
    turtle.forward(100)
    turtle.left(90)

screen.exitonclick()

print("------------------------------------------------------------")  # 60個

import turtle

screen = turtle.Screen()
screen.setup(500, 400)

for i in range(1, 7):
    turtle.forward(100)
    turtle.left(60)

screen.exitonclick()

print("------------------------------------------------------------")  # 60個

import turtle

screen = turtle.Screen()
screen.setup(500, 400)

for i in range(1, 4):
    turtle.forward(100)
    turtle.left(120)

screen.exitonclick()

print("------------------------------------------------------------")  # 60個

import turtle

screen = turtle.Screen()
screen.setup(500, 400)

for i in range(1, 6):
    turtle.forward(150)
    turtle.left(144)

screen.exitonclick()

print("------------------------------------------------------------")  # 60個

import turtle

screen = turtle.Screen()

for i in range(360):
    turtle.forward(2)
    turtle.left(1)

screen.exitonclick()

print("------------------------------------------------------------")  # 60個

#DisplayUnicode
import turtle

turtle.write("\u6B22\u8FCE \u03b1 \u03b2 \u03b3")

turtle.done() 



print("------------------------------------------------------------")  # 60個

from turtle import *
color('green', 'red')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done() 
   


print("------------------------------------------------------------")  # 60個






print("------------------------------------------------------------")  # 60個

   


print("------------------------------------------------------------")  # 60個





