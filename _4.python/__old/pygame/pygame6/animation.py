import pygame , sys, random, math

pygame.init() #將PyGame初始化

#設定使用參數
size = width, height = 460, 380
White = (255, 255, 255)

#設定每秒畫格
Fps = 20 
#利用Clock()方法來確保動畫能持續進行
traceobj = pygame.time.Clock()

#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption('含碰撞偵測的動畫')

#載入圖片，get_rect()取得矩形的移動區域
obj = pygame.image.load('pic\\able.jpg')
#取得矩形的移動區域
objRect = obj.get_rect()
#設定圖片要開始移動的中心點
objRect.center = 350, 300
#屬性topleft取得圖片移動區域左上角到畫布的位置
objX , objY = objRect.topleft 
#以隨機值來取得起始角度並轉為弧度
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
   traceobj.tick(Fps) #每秒執行25次
   #改變水平、垂直位置並重設物件的中心點
   objX += moveX 
   objY += moveY
   objRect.center = objX, objY

   #碰到畫布到時改變moveX、moveY為正值並改變方向
   if(objRect.left <= 0) or \
         (objRect.right >= screen.get_width()):
      moveX *= -1
   elif(objRect.top <= 5) or \
         (objRect.bottom >= screen.get_height() - 5):
      moveY *= -1
   screen.blit(obj, objRect.topleft)
   pygame.display.update()
