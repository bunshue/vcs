import pygame #滙入PyGame套件
import sys


print("------------------------------------------------------------")  # 60個

pygame.init() #將PyGame初始化

#設定使用參數
size = width, height = 560, 500
speed = [1, 1]
White = (255, 255, 255)

#設定每秒畫格25，利用Clock()方法來確保動畫能持續進行
Fps = 25 #每秒的執行次數
traceCar = pygame.time.Clock()

#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption('動畫')

#載入圖片，get_rect()取得矩形區域
car = pygame.image.load('pic\\cart.jpg')
carX, carY = 50, 50 #設定開始移動的X、Y座標
move = 'Down'
traceCar = pygame.time.Clock()

#tick()方法依據fps之值讓移動圖片有動畫效果
#blit()不斷在畫布上繪製圖片
#update()進行動作的更新
while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

   screen.fill(White)
   
   if move == 'Down':
      carY += 5
      if carY == 230 : move = 'Right'
   elif move == 'Right':
      carX += 5
      if carX == 315 : move = 'Up'
   elif move == 'Up':
      carY -= 5
      if carY == 50 : move = 'Left'
   elif move == 'Left':
      carX -= 5
      if carX == 50: move = 'Down'
   #blit()方法在畫布上繪製圖片
   screen.blit(car, (carX, carY))
   pygame.display.update()
   traceCar.tick(Fps) #依fps的值來產生動畫



print("------------------------------------------------------------")  # 60個







import pygame, sys
from pygame.locals import *

pygame.init() #將PyGame初始化

#設定使用參數
size = width, height = 600, 600
White = 255, 255, 255

#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption('滑鼠事件')

#載入圖片並設座標
imge = 'pic\\attend.jpg'
imgeRect = pygame.image.load(imge)
imgeX, imgeY = 0, 0   #起始位置
moveing = False #移動圖片

while True:
   for event in pygame.event.get():
      #判斷事件的常數是否為QUIT常數
      if event.type == pygame.QUIT:
         pygame.quit() #quit()方法結束Pygame程序
         sys.exit()
   screen.fill(White)
   #偵測滑鼠的按鈕
   buts = pygame.mouse.get_pressed()
      
   #按下滑鼠左鍵才能移動圖片
   if buts[0]:
      moving = True
      #取得滑鼠座標
      imgeX, imgeY = pygame.mouse.get_pos()
      #取得座標讓圖片不要超過視窗範圍
      imgeX -= imgeRect.get_width()/2
      imgeY -= imgeRect.get_height()/2
   else:
      moving = False
   screen.blit(imgeRect, (imgeX, imgeY))
   pygame.display.update()






print("------------------------------------------------------------")  # 60個





import pygame, sys
from pygame.locals import *

pygame.init() #將PyGame初始化

#設定使用參數
size = width, height = 500, 500
White = (255, 255, 255)

#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption('按鍵事件')

#載入圖片並設座標
car = 'pic\car.jpg'
face = pygame.image.load(car).convert()
carX, carY = 0, 0   #起始位置
Xmove, Ymove = 0, 0 #移動座標

while True:
   for event in pygame.event.get():
      #判斷事件的常數是否為QUIT常數
      if event.type == pygame.QUIT:
         pygame.quit() #quit()方法結束Pygame程序
         sys.exit()

      screen.fill((White))

      #判斷那個按鍵被按？
      if event.type == KEYDOWN:
         #向上方向鍵，減少座標值
         if event.key == pygame.K_UP:
            Ymove -= 2
         #向下方向鍵，增加座標值
         elif event.key == pygame.K_DOWN:
            Ymove += 2
         #向左方向鍵，減少座標值
         elif event.key == pygame.K_LEFT:
            Xmove -= 2
         #向右方向鍵，增加座標值
         elif event.key == pygame.K_RIGHT:
            Xmove += 2
         
         #計算座標值
         carX += Xmove; carY += Ymove

      #放掉鍵盤按鍵，回到原點
      if event.type == pygame.KEYUP:
         if carX < 0 or carY < 0:
            carX, carY = 0, 0
            Xmove ,Ymove = 0, 0
         if carX == 300 or carY == 300:
            carX, carY = 0, 0
            Xmove ,Ymove = 0, 0
      screen.blit(face, (carX, carY))
      pygame.display.update()





print("------------------------------------------------------------")  # 60個



        

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


        

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



