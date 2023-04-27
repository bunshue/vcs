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


def drawSquare(length):
    drawShape(4, length)


def drawTriangle(length):
    drawShape(4, length)


def drawCircle(length):
    drawShape(360, length)

drawShape(4, 10)
moveTurtle(60, 30)
drawShape(3, 20)
moveTurtle(-100, 20)
drawSquare(30)
moveTurtle(- 10, 20)
drawCircle(1)
drawCircle(2)
moveTurtle(75, -75)
drawTriangle(60)

turtle.done()
