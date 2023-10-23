#CH09-01 三到八邊形  用list[角度]  雙層迴圈
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5);
list1 = [120.0, 90.0, 72.0, 60.0, 51.43, 45.0]
for i in range(3,9):
    for j in range(1,i+1):
        t.forward(100) ;  t.left(list1[i-3])
