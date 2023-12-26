# ch31_16.py
import turtle, time

t = turtle.Pen()
t.color('blue')
t.shape('turtle')
t.stamp()                   # 蓋章第1隻海龜
print("目前有顯示海龜 : ", t.isvisible())
t.forward(100)
secondStamp = t.stamp()     # 蓋章第2隻海龜
time.sleep(3)
t.hideturtle()              # 隱藏目前海龜
print("目前有顯示海龜 : ", t.isvisible())
t.clearstamps(-1)           # 刪除後面1個海龜
time.sleep(3)
t.showturtle()              # 顯示海龜
print("目前有顯示海龜 : ", t.isvisible())


