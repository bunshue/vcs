"""
pygame 測試大全 04

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






import pygame
pygame.mixer.init()

mysound = r'C:\Windows\Media\notify.wav'
soundObj = pygame.mixer.Sound(mysound)      # 建立Sound物件
soundObj.play()                             # 撥放一次
pygame.time.delay(3000)                     # 休息3秒
soundObj.play(2)                            # 播放3次





print("------------------------------------------------------------")  # 60個

from gtts import gTTS
import pygame

text = "Hello, Machine Learning!"
tts = gTTS(text=text, lang='en')
tts.save("hello.mp3")

pygame.mixer.init()
pygame.mixer.music.load("hello.mp3")
pygame.mixer.music.play()

print("------------------------------------------------------------")  # 60個

from gtts import gTTS
import pygame

text = "我愛明志科技大學!"
tts = gTTS(text=text, lang='zh-tw')
tts.save("hello.mp3")

pygame.mixer.init()
pygame.mixer.music.load("hello.mp3")
pygame.mixer.music.play()

print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch33\ch33_2.py

# ch33_2.py
import pygame
pygame.mixer.init()

mysound = r'C:\Windows\Media\notify.wav'
pygame.time.delay(1000)                     # 先給聲音初始化工作

soundObj = pygame.mixer.Sound(mysound)      # 建立Sound物件
soundObj.play()                             # 撥放一次
pygame.time.delay(3000)                     # 休息3秒
soundObj.set_volume(0.1)                    # 聲音變小
soundObj.play(2)                            # 播放3次








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch33\ch33_3.py

# ch33_3.py
import pygame
import time
pygame.mixer.init()

mywav = r'C:Windows\Media\notify.wav'
pygame.time.delay(1000)                     # 先給聲音初始化工作
pygame.mixer.music.load(mywav)              # 下載 wav 音樂檔案
pygame.mixer.music.play()                   # 播放 wav 音樂檔案

time.sleep(5)                               # 程式休息
mymidi = r'C:\Windows\Media\town.mid'
pygame.time.delay(1000)                     # 先給聲音初始化工作
pygame.mixer.music.load(mymidi)             # 下載 midi 音樂檔案
pygame.mixer.music.play()                   # 播放 midi 音樂檔案





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
