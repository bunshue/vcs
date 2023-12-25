import pygame #滙入PyGame套件
import sys
pygame.init() #將PyGame初始化

#設定使用參數
size = width, height = 300, 300
White = (255, 255, 255)


#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption('載入圖片')
screen.fill(White)
#方法load()載入圖片，convert()能提高圖片的處理速度
img = pygame.image.load('pic\\card.jpg')
img.convert()
screen.blit(img, (50, 50))

running = True #判斷程式是否執行狀態
while running:
   for event in pygame.event.get():
      #判斷事件的常數是否為QUIT常數
      if event.type == pygame.QUIT:           
         pygame.quit() #quit()方法結束Pygame程序
         sys.exit()
   pygame.display.update()
