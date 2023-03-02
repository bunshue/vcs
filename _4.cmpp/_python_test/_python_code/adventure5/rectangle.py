import pygame
pygame.init()

windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)
colour = pygame.color.Color('#0A32F4')

done = False
while not done:
    pygame.draw.rect(screen, colour, [10, 20, 30, 40])
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()