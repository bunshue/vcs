import turtle

# 繪製池塘
pond = turtle.Screen()
pond.setup(600, 400)
pond.bgcolor('light blue')
pond.title("Yertle's Pond")

# 繪製小島
mud = turtle.Turtle('circle')
mud.shapesize(stretch_wid=5, stretch_len=5, outline=None)
mud.pencolor('tan')
mud.fillcolor('tan')

# 繪製樹幹
SIDE = 80
ANGLE = 90
log = turtle.Turtle()
log.hideturtle()
log.pencolor('peru')
log.fillcolor('peru')
log.speed(0) # 最快的移動速度
log.penup()
log.setpos(215, -30)
log.lt(45)
log.begin_fill()
for _ in range(2):
    log.fd(SIDE)
    log.lt(ANGLE)
    log.fd(SIDE / 4)
    log.lt(ANGLE)
log.end_fill()

# 繪製樹洞
knot = turtle.Turtle()
knot.hideturtle()
knot.speed(0) # 最快的移動速度
knot.penup()
knot.setpos(245, 5)
knot.begin_fill()
knot.circle(5)
knot.end_fill()

# 繪製鱷龜 Yertle
yertle = turtle.Turtle('turtle')
yertle.color('green')
yertle.speed(1)  # 最慢的移動速度
yertle.fd(200)
yertle.lt(180)
yertle.fd(200)
yertle.rt(176)
yertle.fd(205)
