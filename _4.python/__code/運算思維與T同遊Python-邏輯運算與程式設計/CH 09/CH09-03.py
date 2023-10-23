#CH09-03 三到八邊形  用三list: [邊數] [角度] [筆畫色]
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(1); t.speed(5)
list1 = [3, 4, 5, 6, 7, 8]
list2 = [120.0, 90.0, 72.0, 60.0, 51.43, 45.0]
list3 = ['red', 'orange','yellow','green','blue', 'cyan']
for i in range(1, 7):
    t.color(list3[i-1])
    for j in range(1, list1[i-1]+1):
        t.forward(100)
        t.left(list2[i-1])
