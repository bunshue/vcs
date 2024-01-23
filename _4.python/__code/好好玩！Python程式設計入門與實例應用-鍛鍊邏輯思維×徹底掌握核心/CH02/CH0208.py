import turtle   # 匯入海龜模組

turtle.setup(250, 200)     # 產生250 X 200畫布
turtle.bgcolor('#BEBEBE')  # 背景為灰色 RGB(190, 190, 190)
turtle.colormode(255)      # 色彩以數值表示
show = turtle.Turtle()     # 建立畫布物件
show.pensize(10)           # 畫筆大小
show.speed(1)              # 畫筆速度為慢

show.color((255, 0, 255), (255, 215, 0)) # 設畫筆為洋紅色，塗滿金黃色
show.pu()                  # 抬起畫筆
show.goto(-50, 50)         # 前往指定位置

# 畫一個簡單三角形
show.begin_fill()   # 開始塗色
show.pd()           # pendown()方法簡寫
show.forward(100)   # 前進100像素
show.right(120)     # 畫筆右轉120度
show.fd(100)        # forward()方法簡寫
show.right(120)
show.forward(100)
show.end_fill()     # 結束塗色
