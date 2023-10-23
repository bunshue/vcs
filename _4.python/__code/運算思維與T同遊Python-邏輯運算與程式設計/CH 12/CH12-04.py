#CH12-04:   原點圓心  逆時針 五邊  用串列
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
R = 85.08
list = [[-50.0, -68.82], [50.0, -68.82], [80.9, 26.28], [0.0, 85.08], [-80.9, 26.28]]
t.up(); t.goto(0.0, -R); t.down()  #move only
t.circle(R)
x = list[0][0]; y = list[0][1]
t.up(); t.goto(x, y); t.down() #p0
for i in range(1,6):
    x = list[i%5][0]; y = list[i%5][1]
    t.goto(x, y)    #pn
