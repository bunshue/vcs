import turtle
sides = int(raw_input("Enter the number of sides for your shape: "))
angle = 360.0 / sides
length = 400.0 / sides

turtle.fillcolor("blue")
turtle.begin_fill()

for side in range(sides):
    turtle.forward(length)
    turtle.right(angle)
turtle.end_fill()
turtle.done()