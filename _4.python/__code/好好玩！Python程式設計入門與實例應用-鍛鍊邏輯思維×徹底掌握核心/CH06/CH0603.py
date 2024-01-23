import turtle

turtle.setup(300, 300)
turtle.bgcolor('#363636')  # 設背景為深灰
ps = turtle.Turtle()       # 產生一支畫筆

colors = ('Red', 'LightGreen', 'Yellow', 'Blue')
ps.pensize(2)      # 設畫筆大小

# 以矩形為底的4色螺旋圖
for num in range(100):
   # %運算子取餘數來獲得色彩
   ps.pencolor(colors[num % 4])
   ps.forward(num * 3)
   ps.left(91)
