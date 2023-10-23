#CH03-06  線連續變寬   三四五邊形
import turtle
t = turtle.Pen()
t.shape('turtle'); t.speed(0)
tWidth = 1
for j in range(1,7):
    t.width(tWidth)
    tWidth += 3
    t.forward(10+j*20);  t.left(120)
for j in range(1,9):
    t.width(tWidth)
    tWidth += 3
    t.forward(130+j*10);  t.left(90)
for j in range(1,11):
    t.width(tWidth)
    tWidth += 3
    t.forward(210+j*6);  t.left(72)
