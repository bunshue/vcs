# ch16_13.py
import turtle

t = turtle.Pen()
t.color('blue')
for angle in range(0, 360, 15):
    t.setheading(angle)         # 調整海龜方向
    t.circle(100)


    

