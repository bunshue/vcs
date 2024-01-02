# ch16_18.py
import turtle

t = turtle.Pen()
t.color('blue')         # 設定輪廓顏色
t.fillcolor('yellow')   # 設定填充顏色
t.begin_fill()          # 開始填充
t.circle(50)            # 繪製左方圓
t.end_fill()            # 結束填充
t.forward(100)
t.color('red', 'aqua')  # 設定輪廓顏色是red, 填充顏色是aqua
t.begin_fill()          # 開始填充
t.circle(50)            # 繪製第2個右方圓
t.end_fill()            # 結束填充




