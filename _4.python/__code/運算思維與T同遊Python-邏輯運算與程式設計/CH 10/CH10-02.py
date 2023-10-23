#CH10-02 三到八邊形 
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
def fun(aug1, aug2):
    for j in range(1, aug1+1):
        t.forward(100);  t.left(aug2)
fun(3, 120.0)
for j in range(1, 4+1):
    t.forward(100);  t.left(90.0)
for j in range(1, 5+1):
    t.forward(100);  t.left(72.0)
for j in range(1, 6+1):
    t.forward(100);  t.left(60.0)
for j in range(1, 7+1):
    t.forward(100);  t.left(51.43)
for j in range(1, 8+1):
    t.forward(100);  t.left(45.0)
