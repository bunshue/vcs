import pygame   # 滙入PyGame套件

pygame.init()   # 1-1.將PyGame初始化

size = ()      # 空的Tuple物件
size = width, height = 800, 600
# 1-2.產生視窗，以Surface物件回傳
screen = pygame.display.set_mode(size)
Green = (0, 255, 0)

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
img = pygame.image.load(filename)

# 1-3.標題列秀出文字
pygame.display.set_caption('Hello Python!!')

screen.blit(img, (100, 100))
pygame.display.update()

# 3.訊息廻圈依據事件做偵測，使用者是否按了右上角的X鈕
running = True

while running:
   for event in pygame.event.get():   # 3-1.依據事件
      #判斷事件的常數是否為QUIT常數
      if event.type == pygame.QUIT:
         running = False
   
pygame.quit()   # quit()方法結束Pygame程序
