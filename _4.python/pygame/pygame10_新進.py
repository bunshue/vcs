"""
pygame10_新進

"""

import sys
import pygame
import random

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
pg.display.set_caption("Richard's pygame!")
bk = pg.Surface(screen.get_size())
bk.fill((255, 255, 255))
screen.blit(bk, (0, 0))
pg.display.update()
quit = False
while not quit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit = True
pg.quit()

print("------------------------------------------------------------")  # 60個

import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
pg.display.set_caption("Richard's pygame!")
bk = pg.Surface(screen.get_size())
bk.fill((255, 255, 255))
pg.draw.rect(bk, (255, 0, 0), (100, 100, 300, 300), 2)
screen.blit(bk, (0, 0))
pg.display.update()
quit = False
while not quit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit = True
pg.quit()

print("------------------------------------------------------------")  # 60個

import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))
pg.display.set_caption("Richard's pygame!")
bk = pg.Surface(screen.get_size())
bk.fill((255, 255, 255))
lines = list()
for th in range(0, 361):
    y = 250 - 200 * math.sin(th * math.pi / 180)
    lines.append((th + 140, y))
pg.draw.lines(bk, (0, 0, 255), False, lines, 2)

screen.blit(bk, (0, 0))
pg.display.update()
quit = False
while not quit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit = True
pg.quit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

"""

pygame之畫圖
draw.line()
draw.rect()
draw.polygon()
draw.circle()
draw.ellipse()
draw.arc()



pygame.mixer.music.rewind() #重新啟動音樂
#將當前音樂的播放重新設置為一開始
 
pygame.mixer.music.stop() #停止音樂播放


pygame.mixer.music.pause() #暫時停止音樂播放
pygame.mixer.music.unpause()   #恢復暫停音樂


print('音量0.5')
pygame.mixer.music.set_volume(0.5)  #調節音樂音量
#設置音樂播放的音量。值參數在0.0和1.0之間。當加載新音樂時，音量就會重置
time.sleep(30)
print('音量1')
pygame.mixer.music.set_volume(1)
time.sleep(30)
print('音量0.3')
pygame.mixer.music.set_volume(0.3)
 

b=pygame.mixer.music.get_volume() #返回當前音量
#值將在0.0和1.0之間
 

b=pygame.mixer.music.get_busy()   #檢查音樂流是否在播放
#當音樂流在積極播放時，就會返回True。當音樂空閑時，返回False
#暫停相當于在播放，返回True
 




b=pygame.mixer.get_init()  #測試混音器是否初始化
#如果混音器已初始化，則返回正在使用的播放參數。如果混音器尚未初始化，則返回None
#get_init() -> (frequency, format, channels)
#(22050, -16, 2)



"""
