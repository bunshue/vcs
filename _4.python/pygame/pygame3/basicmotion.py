import pygame

pygame.init()
screen = pygame.display.set_mode((640, 320))
pygame.display.set_caption("動畫基本架構")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))

clock = pygame.time.Clock()  #建立時間元件

running = True
while running:
    clock.tick(30)  #每秒執行30次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))  #清除繪圖視窗

    pygame.display.update()  #更新繪圖視窗
pygame.quit()  #關閉繪圖視窗
