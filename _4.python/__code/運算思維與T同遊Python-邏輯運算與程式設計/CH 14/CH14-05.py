#CH14-05:   原點圓心  七邊形
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
listC7 = [[-50.0, -103.8], [50.0, -103.8], [112.3, -25.6], [90.1, 71.9], [0.0, 115.3], [-90.1, 71.9], [-112.3, -25.6]]
listPair = [0, 1, 2, 3, 4, 5, 6]
R = 115.2
SL = 100
toEnd = 2
t.up(); t.goto(0, -R); t.down()
t.circle(R)
for i in range(0, 7):
    s = listPair[i]
    sx = listC7[s%7][0]; sy = listC7[s%7][1]
    t.up(); t.goto(sx, sy); t.down()   #move to start point
    e = s+toEnd
    ex = listC7[e%7][0]; ey = listC7[e%7][1]
    t.goto(ex, ey)    #draw to end point
