import pygame #滙入PyGame套件
import sys
pygame.init() #將PyGame初始化

#設定使用參數
size = width, height = 400, 300
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)
Fuchsia = (255, 0, 255) #紫色
Aqua = (0, 255, 255) #淺藍色
Gray = (128, 128, 128) #灰色

#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption('繪製矩形')

#利用Surface物件來作為畫布，以fill()方法填上白色
screen.fill(White)

#繪製綠色矩形
pygame.draw.rect(screen, Green, (30, 210, 140, 40))
pygame.draw.rect(screen, Blue, (204, 198, 60, 40))
pygame.draw.rect(screen, Yellow, (304, 190, 60, 40))
pygame.draw.rect(screen, Green, (30, 130, 140, 40))
pygame.draw.rect(screen, Blue, (204, 118, 60, 40))
pygame.draw.rect(screen, Yellow, (304, 110, 60, 40))

running = True #判斷程式是否執行狀態
while running:
   for event in pygame.event.get():
      #判斷事件的常數是否為QUIT常數
      if event.type == pygame.QUIT:           
         pygame.quit() #quit()方法結束Pygame程序
         sys.exit()
   pygame.display.update()
