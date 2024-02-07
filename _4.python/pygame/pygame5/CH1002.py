import pygame, sys # 滙入PyGame套件，系統模組

pygame.init() # 將PyGame初始化

#設定使用參數
size = width, height = 250, 190
White = (255, 255, 255)



#(1)產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption('產生畫布')



#(2).產生Surface物件, 上色，繪製成形
face = pygame.Surface([120, 120])
face.fill(White)
screen.blit(face, (20, 20))



#(3).偵測視窗是否被關閉
while True:
   for event in pygame.event.get():
      
      # 判斷事件的常數是否為QUIT常數
      if event.type == pygame.QUIT:
         pygame.quit() #quit()方法結束Pygame程序
         sys.exit()
      
   pygame.display.update()
