import sys

print("------------------------------------------------------------")  # 60個

"""
print("turtle 01")
import turtle

turtle.pensize(3)
turtle.penup()
turtle.goto(-180, 150)
turtle.pencolor('red')
turtle.fillcolor('yellow')
turtle.pendown()
turtle.begin_fill()
for _ in range(36):
    turtle.forward(200)
    turtle.right(170)
turtle.end_fill()
turtle.mainloop()
"""

print("------------------------------------------------------------")  # 60個

print("turtle 02")
import turtle

turtle.setup(200, 200) # 產生200 X 200畫布

turtle.goto(50, 50)    # 移動畫筆到指定的x、y座標
turtle.goto(50, -50)
turtle.goto(-50, 50)
turtle.goto(-50, -50)

turtle.home()          # 回到原點(x = 0, y = 0)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 03")
import turtle

turtle.setup(200, 200) # 產生200200畫布

turtle.forward(50)     # 畫筆前進
turtle.goto(50, 50)    # 畫筆移到座標(50, 50)
turtle.backward(50)    # 畫筆向後
turtle.home()          # 畫筆回到原點

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 04")
import turtle

turtle.setup(250, 200) # 產生200 X 200畫布
pen = turtle.Turtle()  # 建立畫布物件
pen.penup()            # 畫筆懸空
pen.goto(-50, 50)      # 移向指定座標
pen.pendown()          # 落下畫筆
pen.forward(100)       # 前進100像素
pen.right(90)          # 畫筆右轉90度
pen.fd(100)            # forward()方法簡寫
pen.right(135)
pen.fd(140)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 05")
import turtle

turtle.setup(250, 200)       # 產生250 X 200畫布
turtle.bgcolor('SkyBlue')    # 背景為天空藍

show = turtle.Turtle()       # 建立畫布物件
turtle.colormode(255)        # 變更色彩以數值表示
show.pencolor(255, 255, 255) # 畫筆為白色
show.pensize(10)             # 畫筆大小
show.speed(1)                # 畫筆速度為慢

show.penup()                 # 畫筆懸空
show.goto(-50, 50)           # 移向指定座標

show.pendown()               # 落下畫筆
show.forward(100)            # 前進100像素
show.right(90)               # 畫筆右轉90度
show.fd(100)                 # forward()方法簡寫
show.right(135)
show.fd(140)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 06")
import turtle

turtle.setup(250, 250) # 產生250 X 250畫布
turtle.bgcolor('SkyBlue')  # 背景為天空藍

pen = turtle.Turtle()
pen.pencolor('White')
pen.pensize(2)

# X軸
pen.up()          # 抬起畫筆
pen.goto(-300, 0) # 前進指定座標
pen.down()        # 放下畫筆
pen.forward(600)  # 畫筆前進
pen.left(90)      # 畫筆左轉

# Y軸
pen.up()          # 抬起畫筆
pen.goto(0, -300) # 前進指定座標
pen.down()        # 放下畫筆
pen.forward(600)  # 畫筆前進
pen.left(90)      # 畫筆左轉
pen.home()        # 畫筆回到原點

# 繪製兩個三角形
pen.pencolor('Yellow')
pen.pensize(10)
pen.left(45)
pen.forward(100)     
pen.left(135)    
pen.forward(140) 
pen.home()

pen.right(45)
pen.forward(100)
pen.right(135)    
pen.forward(140)
pen.right(135)    
pen.forward(100)

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 07")

import turtle

turtle.setup(250, 200)     # 產生250 X 200畫布
turtle.bgcolor('SkyBlue')  # 背景為天空藍

show = turtle.Turtle()     # 建立畫布物件
show.pencolor('Yellow')    # 畫筆為黃色
show.pensize(10)           # 畫筆大小
show.speed(1)              # 畫筆速度為慢
# 畫一個簡單矩形
show.forward(70)           # 前進70像素
show.right(90)             # 畫筆右轉90度
show.fd(70)                # forward()方法簡寫
show.right(90)
show.fd(70)
show.right(90)
show.home()

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 08")

import turtle

turtle.setup(250, 200)     # 產生200 X 200畫布
turtle.bgcolor('SkyBlue')  # 背景為天空藍

show = turtle.Turtle()     # 建立畫布物件
show.color('Blue', 'Gold') # 設畫筆為藍色，塗滿金黃色
show.pensize(10)           # 畫筆大小
show.speed(1)              # 畫筆速度為慢
show.pu()                  # 抬起畫筆
show.goto(-50, 50)         # 前往指定位置

# 畫一個簡單矩形
show.begin_fill()   # 開始進行塗色
show.pd()           # pendown()方法簡寫，放下畫筆
show.forward(100)   # 前進100像素
show.right(90)      # 畫筆右轉90度
show.fd(100)        # forward()方法簡寫
show.right(90)
show.fd(100)
show.right(90)
show.fd(100)
show.end_fill()     # 結束塗色動作

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 09")

