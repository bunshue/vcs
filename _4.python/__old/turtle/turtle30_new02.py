import sys

print("------------------------------------------------------------")  # 60個

print("turtle 01")

import turtle

t = turtle.Pen()
t.forward(100)      # 海龜向前繪線移動100
t.left(90)          # 海龜方向左轉90度
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 02")

import turtle

t = turtle.Pen()
for x in range(1, 6):
    t.forward(100)      # 海龜向前繪線移動100
    t.left(144)         # 海龜方向左轉144度

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 03")
import turtle

t = turtle.Pen()
for x in range(1, 20):
    t.forward(100)          # 海龜向前繪線移動100
    t.right(170)            # 海龜方向右轉170度

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 04")
import turtle

t = turtle.Pen()
for x in range(1, 40):
    t.forward(200)          # 海龜向前繪線移動200
    t.right(95)             # 海龜方向右轉95度

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 05")
import turtle

t = turtle.Pen()
for x in range(1, 500):
    t.forward(x)            # 海龜向前繪線移動x
    t.right(91)             # 海龜方向右轉91度

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 06")
import turtle

t = turtle.Pen()

for x in range(1, 37):
    t.forward(100)      # 海龜向前繪線移動100
    t.left(90)          # 海龜方向左轉90度
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(100)         # 海龜方向左轉100度

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 07")
import turtle

t = turtle.Pen()
t.pensize(5)                        # 畫筆寬度
colorValue = 1.0
colorStep = colorValue / 36
for x in range(1, 37):
    colorValue -= colorStep
    t.color(0.5, 1, colorValue)     # 色彩調整
    t.forward(100)                  # 海龜向前繪線移動100
    t.left(90)                      # 海龜方向左轉90度
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(100)                     # 海龜方向左轉100度

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 08")
import turtle

t = turtle.Pen()
colorsList = ['red','orange','yellow','green','blue','cyan','purple','violet']
tWidth = 1                          # 最初畫筆寬度
for x in range(1, 41):
    t.color(colorsList[x % 8])      # 選擇畫筆顏色
    t.forward(2 + x * 5)            # 每次移動距離
    t.right(45)                     # 每次旋轉角度
    tWidth += x * 0.05              # 每次畫筆寬度遞增    
    t.width(tWidth)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 09")
import turtle

t = turtle.Pen()
t.circle(50)            # 繪製第1個左上方圓
t.circle(-50)           # 繪製第2個左下方圓
t.forward(100)
t.circle(50)            # 繪製第3個右上方圓
t.circle(-50)           # 繪製第4個右下方圓

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 10")
import turtle

t = turtle.Pen()
step = 5                # 每次增加距離
for r in range(10, 50, step):
    t.circle(r)         # 繪製圓   
    t.penup()           # 將筆提起
    t.right(90)         # 方向往下
    t.forward(step)     # 移動海龜位置起繪點
    t.right(270)        # 方向往右
    t.pendown()         # 將筆放下準備繪製

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 11")
import turtle

t = turtle.Pen()
step = 5                        # 每次增加距離
for r in range(10, 90, step):
    t.circle(r, 90 + r*2)       # 繪製圓   
    t.penup()                   # 將筆提起
    t.home()                    # 海龜回到原點(0,0)
    t.pendown()                 # 將筆放下準備繪製

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 12")
import turtle

t = turtle.Pen()
colors = ['red', 'orange', 'yellow', 'green', 'blue']
step = 10                       # 每次增加距離
twidth = 0                      # 最初寬度0
for r in range(1, 11):
    t.color(colors[r % 5])      # 選畫筆顏色
    twidth += 1                 # 每次迴圈寬度加1
    t.width(twidth)             # 設定寬度
    t.circle(r*step)            # 繪製圓   
    t.penup()                   # 將筆關閉
    t.right(90)                 # 方向往下
    t.forward(step)             # 移動海龜位置起繪點
    t.right(270)                # 方向往右
    t.pendown()                 # 將筆開啟準備繪製

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 13")
import turtle

t = turtle.Pen()
t.color('blue')
for angle in range(0, 360, 15):
    t.setheading(angle)         # 調整海龜方向
    t.circle(100)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 14")
import turtle

t = turtle.Pen()
t.circle(50)            # 繪製第1個左上方圓
t.circle(-50, steps=3)  # 繪製第2個左下方三角形
t.forward(100)
t.circle(50, steps=4)   # 繪製第3個右上方四邊形
t.circle(-50, steps=5)  # 繪製第4個右下方五邊形

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 15")
import turtle

t = turtle.Pen()
t.color('blue')
t.shape('turtle')
for angle in range(0, 361, 15):
    t.forward(100)
    t.stamp()
    t.home()
    t.seth(angle)         # 調整海龜方向

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 16")
import turtle
import time

