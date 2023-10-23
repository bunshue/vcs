#CH10-01 三到八邊形 
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
for j in range(1, 3+1):
    t.forward(100);  t.left(120.0)
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
