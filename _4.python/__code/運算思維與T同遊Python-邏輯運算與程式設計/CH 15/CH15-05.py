#CH15-05:  五角形 三個單層迴圈
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(5)
SL = 100; SL1 = 161.7; R = 85.08 
sides = 5
ang =360/sides
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
t.up(); t.setheading(-90); t.forward(R); t.setheading(0); t.down()  #move only
t.circle(R)
t.up(); t.home(); t.setheading(-90-ang/2); t.forward(R); t.setheading(0); t.down()  #move onlyt
t.color(colorsList[0])
t.left(0*ang/2)
for j in range(1,sides+1):    #第一個五邊形
    t.forward(SL);  t.left(1*ang)
t.right(0*ang/2)
t.color(colorsList[1])
t.left(1*ang/2)
for j in range(1,sides+1):    #第一個五角形
    t.forward(SL1);  t.left(2*ang)
t.right(1*ang/2)
t.color(colorsList[2])
t.left(2*ang/2)
for j in range(1,sides+1):    #第二個五角形
    t.forward(SL1);  t.left(3*ang)
t.right(2*ang/2)
