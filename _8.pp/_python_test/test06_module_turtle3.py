# 載入turtle模組
import turtle as tu

# 顯示畫布
tu.showturtle()

# 畫右半部直線
tu.color('blue')
tu.forward(150)

# 畫右半部的空心圓
tu.setheading(270)
tu.color('red')
tu.pensize(2)
tu.circle(50)

# 回到中心點
tu.pensize(1)
tu.color('blue')
tu.setheading(180)
tu.penup()
tu.forward(150)
tu.pendown()

# 畫左半部直線
tu.forward(150)
tu.setheading(90)

# 畫左半部空心圓
tu.color('red')
tu.pensize(2)
tu.circle(50)
tu.pensize(1)

# 回到中心點
tu.setheading(0)
tu.penup()
tu.forward(150)

# 畫中央實心三角形
tu.setheading(180)
tu.color('green')
tu.pendown()
tu.begin_fill()
tu.circle(50, 360, 3)
tu.end_fill()
