import turtle   # 匯入海龜模組

turtle.setup(250, 200)     # 產生200 X 200畫布
turtle.bgcolor('SkyBlue')  # 背景為天空藍

show = turtle.Turtle()     # 建立畫布物件
show.color('Blue', 'Gold') # 設畫筆為藍色，塗滿金黃色
show.pensize(10)           # 畫筆大小
show.speed(1)              # 畫筆速度為慢
show.pu()                  # 抬起畫筆
show.goto(-50, 50)         # 前往指定位置

# 畫一個簡單矩形
show.begin_fill()   # 開始進行塗色
show.pd()           # pendown()方法簡寫，放下畫筆
show.forward(100)   # 前進100像素
show.right(90)      # 畫筆右轉90度
show.fd(100)        # forward()方法簡寫
show.right(90)
show.fd(100)
show.right(90)
show.fd(100)
show.end_fill()     # 結束塗色動作