import turtle

turtle.setup(250, 200)     # 產生250 X 200畫布
turtle.bgcolor('#BEBEBE')  # 背景為灰色 RGB(190, 190, 190)
turtle.colormode(255)      # 色彩以數值表示
show = turtle.Turtle()     # 建立畫布物件
show.pensize(10)           # 畫筆大小
show.speed(1)              # 畫筆速度為慢

show.color((255, 0, 255), (255, 215, 0)) # 設畫筆為洋紅色，塗滿金黃色
show.pu()                  # 抬起畫筆
show.goto(-50, 50)         # 前往指定位置

# 畫一個簡單三角形
show.begin_fill()   # 開始塗色
show.pd()           # pendown()方法簡寫
show.forward(100)   # 前進100像素
show.right(120)     # 畫筆右轉120度
show.fd(100)        # forward()方法簡寫
show.right(120)
show.forward(100)
show.end_fill()     # 結束塗色

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 10")

import turtle

turtle.setup(250, 200)     # 產生 250 X 200畫布
turtle.bgcolor('#BEBEBE')  # 背景為灰色 RGB(190, 190, 190)

show = turtle.Turtle()     # 建立畫布物件
show.pensize(10)           # 畫筆大小
show.speed(1)              # 畫筆速度為慢

show.color((1.0, 0, 1.0), (1.0, 0.84, 0.0)) # 設畫筆為洋紅色，塗滿金黃色
show.pu()                  # 抬起畫筆
show.goto(-60, 80)         # 前往指定位置

# 畫一個簡單五邊形
show.begin_fill()   # 開始進行塗色
show.pd()           # pendown()方法簡寫
show.forward(100)   # 前進100像素
show.right(72)      # 畫筆右轉72度
show.fd(100)        # forward()方法簡寫
show.right(72)
show.forward(100)
show.right(72)
show.fd(100)
show.right(72)
show.fd(100)
show.end_fill()     # 結束塗色動作

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 11")
import turtle

turtle.setup(200, 200)     # 畫布大小200 X 200
turtle.bgcolor('#708090')  # 背景為深灰色 RGB(190, 190, 190)

pen = turtle.Turtle()     # 建立畫布物件
pen.pensize(10)           # 畫筆大小
pen.speed(1)              # 畫筆速度為慢
pen.pencolor('#FFFFFF')   # 設畫筆為白色
pen.shape('turtle')       # 設畫筆形狀是海龜
pen.pu()                  # 抬起畫筆
pen.goto(-10, 70)
pen.pd()                  # 放下畫筆
pen.circle(-60, 360, 6)   # 畫出一個六邊形

turtle.mainloop()

print("------------------------------------------------------------")  # 60個

print("turtle 12")
import turtle

turtle.setup(250, 200)    # 產生250 X 200畫布
turtle.bgcolor('SkyBlue') # 背景為天空藍

show = turtle.Turtle()     # 建立畫布物件
show.pencolor('Yellow')    # 畫筆為黃色
show.pensize(10)           # 畫筆大小
show.speed(1)              # 畫筆速度為慢

# 畫一個簡單矩形
for item in range(4):
   show.fd(70)       # 前進70像素
   show.right(90)    # 畫筆右轉90度

show.up()            # 抬起畫筆
show.goto(-50, 10)   # 畫筆移向指定位置
show.write('正方形', font = ('微軟正黑體', 40))

turtle.mainloop()    # 開始主事件的循環

print("------------------------------------------------------------")  # 60個

print("turtle 13")
import turtle

turtle.setup(300, 300)    # 產生300 X 300畫布
turtle.bgcolor('Gray21')  # 背景為深灰

show = turtle.Turtle()    # 建立畫布物件
show.pencolor('White')    # 畫筆為白色
show.pensize(2)           # 畫筆大小
show.speed(1)             # 畫筆速度為慢

# 畫一個連續矩形
for item in range(16):
   show.fd(item * 3) # 依值前進
   #print(item * 3)
   show.right(90)    # 畫筆右轉90度

print("turtle 13 done")
turtle.mainloop()    # 開始主事件的循環

print("------------------------------------------------------------")  # 60個

print("turtle 14")
import turtle

turtle.setup(300, 300)    # 產生300 X 300畫布
turtle.bgcolor('Gray21')  # 背景為深灰

show = turtle.Turtle()    # 建立畫布物件
show.pencolor('White')    # 畫筆為白色
show.pensize(1)           # 畫筆大小

# 畫一個螺旋圖
for item in range(20):
   show.fd(item * 2) # 依值前進   
   show.right(91)    # 畫筆右轉91度

print("turtle 14 done")

turtle.mainloop()    # 開始主事件的循環

print("------------------------------------------------------------")  # 60個

print("turtle 15")
import turtle

turtle.setup(300, 300)    # 產生300 X 300畫布
turtle.bgcolor('Gray21')  # 背景為深灰

