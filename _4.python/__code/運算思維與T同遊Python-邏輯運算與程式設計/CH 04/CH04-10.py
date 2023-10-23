#CH04-10    用code RGB   OK
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
code = 'red'
t.color(code)
for sides in range(3,9):
    ang = 360/sides   
    for i in range(1,sides+1):
        t.forward(100); t.left(ang)
    if (code == 'red'): code = 'green'
    elif (code == 'green'): code = 'blue'
    elif (code == 'blue'): code = 'red'
    else: code = 'error'
    t.color(code)

