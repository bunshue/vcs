#CH07-05   七邊形的示範 
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
sides  = 7
ang = 360/sides   
for i in range(1,sides+1):
    t.forward(100)
    t.left(180)
    t.forward(90)
    t.left(180)
    t.left(ang)
t.hideturtle()
