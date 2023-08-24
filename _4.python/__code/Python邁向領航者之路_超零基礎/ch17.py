# ch17_1.py
import turtle
t = turtle.Pen()
sides = 5                       # 星星的個數
angle = 180 - (180 / sides)     # 每個迴圈海龜轉動角度
size = 100                      # 星星長度
for x in range(sides):
    t.forward(size)             # 海龜向前繪線移動100
    t.right(angle)              # 海龜方向左轉的度數



print('------------------------------------------------------------')	#60個


#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch17\ch17_2.py

# ch17_2.py
import turtle

t = turtle.Pen()
t.pensize(5)                        # 畫筆寬度
colorValue = 1.0
colorStep = colorValue / 36
for x in range(1, 37):
    colorValue -= colorStep
    t.color(0.5, 1, colorValue)     # 色彩調整
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(100)
    
    

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch17\ch17_3.py

# ch17_3.py
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
    


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch17\ch17_4.py

# ch17_4.py
import turtle
n = 300
step = 10
t = turtle.Pen()
t.color('blue')
for i in range(0, n+step, step):
    t.penup()
    t.setpos(i,0)
    t.pendown()
    t.setpos(0, n-i)





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch17\ch17_5.py

# ch17_5.py
import turtle
import random
n = 300
step = 10
t = turtle.Pen()
colorsList = ['red','orange','yellow','green','blue','cyan','purple','violet']
for i in range(0, n+step, step):
    t.color(random.choice(colorsList))      # 使用不同顏色
    t.setpos(i, 0)
    t.setpos(0, n-i)
    t.setpos(-i, 0)
    t.setpos(0, i-n)
    t.setpos(i, 0)





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch17\ch17_6.py

# ch17_6.py
import turtle

t = turtle.Pen()
t.color('blue')
t.penup()
t.setheading(180)                   # 海龜往左
t.forward(150)                      # 移動往左
t.setheading(0)                     # 海龜往右
t.pendown()
t.circle(50)                        # 繪製第1個左上方圓
t.circle(-50)                       # 繪製第2個左下方圓
t.forward(100)
t.circle(50)                        # 繪製第3個右上方圓
t.circle(-50)                       # 繪製第4個右下方圓

t.penup()
t.forward(100)                      # 移動往右
t.pendown()
t.setheading(0)
step = 5                            # 每次增加距離
for r in range(10, 100+step, step):
    t.penup()                       # 將筆提起
    t.setpos(150, -100)             # 海龜到點(150,100)
    t.setheading(0)                 
    t.pendown()                     # 將筆放下準備繪製
    t.circle(r, 90 + r*2)           # 繪製圓      
                                     

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch17\ch17_7.py

# ch17_7.py
import turtle

t = turtle.Pen()
t.color('blue')
for angle in range(0, 360, 15):
    t.setheading(angle)         # 調整海龜方向
    t.circle(100)


    


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch17\ch17_8.py

# ch17_8.py
import turtle

t = turtle.Pen()
t.color('blue')
r = 30                              # 半徑
t.penup()
t.setheading(180)                   # 海龜往左
t.forward(270)                      # 移動往左
t.setheading(0)                     # 海龜往右

for edge in range(3, 13, 1):        # 繪3 - 12邊圖
    t.pendown()
    t.circle(r, steps=edge)
    t.penup()
    t.forward(60)
    
 


    


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch17\ch17_9.py

# ch17_9.py
import turtle

t = turtle.Pen()
t.color('white')
r = 30                              # 半徑
t.penup()
t.setheading(180)                   # 海龜往左
t.forward(270)                      # 移動往左
t.setheading(0)                     # 海龜往右
colorsList = ['red','orange','yellow','green','blue','cyan','purple','violet']
for edge in range(3, 13, 1):        # 繪3 - 12邊圖
    t.pendown()
    t.fillcolor(colorsList[edge % 8])
    t.begin_fill()
    t.circle(r, steps=edge)
    t.end_fill()
    t.penup()
    t.forward(60)
    


