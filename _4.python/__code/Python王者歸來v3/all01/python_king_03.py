# ch28_1.py
import pyautogui

width, height = pyautogui.size()    # 取得螢幕寬度和高度
print(width, height)                # 列印螢幕寬度和高度




#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_10.py

# ch28_10.py
import pyautogui
import time

print('按Ctrl-C 可以中斷本程式')
try:
    while True:
        xloc, yloc = pyautogui.position()       # 獲得滑鼠游標位置
        xylocStr = "x= " + str(xloc).rjust(4) + " y= " + str(yloc).rjust(4)
        print(xylocStr, end="\r", flush=True)   # 設定同一行最左邊輸出
        time.sleep(1)
except KeyboardInterrupt:
    print('\nBye')



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_11.py

# ch28_11.py
import pyautogui

pyautogui.moveTo(500, 450)
pyautogui.click()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_12.py

# ch28_12.py
import pyautogui

pyautogui.click(500, 450)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_13.py

# ch28_13.py
import pyautogui

pyautogui.click(500, 450, button='right')



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_14.py

# ch28_14.py
import pyautogui
import time

pyautogui.mouseDown(button='right')         # 在滑鼠游標位置按住滑鼠右邊建
time.sleep(1)
pyautogui.mouseUp(800, 300, button='right') # 放開後滑鼠游標在(800, 300)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_15.py

# ch28_15.py
import pyautogui
import time

time.sleep(10)      # 這10秒需要繪圖視窗取得焦點,選擇畫筆和選擇顏色
pyautogui.click()   # 按一下設定繪圖起始點                     
displacement = 10
while displacement < 300:
    pyautogui.dragRel(displacement, 0, duration=0.2)
    pyautogui.dragRel(0, displacement, duration=0.2)
    pyautogui.dragRel(-displacement, 0, duration=0.2)
    pyautogui.dragRel(0, -displacement, duration=0.2)
    displacement += 10






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_16.py

# ch28_16.py
import pyautogui
import time

for i in range(1,10):
    pyautogui.scroll(30)    # 往上捲動      
    time.sleep(1)
    pyautogui.scroll(-30)   # 往下捲動
    time.sleep(1)







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_17.py

# ch28_17.py
import pyautogui

screenImage = pyautogui.screenshot("out28_17_1.jpg")    # 方法1
screenImage.save("out28_17_2.jpg")                      # 方法2








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_18.py

# ch28_18.py
import pyautogui

screenImage = pyautogui.screenshot()
cropPict = screenImage.crop((960,210,1900,480))
cropPict.save("out28_18.jpg")








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_19.py

# ch28_19.py
import pyautogui

screenImage = pyautogui.screenshot()
x, y = 200, 200
print(screenImage.getpixel((x,y)))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_2.py

# ch28_2.py
import pyautogui

xloc, yloc = pyautogui.position()    # 獲得滑鼠游標位置
print(xloc, yloc)                    # 列印滑鼠游標位置


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_20.py

# ch28_20.py
import pyautogui

x, y = 200, 200
trueFalse = pyautogui.pixelMatchesColor(x,y,(255,255,255))
print(trueFalse)
trueFalse = pyautogui.pixelMatchesColor(x,y,(0,0,255))
print(trueFalse)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_21.py

# ch28_21.py
import pyautogui
import time

print("請在 5 秒內開啟 Word 並設為焦點視窗")
time.sleep(5)
pyautogui.write('Ming-Chi Institute of Technology')










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_21_1.py

# ch28_21_1.py
import pyautogui
import time

print("請在 5 秒內開啟 Word 並設為焦點視窗")
time.sleep(5)
pyautogui.write('Ming-Chi Institute of Technology', interval=0.2)   











print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_22.py

# ch28_22.py
import pyautogui
import time

print("請在 5 秒內開啟 Word 並設為焦點視窗")
time.sleep(5)
pyautogui.typewrite('Ming-Chi Institute of Technology', 0.2)   











print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_23.py

# ch28_23.py
import pyautogui
import time

print("請在 5 秒內開啟 Word 並設為焦點視窗")
time.sleep(5)
pyautogui.typewrite(['M', 'i', 'n', 'g'], 1)    











print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_24.py

# ch28_24.py
import pyautogui
import time

print("請在 5 秒內開啟 記事本 並設為焦點視窗")
time.sleep(5)
pyautogui.typewrite(['M', 'i', 'm', 'g', 'left', 'left', 'del', 'n'], 1)    











print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_25.py

# ch28_25.py
import pyautogui
import time

print("請在 5 秒內開啟記事本並設為焦點視窗")
time.sleep(5)
pyautogui.typewrite(['M', 'i', 'n', 'k', 'enter'], 1)
pyautogui.typewrite(['M', 'i', 'n', 'g', 'up', 'backspace', 'g'], 1)











print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_26.py

# ch28_26.py
import pyautogui
import time

