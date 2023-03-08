import pygame
pygame.mixer.init()

sound = pygame.mixer.Sound('hit.wav')
sound.play()

pygame.time.wait(int(sound.get_length()) * 1000)
