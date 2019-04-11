import turtle

def moveTurtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

turtle.speed(8)     #speed(速度等級, 1 ~ 10)
turtle.showturtle()

turtle.color('black')
turtle.pensize(2)

moveTurtle(-200, 0)
turtle.goto(200, 0)
turtle.goto(200, 200)
turtle.goto(-200, 200)
turtle.goto(-200, -200)
turtle.goto(200, -200)
turtle.goto(200, 0)
moveTurtle(0, 200)
turtle.goto(0, -200)

moveTurtle(0, 0)

turtle.color('blue')
turtle.pensize(6)

turtle.fillcolor("red")
turtle.begin_fill()

turtle.forward(100) #直走100步
turtle.right(90)    #右轉90度
print("目前方位", turtle.heading())
turtle.forward(50)  #直走50步
turtle.right(90)
print("目前方位", turtle.heading())
turtle.forward(100)
turtle.right(90)
print("目前方位", turtle.heading())
turtle.forward(50)
turtle.right(90)
print("目前方位", turtle.heading())
turtle.end_fill()

turtle.backward(100)


moveTurtle(-100, -100)
turtle.circle(100, 270, 10)

#turtle.clear() #清除畫布的所有內容

moveTurtle(-100, -100)
turtle.color('green')
turtle.circle(100, 270, 10)



moveTurtle(-100, 100)
turtle.dot(100, 'yellow')    #畫一個實心圓圈 (直徑, 顏色)


import time

time.sleep(1)


import time
angle = 0;
while angle < 180:
    angle += 10;
    turtle.setheading(angle)
    time.sleep(0.2)




#turtle.hideturtle()





turtle.done()       #最後用

