#CH02-10   三層for迴圈  部分重疊
import turtle
t = turtle.Pen()
t.speed(0)
for j in range(1,4):   #做三次
    for sides in range(3,6):   #做三次
        ang=360/sides   
        for i in range(1,sides+1): t.forward(100); t.left(ang)
    t.forward(100)






