import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("載入圖片")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,255,0))

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image = pygame.image.load(filename)
image.convert()
compass = pygame.image.load(filename)
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
