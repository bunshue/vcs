#CH06-03    線條不同顏色。多邊形不同的重新開始
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
for sides in range(3,9):
    ang = 360/sides
    colorInd = sides-3
    for i in range(1, sides+1):
        t.color(colorsList[colorInd])
        colorInd = (colorInd+1)%8
        t.forward(100); t.left(ang) 
