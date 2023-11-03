# ch16_25.py
import turtle

t = turtle.Pen()
t.shape('turtle')
# 繪製時鐘中間顏色
t.color('white', 'aqua')
t.setpos(0, -120)
t.begin_fill()
t.circle(120)           # 繪時鐘內圓盤
t.end_fill()
t.penup()               # 畫筆關閉
t.home()
t.pendown()             # 畫筆打開
t.color('black')
t.pensize(5)
# 繪製時鐘刻度
for i in range(1, 13):
    t.penup()           # 畫筆關閉
    t.seth(-30*i+90)    # 設定刻度的角度
    t.forward(180)
    t.pendown()         # 畫筆打開
    t.forward(30)       # 畫時間軸
    t.penup()
    t.forward(20)
    t.write(str(i), align="left") # 寫上刻度
    t.home()
# 繪製時鐘外框
t.home()
t.setpos(0, -270)
t.pendown()
t.pensize(10)
t.pencolor('blue')
t.circle(270)
# 寫上名字
t.penup()
t.setpos(0, 320)
t.pendown()
t.write('Python王者歸來', align="center", font=('新細明體', 24))
t.ht()                  # 隱藏游標


