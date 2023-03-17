import pygame

pygame.init()

windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)
color = pygame.color.Color('#FF0000')

done = False
while not done:
    pygame.draw.circle(screen, color, [200, 150], 50)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('QUIT')
            done = True
            
pygame.quit()
