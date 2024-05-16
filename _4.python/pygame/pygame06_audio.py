"""
pygame 測試大全

用pygame播放mp3檔案
用pygame播放wav檔案
用pygame播放midi檔案

"""

import sys
import time
import pygame

print("------------------------------------------------------------")  # 60個

print('用 pygame 播放音效1')
pygame.mixer.init()

mysound = r'C:\Windows\Media\notify.wav'
soundObj = pygame.mixer.Sound(mysound)      # 建立Sound物件
soundObj.play()                             # 撥放一次
pygame.time.delay(3000)                     # 休息3秒
soundObj.play(2)                            # 播放3次

time.sleep(5)                               # 程式休息

print("------------------------------------------------------------")  # 60個

print('用 pygame 播放音效2')

pygame.mixer.init()

mysound = r'C:\Windows\Media\notify.wav'
pygame.time.delay(1000)                     # 先給聲音初始化工作

soundObj = pygame.mixer.Sound(mysound)      # 建立Sound物件
soundObj.play()                             # 撥放一次
pygame.time.delay(3000)                     # 休息3秒
soundObj.set_volume(0.1)                    # 聲音變小
soundObj.play(2)                            # 播放3次

time.sleep(5)                               # 程式休息

print("------------------------------------------------------------")  # 60個

print('用 pygame 播放音效3')

pygame.mixer.init()

#mywav = r'C:Windows\Media\notify.wav'
mywav = r'_data\notify.wav'

pygame.time.delay(1000)                     # 先給聲音初始化工作
pygame.mixer.music.load(mywav)              # 下載 wav 音樂檔案
pygame.mixer.music.play()                   # 播放 wav 音樂檔案

time.sleep(5)                               # 程式休息

print('用 pygame 播放音效4')

mymidi = r'_data\town.mid'
pygame.time.delay(1000)                     # 先給聲音初始化工作
pygame.mixer.music.load(mymidi)             # 下載 midi 音樂檔案
pygame.mixer.music.play()                   # 播放 midi 音樂檔案


time.sleep(5)                               # 程式休息

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個





