import turtle

def draw_spiral_matrix(size):
    # 初始化海龜
    turtle.speed(0)
    turtle.color("black")
    turtle.penup()
    turtle.goto(-size//2, size//2)
    turtle.pendown()

    # 繪製螺旋矩陣
    for i in range(size//2):
        for direction in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            dx, dy = direction
            for j in range(i*2 + 1):
                turtle.forward(20)
                turtle.left(90)
                if j == i:
                    turtle.penup()
                    turtle.forward(20)
                    turtle.pendown()
            turtle.penup()
            turtle.goto(turtle.xcor()+dx*20, turtle.ycor()+dy*20)
            turtle.pendown()

    # 隱藏海龜
    turtle.hideturtle()

# 畫出螺旋矩陣
draw_spiral_matrix(10)
turtle.done()