print("請在 5 秒內開啟記事本並設為焦點視窗")
time.sleep(5)
# 以下輸出*
pyautogui.keyDown('shift')
pyautogui.press('8')
pyautogui.keyUp('shift')
# 以下開啟檢視功能表
pyautogui.keyDown('alt')
pyautogui.press('V')
pyautogui.keyUp('alt')





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_27.py

# ch28_27.py
import pyautogui
import time

print("請在 5 秒內開啟記事本並設為焦點視窗")
time.sleep(5)
pyautogui.hotkey('shift', '8')     # 輸出 *
pyautogui.hotkey('alt', 'V')       # 開啟檢視功能表





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_28.py

# ch28_28.py
import pyautogui
import time

print("請在10秒內開啟記事本並設為焦點視窗")
time.sleep(10)

pyautogui.write('Taiwan\t',0.3)                     # Taiwan
pyautogui.write('Hung\t',0.3)                       # 姓
pyautogui.write('Jiin-Kwei\t',0.3)                  # 名
pyautogui.write('Jiin-Kwei\t',0.3)                  # 名
pyautogui.write('Hung\t',0.3)                       # 姓
pyautogui.write('1975\t',0.3)                       # 出生年        
pyautogui.write('01\t',0.3)                         # 月
pyautogui.write('01\t',0.3)                         # 日
pyautogui.write('\t',0.3)                           # 選男生
pyautogui.write('Ming-Chi Inst. of Tech\t',0.3)     # 學校
pyautogui.write('Department of ME',0.3)              # 科系






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_29.py

# ch28_29.py
import pyautogui
import time

# 給予一些時間來切換到瀏覽器視窗
time.sleep(5)

# 假設的表單填寫
# 移動到名字輸入框的位置並按一下, 需要根據實際位置調整座標
pyautogui.click(x=200, y=300)       # 這裡的 x 和 y 值需要您自己設定
pyautogui.write('John Doe', interval=0.1)

# 移動到郵件欄位輸入框的位置
pyautogui.click(x=200, y=350)       # 這裡的 x 和 y 值需要您自己設定
pyautogui.write('cshung@example.com', interval=0.1)

# 如果有更多欄位, 重複上述步驟

# 最後移動到提交按鈕並按一下
pyautogui.click(x=200, y=400)       # 這裡的 x 和 y 值需要您自己設定



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_3.py

# ch28_3.py
import pyautogui

xloc = 0
while xloc < 1000:
    xloc, yloc = pyautogui.position()    # 獲得滑鼠游標位置
    print(xloc, yloc)                    # 列印滑鼠游標位置


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_30.py

# ch28_30.py
import pyautogui

# 截取屏幕的一部分
screenshot = pyautogui.screenshot(region=(0, 0, 300, 400))  # x, y, 寬度, 高度
screenshot.save('screenshot.png')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_31.py

# ch28_31.py
import pyautogui
import subprocess
import time

# 打開記事本（或其他應用）
subprocess.Popen('notepad.exe')
time.sleep(2)

# 輸入文本
pyautogui.write('AI實作 - 明志科技大學!', interval=0.1)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_32.py

# ch28_32.py
import pyautogui
import time

time.sleep(5)

# 選擇所有本字, 例如在一個文字編輯器中
pyautogui.hotkey('ctrl', 'a')   # Ctrl + A

# 複製
pyautogui.hotkey('ctrl', 'c')   # Ctrl + C

# 移動到另一個位置或應用
pyautogui.click(100, 100)       # 移動滑鼠游標並按一下

# 貼上
pyautogui.hotkey('ctrl', 'v')   # Ctrl + V



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_4.py

# ch28_4.py
import pyautogui

x, y = 300, 300
for i in range(5):
    pyautogui.moveTo(x, y, duration=0.5)              # 左上角
    pyautogui.moveTo(x+1200, y, duration=0.5)         # 右上角
    pyautogui.moveTo(x+1200, y+400, duration=0.5)     # 右下角
    pyautogui.moveTo(x, y+400, duration=0.5)          # 左下角



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_5.py

# ch28_5.py
import pyautogui
                   
for i in range(5):
    pyautogui.moveRel(300, 0, duration=0.5)     # 往右上角移動
    pyautogui.moveRel(0, 300, duration=0.5)     # 往右下角移動
    pyautogui.moveRel(-300, 0, duration=0.5)    # 往左下角移動
    pyautogui.moveRel(0, -300, duration=0.5)    # 往左上角移動






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_6.py

# ch28_6.py
import pyautogui

xloc = 0
print('按Ctrl-C 可以中斷本程式')
try:
    while xloc < 1000:
        xloc, yloc = pyautogui.position()    # 獲得滑鼠游標位置
        print(xloc, yloc)                    # 列印滑鼠游標位置
except KeyboardInterrupt:
    print('\nBye')




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_7.py

# ch28_7.py
import pyautogui

print('按Ctrl-C 可以中斷本程式')
try:
    while True:
        xloc, yloc = pyautogui.position()    # 獲得滑鼠游標位置
        print(xloc, yloc)                    # 列印滑鼠游標位置
