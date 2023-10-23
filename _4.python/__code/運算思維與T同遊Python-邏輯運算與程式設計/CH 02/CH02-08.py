#CH02-08   more level
import turtle
t = turtle.Pen()
t.speed(5)
for sides in range(3,9):
    ang = 360/sides
    for i in range(1,sides+1): t.forward(100); t.left(ang)
