#CH06-01   線條不同顏色。多邊形重新開始 
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
for sides in range(3,9):
    ang = 360/sides
    t.color(colorsList[(sides-3) % 8])
    for i in range(1,sides+1):
        t.color(colorsList[(i-1)%8])
        t.forward(100); t.left(ang)

