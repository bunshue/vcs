#CH10-A1 三到八邊形
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
def fun(par1, par2):
    for j in range(1, par1+1):
        t.forward(100);  t.left(par2)
fun(3, 120.0)
for j in range(1, 4+1):
    t.forward(100);  t.left(90.0)
for j in range(1, 5+1):
    t.forward(100);  t.left(72.0)
for j in range(1, 6+1):
    t.forward(100);  t.left(60.0)
for j in range(1, 7+1):
    t.forward(100);  t.left(51.43)
fun(8, 45.0)

