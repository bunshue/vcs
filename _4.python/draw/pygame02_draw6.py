import pygame, sys  # 滙入PyGame套件, 系統模組

pygame.init()  # 將PyGame初始化

# 設定視窗寬、高和色彩參數
size = width, height = 400, 300
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)
Fuchsia = (255, 0, 255)  # 紫色
Aqua = (0, 255, 255)  # 淺藍色
Gray = (128, 128, 128)  # 灰色
Gray2 = 181, 181, 181  # 淺灰
RosyBrown = 255, 193, 193  # 玫紅色

# 產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption("**-Drawing...-**")

# 利用Surface物件來作為畫布，以fill()方法填上白色
screen.fill(White)

# 繪製半徑為40的黃色實心圓形
pygame.draw.circle(screen, Red, (103, 103), 82, 12)
pygame.draw.circle(screen, Yellow, (100, 100), 80)

# 繪製圓弧
pygame.draw.arc(screen, Aqua, (15, 10, 200, 185), 4.3, 2.0, 8)

# 繪製線條
pygame.draw.line(screen, Fuchsia, (70, 220), (100, 180), 20)
pygame.draw.line(screen, Green, (198, 185), (280, 30), 6)
pygame.draw.line(screen, Green, (280, 30), (380, 180), 6)

# 繪製綠色矩形
pygame.draw.rect(screen, Green, (30, 210, 140, 40))
pygame.draw.rect(screen, Gray2, (204, 198, 60, 40))
pygame.draw.rect(screen, Gray2, (304, 190, 60, 40))

# 繪製三角形
pygame.draw.polygon(screen, Gray, ((281, 53), (200, 205), (371, 187)))

# 繪製橢圓形
pygame.draw.ellipse(screen, RosyBrown, (250, 230, 70, 30), 8)
pygame.draw.ellipse(screen, Fuchsia, (240, 258, 65, 25), 5)

running = True  # 判斷程式是否執行狀態
while running:
    for event in pygame.event.get():
        # 判斷事件的常數是否為QUIT常數
        if event.type == pygame.QUIT:
            pygame.quit()  # quit()方法結束Pygame程序
            sys.exit()
    pygame.display.update()
