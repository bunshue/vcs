import pygame
pygame.init()

windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.line(screen, [255, 255, 255], pos, [0, 0])
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    clock.tick()

pygame.quit()