#CH09_06 三到八邊形  用list[[邊數 角度 筆畫色]]
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
list1 = [[3,120.0,'red'], [4,90.0,'orange'], [5,72.0,'yellow'], [6,60.0,'green'], [7,51.43,'blue'], [8,45.0,'cyan']]
for i in range(1, 7):
    t.color(list1[i-1][2])
    for j in range(1, list1[i-1][0]+1):
        t.forward(100);  t.left(list1[i-1][1])
