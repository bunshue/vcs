# -*- coding: utf-8 -*-
import turtle   
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
