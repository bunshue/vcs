import pygame

pygame.init()

windowSize = [400, 300]
pygame.display.set_mode(windowSize)

hit = pygame.mixer.Sound("hit.wav")
crash = pygame.mixer.Sound("crash.wav")

done = False
while not done:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        hit.play()

    if keys[pygame.K_s]:
        crash.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()
