"""

基本的 turtle 使用


"""


import sys
import time
import random

import turtle

"""
turtle模組方法

移動海龜
turtle.forward(x)	從目前方向向前走x步
turtle.forwared()
turtle.back(x)		從目前方向向後走x步
turtle.backward()
turtle.backward(50)  # 畫筆向後
turtle.home()  # 畫筆回到原點
turtle.forward(50)  # 畫筆前進
turtle.goto(50, 50)  # 畫筆移到座標(50, 50)
turtle.setx(x_st)
turtle.sety(y_st)
turtle.left(x)		從目前方向逆時針轉x度
turtle.right(x)		從目前方向順時針轉x度

方法   簡寫

簡寫   全名
fd     forward
rt     right        # 順時針轉N度
lt     left         # 逆時針轉N度
pu     penup        # 提筆
pd     pendown      # 下筆
ht     hideturtle   # 隱藏海龜
       showturtle   # 顯示海龜

"""

turtle.speed(0)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print('turtle測試 setheading() stamp()')

# 設定海龜方向 0 : 正右, 90 : 正上, 180 : 正左, 270 : 正下

turtle.color("black")
turtle.pensize(2)  # 設定畫筆大小
turtle.fillcolor("red")

turtle.shape("turtle")
for angle in range(0, 360, 45):
    turtle.home()  # 畫筆回到原點
    #turtle.seth(angle)  # 設定海龜方向 same
    turtle.setheading(angle)  # 設定海龜方向
    turtle.forward(200)
    turtle.stamp()  # 留下箭頭印記
    print("目前方位 :", turtle.heading())
    print("目前位置 :", turtle.pos())
    print("距離原點 :", abs(turtle.pos()))

#turtle.clear() #清除畫布的所有內容

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print('turtle測試 提筆下筆 移動座標')

turtle.up()  # 提筆
turtle.penup()  # 提筆

#移動
turtle.goto(100, 100)  # 前進指定座標
turtle.setpos(50, -50)
turtle.home()  # 畫筆回到原點
x_st, y_st = -200, -200
x_sp, y_sp = 200, 200
turtle.goto(x_st, y_st)
turtle.goto(x_sp, y_sp)

turtle.down()  # 下筆
turtle.pendown()  # 下筆

print('turtle測試 設定畫筆')
turtle.pencolor("Yellow")
turtle.pensize(10)  # 設定畫筆大小

turtle.color("red")  # 線色
turtle.pencolor("blue")
turtle.pensize(10)  # 設定畫筆大小

turtle.setpos(0, 0)

print("------------------------------------------------------------")  # 60個

turtle.width(5)  # 輪廓寬度

turtle.fillcolor("yellow")  # 設定填充顏色
turtle.fillcolor()  # 指定塗滿的色彩
turtle.color("Blue", "Gold")  # 畫筆為Blue, 塗滿為Gold

#turtle.fillcolor(colorsList[i % 3])  # 更改色彩
#turtle.color("white", colorsList[i % 3])  # 更改色彩

print('turtle測試 塗色範例')

turtle.fillcolor("red")
turtle.begin_fill()  # 開始塗色

turtle.circle(100)  #逆時針空心圓

turtle.end_fill()  # 結束塗色

turtle.mainloop()

#範例
turtle.color("red", "aqua")  # 設定輪廓顏色是red, 填充顏色是aqua

turtle.begin_fill()  # 開始塗色
turtle.circle(50)  # 繪製第2個右方圓
turtle.end_fill()  # 結束塗色

print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
t.screen.title("歡迎來到美國")
t.screen.bgcolor("green")  #設定底色
t.screen.setup(640, 480)  # 更改視窗寬和高
width = t.screen.window_width()
height = t.screen.window_height()
print("視窗width  = ", width)
print("視窗height = ", height)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

