import turtle
import math


def moveTurtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


turtle.color("black")
turtle.pensize = 10

moveTurtle(0, 0)
turtle.goto(400, 0)

moveTurtle(0, 0)
turtle.goto(0, 300)

moveTurtle(0, 0)
for x in range(360):
    y = math.sin(2 * math.pi * x / 360)
    turtle.goto(x * 1, y * 250)
    turtle.dot(3, "green")
