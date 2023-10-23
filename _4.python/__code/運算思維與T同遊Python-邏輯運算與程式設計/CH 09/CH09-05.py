#CH09-05 三到八邊形  用兩list[[邊數 角度]] [筆畫色] 
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
list1 = [[3,120.0], [4,90.0], [5,72.0], [6,60.0], [7,51.43], [8,45.0]]
list2 = ['red','orange','yellow','green','blue','cyan']
for i in range(1, 7):
    t.color(list2[i-1])
    for j in range(1, list1[i-1][0]+1):
        t.forward(100);  t.left(list1[i-1][1])
