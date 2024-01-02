# ch16_11.py
import turtle

t = turtle.Pen()
step = 5                        # 每次增加距離
for r in range(10, 90, step):
    t.circle(r, 90 + r*2)       # 繪製圓   
    t.penup()                   # 將筆提起
    t.home()                    # 海龜回到原點(0,0)
    t.pendown()                 # 將筆放下準備繪製
    

