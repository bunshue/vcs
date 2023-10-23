#CH05-07   RGB  錯
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
colors3List = ['red', 'green', 'blue']
colorsIndex = 0
sides = 3
ang = 360/sides
t.color(colors3List[colorsIndex])
colorsIndex += 1
for i in range(1,sides+1):
    t.forward(100); t.left(ang)