except KeyboardInterrupt:
    print('\nBye')




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_8.py

# ch28_8.py

x1 = 1
x2 = 11
x3 = 111
x4 = 1111
print("x= ", str(x1).rjust(4))
print("x= ", str(x2).rjust(4))
print("x= ", str(x3).rjust(4))
print("x= ", str(x4).rjust(4))





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch28\ch28_9.py

# ch28_9.py
import time, sys

x1 = 1
x2 = 11
x3 = 111
x4 = 1111
print("x= ", str(x1).rjust(4), end="\r", flush=True)
time.sleep(1)
print("x= ", str(x2).rjust(4), end="\r", flush=True)
time.sleep(1)
print("x= ", str(x3).rjust(4), end="\r", flush=True)
time.sleep(1)
print("x= ", str(x4).rjust(4), end="\r", flush=True)

print("------------------------------------------------------------")  # 60個

# ch25_1.py
from twilio.rest import Client

# 你從twilio.com申請的帳號
accountSid='AC6fdc3efffd15cabcdee8b361e9d4e67'
# 你從twilio.com獲得的圖騰
authToken='9a6dfab51a342a480e7cf9c1f88d3e638'

client = Client(accountSid, authToken)
message = client.messages.create (
            from_ = "+12512548607",         # 這是twilio.com給你的號碼
            to = "+886952000000",           # 這是收簡訊方的號碼
            body = "Python王者歸來" )       # 發送的訊息


print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_1.py

# ch31_1.py
import turtle
t = turtle.Pen()
sides = 5                       # 星星的個數
angle = 180 - (180 / sides)     # 每個迴圈海龜轉動角度
size = 100                      # 星星長度
for x in range(sides):
    t.forward(size)             # 海龜向前繪線移動100
    t.right(angle)              # 海龜方向左轉的度數



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_10.py

# ch31_10.py
import turtle
t = turtle.Pen()
sides = 5                       # 星星的個數
angle = 180 - (180 / sides)     # 每個迴圈海龜轉動角度
size = 100                      # 星星長度
t.color('blue')
t.begin_fill()
for x in range(sides):
    t.forward(size)             # 海龜向前繪線移動100
    t.right(angle)              # 海龜方向左轉的度數
t.end_fill()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_11.py

# ch31_11.py
import turtle
def stars(sides, size, cr, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / sides)     # 每個迴圈海龜轉動角度
    t.color(cr)
    t.begin_fill()
    for x in range(sides):
        t.forward(size)             # 海龜向前繪線移動100
        t.right(angle)              # 海龜方向左轉的度數
    t.end_fill()
t = turtle.Pen()
t.screen.bgcolor('blue')
stars(5, 60, 'yellow', 0, 0)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_12.py

# ch31_12.py
import turtle
import random
def stars(sides, size, cr, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / sides)     # 每個迴圈海龜轉動角度
    t.color(cr)
    t.begin_fill()
    for x in range(sides):
        t.forward(size)             # 海龜向前繪線移動100
        t.right(angle)              # 海龜方向左轉的度數
    t.end_fill()
t = turtle.Pen()
t.screen.bgcolor('blue')
t.ht()
color_list = ['yellow','white','gold','pink','gray',
              'red','orange','aqua','green']
while True:
    ran_sides = random.randint(2, 5) * 2 + 1   # 限制星星角度是5-11的奇數
    ran_size = random.randint(5, 30)
    ran_color = random.choice(color_list)
    ran_x = random.randint(-250,250)
    ran_y = random.randint(-250,250)
    stars(ran_sides,ran_size,ran_color,ran_x,ran_y)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_13.py

# ch31_13.py
import turtle 
import random

def is_inside():
    ''' 測試是否在繪布範圍 '''
    left = (-t.screen.window_width() / 2) + 100             # 左邊牆
    right = (t.screen.window_width() / 2) - 100             # 右邊牆
    top = (t.screen.window_height() / 2) - 100              # 上邊牆
    bottom = (-t.screen.window_height() / 2) + 100          # 下邊牆
    x, y = t.pos()                                          # 海龜座標
    is_inside = (left < x < right) and (bottom < y < top)
    return is_inside

def turtle_move():
    colors = ['blue', 'pink', 'green', 'red', 'yellow', 'aqua']
    t.color(random.choice(colors))              # 繪圖顏色
    t.begin_fill()
    if is_inside():                             # 如果在繪布範圍
        t.right(random.randint(0, 180))         # 海龜移動角度
        t.forward(length)
    else:
        t.backward(length)
    t.end_fill()
    
t = turtle.Pen()
length = 100                                    # 線長
width = 10                                      # 線寬
t.pensize(width)                                # 設定畫筆寬
t.screen.bgcolor('black')                       # 畫布背景
while True:
    turtle_move()








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_14.py

# ch31_14.py
import turtle

