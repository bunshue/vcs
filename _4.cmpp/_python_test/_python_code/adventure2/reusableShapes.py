import turtle
def drawShape(sides, length):
    angle = 360.0 / sides
    for side in range(sides):
        turtle.forward(length)
        turtle.right(angle)


def moveTurtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


drawShape(4, 10)
moveTurtle(60, 30)
drawShape(3, 20)
turtle.done()
