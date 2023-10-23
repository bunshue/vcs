#CH02-12  四層for迴圈（一）  3~8
import turtle
t = turtle.Pen()
t.speed(0)
for k in range(1,2):
    for j in range(1,3):
        for sides in range(3,9):
            ang=360/sides   
            for i in range(1,sides+1): t.forward(50); t.left(ang)
        t.forward(120.72)
    t.left(180)
    t.forward(2*120.72)
