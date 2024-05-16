"""
pygame 測試大全

1. 一般
2. 畫圖畫字
3. 滑鼠鍵盤

最後再搬出

"""

import sys
import time
import math
import random
import pygame

W, H = 800, 600
screen_size = (W, H)    # 設定屏幕尺寸
surface_size = (W-50, H-50)    # 設定surface尺寸

# 設定顏色
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

RosyBrown = 255, 193, 193 # 玫紅色
fuchsia = (255, 0, 255) #紫色
aqua = (0, 255, 255) #淺藍色
gray = (128, 128, 128) #灰色
grey = 79, 79, 79        # 灰色

# 設定顏色, same
red = pygame.color.Color('#FF0000')
green = pygame.color.Color('#00FF00')
blue = pygame.color.Color('#0000FF')
black = pygame.color.Color('#000000')
white = pygame.color.Color('#FFFFFF')

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

def init_pygame(name, color):
   print(name)
   pygame.init()  # 初始化Pygame
   
   screen = pygame.display.set_mode(screen_size)  # 產生視窗screen
   #screen = pygame.display.set_mode(screen_size, 0, 32)  # 產生視窗screen
   #screen = pygame.display.set_mode(screen_size, 0)  # 產生視窗screen
   
   pygame.display.set_caption(name)
   
   #print("取得screen參數 :", screen.get_size())
   
   #利用screen物件來作為畫布，以fill()方法填上顏色
   screen.fill(color)
   return screen

def run_pygame():
   # 更新屏幕, 保持屏幕打開, 直到用戶退出, 偵測視窗是否被關閉(8)
   pygame.display.update()
   running = True
   while running:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
   pygame.quit()

print("------------------------------------------------------------")  # 60個

pygame_name = 'pygame 01'
screen = init_pygame(pygame_name, yellow)

#方法load()載入圖片，convert()能提高圖片的處理速度
image=pygame.image.load(filename)
image.convert()

#设置图片大小
image=pygame.transform.scale(image,(200, 300))

#绘制视频画面
x_st, y_st = 100, 100
screen.blit(image, (x_st, y_st))

run_pygame()

print('------------------------------------------------------------')	#60個

pygame_name = 'pygame 02 建立畫布'
screen = init_pygame(pygame_name, yellow)

# 產生Surface物件, 上色，繪製成形
surface = pygame.Surface(surface_size)
#print(surface.get_width(), surface.get_height())
surface.convert()           # 產生副本
surface.fill((0,255,0))#設定surface背景顏色

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
surface = surface.convert()
surface.fill((0,255,0))#設定surface背景顏色

print('讀取圖片貼到surface上')
#方法load()載入圖片，convert()能提高圖片的處理速度
image = pygame.image.load(filename)
image.convert()
x_st, y_st = 100, 100
surface.blit(image, (x_st, y_st))

print('將surface貼到screen上')
screen.blit(surface, (25, 25))

run_pygame()

print('------------------------------------------------------------')	#60個

pygame_name = 'pygame 04 不使用surface 載入圖片'
screen = init_pygame(pygame_name, white)

#方法load()載入圖片，convert()能提高圖片的處理速度
image = pygame.image.load(filename)
image.convert()

x_st, y_st = 100, 100
screen.blit(image, (x_st, y_st))

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
       if event.type == pygame.QUIT:
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
   pygame.display.update()
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
      
      #判斷事件的常數是否為QUIT常數
      if event.type == pygame.QUIT:
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

      screen.blit(surface, (carX, carY))
      pygame.display.update()

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
      
      #判斷事件的常數是否為QUIT常數
      if event.type == pygame.QUIT:
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
   pygame.display.update()

print("------------------------------------------------------------")  # 60個

pygame_name = 'pygame 08 偵測滑鼠位置'
screen = init_pygame(pygame_name, white)

clock = pygame.time.Clock()

pos_list = []

# 更新屏幕
pygame.display.update()

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
        #判斷事件的常數是否為QUIT常數
        if event.type == pygame.QUIT:
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
       if event.type == pygame.QUIT:
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
   pygame.display.update()
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
        if event.type == pygame.QUIT:
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
        if event.type == pygame.QUIT:
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
        if event.type == pygame.QUIT:
            print('QUIT')
            done = True
    clock.tick(20)
    
pygame.quit()

print("------------------------------------------------------------")  # 60個

#wobblingSave.py

pygame_name = 'pygame 13'
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
    # pygame ¦s¹ϩR¥O
    pygame.image.save(screen, "circle" + str(fileNo) + ".png")
    fileNo += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(24)
    
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
    	# pygame ¦s¹ϩR¥O
        pygame.image.save(screen, "circle" + str(fileNo) + ".png")
        fileNo += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
        if event.type == pygame.QUIT:
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
        if event.type == pygame.QUIT:
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
        if event.type == pygame.QUIT:
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
        if event.type == pygame.QUIT:
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
        if event.type == pygame.QUIT:
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
        if event.type == pygame.QUIT:
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

