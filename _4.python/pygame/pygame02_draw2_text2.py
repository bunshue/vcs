import pygame, sys  # 滙入PyGame套件、系統模組

pygame.init()  # 將PyGame初始化

# 設定使用參數
size = width, height = 280, 160

Grey = 79, 79, 79  # 灰色
Green = (0, 255, 0)
Yellow = (255, 255, 0)  # 黃色
Aqua = (0, 255, 255)  # 淺藍色
Gray = (128, 128, 128)  # 灰色

# 產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption("繪製文字")
screen.fill(Grey)

# 繪製文字
# ft = pygame.font.SysFont('Malgun Gothic', 36)
ft = pygame.font.SysFont("微軟正黑體", 36)
wd1 = ft.render("Hello Python", False, Aqua)
screen.blit(wd1, (10, 20))
wd2 = ft.render("黃河之水天上來", True, Green, Yellow)
screen.blit(wd2, (10, 80))

running = True  # 判斷程式是否執行狀態
while running:
    for event in pygame.event.get():
        # 判斷事件的常數是否為QUIT常數
        if event.type == pygame.QUIT:
            pygame.quit()  # 結束Pygame程序
            sys.exit()
    pygame.display.update()