t = turtle.Pen()
t.screen.setworldcoordinates(0, 0, 800, 800)
print("列印海龜位置  = ", t.pos())
#print("目前位置 :", turtle.pos())
#print("距離原點 :", abs(turtle.pos()))
t.left(45)
t.forward(400*1.4143)
print("列印新海龜位置  = ", t.pos())
#print("目前位置 :", turtle.pos())
#print("距離原點 :", abs(turtle.pos()))

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

wd = turtle.Screen()  #建立turtle screen實體
wd.setup(width=.5, height=200) #視窗大小與位置
wd.title("turtle繪圖真有趣，簡單又易學")

print("------------------------------------------------------------")  # 60個

print(turtle.getshapes())  # 列印海龜游標字串

for cursor in turtle.getshapes():
    turtle.shape(cursor)  # 更改海龜游標
    turtle.stamp()  # 海龜游標蓋章
    turtle.forward(30)

print("------------------------------------------------------------")  # 60個
print("1. turtle 基本設定")
print("------------------------------------------------------------")  # 60個

print('turtle測試 畫布設定')

turtle.setup(800, 800)  # 產生 800 X 800 畫布

W = 800
H = 800
x_st = 1000
y_st = 20
turtle.setup(W, H, x_st, y_st)  # 指定畫布的大小與位置

print("------------------------------------------------------------")  # 60個

turtle.bgcolor("black")
turtle.bgcolor("#708090")  # 背景為深灰色 RGB(190, 190, 190)
turtle.bgcolor("Skyblue")  # 設定背景色
turtle.bgcolor("Gray21")  # 背景為深灰
turtle.bgcolor("#363636")  # 設背景為深灰
turtle.bgcolor("#BEBEBE")  # 背景為灰色 RGB(190, 190, 190)

turtle.pensize(10)  # 設定畫筆大小

#線色 方法1
turtle.pencolor("Red")

#線色 方法2
#turtle.pencolor("#FF0000")  # 設畫筆為紅色

#線色 方法3
#turtle.colormode(255)  # 變更色彩以數值表示
#turtle.pencolor(255, 0, 0)  # 設定畫筆顏色

turtle.mainloop()

show = turtle.Turtle()  # 建立畫布物件
show.pencolor("Yellow")  # 畫筆為黃色

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

show = turtle.Turtle()  # 建立畫布物件
show.color("Blue", "Gold")  # 設畫筆為藍色，塗滿金黃色
show.penup()  # 提筆
show.goto(-50, 50)  # 前往指定位置

turtle.mainloop()

print("------------------------------------------------------------")  # 60個
print("2. turtle 簡易畫圖")
print("------------------------------------------------------------")  # 60個

turtle.penup()  # 提筆
turtle.goto(-300, 300)
turtle.pendown()  # 下筆

print("畫點")
turtle.dot(100, "yellow")  # 畫一個實心圓圈 (直徑, 顏色)
turtle.dot(50, "Red")
turtle.dot(30, "green")
turtle.dot(10, 'green')

print("畫字")

turtle.right(90)  # 順時針轉N度
turtle.forward(50)
turtle.write("abcde12345", font=("Helvetica", 12, "normal"))

turtle.forward(50)
turtle.write("Welcome to the United States", font = ("Times", 18, "bold"))

turtle.forward(50)
turtle.write("顯示Unicode", font=("微軟正黑體", 40))

turtle.forward(50)
turtle.write("\u6B22\u8FCE \u03b1 \u03b2 \u03b3")

turtle.forward(50)
turtle.write("AAAAAAAAAAAAAAAAAAAAAAA") 

turtle.forward(50)
turtle.write("歡迎來到美國", align="center", font=("新細明體", 24))

turtle.forward(50)
turtle.left(90)
for s in range(30):
    turtle.write("A", font = ('Arial', int(s + 1)))
    turtle.forward(25)

turtle.done()

turtle.mainloop()    # 開始主事件的循環

print("------------------------------------------------------------")  # 60個

print('turtle測試 畫圓')

R = 50

turtle.penup()  # 提筆
turtle.goto(-350, 200)
turtle.pendown()  # 下筆

