"""
pygame 測試大全 02

"""

import sys
import pygame

W, H = 800, 800

pygame.init()   # 初始化Pygame
screen_size = (W, H)    # 設定屏幕尺寸
screen = pygame.display.set_mode(screen_size)   # 創建屏幕
pygame.display.set_caption('畫圖綜合')

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
screen.fill(Gray)


#繪製文字
#ft = pygame.font.SysFont('Malgun Gothic', 36)
ft = pygame.font.SysFont('Arial', 36)
wd1 = ft.render('Encyclopedia', False, blue,Aqua)
screen.blit(wd1, (10, 20))
wd2 = ft.render('百科全書', True, red,Aqua)
screen.blit(wd2, (10, 80))
wd1 = ft.render('lockdown', False, blue,Aqua)
screen.blit(wd1, (10, 140))
wd2 = ft.render('世界大同', True, red,Aqua)
screen.blit(wd2, (10, 200))
wd1 = ft.render('binge-watch', False, blue,Aqua)
screen.blit(wd1, (10, 260))
wd2 = ft.render('追劇', True, red,Aqua)
screen.blit(wd2, (10, 320))



filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

#方法load()載入圖片，convert()能提高圖片的處理速度
img = pygame.image.load(filename)
img.convert()
screen.blit(img, (400, 300))



# 更新屏幕
pygame.display.update()

# 保持屏幕打開，直到用戶退出
#偵測視窗是否被關閉
while True:
    for event in pygame.event.get():
        #判斷事件的常數是否為QUIT常數
        if event.type == pygame.QUIT:
            pygame.quit() #quit()方法結束Pygame程序
            sys.exit()
    pygame.display.update()
