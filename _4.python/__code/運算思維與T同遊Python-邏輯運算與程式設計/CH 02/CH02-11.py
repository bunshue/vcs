#CH02-11  三層for迴圈  3~8
import turtle
t = turtle.Pen()
t.speed(0)
for j in range(1,3):
    for sides in range(3,9):
        ang=360/sides   
        for i in range(1,sides+1): t.forward(50); t.left(ang)
    t.forward(120.72)




