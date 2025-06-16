"""
pygame 測試大全

1. 一般
2. 畫圖畫字
3. 滑鼠鍵盤

最後再搬出

"""


"""
pygame提供的模組

color	提供色彩的設定
display	顯示螢幕
event	處理事件
image	處理圖片
key	處理鍵盤的按鈕
mouse	處理滑鼠訊息
movie	處理視訊播放
mixer	用來播放聲音
time	處理時間

pygame.display.set_mode()	建立視窗並初始化
pygame.display.set_caption()	在標題列顯示文字
pygame.display.flip()		將Surface全部更新後並顯示於畫面上
pygame.display.update()		依據軟體做部分畫面的更新

"""

import sys
import time
import math
import random
import pygame

W, H = 800, 600
screen_size = (W, H)  # 設定屏幕尺寸
surface_size = (W - 50, H - 50)  # 設定surface尺寸

# 設定顏色
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

RosyBrown = 255, 193, 193  # 玫紅色
fuchsia = (255, 0, 255)  # 紫色
aqua = (0, 255, 255)  # 淺藍色
gray = (128, 128, 128)  # 灰色
grey = 79, 79, 79  # 灰色

# 設定顏色, same
red = pygame.color.Color("#FF0000")
green = pygame.color.Color("#00FF00")
blue = pygame.color.Color("#0000FF")
black = pygame.color.Color("#000000")
white = pygame.color.Color("#FFFFFF")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
font_filename = "C:/Windows/Fonts/mingliu.ttc"  # 新細明體


def init_pygame(name, color):
    print(name)
    pygame.init()  # 初始化Pygame

    screen = pygame.display.set_mode(screen_size)  # 產生視窗screen
    # screen = pygame.display.set_mode(screen_size, 0, 32)  # 產生視窗screen
    # screen = pygame.display.set_mode(screen_size, 0)  # 產生視窗screen

    pygame.display.set_caption(name)

    # print("取得screen參數 :", screen.get_size())

    # 利用screen物件來作為畫布，以fill()方法填上顏色
    screen.fill(color)
    return screen


def run_pygame():
    # 更新屏幕, 保持屏幕打開, 直到用戶退出, 偵測視窗是否被關閉(8)
    pygame.display.update()  # 繪製視窗顯示於螢幕上
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
                running = False
    pygame.quit()