show = turtle.Turtle()    # 建立畫布物件
show.pencolor('White')    # 畫筆為白色
show.pensize(1)           # 畫筆大小

# 畫一個螺旋圖
for item in range(20):
   show.fd(item * 5)  # 依值前進   
   show.right(121)    # 畫筆右轉121度

print("turtle 15 done")

turtle.mainloop()     # 開始主事件的循環

print("------------------------------------------------------------")  # 60個

print("turtle 16")
import turtle

turtle.setup(300, 200)    # 產生300 X 200畫布

pen = turtle.Turtle()    # 建立畫布物件
pen.pencolor('White')    # 白色畫筆
pen.speed(1)

#第一層for/in廻圈輸出4列   
for r1 in range(5):

    # 第二層for/in廻圈，依r1值遞減
    for r2 in range(5 - r1):
        pen.pu()            # 抬起畫筆
        p1, p2 = -50, -50   # 設起始座標 x, y(-50, -50)
        p1 = p1 + r1 * 30   # X軸
        p2 = p2 + r2 * 30   # Y軸
        pen.goto(p1, p2)    # 畫筆移向座標
        pen.pd()            # 放下畫筆
        pen.dot(15, 'Blue')   # 畫白色圓點
        print(f'座標(x = {p1}, y = {p2})') # 查看畫圓點的座標位置
    print() #換新行

print("turtle 16 done")

turtle.mainloop()    # 開始主事件的循環    

print("------------------------------------------------------------")  # 60個

print("turtle 17")
import turtle

turtle.setup(300, 300)
turtle.bgcolor('#363636')  # 設背景為深灰
ps = turtle.Turtle()       # 產生一支畫筆

colors = ('Red', 'LightGreen', 'Yellow', 'Blue')
ps.pensize(2)      # 設畫筆大小

# 以矩形為底的4色螺旋圖
for num in range(20):
   # %運算子取餘數來獲得色彩
   ps.pencolor(colors[num % 4])
   ps.forward(num * 3)
   ps.left(91)

print("turtle 17 done")

turtle.mainloop()    # 開始主事件的循環

print("------------------------------------------------------------")  # 60個

"""
print("turtle 18")
import turtle

colors = ['Magenta', 'Gold', 'Cyan', 'PaleGreen',
          'LemonChiffon', 'Orange', 'Pink']   # List
turtle.setup(400, 400)     # 產生400 X 400畫布
turtle.bgcolor('#363636')  # 背景為深灰

pen = turtle.Turtle()   # 建立畫布物件
weeks = []              # 存放輸入字串
count = 0               # 計數器
wk = turtle.textinput(f'一週七天 <{count}>，按0離開',
                      '請輸入星期前三個字母：')

while count <= 6:
   weeks.append(wk)
   #print(count, wk)
   wk = turtle.textinput(f'一週七天 <{count}>，按0離開',
                         '請輸入星期前三個字母：')
   count += 1
   
# 畫一個螺旋形
for item in range(120):
   pen.pencolor(colors [item % len(weeks)]) # 依餘數取色彩值   
   pen.pu()   # 抬起畫筆
   pen.fd(item * 2)   # forward()方法簡寫
   pen.pd()   # 放下畫筆
   # 在畫布秀出星期名稱，並逐漸把字型放大
   pen.write(weeks[item % len(weeks)],
             font = ('Arial', int((item + 4) / 4)))
   pen.left(360 / len(weeks) + 2)   # 依所得外角左轉

turtle.done()

print("turtle 18 done")

turtle.mainloop()    # 開始主事件的循環

"""

print("------------------------------------------------------------")  # 60個

print("turtle 19")
import turtle

import random

tines = ['Red', 'Yellow', 'Orange',
         'Purple', 'Cyan', 'Pink', 'LightGreen', 'Bisque']
turtle.setup(300, 300)     # 產生300 X 300畫布
turtle.bgcolor('Gray21')   # 背景為深灰

pen = turtle.Turtle()      # 建立畫布物件
pen.speed(0)

# 隨機產生螺旋圖
def haphazardTwist():
   # 方法choice()讓畫筆色彩隨機變
   pen.pencolor(random.choice(tines))
   # 隨機產生 8~40 的大小不一的值來作為螺旋圖大小的依據
   size = random.randint(8, 40)
   
   # x, y座標為視窗寬度的一半
   w1 = -turtle.window_width() // 2
   w2 = turtle.window_width() // 2
   h1 = -turtle.window_height() // 2
   h2 = turtle.window_height() // 2
   
   posX = random.randrange(w1, w2)
   posY = random.randrange(h1, h2)
   
   pen.penup()   # 抬畫筆
   pen.goto(posX, posY)
   pen.pendown()
   for item in range(size):
      pen.forward(item * 2)
      pen.left(91)

for num in range(10):
   haphazardTwist()

print("turtle 19 done")

turtle.mainloop()    # 開始主事件的循環

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

