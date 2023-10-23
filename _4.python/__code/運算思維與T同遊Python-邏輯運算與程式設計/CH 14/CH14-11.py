#CH14-11:   原點圓心  十二邊形  二層迴圈
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
sides = 12
listC12 = [[-50.0, -186.6], [50.0, -186.6], [136.6, -136.6], [186.6, -50.0], [186.6, 50.0], [136.6, 136.6], [50.0, 186.6], [-50.0, 186.6], [-136.6, 136.6], [-186.6, 50.0], [-186.6, -50.0], [-136.6, -136.6]]
listCC = listC12
R = 193.2
start = 0; newStart = 2; toEnd = 2
t.up(); t.goto(0, -R); t.down()
t.circle(R)
for j in range(start, start+2):
    s = j
    for i in range(0, int(sides/2)):
        sx = listCC[s%sides][0]; sy = listCC[s%sides][1]
        t.up(); t.goto(sx, sy); t.down()   #move to start point
        e = s + toEnd
        ex = listCC[e%sides][0]; ey = listCC[e%sides][1]
        t.goto(ex, ey)    #draw to end point
        s = s + newStart

