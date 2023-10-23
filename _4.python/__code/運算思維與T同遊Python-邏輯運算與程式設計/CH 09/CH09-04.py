#CH09-04 三到八邊形  用list: [[邊數 角度]]
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
list1 = [[3,120.0], [4,90.0], [5,72.0], [6,60.0], [7,51.43], [8,45.0]]
for i in range(1, 7):
    for j in range(1, list1[i-1][0]+1):
        t.forward(100)
        t.left(list1[i-1][1])