color = pygame.color.Color("#0A32F4")

pygame.draw.rect(screen, color, [620, 620, 160, 160])  # x_st, y_st, w, h
pygame.display.flip()

for i in range(7):
    # 畫線
    pygame.draw.line(screen, red, [0, 100 * i], [W, 100 * i])
    pygame.draw.line(screen, red, [100 * i, 0], [100 * i, H])
    # 繪製矩形
    pygame.draw.rect(screen, green, (100 * i, 0, 50, 50))
    pygame.draw.rect(screen, blue, (0, 100 * i, 50, 50))

# 繪製線條
pygame.draw.line(screen, red, (70, 0), (70, 200), 20)
pygame.draw.line(screen, green, (90, 0), (90, 200), 20)
pygame.draw.line(screen, blue, (110, 0), (110, 200), 20)
pygame.draw.line(screen, yellow, (130, 0), (130, 200), 20)
pygame.draw.line(screen, fuchsia, (150, 0), (150, 200), 20)
pygame.draw.line(screen, aqua, (170, 0), (170, 200), 20)
pygame.draw.line(screen, gray, (190, 0), (190, 200), 20)

# 繪製五個同心圓
cx = 200
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
cx = 400
cy = 300
pygame.draw.circle(screen, red, (cx, cy), 20, 10)
pygame.draw.circle(screen, yellow, (cx, cy), 40, 10)
pygame.draw.circle(screen, green, (cx, cy), 60, 10)
pygame.draw.circle(screen, aqua, (cx, cy), 80, 10)
pygame.draw.circle(screen, fuchsia, (cx, cy), 100, 10)
pygame.draw.circle(screen, blue, (cx, cy), 120, 10)
pygame.draw.circle(screen, gray, (cx, cy), 140, 10)

color = pygame.color.Color("#123456")

pygame.draw.circle(screen, color, [700, 700], 50)
pygame.display.flip()

pygame.draw.ellipse(screen, yellow, [0, 500, 300, 100])

# 畫多邊形
pygame.draw.polygon(screen, red, ((15, 180), (130, 10), (235, 180)))
pygame.draw.polygon(
    screen, blue, [(15, 120), (65, 35), (185, 35), (230, 120), (130, 180)], 6
)

# 繪製文字
ft = pygame.font.SysFont("Malgun Gothic", 60)  # sugar有此字型 但kilo無
wd1 = ft.render("萬象更新", False, green)
screen.blit(wd1, (300, 420))
wd2 = ft.render("brand new", True, red)
screen.blit(wd2, (300, 500))

# ft = pygame.font.SysFont('Malgun Gothic', 36)
ft = pygame.font.SysFont("Arial", 36)
wd1 = ft.render("Encyclopedia", False, blue, aqua)
screen.blit(wd1, (10, 20))
wd2 = ft.render("百科全書", True, red, aqua)
screen.blit(wd2, (10, 80))
wd1 = ft.render("lockdown", False, blue, aqua)
screen.blit(wd1, (10, 140))
wd2 = ft.render("世界大同", True, red, aqua)
screen.blit(wd2, (10, 200))
wd1 = ft.render("binge-watch", False, blue, aqua)
screen.blit(wd1, (10, 260))
wd2 = ft.render("追劇", True, red, aqua)
screen.blit(wd2, (10, 320))

# 產生Surface物件, 上色，繪製成形
surface = pygame.Surface([100, 100])
print("取得surface參數")
print(surface.get_width(), surface.get_height())
surface.fill(red)
screen.blit(surface, (500, 100))

"""
#產生Surface物件, 上色，繪製成形
surface = pygame.Surface(screen.get_size())
print(surface.get_width(), surface.get_height())
surface.convert()#產生副本
surface.fill(red)#填滿指定色
screen.blit(surface, (0, 0))#輸出到畫布上
pygame.display.update()#繪製視窗顯示於螢幕上
"""

run_pygame()

print("------------------------------------------------------------")  # 60個

pygame_name = 'pygame 22 畫圖綜合'
screen = init_pygame(pygame_name, gray)

# 產生Surface物件, 上色，繪製成形
surface = pygame.Surface(surface_size)
screen.fill(gray)

#繪製綠框、內塗紅色矩形
#pygame.draw.rect(screen, green, (60, 35, 120, 120))
#pygame.draw.rect(screen, red, (50, 25, 140, 140), 10)

# 繪製一個實心三角形和框線為6的五邊形
"""
pygame.draw.polygon(screen, red, ((10, 180), (130, 10), (235, 180)))
pygame.draw.polygon(screen, white, [(15, 120), (65, 35), (185, 35), (230, 120), (130, 180)], 8)
"""

