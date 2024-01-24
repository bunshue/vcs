"""
pygame 測試大全 03 keyboard mouse

"""

import sys
import pygame

W, H = 800, 800

pygame.init()   # 初始化Pygame
screen_size = (W, H)    # 設定屏幕尺寸
screen = pygame.display.set_mode(screen_size)   # 創建屏幕
pygame.display.set_caption('偵測滑鼠位置')

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

#利用screen物件來作為畫布，以fill()方法填上顏色
screen.fill(white)

clock = pygame.time.Clock()

pos_list = []


# 更新屏幕
pygame.display.update()

# 保持屏幕打開，直到用戶退出
#偵測視窗是否被關閉
while True:
    screen.fill(black)
    pygame.draw.rect(screen, black, [0, 0, 0, 0])

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:    #滑鼠事件
            pos = pygame.mouse.get_pos()  # 取得滑鼠座標
            print(pos)
            #print(type(pos))
            pos_list.append(pos)
            #pygame.draw.lines(screen, [255, 255, 255], pos_list) TBD
        #判斷事件的常數是否為QUIT常數
        if event.type == pygame.QUIT:
            pygame.quit() #quit()方法結束Pygame程序
            sys.exit()
    pygame.display.flip()
    clock.tick(10)    
