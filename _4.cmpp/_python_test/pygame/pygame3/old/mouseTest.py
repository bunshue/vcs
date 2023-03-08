import pygame
pygame.init()

windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)
black = [0, 0, 0]
clock = pygame.time.Clock()


done = False
while not done:
    screen.fill(black)
    pygame.draw.rect(screen, black, [0, 0, 0, 0])
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print pos
        if event.type == pygame.QUIT:
            done = True
    clock.tick(10)
pygame.quit()