t = turtle.Pen()
t.color('blue')
t.shape('turtle')
firstStamp = t.stamp()      # 蓋章第1隻海龜
t.forward(100)
secondStamp = t.stamp()     # 蓋章第2隻海龜
t.forward(100)
thirdStamp = t.stamp()      # 蓋章第3隻海龜
t.hideturtle()              # 隱藏目前海龜
time.sleep(5)
t.clearstamp(secondStamp)   # 刪除第2隻海龜
time.sleep(5)
t.clearstamps(None)         # 刪除所有海龜

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 17")
import turtle
import time

t = turtle.Pen()
t.color('blue')
t.shape('turtle')
t.stamp()                   # 蓋章第1隻海龜
print("目前有顯示海龜 : ", t.isvisible())
t.forward(100)
secondStamp = t.stamp()     # 蓋章第2隻海龜
time.sleep(3)
t.hideturtle()              # 隱藏目前海龜
print("目前有顯示海龜 : ", t.isvisible())
t.clearstamps(-1)           # 刪除後面1個海龜
time.sleep(3)
t.showturtle()              # 顯示海龜
print("目前有顯示海龜 : ", t.isvisible())

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 18")
import turtle
import time

t = turtle.Pen()
t.color('blue')
print(t.screen.getshapes())             # 列印海龜游標字串

for cursor in t.screen.getshapes():
    t.shape(cursor)                     # 更改海龜游標
    t.stamp()                           # 海龜游標蓋章
    t.forward(30)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 19")
import turtle

t = turtle.Pen()
t.color('blue')         # 設定輪廓顏色
t.fillcolor('yellow')   # 設定填充顏色
t.begin_fill()          # 開始填充
t.circle(50)            # 繪製左方圓
t.end_fill()            # 結束填充
t.forward(100)
t.color('red', 'aqua')  # 設定輪廓顏色是red, 填充顏色是aqua
t.begin_fill()          # 開始填充
t.circle(50)            # 繪製第2個右方圓
t.end_fill()            # 結束填充

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 20")
import turtle

t = turtle.Pen()
t.color('blue')         # 設定輪廓顏色
t.width(5)              # 輪廓寬度
t.fillcolor('yellow')   # 設定填充顏色
t.begin_fill()          # 開始填充
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()            # 結束填充

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 21")
import turtle
import time

colorsList = ['green', 'yellow', 'red']

t = turtle.Pen()
for i in range(0,3):
    t.fillcolor(colorsList[i%3])    # 更改色彩
    t.begin_fill()                  # 開始填充
    t.circle(50)                    # 繪製左方圓
    t.end_fill()                    # 結束填充
    time.sleep(3)                   # 每隔3秒執行一次迴圈

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 22")
import turtle
import time

colorsList = ['green', 'yellow', 'red']

t = turtle.Pen()
t.speed(10)                             # 加速繪製圖形
t.ht()                                  # 隱藏海龜游標
for i in range(0,3):
    t.color('white', colorsList[i%3])   # 更改色彩
    t.begin_fill()                      # 開始填充
    t.circle(50)                        # 繪製左方圓
    t.end_fill()                        # 結束填充
    time.sleep(3)                       # 每隔3秒執行一次迴圈

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 23")
import turtle

t = turtle.Pen()
t.screen.title('Python王者歸來')
t.screen.bgcolor('yellow')

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 24")
import turtle
import time

t = turtle.Pen()
width = t.screen.window_width()
height = t.screen.window_height()
print("視窗width  = ", width)
print("視窗height = ", height)
time.sleep(3)
t.screen.setup(600, 480)            # 更改視窗寬和高
width = t.screen.window_width()
height = t.screen.window_height()
print("新視窗width  = ", width)
print("新視窗height = ", height)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 25")
import turtle
import time

t = turtle.Pen()
t.screen.setworldcoordinates(0,0,800,800)
print("列印海龜位置  = ", t.pos())
t.left(45)
t.forward(300)
print("列印新海龜位置  = ", t.pos())

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 26")
import turtle

t = turtle.Pen()
t.shape('turtle')
# 繪製時鐘中間顏色
t.color('white', 'aqua')
t.setpos(0, -120)
t.begin_fill()
t.circle(120)           # 繪時鐘內圓盤
t.end_fill()
t.penup()               # 畫筆關閉
t.home()
t.pendown()             # 畫筆打開
t.color('black')
t.pensize(5)
# 繪製時鐘刻度
for i in range(1, 13):
    t.penup()           # 畫筆關閉
    t.seth(-30*i+90)    # 設定刻度的角度
    t.forward(180)
    t.pendown()         # 畫筆打開
    t.forward(30)       # 畫時間軸
    t.penup()
    t.forward(20)
    t.write(str(i), align="left") # 寫上刻度
    t.home()
# 繪製時鐘外框
t.home()
t.setpos(0, -270)
t.pendown()
t.pensize(10)
t.pencolor('blue')
t.circle(270)
# 寫上名字
t.penup()
t.setpos(0, 320)
t.pendown()
t.write('Python王者歸來', align="center", font=('新細明體', 24))
t.ht()                  # 隱藏游標

turtle.mainloop()

print("------------------------------------------------------------")  # 60個



