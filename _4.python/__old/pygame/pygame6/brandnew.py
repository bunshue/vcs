import pygame, sys

pygame.init()

#設定使用參數
size = winWidth, winHeight = 400, 400
Gray = (128, 128, 128)
Yellow = (255, 255, 0)
White = (255, 255, 255)
Green = (0, 255, 0)
Red = (255, 0, 0)


#產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption('hello Pygame!!!')
screen.fill(Yellow)


#繪製文字
ft = pygame.font.SysFont('Malgun Gothic', 60)
wd1 = ft.render('萬象更新', False, Green)
screen.blit(wd1, (60, 20))
wd2 = ft.render('brand new', True, Red)
screen.blit(wd2, (60, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

