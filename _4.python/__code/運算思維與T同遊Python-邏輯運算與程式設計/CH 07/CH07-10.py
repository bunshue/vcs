#CH07-10: try-and-error 五邊形   方法二a
import turtle
t = turtle.Pen()
t.shape('turtle'); t.width(2); t.speed(5)
sides = 5
for j in range(1,sides+1):
    t.forward(100); t.left(75)   #手調
t.hideturtle()
    
