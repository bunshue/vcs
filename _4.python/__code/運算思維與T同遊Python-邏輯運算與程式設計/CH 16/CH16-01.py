#CH16-01: 同外接圓不同八角形 黑白
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(3); t.speed(5)
SL = 100
sides = 8
Trans = 2*np.sin(np.pi/sides); R = SL/Trans
ang = 360/sides
#t.up(); t.right(90); t.forward(R); t.left(90); t.down()  #move only
#t.circle(R)
t.up(); t.home(); t.right(90+ang/2); t.forward(R); t.left(90+ang/2); t.down()  #move only
for i in [1,2,3,4,5,6,7]:
    SLn = np.sin(i*np.pi/sides)*2*R
    t.left((i-1)*ang/2)
    for j in range(1,sides+1):
        t.forward(SLn);  t.left(i*ang)
    t.right((i-1)*ang/2)
