# ex31_4.py
import turtle
import random
colorsList = ['green', 'blue', 'red']

t = turtle.Pen()
t.ht()                      # 隱藏海龜
t.speed(0)
t.penup()
t.setpos(-200,0)
t.pendown()
r=100
for i in range(1, 51):
    t.color(random.choice(colorsList))
    t.circle(r)
    t.penup()
    t.fd(5)
    t.pendown()
    r = r - 1