t = turtle.Pen()
t.color('blue')
t.shape('turtle')
for angle in range(0, 361, 15):
    t.forward(100)
    t.stamp()
    t.home()                # 海龜返回原點
    t.seth(angle)           # 調整海龜方向



    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_15.py

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


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_16.py

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



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_17.py

# ch31_17.py
import turtle, time

t = turtle.Pen()
t.color('blue')
print(t.screen.getshapes())             # 列印海龜游標字串

for cursor in t.screen.getshapes():
    t.shape(cursor)                     # 更改海龜游標
    t.stamp()                           # 海龜游標蓋章
    t.forward(30)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_18.py

# ch31_18.py
import turtle, time
colorsList = ['green', 'yellow', 'red']

t = turtle.Pen()
for i in range(0,3):
    t.fillcolor(colorsList[i%3])    # 更改色彩
    t.begin_fill()                  # 開始填充
    t.circle(50)                    # 繪製左方圓
    t.end_fill()                    # 結束填充
    time.sleep(3)                   # 每隔3秒執行一次迴圈
    





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_19.py

# ch31_19.py
import turtle, time
colorsList = ['green', 'yellow', 'red']

t = turtle.Pen()
t.speed(10)                             # 加速繪製圖形
t.ht()                                  # 隱藏海龜游標
for i in range(0,3):
    t.color('white', colorsList[i%3])   # 更改色彩
    t.begin_fill()                      # 開始填充
    t.circle(50)                        # 繪製左方圓
    t.end_fill()                        # 結束填充
    time.sleep(3)                       # 每隔3秒執行一次迴圈
    





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_2.py

# ch31_2.py
import turtle

t = turtle.Pen()
t.pensize(5)                        # 畫筆寬度
colorValue = 1.0
colorStep = colorValue / 36
for x in range(1, 37):
    colorValue -= colorStep
    t.color(0.5, 1, colorValue)     # 色彩調整
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(100)
    
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_20.py

# ch31_20.py
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



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_21.py

# ch31_21.py
import turtle

def printStr(x, y):
    print(x, y)

t = turtle.Pen()
t.screen.onclick(printStr)
t.screen.mainloop()




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_22.py

# ch31_22.py
import turtle
    
def drawSignal(x, y):
    if x > 0:
        t.fillcolor('yellow')
    else:
        t.fillcolor('blue')
    t.penup()
    t.setpos(x,y-50)            # 設定繪圓起點      
    t.begin_fill()
    t.circle(50)
    t.end_fill()

t = turtle.Pen()
t.screen.onclick(drawSignal)
t.screen.mainloop()




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_23.py

# ch31_23.py
import turtle
    
def keyUp():
    t.seth(90)
    t.forward(50)
def keyDn():
    t.seth(270)
    t.forward(50)
    
t = turtle.Pen()
t.screen.onkey(keyUp, 'Up')
t.screen.onkey(keyDn, 'Down')
t.screen.listen()
t.screen.mainloop()




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_24.py

# ch31_24.py
import turtle

t = turtle.Pen()
colorsList = ['red','orange','yellow','green','blue','cyan','purple','violet']
for line in range(200):            
    t.color(colorsList[line % 8])
    t.forward(line*2)
    t.left(91)
    
 


    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_25.py

# ch31_25.py
import turtle
turtle.tracer(0,0)                      # 終止追蹤
t = turtle.Pen()

colorsList = ['red','green','blue']
for line in range(400):            
    t.color(colorsList[line % 3])
    t.forward(line)
    t.right(119)
    
 


    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_26.py

# ch31_26.py
import turtle
# 依據特定階級數繪製Sierpinski三角形
def sierpinski(order, p1, p2, p3):
    if order == 0:      # 階級數為0
        # 將3個點連接繪製成三角形
        drawLine(p1, p2)
        drawLine(p2, p3)
        drawLine(p3, p1)
    else:    
        # 取得三角形各邊長的中點
        p12 = midpoint(p1, p2)
        p23 = midpoint(p2, p3)
        p31 = midpoint(p3, p1)
        # 遞迴呼叫處理繪製三角形
        sierpinski(order - 1, p1, p12, p31)
        sierpinski(order - 1, p12, p2, p23)
        sierpinski(order - 1, p31, p23, p3)   
# 繪製p1和p2之間的線條
def drawLine(p1,p2):
    t.penup()
    t.setpos(p1[0],p1[1])
    t.pendown()
    t.setpos(p2[0],p2[1])
    t.penup()
    t.seth(0)  
# 傳回2點的中間值
def midpoint(p1, p2):
    p = [0,0]                       # 初值設定
    p[0] = (p1[0] + p2[0]) / 2
    p[1] = (p1[1] + p2[1]) / 2
    return p

# main
t = turtle.Pen()
p1 = [0, 86.6]
p2 = [-100, -86.6]
p3 = [100, -86.6]
order = eval(input("輸入階級數 : "))
sierpinski(order, p1, p2, p3)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_3.py

# ch31_3.py
import turtle

