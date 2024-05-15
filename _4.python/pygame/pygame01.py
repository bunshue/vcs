"""
pygame 測試大全

"""

import sys
import time
import pygame

W, H = 800, 600
screen_size = (W, H)    # 設定屏幕尺寸

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

print('pygame 01')

pygame.init()  # 初始化Pygame
screen = pygame.display.set_mode(screen_size)   # 創建屏幕
pygame.display.set_caption('pygame測試01')

#利用screen物件來作為畫布，以fill()方法填上顏色
screen.fill(white)

#方法load()載入圖片，convert()能提高圖片的處理速度
image=pygame.image.load(filename)
#设置图片大小
image=pygame.transform.scale(image,(200, 300))
#绘制视频画面
screen.blit(image,(2,2))

run_pygame()

print('------------------------------------------------------------')	#60個

print('pygame 02')

pygame.init()  # 初始化Pygame
screen = pygame.display.set_mode(screen_size)   # 創建屏幕
pygame.display.set_caption('pygame測試02')

print("取得screen參數")
print(screen.get_size())

#利用screen物件來作為畫布，以fill()方法填上顏色
screen.fill(white)

#方法load()載入圖片，convert()能提高圖片的處理速度
img = pygame.image.load(filename)
img.convert()
x_st, y_st = 200, 100
screen.blit(img, (x_st, y_st))

run_pygame()

print('------------------------------------------------------------')	#60個

print('pygame 03')

pygame.init()  # 初始化Pygame
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('pygame測試03 載入圖片')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,255,0))#設定背景顏色

#方法load()載入圖片，convert()能提高圖片的處理速度
image = pygame.image.load(filename)
image.convert()
x_st, y_st = 20, 20
background.blit(image, (x_st, y_st))

screen.blit(background, (0,0))

run_pygame()

print('------------------------------------------------------------')	#60個

print('pygame 04')

pygame.init()  # 初始化Pygame

#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((W, H), 0, 32)
pygame.display.set_caption('pygame測試04 載入圖片')

#利用screen物件來作為畫布，以fill()方法填上顏色
screen.fill(white)

#方法load()載入圖片，convert()能提高圖片的處理速度
img = pygame.image.load(filename)
img.convert()
x_st, y_st = 20, 20
screen.blit(img, (x_st, y_st))

run_pygame()

print('------------------------------------------------------------')	#60個

print('pygame 05')

pygame.init()  # 初始化Pygame
screen = pygame.display.set_mode(screen_size)   # 創建屏幕
pygame.display.set_caption('pygame測試05')

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

print('pygame 06 最簡單python')

pygame.init()   # 將PyGame初始化
#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('pygame測試06')

run_pygame()

print("------------------------------------------------------------")  # 60個

print('pygame 07')

pygame.init()   # 將PyGame初始化
# 產生視窗，以Surface物件回傳
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('pygame測試07')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
img = pygame.image.load(filename)

x_st, y_st = 100, 100
screen.blit(img, (x_st, y_st))

run_pygame()

print("------------------------------------------------------------")  # 60個

print('pygame 08')

pygame.init() # 將PyGame初始化
# 產生視窗，以Surface物件回傳
screen = pygame.display.set_mode(screen_size, 0, 32)
pygame.display.set_caption('pygame測試08 產生畫布')

# 產生Surface物件, 上色，繪製成形
face = pygame.Surface([120, 120])
face.fill(white)
screen.blit(face, (20, 20))

run_pygame()

print("------------------------------------------------------------")  # 60個

print('pygame 09')

pygame.init()      # 將PyGame初始化

# 產生視窗，以Surface物件回傳
screen = pygame.display.set_mode(screen_size, 0)
pygame.display.set_caption('pygame測試09 白色畫布')

# 產生Surface物件, 上色，繪製成形
face = pygame.Surface(screen.get_size())
print(face.get_width(), face.get_height())
face.convert()           # 產生副本
face.fill(white)         # 填滿白色
screen.blit(face, (0, 0))# 輸出到畫布上

run_pygame()

print("------------------------------------------------------------")  # 60個

print('pygame 10')

pygame.init()      # 將PyGame初始化

# 產生視窗，以Surface物件回傳
screen = pygame.display.set_mode(screen_size, 0)
pygame.display.set_caption('pygame測試10 繪製圓弧')

# 產生Surface物件, 上色，繪製成形
face = pygame.Surface(screen.get_size())
screen.fill(gray)         # 填滿灰色

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

run_pygame()

print("------------------------------------------------------------")  # 60個

print('pygame 11')

pygame.init() #將PyGame初始化

#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode(screen_size, 0, 32)
pygame.display.set_caption('pygame測試11 draw')

#利用Surface物件來作為畫布，以fill()方法填上白色
screen.fill(white)

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

run_pygame()

print("------------------------------------------------------------")  # 60個

print('pygame 12')

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_cat/cat3.png'

pygame.init() #將PyGame初始化
#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode(screen_size, 0, 32)
pygame.display.set_caption('pygame測試12 載入圖片')

screen.fill(white)

#方法load()載入圖片，convert()能提高圖片的處理速度
img = pygame.image.load(filename)
img.convert()
screen.blit(img, (20, 20))

run_pygame()

print("------------------------------------------------------------")  # 60個

print('pygame 12')

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_cat/cat3.png'

pygame.init() #將PyGame初始化
#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode(screen_size, 0, 32)
pygame.display.set_caption('pygame測試12 Animation')

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

print('pygame 13')

pygame.init() #將PyGame初始化
#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode(screen_size, 0, 32)
pygame.display.set_caption('pygame測試13 繪製文字')

screen.fill(grey)

#繪製文字
#ft = pygame.font.SysFont('Malgun Gothic', 36)
ft = pygame.font.SysFont('微軟正黑體', 36)
wd1 = ft.render('Hello Python', False, aqua)
screen.blit(wd1, (10, 20))
#wd2 = ft.render('黃河之水天上來', True, green, yellow)
#screen.blit(wd2, (10, 80))

run_pygame()

print("------------------------------------------------------------")  # 60個

print('pygame 14')

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_cat/cat3.png'

from pygame.locals import *

pygame.init() #將PyGame初始化
#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode(screen_size, 0, 32)
pygame.display.set_caption('pygame測試14 按鍵事件')

#載入圖片並設座標
face = pygame.image.load(filename).convert()
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

      screen.blit(face, (carX, carY))
      pygame.display.update()

print("------------------------------------------------------------")  # 60個

print('pygame 15')

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_cat/cat3.png'

from pygame.locals import *

pygame.init() #將PyGame初始化
#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode(screen_size, 0, 32)
pygame.display.set_caption('pygame測試15 滑鼠事件')

# 載入圖片並設座標
imgeRect = pygame.image.load(filename).convert_alpha()
imgeX, imgeY = 0, 0   # 起始位置
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
      imgeX, imgeY = pygame.mouse.get_pos()
      
      # 取得座標讓圖片不要超過視窗範圍
      imgeX -= imgeRect.get_width()/2
      imgeY -= imgeRect.get_height()/2
      print(imgeX, imgeY)
   else:
      moving = False

   screen.blit(imgeRect, (imgeX, imgeY))
   pygame.display.update()

print("------------------------------------------------------------")  # 60個

print('pygame 16')

filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_cat/cat3.png'

import random, math

pygame.init() #將PyGame初始化
#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode(screen_size, 0, 32)
pygame.display.set_caption('pygame測試16 碰撞的偵測')

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

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


