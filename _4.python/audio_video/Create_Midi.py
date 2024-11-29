print("使用 pygame 播放 midi 檔案")

import pygame

pygame.mixer.init()
pygame.mixer.music.load("data/HotelCalifornia.mid")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

pygame.mixer.quit()
