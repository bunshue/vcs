import pygame

pygame.init()
screen = pygame.display.set_mode((500, 100))
pygame.display.set_caption("繪製文字")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 255, 0))  # 背景為錄色

font_filename = "C:/Windows/Fonts/mingliu.ttc"
font1 = pygame.font.Font(font_filename, 24)  # 新細明體
text1 = font1.render("顯示中文", True, (255, 0, 0), (255, 255, 255))  # 中文,不同背景色
background.blit(text1, (20, 10))
text2 = font1.render("Show english.", True, (0, 0, 255), (0, 255, 0))  # 英文,相同背景色
background.blit(text2, (20, 50))
running = True
screen.blit(background, (0, 0))
pygame.display.update()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