turtle.circle(R)  #逆時針空心圓
turtle.circle(-R, steps=3)  # 順時針空心 正三角形
turtle.forward(100)
turtle.circle(R, steps=4)  # 逆時針空心 正四角形
turtle.circle(-R, steps=5)  # 順時針空心 正五角形
turtle.forward(100)
turtle.circle(R, 360, 6)  # 空心正六邊形
turtle.circle(-R, steps=6)  # 空心正六邊形
turtle.forward(100)

# 空心圓半徑 R, 內接N邊形
N = 5
turtle.circle(R, 360, N)  # 正N邊形
turtle.circle(-R, 235)  # 畫圓弧 235度

turtle.penup()  # 提筆
turtle.goto(100, 200)
turtle.pendown()  # 下筆

print('畫實心內接多邊形')

turtle.setheading(0)  # 設定海龜方向

# 畫中央實心三角形
turtle.color("red")
turtle.begin_fill()  # 開始塗色
turtle.circle(R, 360, 3)
turtle.end_fill()  # 結束塗色

turtle.forward(100)

turtle.color("red")
turtle.pensize(5)  # 設定畫筆大小

turtle.color("red")
turtle.begin_fill()  # 開始塗色
turtle.circle(R, steps=3)
turtle.end_fill()  # 結束塗色

turtle.forward(100)

turtle.color("green")
turtle.begin_fill()  # 開始塗色
turtle.circle(R, 360, 6)
turtle.end_fill()  # 結束塗色

turtle.forward(100)

turtle.color("red")
turtle.begin_fill()  # 開始塗色
#turtle.circle(R, steps = 3)
#turtle.circle(R, steps = 4)
turtle.circle(R, steps = 5)
#turtle.circle(R, steps = 6)
turtle.end_fill()  # 結束塗色

# 和畫圓做比較
#分90步
for i in range(90):
    turtle.forward(5) # 每步步長
    turtle.left(4)#每步左轉4度

#畫圓

def drawCircle(x, y, radius): 
    turtle.penup()  # 提筆
    turtle.goto(x, y - radius)
    turtle.pendown()  # 下筆
    turtle.circle(radius)

cx, cy, R = 0, 0, 50
drawCircle(cx, cy, R)

cx, cy, R = 100, 0, 50
drawCircle(cx, cy, R)

#畫圓
x1, y1 = 0, 0
radius = 150
turtle.penup()  # 提筆
turtle.goto(x1, y1 - radius)
turtle.pendown()  # 下筆

turtle.circle(radius)

turtle.done() 

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

turtle.color("red", "yellow")  # 前 : 線色, 字色, 後 : 標記色

turtle.begin_fill()  # 開始塗色
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()  # 結束塗色
turtle.done()

print("------------------------------------------------------------")  # 60個

wd = turtle.Screen()  #建立turtle screen實體
wd.setup(width=.5, height=200) #視窗大小與位置
wd.title("turtle繪圖真有趣，簡單又易學")

tu = turtle.Turtle()    # 建立海龜turtle實體
tu.color('green')
tu.pensize(5)  # 設定畫筆大小
tu.penup()  # 提筆
tu.setx(-100)
tu.pendown()  # 下筆
for x in range(10):
	tu.circle(30)
	tu.right(360/10)

tu2 = turtle.Turtle()    # 建立第二個海龜名為tu2
tu2.color('#FF00FF', '#55CCBB')
tu2.penup()   # 提筆
tu2.goto(120,-120)
tu2.pendown()  # 下筆
tu2.begin_fill()  # 開始塗色
for x in range(10):
	tu2.forward(100)
	tu2.left(720/5)
tu2.end_fill()  # 結束塗色

wd.exitonclick()#在視窗任一位置按下滑鼠左鍵關閉視窗
turtle.done()

print("------------------------------------------------------------")  # 60個

wd = turtle.Screen()  #建立turtle screen實體
wd.setup(width=.3, height=200, startx=None, starty=None) #視窗大小與位置
wd.bgcolor("green")  #設定底色

