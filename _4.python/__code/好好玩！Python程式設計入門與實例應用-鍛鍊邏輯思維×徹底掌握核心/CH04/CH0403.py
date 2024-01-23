import turtle   # 匯入海龜模組

turtle.setup(300, 300)    # 產生300 X 300畫布
turtle.bgcolor('Gray21')  # 背景為深灰

show = turtle.Turtle()    # 建立畫布物件
show.pencolor('White')    # 畫筆為白色
show.pensize(2)           # 畫筆大小
show.speed(1)             # 畫筆速度為慢

# 畫一個連續矩形
for item in range(56):
   show.fd(item * 3) # 依值前進
   print(item * 3)
   show.right(90)    # 畫筆右轉90度

turtle.mainloop()    # 開始主事件的循環