print("------------------------------------------------------------")  # 60個
'''
pygame_name = 'pygame 01 載入圖片'
screen = init_pygame(pygame_name, white)

#方法load()載入圖片，convert()能提高圖片的處理速度
image=pygame.image.load(filename)
image.convert()

#改變圖片大小
image=pygame.transform.scale(image,(300*5//4, 400*5//4))

x_st, y_st = 100, 100
screen.blit(image, (x_st, y_st))

run_pygame()

print('------------------------------------------------------------')	#60個

pygame_name = 'pygame 02 建立畫布'
screen = init_pygame(pygame_name, yellow)

# 產生Surface物件, 上色，繪製成形
surface = pygame.Surface(surface_size)
#print(surface.get_width(), surface.get_height())#取得surface參數
surface.convert()           # 產生副本
surface.fill((0,255,0))#surface填滿指定色

print('將surface貼到screen上')
screen.blit(surface, (25, 25))# 輸出到畫布上

run_pygame()

print("------------------------------------------------------------")  # 60個

pygame_name = 'pygame 03 使用surface 載入圖片'
screen = init_pygame(pygame_name, white)
print('建立screen')

print('建立surface')
# 產生Surface物件, 上色，繪製成形
surface = pygame.Surface(surface_size)
surface = surface.convert()#產生副本
surface.fill((0,255,0))#surface填滿指定色

print('讀取圖片貼到surface上')
#方法load()載入圖片，convert()能提高圖片的處理速度
image = pygame.image.load(filename)
image.convert()
x_st, y_st = 100, 100
surface.blit(image, (x_st, y_st))

print('將surface貼到screen上')
screen.blit(surface, (25, 25))# 輸出到畫布上

run_pygame()

print('------------------------------------------------------------')	#60個

pygame_name = 'pygame 05 Animation'
screen = init_pygame(pygame_name, white)

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_cat/cat3.png'

speed = [1, 1]

#設定每秒畫格25，利用Clock()方法來確保動畫能持續進行
Fps = 25 #每秒的執行次數
traceCar = pygame.time.Clock()

#載入圖片，get_rect()取得矩形區域
car = pygame.image.load(filename)
carX, carY = 5, 5 #設定開始移動的X、Y座標
move = 'Down'
Fps = 25
traceCar = pygame.time.Clock()

# tick()方法依據fps之值讓移動圖片有動畫效果
# blit()不斷在畫布上繪製圖片
# update()進行動作的更新

running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
          running = False

   screen.fill(white)
   
   if move == 'Down':
      carY += 5
      if carY == 230 : move = 'Right'
   elif move == 'Right':
      carX += 5
      if carX == 315 : move = 'Up'
   elif move == 'Up':
      carY -= 5
      if carY == 10 : move = 'Left'
   elif move == 'Left':
      carX -= 5
      if carX == 10: move = 'Down'
   
   # print('移動座標:', carX, carY)
   # blit()方法在畫布上繪製圖片
   screen.blit(car, (carX, carY))
   pygame.display.update()#繪製視窗顯示於螢幕上
   traceCar.tick(Fps) # 依fps的值來產生動畫

pygame.quit()

print("------------------------------------------------------------")  # 60個
""" 還不能順利退出
pygame_name = 'pygame 06 按鍵事件'
screen = init_pygame(pygame_name, white)

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_cat/cat3.png'

from pygame.locals import *

#載入圖片並設座標
surface = pygame.image.load(filename).convert()
carX, carY = 0, 0   #起始位置
Xmove, Ymove = 0, 0 #移動座標

while True:
   for event in pygame.event.get():
      
      if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
         pygame.quit() #quit()方法結束Pygame程序
         sys.exit()

      screen.fill((white))

      #判斷那個按鍵被按？
      if event.type == KEYDOWN:
         #向左方向鍵，減少座標值
         if event.key == pygame.K_LEFT:
            Xmove -= 5
         #向右方向鍵，增加座標值
         elif event.key == pygame.K_RIGHT:
            Xmove += 5                 
         #向上下向鍵，減少座標值
         elif event.key == pygame.K_UP:
            Ymove -= 5
         #向下方向鍵，增加座標值
         elif event.key == pygame.K_DOWN:
            Ymove += 5
         #計算座標值
         carX += Xmove; carY += Ymove
         #print('X', carX, ' Y', carY)

      #放掉鍵盤按鍵，回到原點
      if event.type == pygame.KEYUP:
         if carX < 0 or carY < 0:
            carX, carY = 0, 0
            Xmove ,Ymove = 0, 0
         if carX == 225 or carY == 225:
            carX, carY = 0, 0
            Xmove ,Ymove = 0, 0

      screen.blit(surface, (carX, carY))# 輸出到畫布上
      pygame.display.update()#繪製視窗顯示於螢幕上

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_cat/cat3.png'

from pygame.locals import *

pygame_name = 'pygame 07 滑鼠事件'
screen = init_pygame(pygame_name, white)

# 載入圖片並設座標
imageRect = pygame.image.load(filename).convert_alpha()
imageX, imageY = 0, 0   # 起始位置
moveing = False       # 移動圖片

while True:
   for event in pygame.event.get():
      
      if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
         pygame.quit() # 結束Pygame程序
         sys.exit()
   screen.fill(black)
   
   # 偵測滑鼠的按鈕
   buts = pygame.mouse.get_pressed()
      
   # 按下滑鼠左鍵才能移動圖片
   if buts[0]:
      moving = True
      # 取得滑鼠座標
      imageX, imageY = pygame.mouse.get_pos()
      
      # 取得座標讓圖片不要超過視窗範圍
      imageX -= imageRect.get_width()/2
      imageY -= imageRect.get_height()/2
      print(imageX, imageY)
   else:
      moving = False

   screen.blit(imageRect, (imageX, imageY))
   pygame.display.update()#繪製視窗顯示於螢幕上

print("------------------------------------------------------------")  # 60個

pygame_name = 'pygame 08 偵測滑鼠位置'
screen = init_pygame(pygame_name, white)

clock = pygame.time.Clock()

pos_list = []

# 更新屏幕
pygame.display.update()#繪製視窗顯示於螢幕上

# 保持屏幕打開，直到用戶退出
#偵測視窗是否被關閉
while True:
    screen.fill(black)
    pygame.draw.rect(screen, black, [0, 0, 0, 0])

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:    #滑鼠事件
            pos = pygame.mouse.get_pos()  # 取得滑鼠座標
            print(pos)
            #print(type(pos))
            pos_list.append(pos)
            #pygame.draw.lines(screen, [255, 255, 255], pos_list) TBD

        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            pygame.quit() #quit()方法結束Pygame程序
            sys.exit()
    pygame.display.flip()
    clock.tick(10)    

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_cat/cat3.png'

pygame_name = 'pygame 09 碰撞的偵測'
screen = init_pygame(pygame_name, white)

#設定每秒畫格20，利用Clock()方法來確保動畫能持續進行
Fps = 20 #每秒的執行次數
traceCar = pygame.time.Clock()

#載入圖片，get_rect()取得矩形的移動區域
car = pygame.image.load(filename)
carRect = car.get_rect()

#屬性center-設定圖片要開始移動的中心點
carRect.center = 400, 400

#屬性topleft取得圖片移動區域左上角到畫布的位置
carX , carY = carRect.topleft

#moveX, moveY = 5, -5 #設定圖片的移動速度會形成固定範圍
#避免移動成固定範圍，以隨機值來取得起始角度並轉為弧度
posi = random.randint(45, 60)
angle = math.radians(posi)
#設定圖片水平和垂直的移動速度
moveX = 5 * math.sin(angle)
moveY = -5 * math.cos(angle)

while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
          pygame.quit()
          sys.exit()

   screen.fill(white)
   traceCar.tick(Fps) #每秒執行25次
   #改變水平、垂直位置並重設物件的中心點
   carX += moveX 
   carY += moveY
   carRect.center = carX, carY

   #偵測水平、垂直方向的移動是否會碰到畫布的左、右或上、下邊界
   #碰到時改變moveX、moveY為正值並改變方向
   if(carRect.left <= 0) or (carRect.right >= screen.get_width()):
      moveX *= -1
      print(moveX, moveY)
   elif(carRect.top <= 5) or (carRect.bottom >= screen.get_height() - 5):
      moveY *= -1
   screen.blit(car, carRect.topleft)
   pygame.display.update()#繪製視窗顯示於螢幕上
"""
print("------------------------------------------------------------")  # 60個

#randomGrid.py

pygame_name = 'pygame 10'
screen = init_pygame(pygame_name, white)

width = 400
height = 300
windowSize = [width, height]

clock = pygame.time.Clock()

sqrW = width / 10
sqrH = height / 10

done = False

while not done:
    red = random.randrange(0, 256)
    green = random.randrange(0, 256)
    blue = random.randrange(0, 256)
    x = random.randrange(0, width, sqrW)
    y = random.randrange(0, width, sqrH)
    pygame.draw.rect(screen, (red, green, blue), (x, y, sqrW, sqrH))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            done = True
    clock.tick(30)
    
pygame.quit()

print("------------------------------------------------------------")  # 60個

#save.py

pygame_name = 'pygame 11'
screen = init_pygame(pygame_name, white)

width = 400
height = 300
windowSize = [width, height]
clock = pygame.time.Clock()

sqrW = width / 10
sqrH = height / 10

done = False

while not done:
    red = random.randrange(0, 255)
    green = random.randrange(0, 255)
    blue = random.randrange(0, 255)
    x = random.randrange(0, width, sqrW)
    y = random.randrange(0, width, sqrH)
    
    pygame.draw.rect(screen, (red, green, blue), (x, y, sqrW, sqrH))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            done = True
    clock.tick(10)

pygame.quit()

print("------------------------------------------------------------")  # 60個

#wobblingEllipse.py

pygame_name = 'pygame 12'
screen = init_pygame(pygame_name, white)

windowSize = [400, 300]
clock = pygame.time.Clock()

width = 200
height = 200
x = windowSize[0] / 2 - width / 2
y = windowSize[1] / 2 - height / 2

color = pygame.color.Color('#FF0000')
background_color = pygame.color.Color('#00FF00')

count = 0

done = False

while not done:
    screen.fill(background_color)
    pygame.draw.ellipse(screen, color, [x, y, width, height])
    width += math.cos(count) * 10
    x -= (math.cos(count) * 10) / 2
    height += math.sin(count) * 10
    y -= (math.sin(count) * 10) / 2
    count += 0.5

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            print('QUIT')
            done = True
    clock.tick(20)
    
pygame.quit()

print("------------------------------------------------------------")  # 60個

#wobblingSaveLimit.py

pygame_name = 'pygame 14'
screen = init_pygame(pygame_name, white)

windowSize = [400, 300]
clock = pygame.time.Clock()

width = 200
height = 200

x = windowSize[0] / 2 - width / 2
y = windowSize[1] / 2 - height / 2

color = pygame.color.Color('#57B0F6')

count = 0

done = False

fileNo = 0
while not done:
    screen.fill(black)
    pygame.draw.ellipse(screen, color, [x, y, width, height])
    width += math.cos(count) * 10
    x -= (math.cos(count) * 10) / 2
    height += math.sin(count) * 10
    y -= (math.sin(count) * 10) / 2
    count += 0.5

    pygame.display.flip()
    if fileNo < 20:
    	# 偽存圖
        #pygame.image.save(screen, "circle" + str(fileNo) + ".png")
        fileNo += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            done = True
    clock.tick(24)

pygame.quit()

print("------------------------------------------------------------")  # 60個

#button.py

pygame_name = 'pygame 15'
screen = init_pygame(pygame_name, white)

windowSize = [400, 300]
clock = pygame.time.Clock()

btnColor = pygame.color.Color("#A45C8F")

btnWidth = 200
btnLength = 150
btnX = (windowSize[0] - btnWidth) / 2
btnY = (windowSize[1] - btnLength) / 2

toggled = False
pos = (0, 0)

done = False
while not done:
    if toggled:
        screen.fill(black)
    else:
        screen.fill(white)

    pygame.draw.rect(screen, btnColor, [btnX, btnY, btnWidth, btnLength])

    if btnX <= pos[0] <= btnX + btnWidth and btnY <= pos[1] <= btnY + btnLength:
        toggled = not toggled
        pos = (0, 0)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            done = True
    pygame.display.flip()
    clock.tick(10)

pygame.quit()

print("------------------------------------------------------------")  # 60個

#explosions.py

pygame_name = 'pygame 16'
screen = init_pygame(pygame_name, white)

def randColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

windowSize = [400, 300]
clock = pygame.time.Clock()

color = randColor

count = 0
click = False
limit = 30
pos = (0, 0)

done = False
while not done:
    screen.fill(black)

    if click and count < limit:
        pygame.draw.circle(screen, color, pos, count)
        count += 1
        if count >= limit:
            click = False

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            click = True
            count = 0
            color = randColor()
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            done = True
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

print("------------------------------------------------------------")  # 60個

#mesh.py

pygame_name = 'pygame 17'
screen = init_pygame(pygame_name, white)

windowSize = [400, 300]
clock = pygame.time.Clock()

points = []

done = False
while not done:
    screen.fill(black)
    if len(points) > 10:
        del points[0]
    if len(points) > 1:
        pygame.draw.lines(screen, white, True, points)
    for point in points:
        pygame.draw.line(screen, white, point, [point[0], windowSize[1]])

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            points.append(pos)
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            done = True
    pygame.display.flip()
    clock.tick(10)

pygame.quit()

print("------------------------------------------------------------")  # 60個

#mousePos.py

pygame_name = 'pygame 18'
screen = init_pygame(pygame_name, white)

windowSize = [400, 300]
clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            done = True
pygame.quit()


print("------------------------------------------------------------")  # 60個

#mouseTrails.py

pygame_name = 'pygame 19'
screen = init_pygame(pygame_name, white)

windowSize = [400, 300]
clock = pygame.time.Clock()

points = []

done = False
while not done:
    screen.fill(black)
    pos = pygame.mouse.get_pos()
    if pos[0] != 0 and pos[1] != 0:
        points.append(pos)
    if len(points) >= 20:
        del points[0]

    if len(points) > 2:
        pygame.draw.aalines(screen, white, False, points)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            done = True
    pygame.display.flip()
    clock.tick(30)

pygame.quit()

print("------------------------------------------------------------")  # 60個

#movingTarget.py

pygame_name = 'pygame 20'
screen = init_pygame(pygame_name, white)

windowSize = [400, 300]
clock = pygame.time.Clock()

btnColor = pygame.color.Color("#A45C8F")

btnWidth = 50
btnLength = 20
btnX = (windowSize[0] - btnWidth) / 2
btnY = (windowSize[1] - btnLength) / 2

toggled = False
pos = (0, 0)

points = 0

done = False
while not done:
    if toggled:
        screen.fill(black)
    else:
        screen.fill(white)

    pygame.draw.rect(screen, btnColor, [btnX, btnY, btnWidth, btnLength])

    if btnX <= pos[0] <= btnX + btnWidth and btnY <= pos[1] <= btnY + btnLength:
        toggled = not toggled
        pos = (0, 0)
        points += 1

    btnX += random.randint(-1 - points, 1 + points)
    btnY += random.randint(-1 - points, 1 + points)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            done = True
    pygame.display.flip()
    clock.tick(10)

pygame.quit()

print(points)

print("------------------------------------------------------------")  # 60個
print("畫圖畫字")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

pygame_name = 'pygame 21 畫圖綜合'
screen = init_pygame(pygame_name, gray)

#pygame.display.flip()

print("畫直線")
line_width = 10  # 線寬
x1, y1 = 50, 50
x2, y2 = 250, 50
# 畫直線 色 起 終 寬
pygame.draw.line(screen, red, (x1, y1), (x2, y2), line_width)
pygame.draw.line(screen, red, (x1, y1 + 50), (x2, y2 + 50), 30)
pygame.draw.line(screen, red, (x1, y1 + 100), (x2, y2 + 100), 15)
pygame.draw.line(screen, red, (x1, y1 + 150), (x2, y2 + 150))  # 無line_width, 即 1 點

# 反鋸齒直線
pygame.draw.aaline(screen, black, [10, 10], [30 + 200, 25 + 200])
pygame.draw.aaline(screen, black, [40, 10], [60 + 200, 25 + 200])

# 繪製矩形
x_st, y_st, w, h = 20, 250, 100, 50
pygame.draw.rect(screen, green, (x_st, y_st, w, h))

y_st = y_st +60
pygame.draw.rect(screen, blue, (x_st, y_st, w, h))

#繪製綠框、內塗紅色矩形
pygame.draw.rect(screen, green, (150, 235, 120, 120))
pygame.draw.rect(screen, red, (140, 225, 140, 140), 10)


# 繪製五個同心圓
cx = 400
cy = 300
radius_1 = 100
radius_2 = 80
radius_3 = 60
radius_4 = 40
radius_5 = 20
pygame.draw.circle(screen, white, (cx, cy), radius_1)
pygame.draw.circle(screen, red, (cx, cy), radius_2)
pygame.draw.circle(screen, green, (cx, cy), radius_3)
pygame.draw.circle(screen, blue, (cx, cy), radius_4)
pygame.draw.circle(screen, yellow, (cx, cy), radius_5)

# 繪製圓形
cx = 650
cy = 300
pygame.draw.circle(screen, red, (cx, cy), 20, 10)
pygame.draw.circle(screen, yellow, (cx, cy), 40, 10)
pygame.draw.circle(screen, green, (cx, cy), 60, 10)
pygame.draw.circle(screen, aqua, (cx, cy), 80, 10)
pygame.draw.circle(screen, fuchsia, (cx, cy), 100, 10)
pygame.draw.circle(screen, blue, (cx, cy), 120, 10)
pygame.draw.circle(screen, gray, (cx, cy), 140, 10)

pygame.draw.circle(screen, red, [500, 500], 100)

#繪製半徑為40的黃色實心圓形
pygame.draw.circle(screen, red, (103+300, 103), 82, 12)
pygame.draw.circle(screen, yellow, (100+300, 100), 80)

#繪製橢圓形
x_st, y_st, w, h = 50, 450, 70, 30
pygame.draw.ellipse(screen, RosyBrown, (x_st, y_st, w, h), 8)

x_st, y_st, w, h = 50, 500, 65, 25
pygame.draw.ellipse(screen, fuchsia, (x_st, y_st, w, h), 5)

x_st, y_st, w, h = 150, 450, 200, 100
pygame.draw.ellipse(screen, yellow, [x_st, y_st, w, h])

# 繪製弧線
x_st, y_st = 400, 400
pygame.draw.arc(screen, aqua, (x_st + 15, y_st + 10, 225, 180), 0, 1.6, 8)
pygame.draw.arc(screen, red, (x_st + 20, y_st + 17, 212, 173), 0, 3.1, 8)
pygame.draw.arc(screen, fuchsia, (x_st + 28, y_st + 27, 195, 157), 0, 4.7, 8)
pygame.draw.arc(screen, green, (x_st + 38, y_st + 37, 173, 137), 0, 9.9, 8)
pygame.draw.arc(screen, aqua, (x_st+150, y_st, 200, 185), 4.3, 2.0, 8)

# 畫多邊形
x_st, y_st = 550, 20
pygame.draw.polygon(screen, red, ((x_st, y_st), (x_st+50, y_st+100), (x_st-50, y_st+100)))

x_st, y_st = 550, 0
pygame.draw.polygon(
    screen, blue, [(x_st+15, y_st+120), (x_st+65, y_st+35), (x_st+185, y_st+35), (x_st+230, y_st+120), (x_st+130, y_st+180)], 6
)

pygame.display.flip()

run_pygame()

print("------------------------------------------------------------")  # 60個

x_st, y_st = 20, 20
dx, dy = 400, 40
font_size = 30

pygame_name = 'pygame 24 畫圖綜合 繪製文字'
screen = init_pygame(pygame_name, white)

#產生Surface物件, 上色，繪製成形
surface = pygame.Surface(screen.get_size())
#print(surface.get_width(), surface.get_height())
surface = surface.convert()#產生副本
surface.fill((255, 255, 255))  #surface填滿指定色

font1 = pygame.font.Font(font_filename, font_size)
text1 = font1.render("顯示中文", True, (255, 0, 0), (255, 255, 255))  # 中文,不同背景色
surface.blit(text1, (x_st+dx*0, y_st+dy*0))

text2 = font1.render("Welcome to the United States 1", True, (0, 0, 255), (0, 255, 0))  # 英文,相同背景色
surface.blit(text2, (x_st+dx*0, y_st + dy*1))
screen.blit(surface, (0, 0))

ft = pygame.font.SysFont("Malgun Gothic", font_size)  # sugar有此字型 但kilo無

wd1 = ft.render("Welcome to the United States 2", False, aqua)
screen.blit(wd1, (x_st+dx*0, y_st + dy*2))

wd2 = ft.render("黃河之水天上來", True, green, yellow)
screen.blit(wd2, (x_st+dx*0, y_st + dy*3))

ft = pygame.font.SysFont("Malgun Gothic", font_size)  # sugar有此字型 但kilo無
wd1 = ft.render("萬象更新", False, green)
screen.blit(wd1, (x_st+dx*0, y_st + dy*4))

wd2 = ft.render("Welcome to the United States 3", True, red)
screen.blit(wd2, (x_st+dx*0, y_st + dy*5))

ft = pygame.font.SysFont("Malgun Gothic", font_size)  # sugar有此字型 但kilo無
#ft = pygame.font.SysFont("Arial", font_size)#fail
wd1 = ft.render("Welcome to the United States 4", False, blue, aqua)
screen.blit(wd1, (x_st+dx*0, y_st + dy*6))

wd2 = ft.render("百科全書", True, red, aqua)
screen.blit(wd2, (x_st+dx*0, y_st + dy*7))

wd1 = ft.render("Welcome to the United States 5", False, blue, aqua)
screen.blit(wd1, (x_st+dx*0, y_st + dy*8))

wd2 = ft.render("世界大同", True, red, aqua)
screen.blit(wd2, (x_st+dx*0, y_st + dy*9))

wd1 = ft.render("Welcome to the United States 6", False, blue, aqua)
screen.blit(wd1, (x_st+dx*0, y_st + dy*10))

wd2 = ft.render("追劇", True, red, aqua)
screen.blit(wd2, (x_st+dx*0, y_st + dy*11))

run_pygame()

print("------------------------------------------------------------")  # 60個

pygame_name = 'pygame 25 畫圖綜合 背景漸層色'
screen = init_pygame(pygame_name, gray)

width = 800
height = 800

color = pygame.color.Color("#F54455")

row = 0
done = False
while not done:
    increment = 255 / 100
    while row <= height:
        pygame.draw.rect(screen, color, (0, row, width, row + increment))
        pygame.display.flip()
        if color[2] + increment < 255:
            color[2] = color[2] + int(increment)
        row += increment

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            done = True

pygame.quit()

        

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# pygame 存圖命令
# pygame.image.save(screen, "tmp_save_pic.png")

print("------------------------------------------------------------")  # 60個


'''