turtle.shape("arrow")     #海龜樣式
turtle.color("yellow","#ff00ff")  #海龜線條顏色與填色顏色
turtle.pensize(10)  # 設定畫筆大小
turtle.forward(50)   
turtle.right(90) 
turtle.forward(50)
turtle.right(90)
turtle.forward(50)

wd.exitonclick()  # 在視窗任一位置按下滑鼠左鍵關閉視窗
turtle.done() #結束tutle繪圖

print("------------------------------------------------------------")  # 60個

# Draw chess board borders
turtle.pensize(3)  # 設定畫筆大小
turtle.penup()  # 提筆
turtle.goto(-120, -120)
turtle.pendown()  # 下筆
turtle.color("red")

for i in range(4):
    turtle.forward(240) # Draw a line
    turtle.left(90) # Turn left 90 degrees

# Draw chess board inside
turtle.color("black")
for j in range(-120, 90, 60): 
    for i in range(-120, 120, 60):
        turtle.penup()  # 提筆
        turtle.goto(i, j)
        turtle.pendown()  # 下筆

       # Draw a small rectangle        
        turtle.begin_fill()  # 開始塗色
        for k in range(4):
            turtle.forward(30) # Draw a line
            turtle.left(90) # Turn left 90 degrees
        turtle.end_fill()  # 結束塗色

for j in range(-90, 120, 60): 
    for i in range(-90, 120, 60):
        turtle.penup()  # 提筆
        turtle.goto(i, j)
        turtle.pendown()  # 下筆

       # Draw a small rectangle        
        turtle.begin_fill()  # 開始塗色
        for k in range(4):
            turtle.forward(30) # Draw a line
            turtle.left(90) # Turn left 90 degrees
        turtle.end_fill()  # 結束塗色

turtle.hideturtle()  # 隱藏海龜

turtle.done() 

print("------------------------------------------------------------")  # 60個

# RandomWalk.py

from random import randint

# Draw 16 by 16 lattices
turtle.color("gray") # Color for lattice
x = -80 
for y in range(-80, 80 + 1, 10):
    turtle.penup()  # 提筆
    turtle.goto(x, y) # Draw a horizontal line
    turtle.pendown()  # 下筆
    turtle.forward(160)

y = 80
turtle.right(90)
for x in range(-80, 80 + 1, 10):
    turtle.penup()  # 提筆
    turtle.goto(x, y) # Draw a vertical line
    turtle.pendown()  # 下筆
    turtle.forward(160)
    
turtle.pensize(3)  # 設定畫筆大小
turtle.color("red")

turtle.penup()  # 提筆
turtle.goto(0, 0) # Go to the center
turtle.pendown()  # 下筆

x = y = 0 # Current pen location at the center of lattice
while abs(x) < 80 and abs(y) < 80:    
    r = randint(0, 3)
    if r == 0:
        x += 10  # Walk east
        turtle.setheading(0)  # 設定海龜方向
        turtle.forward(10)      
    elif r == 1:
        y -= 10 # Walk south
        turtle.setheading(270)  # 設定海龜方向
        turtle.forward(10)      
    elif r == 2:
        x -= 10 # Walk west
        turtle.setheading(180)  # 設定海龜方向
        turtle.forward(10)      
    elif r == 3:
        y += 10 # Walk north
        turtle.setheading(90)  # 設定海龜方向
        turtle.forward(10)      

turtle.done() 

print("------------------------------------------------------------")  # 60個

colorValue = 1.0
colorStep = colorValue / 36
for x in range(1, 37):
    colorValue -= colorStep
    print(colorValue)
    turtle.color(0.5, 1, colorValue)  # 色彩調整
    turtle.circle(20+x*2)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

turtle.color("black")
turtle.pensize = 10

for x in range(0, 360, 30):
    print(x)
    turtle.goto(x/30 * 25, x/30 * 25)
    turtle.dot(20, "green")
    #turtle.forward(25)

