import pygame
pygame.init()

windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)
colour = pygame.color.Color('#FFFFFF')

done = False
while not done:
    pygame.draw.circle(screen, colour, [200, 150], 50)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()