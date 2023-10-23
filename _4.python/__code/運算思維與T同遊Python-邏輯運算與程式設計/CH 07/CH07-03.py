#CH07-03   五邊形內縮為1 
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
sides  = 5
ang = 360/sides   
for i in range(1,sides+1):
    t.forward(100)
    t.left(180)
    t.forward(99)
    t.left(180)
    t.left(ang)
t.hideturtle()





