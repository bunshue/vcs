#CH02-07  迴圈   四六八邊形
import turtle
t = turtle.Pen()
a=90   #四邊形
for i in range(1,5):
    t.forward(100); t.left(a)
a=60   #六邊形
for i in range(1,7):
    t.forward(100); t.left(a)
a=45   #八邊形
for i in range(1,9):
    t.forward(100); t.left(a)
