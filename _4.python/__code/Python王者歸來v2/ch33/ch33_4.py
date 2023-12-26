# ch33_4.py
import pygame
pygame.mixer.init()

pygame.time.delay(1000)                     # 先給聲音初始化工作
pygame.mixer.music.load('house_lo.mp3')     # 下載mp3音樂檔案
pygame.mixer.music.play()                   # 播放mp3音樂檔案


