import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("基本繪圖")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))

pygame.draw.circle(background, (0,0,0), (150,150), 130, 4)
pygame.draw.circle(background, (0,0,255), (100,120), 25, 0)
pygame.draw.circle(background, (0,0,255), (200,120), 25, 0)
pygame.draw.ellipse(background, (255,0,255),[135, 130, 30, 80], 0)
pygame.draw.arc(background, (255,0,0), [80, 130, 150, 120], 3.4, 6.1, 9)
screen.blit(background, (0,0))

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