print("------------------------------------------------------------")  # 60個

print('turtle測試 .home .goto .setpos')

print('比較 .home .goto .setpos, 看起來 .goto與.setpos一樣')

turtle.home()  # 畫筆回到原點
turtle.goto(-300, 300)  # 前進指定座標

turtle.home()  # 畫筆回到原點
turtle.goto(300, 300)  # 前進指定座標

turtle.reset()  # 清空畫布

turtle.home()  # 畫筆回到原點
turtle.setpos(-300, -300)

turtle.home()  # 畫筆回到原點
turtle.setpos(300, -300)

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


for _ in range(5):
    # 預設畫筆形狀 為 小箭頭
    turtle.forward(30)
    turtle.stamp()

for _ in range(5):
    turtle.shape("turtle")  # 設畫筆形狀 為 海龜
    turtle.color("yellow","#ff00ff")  #海龜線條顏色與填色顏色
    turtle.forward(30)
    turtle.stamp()

for _ in range(5):
    turtle.shape("arrow")  # 設畫筆形狀 為 大箭頭
    turtle.forward(30)
    turtle.stamp()


turtle.shape("turtle")  # 設畫筆形狀是海龜

print('蓋章 海龜1')
firstStamp = turtle.stamp()  # 蓋章第1隻海龜

turtle.forward(100)

print('蓋章 海龜2')
secondStamp = turtle.stamp()  # 蓋章第2隻海龜
turtle.forward(100)

print('蓋章 海龜3')
thirdStamp = turtle.stamp()  # 蓋章第3隻海龜

time.sleep(0.5)
print('刪除 海龜2')
turtle.clearstamp(secondStamp)  # 刪除第2隻海龜

time.sleep(0.5)
print('刪除 所有海龜')
turtle.clearstamps(None)  # 刪除所有海龜

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

turtle.shape("turtle")
turtle.stamp()  # 蓋章第1隻海龜
print("目前有顯示海龜 : ", turtle.isvisible())
turtle.forward(100)

secondStamp = turtle.stamp()  # 蓋章第2隻海龜
time.sleep(0.5)
print("目前有顯示海龜 : ", turtle.isvisible())
turtle.clearstamps(-1)  # 刪除後面1個海龜
time.sleep(0.5)
print("目前有顯示海龜 : ", turtle.isvisible())

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

tines = ["Red", "Yellow", "Orange", "Purple", "Cyan", "Pink", "LightGreen", "Bisque"]
# 方法choice()讓畫筆色彩隨機變
turtle.pencolor(random.choice(tines))

# 視窗寬度
w1 = -turtle.window_width() // 2
# 視窗高度
h1 = -turtle.window_height() // 2

turtle.pencolor("blue")

tu = turtle.Turtle()    # 建立海龜turtle實體
tu.color('green')

tu.penup()  # 提筆
tu.setx(-100)
tu.pendown()  # 下筆

tu2 = turtle.Turtle()    # 建立第二個海龜名為tu2
tu2.color('#FF00FF', '#55CCBB')
tu2.penup()  # 提筆
tu2.goto(120,-120)
tu2.pendown()  # 下筆

turtle.done()

print("------------------------------------------------------------")  # 60個
print('turtle測試 視窗相關 鍵鼠控制')
print("------------------------------------------------------------")  # 60個

print('在視窗任一位置按下滑鼠左鍵關閉視窗')
turtle.exitonclick()  #在視窗任一位置按下滑鼠左鍵關閉視窗

print("------------------------------------------------------------")  # 60個

print("取得滑鼠座標")

def drawPoint(x, y):
    print("滑鼠座標 :(", x, y, ")")
    turtle.goto(x, y)
    turtle.dot(50, "Red")

t = turtle.Pen()
t.screen.onclick(drawPoint)
t.screen.mainloop()

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

# HandleMouseClick

def drawPoint(x, y):
    print("滑鼠座標 :(", x, y, ")")
    turtle.goto(x, y)
    turtle.dot(50, "Red")

