"""
pygame 測試大全

用pygame播放mp3檔案
用pygame播放wav檔案
用pygame播放midi檔案

"""

import sys
import time
import pygame


mp3_filename = 'C:/_git/vcs/_1.data/______test_files1/_mp3/16.監獄風雲.mp3'
wav_filename_hit = 'C:/_git/vcs/_1.data/______test_files1/_wav/hit.wav'
wav_filename_crash = 'C:/_git/vcs/_1.data/______test_files1/_wav/crash.wav'

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



import pygame

pygame.mixer.init()

pygame.mixer.music.load(mp3_filename)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():#讀取播放狀態
    pygame.time.delay(200)

print("------------------------------------------------------------")  # 60個

import pygame

pygame.mixer.init()

sound = pygame.mixer.Sound(wav_filename_hit)
sound.play()

pygame.time.wait(int(sound.get_length()) * 1000)

print("------------------------------------------------------------")  # 60個

import pygame

pygame.init()

clock = pygame.time.Clock()

crash = pygame.mixer.Sound(wav_filename_crash)
hit = pygame.mixer.Sound(wav_filename_hit)

count = 0
while count < 200:
    if count % 4 == 0:
        crash.play()
    else:
        hit.play()
    count += 1
    clock.tick(2)
    
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


import pygame

pygame.init()

windowSize = [400, 300]
pygame.display.set_mode(windowSize)

hit = pygame.mixer.Sound(wav_filename_hit)
crash = pygame.mixer.Sound(wav_filename_crash)

hit.play()

#crash.play()




#調整聲音大小

import pygame

pygame.mixer.init()

pygame.mixer.music.load(mp3_filename)
pygame.mixer.music.play()

volume = 0.3
while pygame.mixer.music.get_busy():#讀取播放狀態
    pygame.mixer.music.set_volume(volume)
    print('設定音量 :', volume)
    volume += 0.1
    if volume > 1.0:
        volume = 0.3
    pygame.time.delay(1000)

print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個



