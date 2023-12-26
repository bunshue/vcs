# ch31_15.py
import turtle, time

t = turtle.Pen()
t.color('blue')
t.shape('turtle')
firstStamp = t.stamp()      # 蓋章第1隻海龜
t.forward(100)
secondStamp = t.stamp()     # 蓋章第2隻海龜
t.forward(100)
thirdStamp = t.stamp()      # 蓋章第3隻海龜
t.hideturtle()              # 隱藏目前海龜
time.sleep(5)
t.clearstamp(secondStamp)   # 刪除第2隻海龜
time.sleep(5)
t.clearstamps(None)         # 刪除所有海龜

