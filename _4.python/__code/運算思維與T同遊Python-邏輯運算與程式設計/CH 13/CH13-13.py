#CH13-13:   原點圓心  dX dY
import turtle
import numpy as np
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
Rad = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dX =  [ 50.0, -50.0,  -50.0,  -50.0,  -50.0,  -50.0,  -50.0,  -50.0,  -50.0,  -50.0]
dY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
SL = 100
for i in range(5, 15):
    ang = 360/i
    Rad[i-5] = round(-1*SL/(2*np.sin(ang*np.pi/360)), 1)
    dY[i-5] = round(-1*SL/(2*np.tan(ang*np.pi/360)), 1)
print(Rad)
print(dY)
