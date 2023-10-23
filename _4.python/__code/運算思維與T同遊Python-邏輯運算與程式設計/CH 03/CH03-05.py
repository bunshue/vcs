#CH03-05   多邊形不同的固定寬度   三四五邊形
import turtle
t = turtle.Pen()
t.shape('turtle'); t.speed(0)
tWidth = 1
t.width(tWidth)
tWidth += 3
for j in range(1,7):
    t.forward(10+j*20);  t.left(120)
t.width(tWidth)
tWidth += 3
for j in range(1,9):
    t.forward(130+j*10);  t.left(90)
t.width(tWidth)
tWidth += 3
for j in range(1,11):
    t.forward(210+j*6);  t.left(72)

