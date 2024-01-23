import turtle   # 匯入海龜模組

turtle.setup(300, 200)    # 產生300 X 200畫布

pen = turtle.Turtle()    # 建立畫布物件
pen.pencolor('White')    # 白色畫筆
pen.speed(1)

#第一層for/in廻圈輸出4列   
for r1 in range(5):

    # 第二層for/in廻圈，依r1值遞減
    for r2 in range(5 - r1):
        pen.pu()            # 抬起畫筆
        p1, p2 = -50, -50   # 設起始座標 x, y(-50, -50)
        p1 = p1 + r1 * 30   # X軸
        p2 = p2 + r2 * 30   # Y軸
        pen.goto(p1, p2)    # 畫筆移向座標
        pen.pd()            # 放下畫筆
        pen.dot(15, 'Blue')   # 畫白色圓點
        print(f'座標(x = {p1}, y = {p2})') # 查看畫圓點的座標位置
    print() #換新行

turtle.mainloop()    # 開始主事件的循環    