# 產生圓弧線
pygame.draw.arc(screen, aqua, (15, 10, 225, 180), 0, 1.6, 8)
pygame.draw.arc(screen, red, (20, 17, 212, 173), 0, 3.1, 8)
pygame.draw.arc(screen, fuchsia, (28, 27, 195, 157), 0, 4.7, 8)
pygame.draw.arc(screen, green, (38, 37, 173, 137), 0, 9.9, 8)
pygame.draw.line(screen, yellow, (10, 100), (240, 100), 2)
pygame.draw.line(screen, white, (125, 5), (125, 180), 2)

# 繪製五個同心圓
center_x = screen_size[0] // 2
center_y = screen_size[1] // 2

radius_1 = 200
radius_2 = 150
radius_3 = 100
radius_4 = 50
radius_5 = 20

pygame.draw.circle(screen, white, (center_x, center_y), radius_1)
pygame.draw.circle(screen, red, (center_x, center_y), radius_2)
pygame.draw.circle(screen, green, (center_x, center_y), radius_3)
pygame.draw.circle(screen, blue, (center_x, center_y), radius_4)
pygame.draw.circle(screen, yellow, (center_x, center_y), radius_5)

run_pygame()

print('------------------------------------------------------------')	#60個

pygame_name = 'pygame 23 畫圖綜合'
screen = init_pygame(pygame_name, white)

#繪製半徑為40的黃色實心圓形
pygame.draw.circle(screen, red, (103, 103), 82, 12)
pygame.draw.circle(screen, yellow, (100, 100), 80)

#繪製圓弧
pygame.draw.arc(screen, aqua, (15, 10, 200, 185), 4.3, 2.0, 8)

#繪製線條
pygame.draw.line(screen, fuchsia, (70, 220), (100, 180), 20)
pygame.draw.line(screen, green, (198, 185), (280, 30), 6)
pygame.draw.line(screen, green, (280, 30), (380, 180), 6)

#繪製綠色矩形
pygame.draw.rect(screen, green, (30, 210, 140, 40))
pygame.draw.rect(screen, gray, (204, 198, 60, 40))
pygame.draw.rect(screen, gray, (304, 190, 60, 40))

#繪製三角形
pygame.draw.polygon(screen, gray, ((281, 53), (200, 205), (371, 187)))

#繪製橢圓形
pygame.draw.ellipse(screen, RosyBrown, (250, 230, 70, 30), 8)
pygame.draw.ellipse(screen, fuchsia, (240, 258, 65, 25), 5)

# 反鋸齒直線
pygame.draw.aaline(screen, black, [10, 10], [30 + 600, 25 + 600])
pygame.draw.aaline(screen, black, [40, 10], [60 + 600, 25 + 600])

run_pygame()

print("------------------------------------------------------------")  # 60個

pygame_name = 'pygame 24 畫圖綜合 繪製文字'
screen = init_pygame(pygame_name, white)

surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((0, 255, 0))  # 背景為錄色

font_filename = "C:/Windows/Fonts/mingliu.ttc"
font1 = pygame.font.Font(font_filename, 24)  # 新細明體
text1 = font1.render("顯示中文", True, (255, 0, 0), (255, 255, 255))  # 中文,不同背景色
surface.blit(text1, (20, 10))
text2 = font1.render("Show english.", True, (0, 0, 255), (0, 255, 0))  # 英文,相同背景色
surface.blit(text2, (20, 50))
screen.blit(surface, (0, 0))
pygame.display.update()

# 繪製文字
# ft = pygame.font.SysFont('Malgun Gothic', 36)
ft = pygame.font.SysFont("微軟正黑體", 36)
wd1 = ft.render("Hello Python", False, aqua)
screen.blit(wd1, (10, 20+200))
wd2 = ft.render("黃河之水天上來", True, green, yellow)
screen.blit(wd2, (10, 80+200))

run_pygame()

print("------------------------------------------------------------")  # 60個

pygame_name = 'pygame 25 畫圖綜合 背景漸層色'
screen = init_pygame(pygame_name, gray)

width = 800
height = 800

color = pygame.color.Color("#F54455")

# [100, 100, 0]
print(color)

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
        if event.type == pygame.QUIT:
            done = True

pygame.quit()

"""
print('------------------------------------------------------------')	#60個

# 更新屏幕
pygame.display.update()

# 保持屏幕打開，直到用戶退出
#偵測視窗是否被關閉
while True:
    for event in pygame.event.get():
        #判斷事件的常數是否為QUIT常數
        if event.type == pygame.QUIT:
            pygame.quit() #quit()方法結束Pygame程序
            sys.exit()
    pygame.display.update()
"""

print("------------------------------------------------------------")  # 60個



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


