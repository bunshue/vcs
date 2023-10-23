#CH14-09:   原點圓心  針對六邊形  兩個單層迴圈
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
sides = 6
listC6 = [[-50.0, -86.6], [50.0, -86.6], [100.0, 0.0], [50.0, 86.6], [-50.0, 86.6], [-100.0, 0.0]]
listCC = listC6
Rad = [85.1, 100.0, 115.2, 130.7, 146.2, 161.8, 177.5, 193.2, 208.9, 224.7]
R = 100
start = 0; newStart = 2; toEnd = 2
t.up(); t.goto(0, -R); t.down()
t.circle(R)
s = start
for i in range(0, int(sides/2)):   #Notice
    sx = listCC[s%sides][0]; sy = listCC[s%sides][1]
    t.up(); t.goto(sx, sy); t.down()   #move to start point
    e = s + toEnd
    ex = listCC[e%sides][0]; ey = listCC[e%sides][1]
    t.goto(ex, ey)    #draw to end point
    s = s + newStart
s = start+1
for i in range(0, int(sides/2)):   #Notice
    sx = listCC[s%sides][0]; sy = listCC[s%sides][1]
    t.up(); t.goto(sx, sy); t.down()   #move to start point
    e = s + toEnd
    ex = listCC[e%sides][0]; ey = listCC[e%sides][1]
    t.goto(ex, ey)    #draw to end point
    s = s + newStart


