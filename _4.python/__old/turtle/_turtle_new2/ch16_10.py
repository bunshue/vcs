# ch16_10.py
import turtle

t = turtle.Pen()
step = 5                # 每次增加距離
for r in range(10, 50, step):
    t.circle(r)         # 繪製圓   
    t.penup()           # 將筆提起
    t.right(90)         # 方向往下
    t.forward(step)     # 移動海龜位置起繪點
    t.right(270)        # 方向往右
    t.pendown()         # 將筆放下準備繪製
    