def drawPoint2(x, y):
    turtle.circle(30)

# Bind handlers with the mouse-click event
t = turtle.Pen()
t.screen.onclick(drawPoint)
t.screen.onclick(drawPoint2, add = True) # 附加另一個事件
 
turtle.done() 

print("------------------------------------------------------------")  # 60個


def fxn1(x,y):
    print('滑鼠按下')
    turtle.fillcolor("red") 

def fxn2(x,y):
    print('滑鼠放開')
    turtle.fillcolor("black") 
      
# set screen and turtle 
sc=turtle.Screen() 
sc.setup(400,300) 
  
turtle.shape("turtle") 
turtle.turtlesize(2) 
  
# 滑鼠按下事件
turtle.onclick(fxn1) 

# 滑鼠放開事件  
turtle.onrelease(fxn2)

print("------------------------------------------------------------")  # 60個

# HandleMouseRelease.py

def displaySqaure(x, y):
    turtle.penup()  # 提筆
    turtle.goto(x - 100, y - 100)
    turtle.pendown()  # 下筆
    turtle.begin_fill()  # 開始塗色
    turtle.circle(50)
    turtle.end_fill()  # 結束塗色

# Bind a handler with the mouse-release event
turtle.onrelease(displaySqaure)
turtle.done() 

print("------------------------------------------------------------")  # 60個

def keyRight():
    turtle.setheading(0)  # 設定海龜方向
    turtle.forward(50)


def keyUp():
    turtle.setheading(90)  # 設定海龜方向
    turtle.forward(50)


def keyLeft():
    turtle.setheading(180)  # 設定海龜方向
    turtle.forward(50)


def keyDown():
    turtle.setheading(270)  # 設定海龜方向
    turtle.forward(50)


t = turtle.Pen()
t.screen.onkey(keyRight, "Right")
t.screen.onkey(keyUp, "Up")
t.screen.onkey(keyLeft, "Left")
t.screen.onkey(keyDown, "Down")
t.screen.listen()
t.screen.mainloop()

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

wk = turtle.textinput(f'一週七天，按0離開',
                      '請輸入星期前三個字母：')

if wk==None:
    print('你按了取消')
else:
    print('輸入資料 :', wk)

print("------------------------------------------------------------")  # 60個

