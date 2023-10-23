#CH03-01   四邊形 
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(0)
sides = 4
ang = 360/sides   
for i in range(1,sides+1):
    t.forward(100); t.left(90)