t = turtle.Pen()
colorsList = ['red','orange','yellow','green','blue','cyan','purple','violet']
tWidth = 1                          # 最初畫筆寬度
for x in range(1, 41):
    t.color(colorsList[x % 8])      # 選擇畫筆顏色
    t.forward(2 + x * 5)            # 每次移動距離
    t.right(45)                     # 每次旋轉角度
    tWidth += x * 0.05              # 每次畫筆寬度遞增    
    t.width(tWidth)
    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_4.py

# ch31_4.py
import turtle
n = 300
step = 10
t = turtle.Pen()
t.color('blue')
for i in range(0, n+step, step):
    t.penup()
    t.setpos(i,0)
    t.pendown()
    t.setpos(0, n-i)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_5.py

# ch31_5.py
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





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_6.py

# ch31_6.py
import turtle

t = turtle.Pen()
t.color('blue')
t.penup()
t.setheading(180)                   # 海龜往左
t.forward(150)                      # 移動往左
t.setheading(0)                     # 海龜往右
t.pendown()
t.circle(50)                        # 繪製第1個左上方圓
t.circle(-50)                       # 繪製第2個左下方圓
t.forward(100)
t.circle(50)                        # 繪製第3個右上方圓
t.circle(-50)                       # 繪製第4個右下方圓

t.penup()
t.forward(100)                      # 移動往右
t.pendown()
t.setheading(0)
step = 5                            # 每次增加距離
for r in range(10, 100+step, step):
    t.penup()                       # 將筆提起
    t.setpos(150, -100)             # 海龜到點(150,100)
    t.setheading(0)                 
    t.pendown()                     # 將筆放下準備繪製
    t.circle(r, 90 + r*2)           # 繪製圓      
                                     

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_7.py

# ch31_7.py
import turtle

t = turtle.Pen()
t.color('blue')
for angle in range(0, 360, 15):
    t.setheading(angle)         # 調整海龜方向
    t.circle(100)


    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_8.py

# ch31_8.py
import turtle

t = turtle.Pen()
t.color('blue')
r = 30                              # 半徑
t.penup()
t.setheading(180)                   # 海龜往左
t.forward(270)                      # 移動往左
t.setheading(0)                     # 海龜往右

for edge in range(3, 13, 1):        # 繪3 - 12邊圖
    t.pendown()
    t.circle(r, steps=edge)
    t.penup()
    t.forward(60)
    
 


    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch31\ch31_9.py

# ch31_9.py
import turtle

t = turtle.Pen()
t.color('white')
r = 30                              # 半徑
t.penup()
t.setheading(180)                   # 海龜往左
t.forward(270)                      # 移動往左
t.setheading(0)                     # 海龜往右
colorsList = ['red','orange','yellow','green','blue','cyan','purple','violet']
for edge in range(3, 13, 1):        # 繪3 - 12邊圖
    t.pendown()
    t.fillcolor(colorsList[edge % 8])
    t.begin_fill()
    t.circle(r, steps=edge)
    t.end_fill()
    t.penup()
    t.forward(60)
    
 


    


print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch32\ch32_1.py

# ch32_1.py
import yfinance as yf

apple = yf.Ticker("AAPL")                           # 建立Apple物件
print("Apple公司財務報表")
financials = apple.financials                       # 獲取財務報表
print(financials)
quarterly_financials = apple.quarterly_financials   # 獲取季度財務報表
print(quarterly_financials)

tsmc = yf.Ticker("2330.TW")                         # 建立Apple物件
print("台積電財務報表")
financials = tsmc.financials                        # 獲取財務報表
print(financials)
quarterly_financials = tsmc.quarterly_financials    # 獲取季度財務報表
print(quarterly_financials)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch32\ch32_2.py

# ch32_2.py
import yfinance as yf

def fetch_apple_stock_price():
    # 獲取Apple股票資料
    apple = yf.Ticker("AAPL")
    
    # 獲取即時股價
    apple_stock_info = apple.history(period="1d")
    
    # 輸出股價
    print("Apple公司的股價(目前或最近交易日) : ")
    print("開盤價：", apple_stock_info['Open'].iloc[0])
    print("收盤價：", apple_stock_info['Close'].iloc[0])
    print("最高價：", apple_stock_info['High'].iloc[0])
    print("最低價：", apple_stock_info['Low'].iloc[0])
    print("交易量：", apple_stock_info['Volume'].iloc[0])

fetch_apple_stock_price()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch32\ch32_3.py

# ch32_3.py
import yfinance as yf
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 下載蘋果公司最近三個月的股價數據
apple = yf.Ticker("AAPL")
data = apple.history(period="3mo")

# 計算5天和20天移動平均線
data['MA5'] = data['Close'].rolling(window=5).mean()
data['MA20'] = data['Close'].rolling(window=20).mean()

# 繪製股價和移動平均線
plt.figure(figsize=(10,6))
plt.plot(data['Close'], label='AAPL Close', color='blue')
plt.plot(data['MA5'], label='5-Day MA', color='green')
plt.plot(data['MA20'], label='20-Day MA', color='red')

