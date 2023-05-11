import pygame
pygame.init()
screen = pygame.display.set_mode((640, 300))
pygame.display.set_caption("滑鼠滑動事件")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
ball = pygame.Surface((30,30))  #建立球矩形繪圖區
ball.fill((255,255,255))  #矩形區塊背景為白色
pygame.draw.circle(ball, (0,0,255), (15,15), 15, 0)  #畫藍色球
rect1 = ball.get_rect()  #取得球矩形區塊
rect1.center = (320,150)  #球起始位置
x, y = rect1.topleft  #球左上角坐標
clock = pygame.time.Clock()
running = True
playing = False  #開始時球不能移動
while running:
    clock.tick(30)  #每秒執行30次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    buttons = pygame.mouse.get_pressed()
    if buttons[0]:  #按滑鼠左鍵後球可移動
        playing = True
    elif buttons[2]:  #按滑鼠右鍵後球不能移動
        playing = False
    if playing == True:  #球可移動狀態
        mouses = pygame.mouse.get_pos()  #取得滑鼠坐標
        rect1.centerx = mouses[0]  #移動滑鼠
        rect1.centery = mouses[1]
    screen.blit(background, (0,0))  #清除繪圖視窗
    screen.blit(ball, rect1.topleft)
    pygame.display.update()
pygame.quit()