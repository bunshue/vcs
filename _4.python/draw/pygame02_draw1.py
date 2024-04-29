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

color = pygame.color.Color("#0A32F4")
pygame.draw.rect(screen, color, [620, 620, 160, 160])  # x_st, y_st, w, h
pygame.display.flip()

for i in range(7):
    # 畫線
    pygame.draw.line(screen, red, [0, 100 * i], [W, 100 * i])
    pygame.draw.line(screen, red, [100 * i, 0], [100 * i, H])
    # 繪製矩形
    pygame.draw.rect(screen, green, (100 * i, 0, 50, 50))
    pygame.draw.rect(screen, blue, (0, 100 * i, 50, 50))

# 繪製線條
pygame.draw.line(screen, red, (70, 0), (70, 200), 20)
pygame.draw.line(screen, green, (90, 0), (90, 200), 20)
pygame.draw.line(screen, blue, (110, 0), (110, 200), 20)
pygame.draw.line(screen, yellow, (130, 0), (130, 200), 20)
pygame.draw.line(screen, Fuchsia, (150, 0), (150, 200), 20)
pygame.draw.line(screen, Aqua, (170, 0), (170, 200), 20)
pygame.draw.line(screen, Gray, (190, 0), (190, 200), 20)


# 繪製五個同心圓
cx = 200
cy = 300

radius_1 = 100
radius_2 = 80
radius_3 = 60
radius_4 = 40
radius_5 = 20

pygame.draw.circle(screen, white, (cx, cy), radius_1)
pygame.draw.circle(screen, red, (cx, cy), radius_2)
pygame.draw.circle(screen, green, (cx, cy), radius_3)
pygame.draw.circle(screen, blue, (cx, cy), radius_4)
pygame.draw.circle(screen, yellow, (cx, cy), radius_5)


# 繪製圓形
cx = 400
cy = 300
pygame.draw.circle(screen, red, (cx, cy), 20, 10)
pygame.draw.circle(screen, yellow, (cx, cy), 40, 10)
pygame.draw.circle(screen, green, (cx, cy), 60, 10)
pygame.draw.circle(screen, Aqua, (cx, cy), 80, 10)
pygame.draw.circle(screen, Fuchsia, (cx, cy), 100, 10)
pygame.draw.circle(screen, blue, (cx, cy), 120, 10)
pygame.draw.circle(screen, Gray, (cx, cy), 140, 10)

color = pygame.color.Color("#123456")
pygame.draw.circle(screen, color, [700, 700], 50)
pygame.display.flip()


pygame.draw.ellipse(screen, yellow, [0, 500, 300, 100])

# 畫多邊形
pygame.draw.polygon(screen, red, ((15, 180), (130, 10), (235, 180)))
pygame.draw.polygon(
    screen, blue, [(15, 120), (65, 35), (185, 35), (230, 120), (130, 180)], 6
)


# 繪製文字
ft = pygame.font.SysFont("Malgun Gothic", 60)  # sugar有此字型 但kilo無
wd1 = ft.render("萬象更新", False, green)
screen.blit(wd1, (300, 420))
wd2 = ft.render("brand new", True, red)
screen.blit(wd2, (300, 500))

# ft = pygame.font.SysFont('Malgun Gothic', 36)
ft = pygame.font.SysFont("Arial", 36)
wd1 = ft.render("Encyclopedia", False, blue, Aqua)
screen.blit(wd1, (10, 20))
wd2 = ft.render("百科全書", True, red, Aqua)
screen.blit(wd2, (10, 80))
wd1 = ft.render("lockdown", False, blue, Aqua)
screen.blit(wd1, (10, 140))
wd2 = ft.render("世界大同", True, red, Aqua)
screen.blit(wd2, (10, 200))
wd1 = ft.render("binge-watch", False, blue, Aqua)
screen.blit(wd1, (10, 260))
wd2 = ft.render("追劇", True, red, Aqua)
screen.blit(wd2, (10, 320))

# 產生Surface物件, 上色，繪製成形
face = pygame.Surface([100, 100])
print("取得face參數")
print(face.get_width(), face.get_height())
face.fill(red)
screen.blit(face, (500, 100))

"""
#產生Surface物件, 上色，繪製成形
face = pygame.Surface(screen.get_size())
print(face.get_width(), face.get_height())
face.convert()#產生副本
face.fill(red)#填滿指定色
screen.blit(face, (0, 0))#輸出到畫布上
pygame.display.update()#繪製視窗顯示於螢幕上
"""

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
