# ch16_13_1.py
import turtle

t = turtle.Pen()
t.circle(50)            # 繪製第1個左上方圓
t.circle(-50, steps=3)  # 繪製第2個左下方三角形
t.forward(100)
t.circle(50, steps=4)   # 繪製第3個右上方四邊形
t.circle(-50, steps=5)  # 繪製第4個右下方五邊形



