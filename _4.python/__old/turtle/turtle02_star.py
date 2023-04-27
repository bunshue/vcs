import turtle

def moveTurtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def drawStar(length):       #畫星形
    turtle.right(108)       #右轉 ? 度
    turtle.forward(length)  #直走length步
    turtle.left(144)    #右轉 ? 度
    turtle.forward(length)  #直走length步
    turtle.left(144)    #右轉 ? 度
    turtle.forward(length)  #直走length步
    turtle.left(144)    #右轉 ? 度
    turtle.forward(length)  #直走length步
    turtle.left(144)    #右轉 ? 度
    turtle.forward(length)  #直走length步

def drawStar2(length):       #畫星形
    turtle.right(108)       #右轉 ? 度
    drawDashline(length)
    turtle.left(144)    #右轉 ? 度
    drawDashline(length)
    turtle.left(144)    #右轉 ? 度
    drawDashline(length)
    turtle.left(144)    #右轉 ? 度
    drawDashline(length)
    turtle.left(144)    #右轉 ? 度
    drawDashline(length)

def drawDashline(length):       #畫dashline
    length2 = length / 9
    turtle.forward(length2)
    turtle.penup()
    turtle.forward(length2)
    turtle.pendown()
    turtle.forward(length2)
    turtle.penup()
    turtle.forward(length2)
    turtle.pendown()
    turtle.forward(length2)
    turtle.penup()
    turtle.forward(length2)
    turtle.pendown()
    turtle.forward(length2)
    turtle.penup()
    turtle.forward(length2)
    turtle.pendown()
    turtle.forward(length2)
   
    

moveTurtle(0, 0)

turtle.fillcolor('red')
turtle.begin_fill()

turtle.hideturtle()
turtle.pensize(5)
turtle.color('blue')
#drawStar(200)

turtle.end_fill()

moveTurtle(100, 100)
turtle.circle(20, 360, 10)
turtle.dot(10, 'green')

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.goto(100, 100)
turtle.goto(200, 0)
turtle.penup()

turtle.done()       #最後用

print("done")
