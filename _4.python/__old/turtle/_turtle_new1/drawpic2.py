import turtle

def draw_hexagon_spiral(size):
    # 初始化海龜
    turtle.speed(0)
    turtle.color("black")
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    # 繪製六邊形螺旋
    side_length = 10
    for i in range(size):
        for j in range(6):
            turtle.forward(side_length*(i+1))
            turtle.right(60)
        turtle.right(60)

    # 隱藏海龜
    turtle.hideturtle()

# 畫出六邊形螺旋
draw_hexagon_spiral(10)
turtle.done()
