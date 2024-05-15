"""
pygame 測試大全

"""

import sys
import time
import pygame

W, H = 800, 600
screen_size = (W, H)    # 設定屏幕尺寸

# 設定顏色
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

Fuchsia = (255, 0, 255) #紫色
Aqua = (0, 255, 255) #淺藍色
Gray = (128, 128, 128) #灰色

# 設定顏色, same
red = pygame.color.Color('#FF0000')
green = pygame.color.Color('#00FF00')
blue = pygame.color.Color('#0000FF')
black = pygame.color.Color('#000000')
white = pygame.color.Color('#FFFFFF')

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

print('------------------------------------------------------------')	#60個

def run_pygame():
   # 更新屏幕, 保持屏幕打開, 直到用戶退出, 偵測視窗是否被關閉(8)
   pygame.display.update()
   running = True
   while running:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
   pygame.quit()

print('------------------------------------------------------------')	#60個

print('pygame 01')

pygame.init()  # 初始化Pygame
screen = pygame.display.set_mode(screen_size)   # 創建屏幕
pygame.display.set_caption('pygame測試01')

#利用screen物件來作為畫布，以fill()方法填上顏色
screen.fill(white)

#方法load()載入圖片，convert()能提高圖片的處理速度
image=pygame.image.load(filename)
#设置图片大小
image=pygame.transform.scale(image,(200, 300))
#绘制视频画面
screen.blit(image,(2,2))

run_pygame()

print('------------------------------------------------------------')	#60個

print('pygame 02')

pygame.init()  # 初始化Pygame
screen = pygame.display.set_mode(screen_size)   # 創建屏幕
pygame.display.set_caption('pygame測試02')

print("取得screen參數")
print(screen.get_size())

#利用screen物件來作為畫布，以fill()方法填上顏色
screen.fill(white)

#方法load()載入圖片，convert()能提高圖片的處理速度
img = pygame.image.load(filename)
img.convert()
x_st, y_st = 200, 100
screen.blit(img, (x_st, y_st))

run_pygame()

print('------------------------------------------------------------')	#60個

print('pygame 03')

pygame.init()  # 初始化Pygame
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('pygame測試03 載入圖片')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,255,0))#設定背景顏色

#方法load()載入圖片，convert()能提高圖片的處理速度
image = pygame.image.load(filename)
image.convert()
x_st, y_st = 20, 20
background.blit(image, (x_st, y_st))

screen.blit(background, (0,0))

run_pygame()

print('------------------------------------------------------------')	#60個

print('pygame 04')

pygame.init()  # 初始化Pygame

#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((W, H), 0, 32)
pygame.display.set_caption('pygame測試04 載入圖片')

#利用screen物件來作為畫布，以fill()方法填上顏色
screen.fill(white)

#方法load()載入圖片，convert()能提高圖片的處理速度
img = pygame.image.load(filename)
img.convert()
x_st, y_st = 20, 20
screen.blit(img, (x_st, y_st))

run_pygame()

print('------------------------------------------------------------')	#60個

print('pygame 05')

pygame.init()  # 初始化Pygame

screen = pygame.display.set_mode(screen_size)   # 創建屏幕
pygame.display.set_caption('pygame測試05')

# 繪製五個同心圓
center_x = screen_size[0] // 2
center_y = screen_size[1] // 2

radius_1 = 200
radius_2 = 150
radius_3 = 100
radius_4 = 50
radius_5 = 20

pygame.draw.circle(screen, white, (center_x, center_y), radius_1)
pygame.draw.circle(screen, red, (center_x, center_y), radius_2)
pygame.draw.circle(screen, green, (center_x, center_y), radius_3)
pygame.draw.circle(screen, blue, (center_x, center_y), radius_4)
pygame.draw.circle(screen, yellow, (center_x, center_y), radius_5)

run_pygame()

print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


