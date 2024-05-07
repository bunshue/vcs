"""

Python 聲音處理 pygame

"""

import os
import sys
import time
import random

import pygame

print("------------------------------------------------------------")  # 60個

def playmp3(filename): #播放新曲
    pygame.mixer.music.stop() # 要先stop, 才不會冒出一個雜音
    pygame.mixer.music.load(filename)   
    pygame.mixer.music.play(loops=-1)  

filename1 = 'C:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/_mp3/16.監獄風雲.mp3'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/_wav/harumi99.wav'
filename4 = 'C:/_git/vcs/_1.data/______test_files1/_mp3/mario.mp3'

pygame.mixer.init()

playmp3(filename2)

#mixer.music.stop()

print("------------------------------------------------------------")  # 60個

import pygame

pygame.init()

windowSize = [400, 300]
pygame.display.set_mode(windowSize)


filename1 = 'C:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/_mp3/16.監獄風雲.mp3'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/_wav/harumi99.wav'

'''
file1 = pygame.mixer.Sound(filename1)
file2 = pygame.mixer.Sound(filename2)
file3 = pygame.mixer.Sound(filename3)

done = False
while not done:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_1]:
        file1.play()
        file2.stop()
        file3.stop()

    if keys[pygame.K_2]:
        file1.stop()
        file2.play()
        file3.stop()

    if keys[pygame.K_3]:
        file1.stop()
        file2.stop()
        file3.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()
'''


import pygame

pygame.mixer.init()
pygame.mixer.music.load(filename3)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.delay(200)


print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3"

import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(filename)
pygame.mixer.music.play()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
