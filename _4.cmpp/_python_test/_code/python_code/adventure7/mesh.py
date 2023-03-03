import pygame
pygame.init()

windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

points = []

black = pygame.color.Color("#000000")
white = pygame.color.Color("#FFFFFF")

done = False
while not done:
    screen.fill(black)
    if len(points) > 10:
        del points[0]
    if len(points) > 1:
        pygame.draw.lines(screen, white, True, points)
    for point in points:
        pygame.draw.line(screen, white, point, [point[0], windowSize[1]])

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            points.append(pos)
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    clock.tick(10)
pygame.quit()