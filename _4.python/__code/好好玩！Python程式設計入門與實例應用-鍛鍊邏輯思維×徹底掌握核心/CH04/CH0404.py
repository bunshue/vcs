import turtle   # 匯入海龜模組

turtle.setup(300, 300)    # 產生300 X 300畫布
turtle.bgcolor('Gray21')  # 背景為深灰

show = turtle.Turtle()    # 建立畫布物件
show.pencolor('White')    # 畫筆為白色
show.pensize(1)           # 畫筆大小

# 畫一個螺旋圖
for item in range(100):
   show.fd(item * 2) # 依值前進   
   show.right(91)    # 畫筆右轉91度

turtle.mainloop()    # 開始主事件的循環
