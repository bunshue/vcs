import turtle   # 匯入海龜模組

turtle.setup(250, 200)     # 產生250 X 200畫布
turtle.bgcolor('SkyBlue')  # 背景為天空藍

show = turtle.Turtle()     # 建立畫布物件
show.pencolor('Yellow')    # 畫筆為黃色
show.pensize(10)           # 畫筆大小
show.speed(1)              # 畫筆速度為慢
# 畫一個簡單矩形
show.forward(70)           # 前進70像素
show.right(90)             # 畫筆右轉90度
show.fd(70)                # forward()方法簡寫
show.right(90)
show.fd(70)
show.right(90)
show.home()
