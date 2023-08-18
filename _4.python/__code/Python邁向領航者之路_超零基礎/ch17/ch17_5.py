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




