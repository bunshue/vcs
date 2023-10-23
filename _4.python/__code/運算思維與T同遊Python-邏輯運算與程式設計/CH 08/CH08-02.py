#CH08-02    變數
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(5); t.speed(5)
dist = +100
ang = +120
for i in range(1,4): t.forward(dist); t.left(ang)
#for i in range(1,4): t.forward(dist); t.right(ang)
#for i in range(1,4): t.backward(dist); t.left(ang)
#for i in range(1,4): t.backward(dist); t.right(ang)

