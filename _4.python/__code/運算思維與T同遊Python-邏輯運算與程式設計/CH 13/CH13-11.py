#CH13-11: 五邊型 累積位置值 round 雙層串列
import turtle
import numpy as np
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(0)
SL = 100.0; ang = 360/5
accumAng = 0.0; accumPX = 0.0; accumPY = 0.0
listStr = "["
listStr +='['+str(accumPX)+ ','+str(accumPY)+']'
sides = 5
for j in range(1, sides+1):
    t.forward(100); t.left(ang)
    accumPX += SL *np.cos(accumAng*np.pi/180) 
    accumPY += SL *np.sin(accumAng*np.pi/180)
    accumAng += ang
    roundAccumPX = round(accumPX, 1)
    roundAccumPY = round(accumPY, 1)
    listStr += ', ['+str(roundAccumPX)+ ','+str(roundAccumPY)+']'
listStr += ']'
print(listStr)
