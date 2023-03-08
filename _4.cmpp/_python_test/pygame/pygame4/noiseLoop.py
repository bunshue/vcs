import pygame
pygame.init()

clock = pygame.time.Clock()

crash = pygame.mixer.Sound('crash.wav')
hit = pygame.mixer.Sound('hit.wav')

count = 0
while count < 200:
    if count % 4 == 0:
        crash.play()
    else:
        hit.play()
    count += 1
    clock.tick(2)