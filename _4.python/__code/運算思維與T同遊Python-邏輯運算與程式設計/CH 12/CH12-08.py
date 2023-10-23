#CH12-08:   原點圓心  五邊形  用listPair(非連續)
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
R = 85.08
list = [[-50, -68.82], [50, -68.82], [80.9, 26.28], [0, 85.08], [-80.9, 26.28]]
listPair = [[0, 1], [2, 3], [4, 0], [1, 2], [3, 4]]
t.up(); t.goto(0, -R); t.down()
t.circle(R)
for i in range(0, 5):
    s = listPair[i][0]; e = listPair[i][1]
    sx = list[s][0]; sy = list[s][1]
    ex = list[e][0]; ey = list[e][1]
    t.up(); t.goto(sx, sy); t.down()   #move to start point
    t.goto(ex, ey)    #draw to end point
