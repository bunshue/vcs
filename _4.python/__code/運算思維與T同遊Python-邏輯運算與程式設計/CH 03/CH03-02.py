#CH03-02  長度連續變大 三邊形
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(0)
for j in range(1,11):
    t.forward(10+j*20);  t.left(120)
