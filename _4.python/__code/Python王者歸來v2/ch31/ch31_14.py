# ch31_14.py
import turtle

t = turtle.Pen()
t.color('blue')
t.shape('turtle')
for angle in range(0, 361, 15):
    t.forward(100)
    t.stamp()
    t.home()
    t.seth(angle)         # 調整海龜方向



    

