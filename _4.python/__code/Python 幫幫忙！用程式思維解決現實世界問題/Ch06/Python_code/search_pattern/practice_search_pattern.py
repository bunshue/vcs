import time
import random
import turtle
   
SA_X = 600  # 設定搜索區域寬度
SA_Y = 480  # 設定搜索區域高度
TRACK_SPACING = 40  # 設定搜索軌跡間的距離

# 設定視窗
screen = turtle.Screen()
screen.setup(width = SA_X, height = SA_Y)
turtle.resizemode('user')
screen.title("Search Pattern")
rand_x = random.randint(0, int(SA_X / 2)) * random.choice([-1, 1])
rand_y = random.randint(0, int(SA_Y / 2)) * random.choice([-1, 1])

rand_x = 0
rand_y = 0

print('人的位置 :', rand_x, ' ', rand_y)

# 設定 turtle 圖案
seaman_image = 'seaman.gif'
screen.addshape(seaman_image)
copter_image_left = 'helicopter_left.gif'
copter_image_right = 'helicopter_right.gif'
screen.addshape(copter_image_left)
screen.addshape(copter_image_right)

# 建立漁夫
seaman = turtle.Turtle(seaman_image)
seaman.hideturtle()
seaman.penup()
seaman.setpos(rand_x, rand_y)
seaman.showturtle()

# 建立直升機
turtle.shape(copter_image_right)
turtle.hideturtle()
turtle.pencolor('black')
turtle.penup()
turtle.setpos(-(int(SA_X / 2) - TRACK_SPACING), int(SA_Y / 2) - TRACK_SPACING)
turtle.showturtle()
turtle.pendown()

# 開始搜索行動，並宣布找到漁夫
for i in range(int(SA_Y / TRACK_SPACING)):     
    turtle.fd(SA_X - TRACK_SPACING * 2)
    turtle.rt(90)
    turtle.fd(TRACK_SPACING / 2)
    turtle.rt(90)
    turtle.shape(copter_image_left)
    turtle.fd(SA_X - TRACK_SPACING * 2)
    turtle.lt(90)
    turtle.fd(TRACK_SPACING / 2)
    turtle.lt(90)
    turtle.shape(copter_image_right)
    if turtle.ycor() - seaman.ycor() <= 10:
        print('turtle.ycor() =', turtle.ycor())
        print('seaman.ycor() =', seaman.ycor())
        turtle.write("      Seaman found!",
                     align = 'left',
                     font = ("Arial", 15, 'normal', 'bold', 'italic'))
        time.sleep(3)

        break
