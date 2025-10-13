"""
Python 聲音處理 pygame

mixer	用來播放聲音

用 pygame 播放 mp3 檔案
用 pygame 播放 wav 檔案
用 pygame 播放 midi 檔案
"""

import sys
import time
import math
import random
import pygame


# 播放mp3
def play_audio_file(filename):
    from pygame import mixer

    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()
    while mixer.music.get_busy():
        continue


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(filename)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():#讀取播放狀態, True:正在播放, False:不在播放中
    pygame.time.delay(10)  # msec
    print('.')

print('結束播放')

"""


"""

#要能夠順利讀取各種奇怪的檔名中日文字

print("測試寫檔")
mp3_foldername1 = 'D:/_git/vcs/_1.data/______test_files1/_mp3/'
mp3_foldername2 = 'D:/vcs/astro/_DATA2/_mp3/陳一郎_台語精選集6CD/disc2/'
mp3_foldername3 = 'D:/vcs/astro/_DATA2/_mp3/japanese/昭和の歌--演歌系列9/'
mp3_foldername4 = 'D:/vcs/astro/_DATA2/_________整理_mp3/_mp3_日本_new/(アルバム)演歌 八代亜紀 -[全曲集(Disc1-2)](全24曲)/渕_辙 - [葢轿瘅(Disc1)]'
mp3_foldername5 = 'D:/vcs/astro/_DATA2/_mp3/japanese/美空ひばり(美空云雀).-.[美空ひばり全曲集1].专辑.(MP3)/'

mp3_foldernames = [mp3_foldername1, mp3_foldername2, mp3_foldername3, mp3_foldername4, mp3_foldername5]

print(mp3_foldernames)

filename = "tk_ex_MusicPlayer1.txt"

print("檔名 :", filename)
with open(filename, "w", encoding="utf-8") as f:
    for _ in mp3_foldernames:
        f.write(_)
        f.write("\n")

print("測試讀檔")
filename = "tk_ex_MusicPlayer1.txt"

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)

"""

import pygame
import time

pygame.init()
# screen = pygame.display.set_mode((640, 480))
# pygame.display.set_caption("my mp3 player")

filename = "D:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3"

pygame.mixer.music.load(filename)  # 載入音樂
# 音樂可以是ogg、mp3、wav等格式
# 載入的音樂不會全部放到內容中，而是以流的形式播放的，即在播放的時候才會一點點從文件中讀取

pygame.mixer.music.play()  # 播放載入的音樂
# 該函數立即返回，音樂播放在后臺進行。play方法還可以使用兩個參數
# 如果音樂已經播放，它就會重新啟動
# play(loops=0, start=0.0) -> None
# 參數1:控制音樂播放的次數。播放(5)將使音樂播放一次，然后重復5次，總共是6次。如果循環是-1，那么音樂就會無限重復
# 起始位置的參數控制著歌曲開始播放的地方。起始位置取決于音樂演奏的格式。MP3和OGG以時間為單位(以秒為單位)。MOD音樂是模式的序號。如果不能設置起始位置，通過一個startpos將會拋出一個NotImplementedError


time.sleep(5)

pygame.mixer.music.load(filename)  # 如果一個音樂流已經播放，它就會被停止。這并不是音樂的開始
pygame.mixer.music.play()  # 播放載入的音樂


pygame.mixer.music.set_endevent(pygame.KEYDOWN)  # 當播放停止時，音樂會發送一個事件
# 參數：事件
# 每次音樂結束時，這個事件都會被排隊，而不僅僅是第一次[只要不在播放狀態，會一直發送]。為了防止事件被排隊，請調用這個方法，沒有參數

b = pygame.mixer.music.get_endevent()  # 當播放停止時，獲取set_endevent發送的事件--int
# pygame.KEYDOWN=2
# 如果沒有endevent，函數將返回pygame.NOEVENT

print("xxxxxxx", b)

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        print("aaaaa")
        exit()
        print("bbbbb")
    # print('aaaaaa',event)
    pygame.display.update()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


"""
if not mixer.music.get_busy():
    mixer.music.load(playsong)
    mixer.music.play(loops=-1)
else:
    mixer.music.unpause()

mixer.music.load(playsong)
mixer.music.play(loops=-1)

msg.set("\n停止播放")
msg.set("\n正在播放：{}".format(playsong))


win.destroy()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import pygame
import time

# 播放音樂

# pygame.init()

filename = "data/hit.wav"
filename = "D:/_git/vcs/_1.data/______test_files1/_wav/harumi99.wav"

pygame.mixer.init()

# 用 mixer.Sound
# soundhit = pygame.mixer.Sound(filename)
# soundhit.play()

# 用 music.load
pygame.mixer.music.load(filename)

# print("設定音量 0.5")
pygame.mixer.music.set_volume(0.5)  # 設定音量 0.0~1.0

pygame.mixer.music.play()  # 單次播放

# pygame.mixer.music.play(-1)  # 循環播放
# pygame.mixer.music.play(-1, 0.0)  # 循環播放

a = 0
running = True
while running:
    # print(a)
    time.sleep(1)  # 1秒
    status = pygame.mixer.music.get_busy()  # 檢查音樂流是否在播放
    if status == False:
        print("播放完畢")
        running = False
    volume = pygame.mixer.music.get_volume()  # 返回當前音量 0.0~1.0
    # print(volume)
    a += 1
    if a >= 20:
        a = 0


"""
pygame.mixer.music.rewind()  # 重新啟動音樂 # 將當前音樂的播放重新設置為一開始
pygame.mixer.music.stop()  # 停止播放
pygame.mixer.music.pause()  # 暫停播放
pygame.mixer.music.unpause()  # 恢復暫停音樂

status = pygame.mixer.music.get_busy()  # 檢查音樂流是否在播放
# 當音樂流在積極播放時，就會返回True。當音樂空閑時，返回False
# 暫停相當于在播放，返回True

b = pygame.mixer.get_init()  # 測試混音器是否初始化
# 如果混音器已初始化，則返回正在使用的播放參數。如果混音器尚未初始化，則返回None
# get_init() -> (frequency, format, channels)
# (22050, -16, 2)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Load music and sound
coinSound = pygame.mixer.Sound("data/coin.wav")
coinSound.play()

pygame.mixer.music.load("data/music.mp3")
pygame.mixer.music.play(-1)  # 循環播放

print("------------------------------")  # 30個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
