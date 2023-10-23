#CH03-15  連續變大&線變窄三邊形  需小修正
import turtle
t = turtle.Pen()
t.shape('turtle'); t.speed(0)
tWidth = 10
j = 1
while ((1<=j) and (j<=10) and (tWidth >= 0)):
    j += 1
    t.width(tWidth)
    tWidth -= 1.5
    #if (tWidth >= 0):
    t.forward(10+j*20);  t.left(120)
