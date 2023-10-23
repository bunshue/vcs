#CH08-03     變數
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(5); t.speed(5)
dist = +100
ang = +120
for i in range(1,4):
    t.forward(dist); t.left(ang)
    #t.forward(dist); t.right(ang)
    #t.backward(dist); t.left(ang)
    #t.backward(dist); t.right(ang)


