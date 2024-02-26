import pygame   # 滙入PyGame套件
import sys      # 滙入系統套件

pygame.init()   # 將PyGame初始化

# Tuple儲存視窗寬和高
size = width, height = 350, 300

#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size))

pygame.display.set_caption('Hello Python!!')

running = True

while running:
   for event in pygame.event.get():   # 依據事件
      if event.type == pygame.QUIT:
         pygame.quit()                # quit()方法關閉視窗
         sys.exit()                   # 結束應用程式