# 自動選擇顏色
colorsList = ["red", "orange", "yellow", "green", "blue", "cyan", "purple", "violet"]
r = 30  # 半徑
for i in range(30):
    turtle.color(colorsList[i % len(colorsList)])  # 選擇畫筆顏色
    #turtle.circle(r+i)
    turtle.circle(50+i, steps = i+1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print('turtle測試 .circle 空心圓')

r = 30  # 半徑
turtle.penup()  # 提筆

for edge in range(3, 13, 1):  # 繪3 - 12邊圖
    turtle.pendown()  # 下筆
    turtle.circle(r, steps=edge)
    turtle.penup()  # 提筆
    turtle.forward(60)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print('turtle測試 .circle 實心圓')

turtle.color("white")
r = 30  # 半徑
turtle.penup()  # 提筆
colorsList = ["red", "orange", "yellow", "green", "blue", "cyan", "purple", "violet"]
for edge in range(3, 13, 1):  # 繪3 - 12邊圖
    turtle.pendown()  # 下筆
    turtle.fillcolor(colorsList[edge % 8])
    turtle.begin_fill()  # 開始塗色
    turtle.circle(r, steps=edge)
    turtle.end_fill()  # 結束塗色
    turtle.penup()  # 提筆
    turtle.forward(60)

print("------------------------------------------------------------")  # 60個






print("------------------------------------------------------------")  # 60個
print("零散的")  # 60個
print("------------------------------------------------------------")  # 60個


turtle.ondrag(turtle.goto)

turtle.home()  # 畫筆回到原點

turtle.undo()



t = turtle.Pen()
t.screen.bgcolor("blue")
t.hideturtle()  # 隱藏海龜


""" 新進
turtle.bk(30)
turtle.bk(30)
turtle.bk(4)
turtle.Screen().reset()

"""

#似乎都要用以下這個當結尾，關閉後，才不會有error
turtle.mainloop()

turtle.colormode(255)  # 色彩以數值表示
show = turtle.Turtle()  # 建立畫布物件
show.pensize(10)  # 設定畫筆大小

show.color((255, 0, 255), (255, 215, 0))  # 設畫筆為洋紅色，塗滿金黃色

show.penup()  # 提筆
show.goto(-50, 50)  # 前往指定位置

turtle.mainloop()



"""
turtle.speed(N)  #設定畫筆移動速度 1~10
0  最快
1  最慢
6  正常
10 快

"""

turtle.color("red", "yellow")

turtle.hideturtle()  # 隱藏海龜
turtle.hide()
turtle.showturtle()  # 顯示海龜



colors = ['Magenta', 'Gold', 'Cyan', 'PaleGreen',
          'LemonChiffon', 'Orange', 'Pink']   # List

turtle.pencolor(colors [item % len(weeks)]) # 依餘數取色彩值

turtle.color((1.0, 0, 1.0), (1.0, 0.84, 0.0))  # 設畫筆為洋紅色，塗滿金黃色


# 使用screen視窗, 滑鼠點擊退出視窗
screen = turtle.Screen()

screen.setup(500, 400)
screen.setup(500, 400, startx=20, starty=50)
screen.setup(width=.5, height=200) #視窗大小與位置
screen.setup(width=.3, height=200, startx=None, starty=None) #視窗大小與位置

screen.exitonclick()#在視窗任一位置按下滑鼠左鍵關閉視窗

# ----------------------------------------

time.sleep(1)
time.sleep(0.2)

turtle.home()  # 畫筆回到原點

colors = ["red", "orange", "yellow", "green", "blue"]
turtle.color(colors[r % 5])  # 選畫筆顏色
turtle.width(twidth)  # 設定寬度

print("------------------------------------------------------------")  # 60個

turtle.home()  # 畫筆回到原點

show = turtle.Turtle()  # 建立畫布物件
show.pencolor("Yellow")  # 畫筆為黃色
show.pensize(10)  # 設定畫筆大小

turtle.mainloop()  # 開始主事件的循環

show = turtle.Turtle()  # 建立畫布物件
show.pencolor("Red")  # 畫筆為紅色
show.pensize(2)  # 設定畫筆大小

print("------------------------------------------------------------")  # 60個

turtle.forward(50)  # 前進=fd  vs backward後退

turtle.pensize(width=5)  # 設定畫筆大小
turtle.width(width=5)  # 同上
turtle.setpos(-200, 0)

turtle.done()  # 最後用





#6種
arrow, turtle, circle, square, triangle, classic(預設)
w = W / 3
h = H / 3
turtle.goto(w, 0)
turtle.goto(w, h)
turtle.goto(-w, h)
turtle.goto(-w, -h)
turtle.goto(w, -h)
turtle.home()  # 畫筆回到原點

#畫筆上色
#turtle.color(colorstring)
turtle.color((r,g,b))   #浮點數
turtle.color(r,g,b)     #16進制表示
turtle.color('#FF0000') #紅色

turtle.done() #結束tutle繪圖

turtle.reset()  # 清空畫布



turtle.color("red", "yellow")
turtle.begin_fill()  # 開始塗色
# draw
turtle.end_fill()  # 結束塗色

turtle.bgcolor("#87CEEB")

turtle.pensize(10)  # 設定畫筆大小

turtle.penup()  # 提筆

turtle.setposition(x, y)

turtle.pendown()  # 下筆


# 量測時間

import time

start_time = time.perf_counter()

R = 200
turtle.circle(R)  #逆時針空心圓

end_time = time.perf_counter()

print("經過時間 :", end_time - start_time, "秒")

#取平均
#times 是 list
import statistics
line_ave = statistics.mean(times)


