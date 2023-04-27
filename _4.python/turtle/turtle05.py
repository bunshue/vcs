import turtle

def drawShape(sides, length):   #畫多邊形
    angle = 360.0 / sides
    for side in range(sides):
        turtle.forward(length)
        turtle.right(angle)

def moveTurtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def drawSquare(length):         #畫正方形
    drawShape(4, length)


def drawTriangle(length):       #畫三角形
    drawShape(3, length)

def drawCircle(length):         #畫圓形
    drawShape(360, length)


turtle.forward(100) #直走100步
turtle.right(90)    #右轉90度
turtle.forward(50)  #直走50步
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)


repeats = 0
while repeats < 360:   #走一步轉一度
    turtle.forward(1)
    turtle.right(1)
    repeats = repeats + 1
    

length = 0
angle = 90
while length < 200:
    turtle.forward(length)
    turtle.left(angle)
    length = length + 10
    

#sides = int(input("Enter the number of sides for your shape: "))
#畫八邊形
sides = 8
angle = 360.0 / sides
length = 400.0 / sides

for side in range(sides):
    turtle.forward(length)
    turtle.right(angle)
#turtle.done()      #最後再用
    

moveTurtle(160, 0)

#畫實心八邊形
sides = 8
angle = 360.0 / sides
length = 400.0 / sides

turtle.fillcolor("red")
turtle.begin_fill()

for side in range(sides):
    turtle.forward(length)
    turtle.right(angle)
turtle.end_fill()

#turtle.done()      #最後再用
    

drawShape(4, 10)
moveTurtle(60, 30)
drawShape(3, 20)

drawShape(4, 10)

drawSquare(30)
drawCircle(1)
drawCircle(2)
drawTriangle(60)

turtle.done()       #最後用

