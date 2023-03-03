import pygame
pygame.init()
# Window setup
size = [400, 300]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Game loop
done = False
while not done:
    keys = pygame.key.get_pressed()

    #player movement
    if keys[pygame.K_w]:
        print "Hello"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(32)
pygame.quit()