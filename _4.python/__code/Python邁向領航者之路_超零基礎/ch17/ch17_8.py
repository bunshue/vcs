# ch17_8.py
import turtle

t = turtle.Pen()
t.color('blue')
r = 30                              # 半徑
t.penup()
t.setheading(180)                   # 海龜往左
t.forward(270)                      # 移動往左
t.setheading(0)                     # 海龜往右

for edge in range(3, 13, 1):        # 繪3 - 12邊圖
    t.pendown()
    t.circle(r, steps=edge)
    t.penup()
    t.forward(60)
    
 


    

