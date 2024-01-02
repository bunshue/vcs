import pygame #滙入PyGame套件
import sys
pygame.init() #將PyGame初始化

#設定使用參數
size = width, height = 300, 300
Red = (255, 0, 0)

#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size), 0)
pygame.display.set_caption('將整個視窗畫布上色')

#產生Surface物件, 上色，繪製成形
face = pygame.Surface(screen.get_size())
print(face.get_width(), face.get_height())
face.convert()#產生副本
face.fill(Red)#填滿指定色
screen.blit(face, (0, 0))#輸出到畫布上
pygame.display.update()#繪製視窗顯示於螢幕上

#偵測視窗是否被關閉
while True:
   for event in pygame.event.get():
      #判斷事件的常數是否為QUIT常數
      if event.type == pygame.QUIT:
         pygame.quit() #quit()方法結束Pygame程序
         sys.exit()
