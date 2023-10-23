#CH02-09   三層for迴圈  往右三個
import turtle
t = turtle.Pen()
t.speed(0)
for j in range(1,4):   #做3次
    for sides in range(3,5):   #做2次
        ang=360/sides   
        for i in range(1,sides+1): t.forward(100); t.left(ang)
    t.forward(100)




