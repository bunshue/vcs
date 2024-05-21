"""

"""

import sys
import time
import pygame

mp3_filename = 'C:/_git/vcs/_1.data/______test_files1/_mp3/16.監獄風雲.mp3'

wav_filename_hit = 'C:/_git/vcs/_1.data/______test_files1/_wav/hit.wav'
wav_filename_crash = 'C:/_git/vcs/_1.data/______test_files1/_wav/crash.wav'

print("------------------------------------------------------------")  # 60個
'''
import pygame

pygame.mixer.init()

pygame.mixer.music.load(mp3_filename)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
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

print('做聲音大小變化')
import math
import pygame

pygame.mixer.init()

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()

count = 0
while pygame.mixer.music.get_busy():
    volume = abs(math.sin(count))
    pygame.mixer.music.set_volume(volume)
    count += 0.2
    pygame.time.delay(200)

print("------------------------------------------------------------")  # 60個

print('用tk.Scale控制聲音大小')

import pygame
import tkinter as tk

window = tk.Tk()

pygame.init()

pygame.mixer.music.load("music.mp3")

started = False
playing = False

def buttonClick():
    global playing, started
    if not playing:
        if not started:
            pygame.mixer.music.play(-1)
            started = True
        else:
            pygame.mixer.music.unpause()
        button.config(text="Pause")
    else:
        pygame.mixer.music.pause()
        button.config(text="Play")
    playing = not playing


def setVolume(val):
    volume = float(slider.get())
    pygame.mixer.music.set_volume(volume / 100)

slider = tk.Scale(window, from_=100, to=0, command=setVolume)
button = tk.Button(window, text="Play", command=buttonClick)
slider.pack()
slider.set(100)
button.pack()

window.mainloop()



print("------------------------------------------------------------")  # 60個

import random
import pygame

pygame.init()

def move(image1, image2):
    global count
    if count < 5:
        image = image1
    elif count >= 5:
        image = image2

    if count >= 10:
        count = 0
    else:
        count += 1
    return image

windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

standing = pygame.image.load('standing.png')

down1 = pygame.image.load('down1.png')
down2 = pygame.image.load('down2.png')

up1 = pygame.image.load('up1.png')
up2 = pygame.image.load('up2.png')

left1 = pygame.image.load('side1.png')
left2 = pygame.image.load('side2.png')

right1 = pygame.image.load('side1.png')
right2 = pygame.image.load('side2.png')
right1 = pygame.transform.flip(right1, True, False)
right2 = pygame.transform.flip(right2, True, False)

teleport1 = pygame.image.load('teleport1.png')
teleport2 = pygame.image.load('teleport2.png')
teleport3 = pygame.image.load('teleport3.png')

white = pygame.color.Color("#FFFFFF")

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()
teleportSound = pygame.mixer.Sound("teleport.wav")

# Game loop
count = 0
crash.wavx = 0
y = 0
locked = False
done = False
while not done:
    screen.fill(white)
    keys = pygame.key.get_pressed()

    if not locked:
        #player movement
        if keys[pygame.K_s]:
            image = move(down1, down2)
            y += 1
        elif keys[pygame.K_w]:
            image = move(up1, up2)
            y -= 1
        elif keys[pygame.K_a]:
            image = move(left1, left2)
            x -= 1
        elif keys[pygame.K_d]:
            image = move(right1, right2)
            x += 1
        elif keys[pygame.K_SPACE]:
            locked = True
        else:
            image = standing
            count = 0
    else:
        if count == 0:
            teleportSound.play()
        if count < 5:
            image = teleport1
        elif count < 10:
            image = teleport2
        elif count < 15:
            image = teleport3
        else:
            x = random.randrange(0, windowSize[0])
            y = random.randrange(0, windowSize[1])
            count = 0
            locked = False
        count += 1

    screen.blit(image, (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
    clock.tick(32)

pygame.quit()


print("------------------------------------------------------------")  # 60個
'''

print("------------------------------------------------------------")  # 60個

print('pygame 接受鍵盤按鍵 A S')
import pygame

pygame.init()

windowSize = [400, 300]
pygame.display.set_mode(windowSize)

hit = pygame.mixer.Sound(wav_filename_hit)
crash = pygame.mixer.Sound(wav_filename_crash)

done = False
while not done:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        hit.play()

    if keys[pygame.K_s]:
        crash.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個





