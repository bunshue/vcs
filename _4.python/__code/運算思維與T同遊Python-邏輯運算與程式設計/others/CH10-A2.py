#CH10-A2 三到八邊形   顏色
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(0)
def funDraw(sides, ang):
    for j in range(1, sides+1):
        t.forward(100);  t.left(ang)
def funExt(sides, ang, color):
    t.color(color)
    funDraw(sides, ang)
def funExt1(sides, ang, color, width):
    t.width(width)
    funExt(sides, ang, color)
funExt1(3, 120.0, 'red', 1)
funExt1(4, 90.0, 'orange', 3)
funExt1(5, 72.0, 'yellow', 1)
funExt1(6, 60.0, 'green', 3)
funExt1(7, 51.43, 'blue', 1)
funExt1(8, 45.0, 'cyan', 3)
