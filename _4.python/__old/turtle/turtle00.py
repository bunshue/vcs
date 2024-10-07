"""
基本的 turtle 使用



"""

import turtle

"""
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
"""

turtle.Turtle()
W = 640
H = 480
x_st = 200
y_st = 200
turtle.setup(W,H,x_st,y_st) #指定畫布的大小與位置
turtle.bgcolor('Skyblue')   #設定背景色

turtle.shape('turtle')  #設定畫筆形狀, 預設為箭頭
"""
6種
arrow, turtle, circle, square, triangle, classic(預設)

"""

"""
w = W / 3
h = H / 3
turtle.goto(w, 0)
turtle.goto(w, h)
turtle.goto(-w, h)
turtle.goto(-w, -h)
turtle.goto(w, -h)
turtle.home()   #畫筆回到原點
"""

'''
turtle.forward(50)#前進=fd  vs backward後退
turtle.left(90)#左轉
turtle.forward(50)
turtle.right(90)#右轉
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

turtle.penup()#舉起畫筆 不畫 = pu
turtle.pendown()#放下畫筆 畫 = pd

turtle.pensize(width = 5)#設定畫筆大小
turtle.width(width =5)#同上

"""
turtle.speed()  #設定畫筆移動速度
fastest  0  最快
fast     10 快
normal   6 正常
slow     3 慢
slowest  1 最慢

"""

"""
#畫筆上色
#turtle.color(colorstring)
turtle.color((r,g,b))   #浮點數
turtle.color(r,g,b)     #16進制表示
turtle.color('#FF0000') #紅色
"""

#塗上顏色
turtle.begin_fill()    #開始塗色
turtle.end_fill()    #結束塗色
turtle.fillcolor()#指定塗滿的色彩
turtle.color('Blue', 'Gold')#畫筆為Blue, 塗滿為Gold

turtle.penup()
turtle.home()   #畫筆回到原點

turtle.begin_fill()    #開始塗色
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.end_fill()    #結束塗色
'''

print('畫點')
turtle.dot(50, 'Ivory')


print('畫圓, 圓心在turtle的左邊 ??')
r = 100
turtle.circle(r) # r 正值, 逆時針畫圓

r = -100
turtle.circle(r)# r 負值, 順時針畫圓

r = 75
turtle.circle(r, 235) # 畫圓弧 235度

r = 50
N = 5
turtle.circle(r, 360, N) # 正N邊形



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