# 標題和圖例
plt.title('Apple公司股價 5 日和 20 日移動平均線')
plt.xlabel('日期')
plt.ylabel('價格')
plt.legend()

# 顯示圖表
plt.show()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch32\ch32_4.py

# ch32_4.py
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 下載台積電最近三個月的股價數據
tsmc = yf.Ticker("2330.TW")                 
data = tsmc.history(period='1y')

# 計算5日和20日的簡單移動平均
data['SMA5'] = data['Close'].rolling(window=5).mean()
data['SMA20'] = data['Close'].rolling(window=20).mean()

# 繪製收盤價和移動平均線
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Close Price', alpha=0.5)
plt.plot(data['SMA5'], label='5-Day SMA', alpha=0.8)
plt.plot(data['SMA20'], label='20-Day SMA', alpha=0.8)
plt.title('台積電股價 5 日和 20 日移動平均線')
plt.xlabel('日期')
plt.ylabel('價格')
plt.legend()
plt.grid(True)
plt.show()

# 移動平均生成交易信號
# 買入信號: 5日均線從下方突破20日均線
# 賣出信號: 5日均線從上方跌破20日均線
data['Signal'] = 0.0
data.iloc[5:, data.columns.get_loc('Signal')] =\
    np.where(data['SMA5'].iloc[5:] > data['SMA20'].iloc[5:], 1.0, 0.0)
data['Signal_change'] = data['Signal'].diff()

# 找出買入和賣出的日期
buy_dates = data[data['Signal_change'] == 1].index
sell_dates = data[data['Signal_change'] == -1].index

print(f"買入日期: {buy_dates.tolist()}")
print(f"賣出日期: {sell_dates.tolist()}")




print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch33\ch33_1.py

# ch33_1.py
import pygame
pygame.mixer.init()

mysound = r'C:\Windows\Media\notify.wav'
soundObj = pygame.mixer.Sound(mysound)      # 建立Sound物件
soundObj.play()                             # 撥放一次
pygame.time.delay(3000)                     # 休息3秒
soundObj.play(2)                            # 播放3次








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch33\ch33_10.py

# ch33_10.py
from gtts import gTTS
import pygame

text = "Hello, Machine Learning!"
tts = gTTS(text=text, lang='en')
tts.save("hello.mp3")

pygame.mixer.init()
pygame.mixer.music.load("hello.mp3")
pygame.mixer.music.play()




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch33\ch33_11.py

# ch33_11.py
from gtts import gTTS
import pygame

text = "我愛明志科技大學!"
tts = gTTS(text=text, lang='zh-tw')
tts.save("hello.mp3")

pygame.mixer.init()
pygame.mixer.music.load("hello.mp3")
pygame.mixer.music.play()






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch33\ch33_12.py

# ch33_12.py
from deep_translator import GoogleTranslator

# 要翻譯的文本
text = '早安'

# 翻譯成英文
translator = GoogleTranslator(source='auto', target='en')
translation_en = translator.translate(text)
print("英文:", translation_en)

# 翻譯成日文, 另一種寫法
translation_ja = GoogleTranslator(source='auto', target='ja').translate(text)
print("日文:", translation_ja)

# 翻譯成韓文
translation_ko = GoogleTranslator(source='auto', target='ko').translate(text)
print("韓文:", translation_ko)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch33\ch33_2.py

# ch33_2.py
import pygame
pygame.mixer.init()

mysound = r'C:\Windows\Media\notify.wav'
pygame.time.delay(1000)                     # 先給聲音初始化工作

soundObj = pygame.mixer.Sound(mysound)      # 建立Sound物件
soundObj.play()                             # 撥放一次
pygame.time.delay(3000)                     # 休息3秒
soundObj.set_volume(0.1)                    # 聲音變小
soundObj.play(2)                            # 播放3次








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch33\ch33_3.py

# ch33_3.py
import pygame
import time
pygame.mixer.init()

mywav = r'C:Windows\Media\notify.wav'
pygame.time.delay(1000)                     # 先給聲音初始化工作
pygame.mixer.music.load(mywav)              # 下載 wav 音樂檔案
pygame.mixer.music.play()                   # 播放 wav 音樂檔案

time.sleep(5)                               # 程式休息
mymidi = r'C:\Windows\Media\town.mid'
pygame.time.delay(1000)                     # 先給聲音初始化工作
pygame.mixer.music.load(mymidi)             # 下載 midi 音樂檔案
pygame.mixer.music.play()                   # 播放 midi 音樂檔案


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch33\ch33_4.py

# ch33_4.py
import matplotlib.pyplot as plt
from scipy.io import wavfile

mywav = r'C:Windows\Media\notify.wav'
# 讀取.wav文件
sample_rate, data = wavfile.read(mywav)

