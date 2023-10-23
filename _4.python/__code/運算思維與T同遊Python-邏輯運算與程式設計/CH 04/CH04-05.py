#CH04-05    用code
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
code = 1
t.color('red')
for sides in range(3,9):
    ang = 360/sides   
    for i in range(1,sides+1):
        t.forward(100); t.left(ang)
    if (code == 1):
        code = 2
        t.color('green')
    else:
        code = 1
        t.color('red')

