#CH16-06: 同外接圓不同十二角形 上下尖  減少重複性
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(5)
SL = 100
sides = 12
Trans = 2*np.sin(np.pi/sides); R = SL/Trans
ang = 360/sides
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
modiList = [[1,sides], [2,6], [3,4], [4,3], [5,sides], [6,2], [7,sides], [8,3], [9,4], [10,6], [11,sides], [12,sides]]
t.up(); t.home(); t.right(90); t.forward(R); t.left(90); t.down()  #move only
t.left(ang/2)
for i in [1,2,3,4,5,6,7,8,9,10,11]:
    t.color(colorsList[(i-1)%8])
    SLn = np.sin(i*np.pi/sides)*2*R
    t.left((i-1)*ang/2)
    k = modiList[i-1]
    for j in range(1,k[1]+1):
        t.forward(SLn);  t.left(i*ang)
    t.right((i-1)*ang/2)
t.right(ang/2)
