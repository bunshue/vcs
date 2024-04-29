"""
pygame 測試大全

"""

import sys
import pygame

W, H = 800, 800

pygame.init()  # 初始化Pygame
screen_size = (W, H)  # 設定屏幕尺寸
screen = pygame.display.set_mode(screen_size)  # 創建屏幕
pygame.display.set_caption("畫圖綜合")

# 設定顏色
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

Fuchsia = (255, 0, 255)  # 紫色
Aqua = (0, 255, 255)  # 淺藍色
Gray = (128, 128, 128)  # 灰色
# 設定顏色, same
red = pygame.color.Color("#FF0000")
green = pygame.color.Color("#00FF00")
blue = pygame.color.Color("#0000FF")
black = pygame.color.Color("#000000")
white = pygame.color.Color("#FFFFFF")

print("取得screen參數")
print(screen.get_size())

# 利用screen物件來作為畫布，以fill()方法填上顏色
screen.fill(Gray)

print("------------------------------------------------------------")  # 60個


done = False

while not done:
    screen.fill(white)

    # 反鋸齒直線
    pygame.draw.aaline(screen, black, [10, 10], [30 + 600, 25 + 600])
    pygame.draw.aaline(screen, black, [40, 10], [60 + 600, 25 + 600])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()

pygame.quit()

import sys

sys.exit()


print("------------------------------------------------------------")  # 60個

# 更新屏幕
pygame.display.update()

# pygame 存圖命令
# pygame.image.save(screen, "tmp_save_pic.png")

# 保持屏幕打開，直到用戶退出
# 偵測視窗是否被關閉
while True:
    for event in pygame.event.get():
        # 判斷事件的常數是否為QUIT常數
        if event.type == pygame.QUIT:
            pygame.quit()  # quit()方法結束Pygame程序
            sys.exit()
    pygame.display.update()
