#CH10-05 三到八邊形   顏色
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
def funExt(sides, ang, color):
    t.color(color)
    for j in range(1, sides+1):
        t.forward(100);  t.left(ang)
funExt(3, 120.0, 'red')
funExt(4, 90.0, 'orange')
funExt(5, 72.0, 'yellow')
funExt(6, 60.0, 'green')
funExt(7, 51.43, 'blue')
funExt(8, 45.0, 'cyan')
