"""
基本的 turtle 使用


"""

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

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


"""
新進暫存



t.hideturtle()	隱藏海歸以免遮蔽
t.home() 回原點
t.left(65) 試左轉65度

互補的指令
t.left()	t.right()
t.forwared()	t.backward




print("------------------------------------------------------------")  # 60個


import turtle  #載入turtle模組
wd = turtle.Screen()  #建立名為wd的screen實體
pen = turtle.Turtle()    # 建立一個名為tu的海龜turtle實體
pen.forward(50)   #tu往前50pixels
pen.right(90)  #tu往右轉90度
pen.forward(150)   #tu往前150pixels
wd.exitonclick()      #在視窗任一位置按下滑鼠左鍵關閉視窗

print("------------------------------------------------------------")  # 60個



import turtle   

wd = turtle.Screen()  #建立turtle screen實體
wd.setup(width=.5, height=200) #視窗大小與位置
wd.title("turtle繪圖真有趣，簡單又易學")
tu = turtle.Turtle()    # 建立海龜turtle實體
tu.color('green')
tu.pensize(5)
tu.penup()
tu.setx(-100)
tu.pendown()
for x in range(10):
	tu.circle(30)
	tu.right(360/10)

tu2 = turtle.Turtle()    # 建立第二個海龜名為tu2
tu2.color('#FF00FF', '#55CCBB')
tu2.penup() 
tu2.goto(120,-120)
tu2.pendown()
tu2.begin_fill()
for x in range(10):
	tu2.forward(100)
	tu2.left(720/5)
tu2.end_fill()  

wd.exitonclick()
turtle.done()

print("------------------------------------------------------------")  # 60個

import turtle   

wd = turtle.Screen()  #建立turtle screen實體
wd.setup(width=.3, height=200, startx=None, starty=None) #視窗大小與位置
wd.bgcolor("green")  #設定底色
pen = turtle.Turtle()    # 建立一個海龜turtle實體
pen.shape("arrow")     #海龜樣式
pen.color("yellow","#ff00ff")  #海龜線條顏色與填色顏色
pen.pensize(10)   #線條寬度
pen.speed(3)     #海龜繪圖速度
pen.forward(50)   
pen.right(90) 
pen.forward(50)
pen.right(90)
pen.forward(50)
wd.exitonclick()      
turtle.done() #結束tutle繪圖

print("------------------------------------------------------------")  # 60個

















"""


