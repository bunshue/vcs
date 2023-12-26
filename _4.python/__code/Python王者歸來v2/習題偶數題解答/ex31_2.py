# ex31_2.py
import turtle

def mysquare(x,y,n):
    t.penup()
    t.setpos(x+n/2,y+n/2)
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
    t.setpos(0,0)
    t.seth(0)
    
x,y = eval(input("請輸入x和y : "))
n = eval(input("請輸入n : "))

t = turtle.Pen()
mysquare(x,y,n)














