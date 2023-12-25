import pygame #滙入PyGame套件
import sys
pygame.init() #將PyGame初始化

#設定使用參數
size = width, height = 300, 300
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
pygame.display.set_caption('晝圖練習')

#填上白色
screen.fill(Gray)

#繪製圓形
pygame.draw.circle(screen, Red, (140, 130), 120, 12)
pygame.draw.circle(screen, Green, (140, 130), 120, 10)
pygame.draw.circle(screen, Blue, (140, 130), 120, 8)
pygame.draw.circle(screen, Blue, (193, 113), 50)
pygame.draw.circle(screen, Green, (193, 113), 40)
pygame.draw.circle(screen, Yellow, (193, 113), 30)

#繪製矩形
pygame.draw.rect(screen, Green, (55, 100, 60, 20))
pygame.draw.rect(screen, Yellow, (75, 120, 60, 20))

running = True #判斷程式是否執行狀態
while running:
   for event in pygame.event.get():
      #判斷事件的常數是否為QUIT常數
      if event.type == pygame.QUIT:           
         pygame.quit() #quit()方法結束Pygame程序
         sys.exit()
   pygame.display.update()
