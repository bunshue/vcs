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
