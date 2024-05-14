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

print('pygame 01')
pygame.init()   # 初始化Pygame

screen = pygame.display.set_mode(screen_size)   # 創建屏幕
pygame.display.set_caption('畫圖綜合')


#利用screen物件來作為畫布，以fill()方法填上顏色
screen.fill(Gray)

"""
#加载图像
image=pygame.image.load(filename)
#设置图片大小
image=pygame.transform.scale(image,(640,480))
#绘制视频画面
screen.blit(image,(2,2))
"""

# 更新屏幕
pygame.display.update()

# 保持屏幕打開，直到用戶退出
#偵測視窗是否被關閉
exit_pygame = False
while True:
    for event in pygame.event.get():
        #判斷事件的常數是否為QUIT常數
        if event.type == pygame.QUIT:
            pygame.quit() #quit()方法結束Pygame程序
            exit_pygame = True
            break
    if exit_pygame == True:
        break
    pygame.display.update()

print('------------------------------------------------------------')	#60個

print('pygame 02')
pygame.init()   # 初始化Pygame

screen = pygame.display.set_mode(screen_size)   # 創建屏幕
pygame.display.set_caption('畫圖綜合')

print("取得screen參數")
print(screen.get_size())

#利用screen物件來作為畫布，以fill()方法填上顏色
screen.fill(Gray)

#方法load()載入圖片，convert()能提高圖片的處理速度
img = pygame.image.load(filename)
img.convert()
screen.blit(img, (400, 300))

# 更新屏幕
pygame.display.update()

# 保持屏幕打開，直到用戶退出
#偵測視窗是否被關閉
exit_pygame = False
while True:
    for event in pygame.event.get():
        #判斷事件的常數是否為QUIT常數
        if event.type == pygame.QUIT:
            pygame.quit() #quit()方法結束Pygame程序
            exit_pygame = True
            break
    if exit_pygame == True:
        break
    pygame.display.update()

print('------------------------------------------------------------')	#60個

print('pygame 03')
pygame.init()

screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("載入圖片")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,255,0))

image = pygame.image.load(filename)
image.convert()
compass = pygame.image.load(filename)
compass.convert()
background.blit(image, (20,10))
background.blit(compass, (400,50))
screen.blit(background, (0,0))
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()


print('------------------------------------------------------------')	#60個

print('pygame 04')
pygame.init() #將PyGame初始化

#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((W, H), 0, 32)
pygame.display.set_caption('載入圖片')
screen.fill(white)
#方法load()載入圖片，convert()能提高圖片的處理速度

img = pygame.image.load(filename)
img.convert()
screen.blit(img, (20, 20))

pygame.display.update()

running = True #判斷程式是否執行狀態
while running:
   for event in pygame.event.get():
      #判斷事件的常數是否為QUIT常數
      if event.type == pygame.QUIT:
          running = False
   
pygame.quit() #quit()方法結束Pygame程序

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


