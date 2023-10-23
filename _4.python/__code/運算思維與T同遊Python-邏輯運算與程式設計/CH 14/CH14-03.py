#CH14-03:   原點圓心  七角形
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
listC7 = [[-50.0, -103.8], [50.0, -103.8], [112.3, -25.6], [90.1, 71.9], [0.0, 115.3], [-90.1, 71.9], [-112.3, -25.6]]
listPair = [[0, 3], [3, 6], [6, 2], [2, 5], [5, 1], [1, 4], [4, 0]]
R = 115.2
SL = 100
t.up(); t.goto(0, -R); t.down()
t.circle(R)
for i in range(0, 7):
    s = listPair[i][0]
    sx = listC7[s%7][0]; sy = listC7[s%7][1]
    t.up(); t.goto(sx, sy); t.down()   #move to start point
    e = listPair[i][1]
    ex = listC7[e%7][0]; ey = listC7[e%7][1]
    t.goto(ex, ey)    #draw to end point
