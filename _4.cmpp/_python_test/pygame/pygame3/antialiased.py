import pygame
pygame.init()

screen = pygame.display.set_mode([400, 300])

black = pygame.color.Color("#000000")
white = pygame.color.Color("#FFFFFF")

done = False
while not done:
    screen.fill(white)

    pygame.draw.aaline(screen, black, [10, 10], [30, 25])
    pygame.draw.aaline(screen, black, [40, 10], [60, 25])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
pygame.quit()