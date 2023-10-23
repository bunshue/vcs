#CH12-02:   原點圓心  逆時針 五角形
import turtle
t = turtle.Pen()
t.shape("turtle"); t.width(1); t.speed(5)
t.up(); t.goto(0.0, -85.08); t.down()
t.circle(85.08)
t.up(); t.goto(-50.0, -68.82); t.down() #p0
t.goto(80.9, 26.28)   #p2
t.goto(-80.9, 26.28)  #p4
t.goto(50.0, -68.82)    #p1
t.goto(0.0, 85.08)      #p3
t.goto(-50.0, -68.82)   #p0