print('------------------------------------------------------------')	#60個





#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch17\ch17_10.py

# ch17_10.py
import turtle
t = turtle.Pen()
sides = 5                       # 星星的個數
angle = 180 - (180 / sides)     # 每個迴圈海龜轉動角度
size = 100                      # 星星長度
t.color('blue')
t.begin_fill()
for x in range(sides):
    t.forward(size)             # 海龜向前繪線移動100
    t.right(angle)              # 海龜方向左轉的度數
t.end_fill()





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch17\ch17_11.py

# ch17_11.py
import turtle
def stars(sides, size, cr, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / sides)     # 每個迴圈海龜轉動角度
    t.color(cr)
    t.begin_fill()
    for x in range(sides):
        t.forward(size)             # 海龜向前繪線移動100
        t.right(angle)              # 海龜方向左轉的度數
    t.end_fill()
t = turtle.Pen()
t.screen.bgcolor('blue')
stars(5, 60, 'yellow', 0, 0)






print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch17\ch17_12.py

# ch17_12.py
import turtle
import random
def stars(sides, size, cr, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / sides)     # 每個迴圈海龜轉動角度
    t.color(cr)
    t.begin_fill()
    for x in range(sides):
        t.forward(size)             # 海龜向前繪線移動100
        t.right(angle)              # 海龜方向左轉的度數
    t.end_fill()
t = turtle.Pen()
t.screen.bgcolor('blue')
t.ht()
color_list = ['yellow','white','gold','pink','gray',
              'red','orange','aqua','green']
while True:
    ran_sides = random.randint(2, 5) * 2 + 1   # 限制星星角度是5-11的奇數
    ran_size = random.randint(5, 30)
    ran_color = random.choice(color_list)
    ran_x = random.randint(-250,250)
    ran_y = random.randint(-250,250)
    stars(ran_sides,ran_size,ran_color,ran_x,ran_y)






print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch17\ch17_13.py

# ch17_13.py
import turtle 
import random

def is_inside():
    ''' 測試是否在繪布範圍 '''
    left = (-t.screen.window_width() / 2) + 100             # 左邊牆
    right = (t.screen.window_width() / 2) - 100             # 右邊牆
    top = (t.screen.window_height() / 2) - 100              # 上邊牆
    bottom = (-t.screen.window_height() / 2) + 100          # 下邊牆
    x, y = t.pos()                                          # 海龜座標
    is_inside = (left < x < right) and (bottom < y < top)
    return is_inside

def turtle_move():
    colors = ['blue', 'pink', 'green', 'red', 'yellow', 'aqua']
    t.color(random.choice(colors))              # 繪圖顏色
    t.begin_fill()
    if is_inside():                             # 如果在繪布範圍
        t.right(random.randint(0, 180))         # 海龜移動角度
        t.forward(length)
    else:
        t.backward(length)
    t.end_fill()
    
t = turtle.Pen()
length = 100                                    # 線長
width = 10                                      # 線寬
t.pensize(width)                                # 設定畫筆寬
t.screen.bgcolor('black')                       # 畫布背景
while True:
    turtle_move()








print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch17\ch17_14.py

# ch17_14.py
import turtle

t = turtle.Pen()
colorsList = ['red','orange','yellow','green','blue','cyan','purple','violet']
for line in range(200):            
    t.color(colorsList[line % 8])
    t.forward(line*2)
    t.left(91)
    
 


    


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch17\ch17_15.py

# ch17_15.py
import turtle
turtle.tracer(0,0)                      # 終止追蹤
t = turtle.Pen()

colorsList = ['red','green','blue']
for line in range(400):            
    t.color(colorsList[line % 3])
    t.forward(line)
    t.right(119)
    
 


    


print('------------------------------------------------------------')	#60個


