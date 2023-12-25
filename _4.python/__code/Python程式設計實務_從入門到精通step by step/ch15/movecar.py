import pygame #滙入PyGame套件
import sys

pygame.init() #將PyGame初始化

#設定使用參數
size = width, height = 560, 500
speed = [1, 1]
White = (255, 255, 255)

#設定每秒畫格25，利用Clock()方法來確保動畫能持續進行
Fps = 25 #每秒的執行次數
traceCar = pygame.time.Clock()

#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption('動畫')

#載入圖片，get_rect()取得矩形區域
car = pygame.image.load('pic\\cart.jpg')
carX, carY = 50, 50 #設定開始移動的X、Y座標
move = 'Down'
traceCar = pygame.time.Clock()

#tick()方法依據fps之值讓移動圖片有動畫效果
#blit()不斷在畫布上繪製圖片
#update()進行動作的更新
while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

   screen.fill(White)
   
   if move == 'Down':
      carY += 5
      if carY == 230 : move = 'Right'
   elif move == 'Right':
      carX += 5
      if carX == 315 : move = 'Up'
   elif move == 'Up':
      carY -= 5
      if carY == 50 : move = 'Left'
   elif move == 'Left':
      carX -= 5
      if carX == 50: move = 'Down'
   #blit()方法在畫布上繪製圖片
   screen.blit(car, (carX, carY))
   pygame.display.update()
   traceCar.tick(Fps) #依fps的值來產生動畫
