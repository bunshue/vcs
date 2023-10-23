#CH15-03: 等角平分線   第三回
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(5)
SL = 100; SL1= 161.7 
sides = 5
ang =360/sides
t.color("black")
for i in range(1,sides+1):
    t.forward(100);  t.left(ang)
t.color("green")
t.width(5)
t.left(ang/2)
t.forward(SL1)
t.left(4*ang/2)
t.forward(SL1)
t.color("red")
t.width(3)
t.left(3*ang/2)
t.forward(SL1);  t.backward(SL1);
for i in range(1,sides+1):
    t.left(ang/2)
    t.forward(SL1);  t.backward(SL1);
t.left(180)