# 繪製聲波圖
plt.figure(figsize=(10, 4))
plt.plot(data)
plt.title('Waveform of nofity.wav file')
plt.ylabel('Amplitude')
plt.xlabel('Sample')
plt.show()




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch33\ch33_5.py

# ch33_5.py
from pydub import AudioSegment

mywav = r'C:Windows\Media\notify.wav'
# 讀取.wav文件
wav_audio = AudioSegment.from_wav(mywav)

# 轉換為.mp3
wav_audio.export("notify.mp3", format="mp3")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch33\ch33_6.py

# ch33_6.py
from tkinter import *
import pygame

def playmusic():                                        # 處理按撥放紐
    selection = var.get()                               # 獲得音樂選項
    if selection == '1':
        pygame.mixer.music.load('notify.mp3')           # 撥放選項1音樂
        pygame.mixer.music.play(-1)                     # 循環撥放
    if selection == '2':
        town = r'C:\Windows\Media\town.mid'
        pygame.mixer.music.load(town)                   # 撥放選項2音樂
        pygame.mixer.music.play(-1)                     # 循環撥放
    if selection == '3':
        onestop = r'C:\Windows\Media\onestop.mid'
        pygame.mixer.music.load(onestop)                # 撥放選項3音樂
        pygame.mixer.music.play(-1)                     # 循環撥放 
def stopmusic():                                        # 處理按結束紐
    pygame.mixer.music.stop()                           # 停止撥放此首
    
# 建立音樂選項鈕內容的串列
musics = [('notify.mp3', 1),                            # 音樂選單串列
          ('town.mid', 2),
          ('onestop.mid', 3)]

pygame.mixer.init()                                     # 最初化mixer

tk = Tk()
tk.geometry('480x220')                                  # 開啟視窗
tk.title('Music Player')                                # 建立視窗標題
mp3Label = Label(tk, text='\n我的 Music 撥放程式')      # 視窗內標題
mp3Label.pack()
# 建立選項紐Radio button
var = StringVar()                                       # 設定以字串表示選單編號
var.set('1')                                            # 預設音樂是1
for music, num in musics:                               # 建立系列選項紐
    radioB = Radiobutton(tk, text=music, variable=var, value=num)
    radioB.pack()
# 建立按鈕Button
button1 = Button(tk, text='撥放', width=10, command=playmusic)    # 撥放音樂
button1.pack()
button2 = Button(tk, text='結束', width=10, command=stopmusic)    # 停止撥放音樂
button2.pack()
mainloop()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch33\ch33_7.py

# ch33_7.py
import speech_recognition as sr

r = sr.Recognizer()

# 設定錄音檔案的儲存路徑
audio_file_path = "out33_7.wav"

with sr.Microphone() as source:
    print("請說英文 ...")
    audio = r.listen(source)

    # 將聲音保存為 WAV 檔案
    with open(audio_file_path, "wb") as file:
        file.write(audio.get_wav_data())

    try:
        # 使用Google的語音識別API
        text = r.recognize_google(audio)  
        print("你說的英文是 : {}".format(text))
    except:
        print("抱歉無法聽懂你的語音")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch33\ch33_8.py

# ch33_8.py
import speech_recognition as sr

r = sr.Recognizer()

# 設定錄音檔案的儲存路徑
audio_file_path = "out33_8.wav"

with sr.Microphone() as source:
    print("請說中文 ...")
    audio = r.listen(source)

    # 將聲音保存為 WAV 檔案
    with open(audio_file_path, "wb") as file:
        file.write(audio.get_wav_data())

    try:
        # 使用Google的語音識別API
        text = r.recognize_google(audio, language="zh-TW")  
        print("你說的中文是 : {}".format(text))
    except:
        print("抱歉無法聽懂你的語音")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch33\ch33_9.py

# ch33_9.py
import matplotlib.pyplot as plt
from scipy.io import wavfile

mywav = 'out33_7.wav'
# 讀取.wav文件
sample_rate, data = wavfile.read(mywav)

# 繪製聲波圖
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.figure(figsize=(10, 4))
plt.plot(data)
plt.title('Good Morning聲波圖')
plt.ylabel('Amplitude')
plt.xlabel('Sample')
plt.show()




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch33\ch33_9_1.py

# ch33_9_1.py
import matplotlib.pyplot as plt
from scipy.io import wavfile

mywav = 'out33_8.wav'
# 讀取.wav文件
sample_rate, data = wavfile.read(mywav)

# 繪製聲波圖
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.figure(figsize=(10, 4))
plt.plot(data)
plt.title('早安 聲波圖')
plt.ylabel('Amplitude')
plt.xlabel('Sample')
plt.show()




print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch36\ch36_1.py

# ch36_1.py
from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=dhzsf5QXmns")
print("下載中   ... ")
yt.streams[0].download()
print("下載完成 ... ")





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch36\ch36_2.py

