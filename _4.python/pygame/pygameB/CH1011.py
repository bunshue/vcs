import pygame , sys, random, math

pygame.init() #將PyGame初始化

#設定使用參數
size = width, height = 400, 280
White = (255, 255, 255)

#設定每秒畫格20，利用Clock()方法來確保動畫能持續進行
Fps = 20 #每秒的執行次數
traceCar = pygame.time.Clock()

#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption('碰撞的偵測')

#載入圖片，get_rect()取得矩形的移動區域
car = pygame.image.load('Source\\006.jpg')
carRect = car.get_rect()

#屬性center-設定圖片要開始移動的中心點
carRect.center = 200, 140

#屬性topleft取得圖片移動區域左上角到畫布的位置
carX , carY = carRect.topleft

#moveX, moveY = 5, -5 #設定圖片的移動速度會形成固定範圍
#避免移動成固定範圍，以隨機值來取得起始角度並轉為弧度
posi = random.randint(45, 60)
angle = math.radians(posi)
#設定圖片水平和垂直的移動速度
moveX = 5 * math.sin(angle)
moveY = -5 * math.cos(angle)

while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

   screen.fill(White)
   traceCar.tick(Fps) #每秒執行25次
   #改變水平、垂直位置並重設物件的中心點
   carX += moveX 
   carY += moveY
   carRect.center = carX, carY

   #偵測水平、垂直方向的移動是否會碰到畫布的左、右或上、下邊界
   #碰到時改變moveX、moveY為正值並改變方向
   if(carRect.left <= 0) or \
         (carRect.right >= screen.get_width()):
      moveX *= -1
      print(moveX, moveY)
   elif(carRect.top <= 5) or \
         (carRect.bottom >= screen.get_height() - 5):
      moveY *= -1
   screen.blit(car, carRect.topleft)
   pygame.display.update()
