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





