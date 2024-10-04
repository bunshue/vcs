import sys

print("------------------------------------------------------------")  # 60個

#import turtle


import turtle as t

#t.hideturtle()

#set origin point
origin=0,0
#set other turtle stuff
t.speed(2)
t.pu()# 提筆
t.goto(origin)
t.pd()# 下筆
t.color("white")
t.bgcolor("black")

# 初始化完成

t.pu()# 提筆
t.pd()# 下筆

t.fd(100)
t.rt(90)#順時針轉N度
t.fd(100)
t.lt(90)#逆時針轉N度
t.fd(100)

#t.circle(100) # 畫一個圓

t.pu()# 提筆

t.goto(origin)

t.write("12345",font=("Helvetica",12,"normal"))

t.rt(90)#順時針轉N度
t.fd(100)
t.write("abcde",font=("Helvetica",12,"normal"))

t.fd(100)
t.write("ABCDE",font=("Helvetica",12,"normal"))


'''

t.bk(30)

t.bk(30)
t.bk(4)

'''
"""

t.Screen().reset()

"""




print("------------------------------------------------------------")  # 60個

   


print("------------------------------------------------------------")  # 60個






print("------------------------------------------------------------")  # 60個

   


print("------------------------------------------------------------")  # 60個





