import pygame
pygame.init()
screen = pygame.display.set_mode((640, 280))
pygame.display.set_caption("載入圖片")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,255,0))
image = pygame.image.load("media\\img01.jpg")
image.convert()
compass = pygame.image.load("media\\compass.png")
compass.convert()
background.blit(image, (20,10))
background.blit(compass, (400,50))
running = True
screen.blit(background, (0,0))
pygame.display.update()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()