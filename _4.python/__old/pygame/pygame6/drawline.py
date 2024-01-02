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
pygame.display.set_caption('繪製線條')

#利用Surface物件來作為畫布，以fill()方法填上白色
screen.fill(White)

#繪製線條
pygame.draw.line(screen, Red, (70, 0), (70, 300), 20)
pygame.draw.line(screen, Green, (90, 0), (90, 300), 20)
pygame.draw.line(screen, Blue, (110, 0), (110, 300), 20)
pygame.draw.line(screen, Yellow, (130, 0), (130, 300), 20)
pygame.draw.line(screen, Fuchsia, (150, 0), (150, 300), 20)
pygame.draw.line(screen, Aqua, (170, 0), (170, 300), 20)
pygame.draw.line(screen, Gray, (190, 0), (190, 300), 20)


running = True #判斷程式是否執行狀態
while running:
   for event in pygame.event.get():
      #判斷事件的常數是否為QUIT常數
      if event.type == pygame.QUIT:           
         pygame.quit() #quit()方法結束Pygame程序
         sys.exit()
   pygame.display.update()
