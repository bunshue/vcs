# ch16_19.py
import turtle

t = turtle.Pen()
t.color('blue')         # 設定輪廓顏色
t.width(5)              # 輪廓寬度
t.fillcolor('yellow')   # 設定填充顏色
t.begin_fill()          # 開始填充
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()            # 結束填充

