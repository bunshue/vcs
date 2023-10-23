#CH12-05:   原點圓心  五邊  迴圈用串列
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
R = 85.08
list = [[-50.0, -68.82], [50.0, -68.82], [80.9, 26.28], [0.0, 85.08], [-80.9, 26.28]]
t.up(); t.goto(0.0, -R); t.down()
t.circle(R)
x = list[0][0]; y = list[0][1]
t.up(); t.goto(x, y); t.down() #p0
for i in [1, 2, 3, 4, 0]:
    x = list[i][0]; y = list[i][1]
    t.goto(x, y)    #pn