# ch36_2.py
from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=dhzsf5QXmns")
videoViews = yt.views
print(f"影片觀賞次數 : {videoViews}")
videoSeconds = yt.length
print(f"影片長度(秒) : {videoSeconds}")
videoRating = yt.rating
print(f"影片評價     : {videoRating}")
videoTitle = yt.title
print(f"影片標題     : {videoTitle}\n下載中 ... ")
yt.streams[0].download()
print("下載完成 ... ")










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch36\ch36_3.py

# ch36_3.py
from pytube import YouTube
import os

path = r"d:\myYouTube"
if not os.path.isdir(path):         # 如果不存在則建立此資料夾
    os.mkdir(path)

yt = YouTube("https://www.youtube.com/watch?v=dhzsf5QXmns")
videoViews = yt.views
print(f"影片觀賞次數 : {videoViews}")
videoSeconds = yt.length
print(f"影片長度(秒) : {videoSeconds}")
videoRating = yt.rating
print(f"影片評價     : {videoRating}")
videoTitle = yt.title
print(f"影片標題     : {videoTitle}\n下載中 ... ")
yt.streams[0].download(path)        # 所下載影音檔案儲存在path
print("下載完成 ... ")










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch36\ch36_4.py

# ch36_4.py
from pytube import YouTube
import os

path = r"d:\myYouTube"
if not os.path.isdir(path):             # 如果不存在則建立此資料夾
    os.mkdir(path)

links = ["https://www.youtube.com/watch?v=dhzsf5QXmns",
         "https://www.youtube.com/watch?v=z8eE3CGyQiE"]
for video in links:
    yt = YouTube(video)
    videoViews = yt.views
    print(f"影片觀賞次數 : {videoViews}")
    videoSeconds = yt.length
    print(f"影片長度(秒) : {videoSeconds}")
    videoRating = yt.rating
    print(f"影片評價     : {videoRating}")
    videoTitle = yt.title
    print(f"影片標題     : {videoTitle}\n下載中 ... ")
    print(f"影片格式數量 : {len(yt.streams)}")
    yt.streams[0].download(path)        # 所下載影音檔案儲存在path
    print("下載完成 ... ")










print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch36\ch36_5.py

# ch36_5.py
import threading 
import os  
from pytube import YouTube  

def download_video(url):
    try:
        yt = YouTube(url)                       # 建立 YouTube 物件
        yt.streams[0].download(download_path)   # 選擇第1個並下載
        print(f"下載完成 : {url}")              # 輸出下載完成的訊息
    except Exception as e:
        print(f"錯誤下載 {url}: {str(e)}")      # 如果錯誤, 輸出錯誤訊息

# 下載影片的 URL 列表
urls = [
    "https://www.youtube.com/watch?v=dhzsf5QXmns",
    "https://www.youtube.com/watch?v=z8eE3CGyQiE",
    "https://www.youtube.com/watch?v=GLlsu31FBt8",
    "https://www.youtube.com/watch?v=VMCk7fh9SGw",
    "https://www.youtube.com/watch?v=_32sspKCF8Y",
]

# 定義當前目錄下的 out36_5 資料夾作為下載路徑
download_path = os.path.join(os.getcwd(), 'out36_5')

# 檢查該資料夾是否存在，如果不存在則建立
if not os.path.exists(download_path):
    os.makedirs(download_path)

threads = []                                    # 建立一個空串列儲存執行緒

# 為每個 URL 建立一個新的執行緒
for url in urls:
    thread = threading.Thread(target=download_video, args=(url,))
    threads.append(thread)                      # 將執行緒添加到串列中
    thread.start()                              # 開始執行緒的執行

# 等待所有執行緒完成
for thread in threads:
    thread.join()

print("所有影片下載完成")                       

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch36\ch36_6.py

# ch36_6.py
from tkinter import *
from pytube import YouTube

def loadVideo():                    # 列印下載資訊
    vlinks = "https//www.youtube.com/watch?v="
    vlinks = vlinks + links.get()   # 影音檔案網址
    yt = YouTube(vlinks)
    yt.streams[0].download()
    x.set("影音檔案下載完成 ...")
          
window = Tk()
window.title("ch35_6")              # 視窗標題

x = StringVar()
x.set("請輸入影音檔案序列碼")
links = StringVar()

lab1 = Label(window,text="輸入影音檔案序列碼 : ").grid(row=0)
lab2 = Label(window,text="請輸入儲存的資料夾 : ").grid(row=1)
lab3 = Label(window,textvariable=x,
             height=3).grid(row=2,column=0,columnspan=2)
             
e1 = Entry(window,textvariable=links)   # 文字方塊1
e2 = Entry(window)                      # 文字方塊2
e1.grid(row=0,column=1)                 # 定位文字方塊1
e2.grid(row=1,column=1)                 # 定位文字方塊2

btn1 = Button(window,text="下載",command=loadVideo)
btn1.grid(row=3,column=0)
btn2 = Button(window,text="結束",command=window.destroy)
btn2.grid(row=3,column=1)

window.mainloop()







print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




