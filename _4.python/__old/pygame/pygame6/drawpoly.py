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
pygame.display.set_caption('繪製多邊形')

#利用Surface物件來作為畫布，以fill()方法填上白色
screen.fill(White)

pygame.draw.polygon(screen, Red, ((15, 180),
(130, 10), (235, 180)))
pygame.draw.polygon(screen, Blue, [(15, 120), (65, 35),
      (185, 35), (230, 120), (130, 180)], 6)

running = True #判斷程式是否執行狀態
while running:
   for event in pygame.event.get():
      #判斷事件的常數是否為QUIT常數
      if event.type == pygame.QUIT:           
         pygame.quit() #quit()方法結束Pygame程序
         sys.exit()
   pygame.display.update()
