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
