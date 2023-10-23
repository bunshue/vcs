#CH05-10    RGBGr
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
colors3List = ['red', 'green', 'blue', 'gray']
colorsIndex = 0
sides = 4
ang = 360/sides
for i in range(1,sides+1):
    t.color(colors3List[colorsIndex])
    colorsIndex += 1
    t.forward(100); t.left(ang)
