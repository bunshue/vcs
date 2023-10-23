#CH07-10: TAE 五邊 累積位置值   方法二a
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
SL = 100; ang = 75    #手調
accumAng = 0; accumPX = 0; accumPY = 0
print(accumAng, accumPX, accumPY)
for sides in range(5,6):
    for j in range(1, sides+1):
        t.forward(100); t.left(ang)
        accumPX += SL *np.cos(accumAng*np.pi/180) 
        accumPY += SL *np.sin(accumAng*np.pi/180)
        accumAng += ang
        print(accumAng, accumPX, accumPY)
t.hideturtle()
    
