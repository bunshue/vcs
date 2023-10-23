#CH10-04 三到八邊形
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
def funDraw(sides, ang):
    for j in range(1, sides+1):
        t.forward(100);  t.left(ang)
funDraw(3, 120.0)
funDraw(4, 90.0)
funDraw(5, 72.0)
funDraw(6, 60.0)
funDraw(7, 51.43)
funDraw(8, 45.0)
