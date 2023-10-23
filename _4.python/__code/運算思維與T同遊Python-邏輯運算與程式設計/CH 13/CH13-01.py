#CH13-01: 五邊型 累積位置值 round
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
SL = 100.0; ang = 360/5
accumAng = 0.0; accumPX = 0.0; accumPY = 0.0
print(accumAng, accumPX, accumPY)
sides = 5
for j in range(1, sides+1):
    t.forward(100); t.left(ang)
    accumPX += SL *np.cos(accumAng*np.pi/180) 
    accumPY += SL *np.sin(accumAng*np.pi/180)
    accumAng += ang
    print(accumAng, accumPX, accumPY)

    
