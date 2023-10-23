#CH02-16   demo 
import turtle
t = turtle.Pen()
t.speed(0)
for k in range(1,3):
    for j in range(1,3):
        for sides in range(3,9):
            ang = 360/sides
            for i in range(1,sides+1): t.forward(50); t.left(ang)
        t.penup(); t.forward(120.72); t.pendown()
    t.penup(); t.left(180); t.forward(2*120.72); t.left(270); t.forward(120.72); t.left(270); t.pendown()
t.penup(); t.left(270); t.forward(2*120.72); t.left(90); t.pendown()
