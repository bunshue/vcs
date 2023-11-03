# ch16_21.py
import turtle, time
colorsList = ['green', 'yellow', 'red']

t = turtle.Pen()
t.speed(10)                             # 加速繪製圖形
t.ht()                                  # 隱藏海龜游標
for i in range(0,3):
    t.color('white', colorsList[i%3])   # 更改色彩
    t.begin_fill()                      # 開始填充
    t.circle(50)                        # 繪製左方圓
    t.end_fill()                        # 結束填充
    time.sleep(3)                       # 每隔3秒執行一次迴圈
    




