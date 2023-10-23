#CH06-02   線條不同顏色。接續原來的順序
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
colorInd=0
for sides in range(3,9):
    ang = 360/sides
    for i in range(1,sides+1):
        t.color(colorsList[colorInd])
        t.forward(100); t.left(ang)
        colorInd = (colorInd+1)%8
