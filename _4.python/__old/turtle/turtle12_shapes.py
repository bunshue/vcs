import turtle

#sides = int(input("Enter the number of sides for your shape: "))

print('正N邊形')

N = 6


angle = 360.0 / N
length = 400.0 / N

for side in range(N):
    turtle.forward(length)
    turtle.right(angle)

turtle.done()


import turtle

#sides = int(input("Enter the number of sides for your shape: "))
print('正N邊形')

N = 6

angle = 360.0 / N
length = 400.0 / N

turtle.fillcolor("blue")
turtle.begin_fill()

for side in range(N):
    turtle.forward(length)
    turtle.right(angle)
turtle.end_fill()
turtle.done()

