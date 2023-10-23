#CH03-11  連續變大&線變窄三邊形
import turtle
t = turtle.Pen()
t.shape('turtle'); t.speed(0)
tWidth = 10
for j in range(1,11):
    t.width(tWidth)
    tWidth -= 1.5
    if (tWidth > 0):
        t.forward(10+j*20);  t.left(120)

