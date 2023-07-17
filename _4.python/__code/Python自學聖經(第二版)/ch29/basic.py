import pygame
pygame.init()  #啟動Pygame
screen = pygame.display.set_mode((640, 320))  #建立繪圖視窗
pygame.display.set_caption("基本架構")  #繪圖視窗標題
background = pygame.Surface(screen.get_size())  #建立畫布
background = background.convert()
background.fill((255,255,255))  #畫布為白色
screen.blit(background, (0,0))  #在繪圖視窗繪製畫布
pygame.display.update()  #更新繪圖視窗
running = True
while running:  #無窮迴圈
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #使用者按關閉鈕
            running = False
pygame.quit()  #關閉繪圖視窗