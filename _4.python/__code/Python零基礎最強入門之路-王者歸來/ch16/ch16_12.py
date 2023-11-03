# ch16_12.py
import turtle

t = turtle.Pen()
colors = ['red', 'orange', 'yellow', 'green', 'blue']
step = 10                       # 每次增加距離
twidth = 0                      # 最初寬度0
for r in range(1, 11):
    t.color(colors[r % 5])      # 選畫筆顏色
    twidth += 1                 # 每次迴圈寬度加1
    t.width(twidth)             # 設定寬度
    t.circle(r*step)            # 繪製圓   
    t.penup()                   # 將筆關閉
    t.right(90)                 # 方向往下
    t.forward(step)             # 移動海龜位置起繪點
    t.right(270)                # 方向往右
    t.pendown()                 # 將筆開啟準備繪製
    

