#CH12-06:   原點圓心  五邊形 用listSeq
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
R = 85.08
list = [[-50.0, -68.82], [50.0, -68.82], [80.9, 26.28], [0.0, 85.08], [-80.9, 26.28]]
listSeq = [0, 1, 2, 3, 4, 0]
t.up(); t.goto(0.0, -R); t.down()
t.circle(R)
x = list[0][0]; y = list[0][1]
t.up(); t.goto(x, y); t.down() #p0  由listSeq定的起點
for i in range(1, 6):
    k = listSeq[i]
    ex = list[k][0]; ey = list[k][1]
    t.goto(ex, ey)    #draw to end point
    sx = ex; sy = ey
    t.up(); t.goto(sx, sy); t.down()   #move to start point
   
