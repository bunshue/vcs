import pygame, sys # 滙入PyGame套件，系統模組

pygame.init()      # 將PyGame初始化

#設定使用參數
size = width, height = 250, 190
White = (255, 255, 255)

#(1).產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size), 0)
pygame.display.set_caption('白色畫布')



#(2)產生Surface物件, 上色，繪製成形
face = pygame.Surface(screen.get_size())
print(face.get_width(), face.get_height())
face.convert()           # 產生副本
face.fill(White)         # 填滿白色
screen.blit(face, (0, 0))# 輸出到畫布上
pygame.display.update()  # 繪製視窗顯示於螢幕上



#(3).偵測視窗是否被關閉
while True:
   for event in pygame.event.get():
      #判斷事件的常數是否為QUIT常數
      if event.type == pygame.QUIT:
         pygame.quit() #quit()方法結束Pygame程序
         sys.exit()
