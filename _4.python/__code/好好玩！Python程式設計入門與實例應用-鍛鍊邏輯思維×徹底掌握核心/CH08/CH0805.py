import turtle, random   # 匯入海龜、亂數 模組

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

for num in range(40):
   haphazardTwist()
   
turtle.mainloop()    # 開始主事件的循環
