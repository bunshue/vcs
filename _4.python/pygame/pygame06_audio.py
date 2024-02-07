"""
pygame 測試大全


用gtts製作mp3檔案

用pygame播放mp3檔案


"""

import sys
import time

print("------------------------------------------------------------")  # 60個

print('用 pygame 播放音效1')
import pygame
pygame.mixer.init()

mysound = r'C:\Windows\Media\notify.wav'
soundObj = pygame.mixer.Sound(mysound)      # 建立Sound物件
soundObj.play()                             # 撥放一次
pygame.time.delay(3000)                     # 休息3秒
soundObj.play(2)                            # 播放3次

time.sleep(5)                               # 程式休息

print("------------------------------------------------------------")  # 60個

print('用 pygame 播放音效2')
import pygame
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

import pygame
import time
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

mp3_filename = 'tmp_mp3_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.mp3'

from gtts import gTTS
import pygame

text = "Welcome to the United States and have a nice day."
tts = gTTS(text=text, lang='en')
tts.save(mp3_filename)

pygame.mixer.init()
pygame.mixer.music.load(mp3_filename)
pygame.mixer.music.play()

time.sleep(5)                               # 程式休息

print("------------------------------------------------------------")  # 60個

mp3_filename = 'tmp_mp3_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.mp3'

from gtts import gTTS
import pygame

text = "黃河遠上白雲間，一片孤城萬仞山。羌笛何須怨楊柳？春風不度玉門關。"

tts = gTTS(text=text, lang='zh-tw')
tts.save(mp3_filename)

pygame.mixer.init()
pygame.mixer.music.load(mp3_filename)
pygame.mixer.music.play()

print("------------------------------------------------------------")  # 60個


