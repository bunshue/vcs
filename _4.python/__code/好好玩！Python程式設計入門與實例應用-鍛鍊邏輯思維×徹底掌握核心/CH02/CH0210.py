import turtle   # 匯入海龜模組

turtle.setup(200, 200)     # 畫布大小200 X 200
turtle.bgcolor('#708090')  # 背景為深灰色 RGB(190, 190, 190)

pen = turtle.Turtle()     # 建立畫布物件
pen.pensize(10)           # 畫筆大小
pen.speed(1)              # 畫筆速度為慢
pen.pencolor('#FFFFFF')   # 設畫筆為白色
pen.shape('turtle')       # 設畫筆形狀是海龜
pen.pu()                  # 抬起畫筆
pen.goto(-10, 70)
pen.pd()                  # 放下畫筆
pen.circle(-60, 360, 6)   # 畫出一個六邊形
