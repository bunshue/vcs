import pygame
import sys

# 初始化Pygame
pygame.init()

# 設定屏幕尺寸
screen_size = (600, 600)

# 創建屏幕
screen = pygame.display.set_mode(screen_size)

# 設定顏色
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# 繪製五個同心圓
center_x = screen_size[0] // 2
center_y = screen_size[1] // 2

radius_1 = 200
radius_2 = 150
radius_3 = 100
radius_4 = 50
radius_5 = 20

pygame.draw.circle(screen, white, (center_x, center_y), radius_1)
pygame.draw.circle(screen, red, (center_x, center_y), radius_2)
pygame.draw.circle(screen, green, (center_x, center_y), radius_3)
pygame.draw.circle(screen, blue, (center_x, center_y), radius_4)
pygame.draw.circle(screen, yellow, (center_x, center_y), radius_5)

# 更新屏幕
pygame.display.update()

# 保持屏幕打開，直到用戶退出
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
