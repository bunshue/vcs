import pygame, sys

pygame.init()

#設定使用參數
size = winWidth, winHeight = 300, 300
White = (255,255, 255)

#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption('hello Pygame!!!')
screen.fill(White)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
