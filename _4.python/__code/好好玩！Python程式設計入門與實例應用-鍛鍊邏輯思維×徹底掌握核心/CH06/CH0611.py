import turtle   # 匯入海龜模組

colors = ['Magenta', 'Gold', 'Cyan', 'PaleGreen',
          'LemonChiffon', 'Orange', 'Pink']   # List
turtle.setup(400, 400)     # 產生400 X 400畫布
turtle.bgcolor('#363636')  # 背景為深灰

pen = turtle.Turtle()   # 建立畫布物件
weeks = []              # 存放輸入字串
count = 0               # 計數器
wk = turtle.textinput(f'一週七天 <{count}>，按0離開',
                      '請輸入星期前三個字母：')

while count <= 6:
   weeks.append(wk)
   #print(count, wk)
   wk = turtle.textinput(f'一週七天 <{count}>，按0離開',
                         '請輸入星期前三個字母：')
   count += 1
   
# 畫一個螺旋形
for item in range(120):
   pen.pencolor(colors [item % len(weeks)]) # 依餘數取色彩值   
   pen.pu()   # 抬起畫筆
   pen.fd(item * 2)   # forward()方法簡寫
   pen.pd()   # 放下畫筆
   # 在畫布秀出星期名稱，並逐漸把字型放大
   pen.write(weeks[item % len(weeks)],
             font = ('Arial', int((item + 4) / 4)))
   pen.left(360 / len(weeks) + 2)   # 依所得外角左轉

turtle.done()
