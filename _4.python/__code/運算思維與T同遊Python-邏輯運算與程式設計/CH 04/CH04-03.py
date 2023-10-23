#CH04-03    用toggle
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
toggle = True
t.color('red')
for sides in range(3,9):
    ang = 360/sides   
    for i in range(1,sides+1):
        t.forward(100); t.left(ang)
    if (toggle == True):
        t.color('green')
        toggle = False
    else:
        t.color('red')
        toggle = True
