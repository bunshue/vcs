import turtle          # 匯入海龜模組

turtle.setup(250, 250) # 產生250 X 250畫布
turtle.bgcolor('SkyBlue')  # 背景為天空藍

pen = turtle.Turtle()
pen.pencolor('White')
pen.pensize(2)

# X軸
pen.up()          # 抬起畫筆
pen.goto(-300, 0) # 前進指定座標
pen.down()        # 放下畫筆
pen.forward(600)  # 畫筆前進
pen.left(90)      # 畫筆左轉

# Y軸
pen.up()          # 抬起畫筆
pen.goto(0, -300) # 前進指定座標
pen.down()        # 放下畫筆
pen.forward(600)  # 畫筆前進
pen.left(90)      # 畫筆左轉
pen.home()        # 畫筆回到原點

# 繪製兩個三角形
pen.pencolor('Yellow')
pen.pensize(10)
pen.left(45)
pen.forward(100)     
pen.left(135)    
pen.forward(140) 
pen.home()

pen.right(45)
pen.forward(100)
pen.right(135)    
pen.forward(140)
pen.right(135)    
pen.forward(100)