print("------------------------------------------------------------")  # 60個

# 基本架構
import pygame

pygame.init()  # 啟動Pygame

screen = pygame.display.set_mode((640, 320))  # 建立繪圖視窗
pygame.display.set_caption("基本架構")  # 繪圖視窗標題

background = pygame.Surface(screen.get_size())  # 建立畫布
background = background.convert()
background.fill((255, 255, 255))  # 畫布為白色
screen.blit(background, (0, 0))  # 在繪圖視窗繪製畫布

pygame.display.update()  # 更新繪圖視窗
running = True
while running:  # 無窮迴圈
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 使用者按關閉鈕
            running = False
pygame.quit()  # 關閉繪圖視窗


print("------------------------------------------------------------")  # 60個

import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("基本繪圖")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

pygame.draw.circle(background, (0, 0, 0), (150, 150), 130, 4)
pygame.draw.circle(background, (0, 0, 255), (100, 120), 25, 0)
pygame.draw.circle(background, (0, 0, 255), (200, 120), 25, 0)
pygame.draw.ellipse(background, (255, 0, 255), [135, 130, 30, 80], 0)
pygame.draw.arc(background, (255, 0, 0), [80, 130, 150, 120], 3.4, 6.1, 9)
screen.blit(background, (0, 0))

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


print("------------------------------------------------------------")  # 60個

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 320))
pygame.display.set_caption("動畫基本架構")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

clock = pygame.time.Clock()  # 建立時間元件

running = True
while running:
    clock.tick(30)  # 每秒執行30次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))  # 清除繪圖視窗

    pygame.display.update()  # 更新繪圖視窗
pygame.quit()  # 關閉繪圖視窗


print("------------------------------------------------------------")  # 60個


"""
# https://gamedevacademy.org/pygame-time-clock-tutorial-complete-guide/
#Tracking Frames Per Second (FPS)

import pygame
pygame.init()
clock = pygame.time.Clock()
cnt = 0
while True:
    clock.tick(60)
    cnt += 1
    if cnt % 60 == 0:
        print('a')
    if cnt > 1000:
        break


print("程式執行完畢！")
"""


print("pygame 讀取 鍵盤輸入")

pygame.init()

windowSize = [400, 300]
pygame.display.set_mode(windowSize)

done = False
while not done:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_1]:
        print("你按了鍵盤 1")

    if keys[pygame.K_2]:
        print("你按了鍵盤 2")

    if keys[pygame.K_3]:
        print("你按了鍵盤 3")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
