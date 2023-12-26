# ch31_17.py
import turtle, time

t = turtle.Pen()
t.color('blue')
print(t.screen.getshapes())             # 列印海龜游標字串

for cursor in t.screen.getshapes():
    t.shape(cursor)                     # 更改海龜游標
    t.stamp()                           # 海龜游標蓋章
    t.forward(30)
