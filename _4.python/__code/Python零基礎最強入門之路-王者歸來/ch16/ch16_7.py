# ch16_7.py
import turtle

t = turtle.Pen()
t.pensize(5)                        # 畫筆寬度
colorValue = 1.0
colorStep = colorValue / 36
for x in range(1, 37):
    colorValue -= colorStep
    t.color(0.5, 1, colorValue)     # 色彩調整
    t.forward(100)                  # 海龜向前繪線移動100
    t.left(90)                      # 海龜方向左轉90度
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(100)                     # 海龜方向左轉100度
    
    
