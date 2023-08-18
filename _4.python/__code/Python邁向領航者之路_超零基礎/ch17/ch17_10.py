# ch17_10.py
import turtle
t = turtle.Pen()
sides = 5                       # 星星的個數
angle = 180 - (180 / sides)     # 每個迴圈海龜轉動角度
size = 100                      # 星星長度
t.color('blue')
t.begin_fill()
for x in range(sides):
    t.forward(size)             # 海龜向前繪線移動100
    t.right(angle)              # 海龜方向左轉的度數
t.end_fill()




