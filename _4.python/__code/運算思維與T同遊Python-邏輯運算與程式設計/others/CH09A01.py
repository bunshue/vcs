#CH09A01 三到八邊形  用兩list[[筆畫色 角度]] [邊數]
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
list1 = [['red', 120.0], ['orange', 90.0], ['yellow', 72.0], ['green', 60.0], ['blue', 51.43], ['cyan', 45.0]]
list2 = [3,4,5,6,7,8]
for i in range(1, 7):
    t.color(list1[i-1][0])
    for j in range(1, list2[i-1]+1):
        t.forward(100);  t.left(list1[i-1][1]) 
