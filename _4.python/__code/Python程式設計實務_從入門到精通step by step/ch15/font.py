import pygame #滙入PyGame套件
import sys
pygame.init() #將PyGame初始化

#設定使用參數
size = width, height = 400, 400
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
pygame.display.set_caption('繪製文字')
screen.fill(White)
#繪製文字
#ft = pygame.font.SysFont('Malgun Gothic', 36)
ft = pygame.font.SysFont('Arial', 36)
wd1 = ft.render('Encyclopedia', False, Blue,Aqua)
screen.blit(wd1, (10, 20))
wd2 = ft.render('百科全書', True, Red,Aqua)
screen.blit(wd2, (10, 80))
wd1 = ft.render('lockdown', False, Blue,Aqua)
screen.blit(wd1, (10, 140))
wd2 = ft.render('封城', True, Red,Aqua)
screen.blit(wd2, (10, 200))
wd1 = ft.render('binge-watch', False, Blue,Aqua)
screen.blit(wd1, (10, 260))
wd2 = ft.render('追劇', True, Red,Aqua)
screen.blit(wd2, (10, 320))

running = True #判斷程式是否執行狀態
while running:
   for event in pygame.event.get():
      #判斷事件的常數是否為QUIT常數
      if event.type == pygame.QUIT:
         pygame.quit() #quit()方法結束Pygame程序
         sys.exit()
   pygame.display.update()
