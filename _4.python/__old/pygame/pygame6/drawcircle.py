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
pygame.display.set_caption('畫圓形')

#利用Surface物件來作為畫布，以fill()方法填上白色
screen.fill(White)

#繪製圓形
pygame.draw.circle(screen, Red, (200, 150), 20, 10)
pygame.draw.circle(screen, Yellow, (200, 150),40, 10)
pygame.draw.circle(screen, Green, (200, 150), 60,10)
pygame.draw.circle(screen, Aqua, (200, 150), 80, 10)
pygame.draw.circle(screen, Fuchsia, (200, 150),100, 10)
pygame.draw.circle(screen, Blue, (200, 150), 120,10)
pygame.draw.circle(screen, Gray, (200, 150), 140, 10)

running = True #判斷程式是否執行狀態
while running:
   for event in pygame.event.get():
      #判斷事件的常數是否為QUIT常數
      if event.type == pygame.QUIT:           
         pygame.quit() #quit()方法結束Pygame程序
         sys.exit()
   pygame.display.update()
