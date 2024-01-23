import turtle          # 匯入海龜模組

turtle.setup(250, 200) # 產生200 X 200畫布
pen = turtle.Turtle()  # 建立畫布物件
pen.penup()            # 畫筆懸空
pen.goto(-50, 50)      # 移向指定座標
pen.pendown()          # 落下畫筆
pen.forward(100)       # 前進100像素
pen.right(90)          # 畫筆右轉90度
pen.fd(100)            # forward()方法簡寫
pen.right(135)
pen.fd(140)

