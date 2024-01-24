import pygame, sys # 滙入PyGame套件、系統模組
from pygame.locals import *

pygame.init() #將PyGame初始化

#設定使用參數
size = width, height = 400, 270
Black = 0, 0, 0

#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption('滑鼠事件')

# 載入圖片並設座標
imge = 'Source\\004.png'
imgeRect = pygame.image.load(imge).convert_alpha()
imgeX, imgeY = 0, 0   # 起始位置
moveing = False       # 移動圖片

while True:
   for event in pygame.event.get():
      
      #判斷事件的常數是否為QUIT常數
      if event.type == pygame.QUIT:
         pygame.quit() # 結束Pygame程序
         sys.exit()
   screen.fill(Black)
   
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
