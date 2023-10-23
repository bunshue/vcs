#CH07-09: try-and-error 五邊形 color   方法一
import turtle
t = turtle.Pen(); 
t.shape('turtle'); t.width(2); t.speed(5)
sides = 5
colorsList = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple', 'black']
colorInd = 0
for ang in [71,72,73,74]:
    t.color(colorsList[(colorInd)%4]); colorInd += 1
    for j in range(1, sides+1):
        t.forward(100); t.left(ang)
    t.penup()
    t.home()
    t.pendown()
t.hideturtle()
    
