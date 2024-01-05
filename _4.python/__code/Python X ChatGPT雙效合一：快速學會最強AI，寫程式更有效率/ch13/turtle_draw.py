# -*- coding: utf-8 -*-

import turtle   
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
