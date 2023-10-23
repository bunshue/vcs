#CH04-04    用toggle
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
toggle = True
for sides in range(3,9):
    ang = 360/sides   
    if (toggle == True):
        t.color('red')
        toggle = False
    else:
        t.color('green')
        toggle = True
    for i in range(1,sides+1):
        t.forward(100); t.left(ang)
    
