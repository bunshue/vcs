import pygame
pygame.init()

windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

points = []

white = pygame.color.Color("#FFFFFF")
black = pygame.color.Color("#000000")

done = False
while not done:
    screen.fill(black)
    pos = pygame.mouse.get_pos()
    if pos[0] != 0 and pos[1] != 0:
        points.append(pos)
    if len(points) >= 20:
        del points[0]

    if len(points) > 2:
        pygame.draw.aalines(screen, white, False, points)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    clock.tick(30)

pygame.quit()