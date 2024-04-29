import pygame, sys  # 滙入PyGame套件，系統模組

pygame.init()  # 將PyGame初始化


# 設定使用參數
size = width, height = 240, 190
White = (255, 255, 255)  # 白色
Red = (255, 0, 0)  # 紅色
Green = (0, 255, 0)  # 綠色
Gray = (128, 128, 128)  # 灰色
Yellow = (255, 255, 0)  # 黃色
Aqua = (0, 255, 255)  # 淺藍色
Fuchsia = (255, 0, 255)  # 紫色


# (1).產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size), 0)
pygame.display.set_caption("繪製圓弧")

# (2)產生Surface物件, 上色，繪製成形
face = pygame.Surface(screen.get_size())
screen.fill(Gray)  # 填滿灰色

# 繪製綠框、內塗紅色矩形
# pygame.draw.rect(screen, Green, (60, 35, 120, 120))
# pygame.draw.rect(screen, Red, (50, 25, 140, 140), 10)

# 繪製一個實心三角形和框線為6的五邊形
"""pygame.draw.polygon(screen, Red, ((10, 180),
    (130, 10), (235, 180)))
pygame.draw.polygon(screen, White, [(15, 120), (65, 35),
      (185, 35), (230, 120), (130, 180)], 8)"""

# 產生圓弧線
pygame.draw.arc(screen, Aqua, (15, 10, 225, 180), 0, 1.6, 8)
pygame.draw.arc(screen, Red, (20, 17, 212, 173), 0, 3.1, 8)
pygame.draw.arc(screen, Fuchsia, (28, 27, 195, 157), 0, 4.7, 8)
pygame.draw.arc(screen, Green, (38, 37, 173, 137), 0, 9.9, 8)
pygame.draw.line(screen, Yellow, (10, 100), (240, 100), 2)
pygame.draw.line(screen, White, (125, 5), (125, 180), 2)


# (3).偵測視窗是否被關閉
while True:
    for event in pygame.event.get():
        # 判斷事件的常數是否為QUIT常數
        if event.type == pygame.QUIT:
            pygame.quit()  # quit()方法結束Pygame程序
            sys.exit()
    pygame.display.update()  # 繪製視窗顯示於螢幕上
