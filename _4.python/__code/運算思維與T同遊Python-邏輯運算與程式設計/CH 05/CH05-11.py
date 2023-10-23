#CH05-11    %
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
colors3List = ['red', 'green', 'blue']
colorsIndex = 0
sides = 5
ang = 360/sides
for i in range(1,sides+1):
    t.color(colors3List[colorsIndex % 3])
    colorsIndex += 1
    t.forward(100); t.left(ang)
