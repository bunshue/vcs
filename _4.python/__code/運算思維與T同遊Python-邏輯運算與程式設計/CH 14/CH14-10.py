#CH14-10:   原點圓心  八邊形  二層迴圈
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
sides = 8
listC8 = [[-50.0, -120.7], [50.0, -120.7], [120.7, -50.0], [120.7, 50.0], [50.0, 120.7], [-50.0, 120.7], [-120.7, 50.0], [-120.7, -50.0]]
listCC = listC8
Rad = [85.1, 100.0, 115.2, 130.7, 146.2, 161.8, 177.5, 193.2, 208.9, 224.7]
R = 130.7
start = 0; newStart = 2; toEnd = 2
t.up(); t.goto(0, -R); t.down()
t.circle(R)
for j in range(start, start+2):
    s = j
    for i in range(0, int(sides/2)):   #Notice
        sx = listCC[s%sides][0]; sy = listCC[s%sides][1]
        t.up(); t.goto(sx, sy); t.down()   #move to start point
        e = s + toEnd
        ex = listCC[e%sides][0]; ey = listCC[e%sides][1]
        t.goto(ex, ey)    #draw to end point
        s = s + newStart

