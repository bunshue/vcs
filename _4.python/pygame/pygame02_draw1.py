"""
pygame 測試大全
"""

import sys
import time
import pygame

W, H = 800, 600
screen_size = (W, H)    # 設定屏幕尺寸
surface_size = (W-50, H-50)    # 設定surface尺寸

# 設定顏色
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

RosyBrown = 255, 193, 193 # 玫紅色
fuchsia = (255, 0, 255) #紫色
aqua = (0, 255, 255) #淺藍色
gray = (128, 128, 128) #灰色
grey = 79, 79, 79        # 灰色

# 設定顏色, same
red = pygame.color.Color('#FF0000')
green = pygame.color.Color('#00FF00')
blue = pygame.color.Color('#0000FF')
black = pygame.color.Color('#000000')
white = pygame.color.Color('#FFFFFF')

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

def run_pygame():
   # 更新屏幕, 保持屏幕打開, 直到用戶退出, 偵測視窗是否被關閉(8)
   pygame.display.update()
   running = True
   while running:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
   pygame.quit()

print("------------------------------------------------------------")  # 60個

print('pygame 01')

pygame.init()  # 初始化Pygame
screen = pygame.display.set_mode(screen_size)  # 創建屏幕
pygame.display.set_caption("畫圖綜合")

print("取得screen參數")
print(screen.get_size())

# 利用screen物件來作為畫布，以fill()方法填上顏色
screen.fill(gray)

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
pygame.draw.line(screen, fuchsia, (150, 0), (150, 200), 20)
pygame.draw.line(screen, aqua, (170, 0), (170, 200), 20)
pygame.draw.line(screen, gray, (190, 0), (190, 200), 20)


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
pygame.draw.circle(screen, aqua, (cx, cy), 80, 10)
pygame.draw.circle(screen, fuchsia, (cx, cy), 100, 10)
pygame.draw.circle(screen, blue, (cx, cy), 120, 10)
pygame.draw.circle(screen, gray, (cx, cy), 140, 10)

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
wd1 = ft.render("Encyclopedia", False, blue, aqua)
screen.blit(wd1, (10, 20))
wd2 = ft.render("百科全書", True, red, aqua)
screen.blit(wd2, (10, 80))
wd1 = ft.render("lockdown", False, blue, aqua)
screen.blit(wd1, (10, 140))
wd2 = ft.render("世界大同", True, red, aqua)
screen.blit(wd2, (10, 200))
wd1 = ft.render("binge-watch", False, blue, aqua)
screen.blit(wd1, (10, 260))
wd2 = ft.render("追劇", True, red, aqua)
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


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print('pygame 10')

pygame.init()  # 初始化Pygame
#screen = pygame.display.set_mode(screen_size)  # 產生視窗screen
screen = pygame.display.set_mode(screen_size, 0)  # 產生視窗screen
pygame.display.set_caption('pygame測試10 draw')

# 產生Surface物件, 上色，繪製成形
surface = pygame.Surface(surface_size)
screen.fill(gray)

#繪製綠框、內塗紅色矩形
#pygame.draw.rect(screen, green, (60, 35, 120, 120))
#pygame.draw.rect(screen, red, (50, 25, 140, 140), 10)

# 繪製一個實心三角形和框線為6的五邊形
"""
pygame.draw.polygon(screen, red, ((10, 180), (130, 10), (235, 180)))
pygame.draw.polygon(screen, white, [(15, 120), (65, 35), (185, 35), (230, 120), (130, 180)], 8)
"""

# 產生圓弧線
pygame.draw.arc(screen, aqua, (15, 10, 225, 180), 0, 1.6, 8)
pygame.draw.arc(screen, red, (20, 17, 212, 173), 0, 3.1, 8)
pygame.draw.arc(screen, fuchsia, (28, 27, 195, 157), 0, 4.7, 8)
pygame.draw.arc(screen, green, (38, 37, 173, 137), 0, 9.9, 8)
pygame.draw.line(screen, yellow, (10, 100), (240, 100), 2)
pygame.draw.line(screen, white, (125, 5), (125, 180), 2)

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

run_pygame()

print('------------------------------------------------------------')	#60個

print('pygame 11')

pygame.init()  # 初始化Pygame
screen = pygame.display.set_mode(screen_size, 0, 32)  # 產生視窗screen
pygame.display.set_caption('pygame測試11 draw')

#利用Surface物件來作為畫布，以fill()方法填上白色
screen.fill(white)

#繪製半徑為40的黃色實心圓形
pygame.draw.circle(screen, red, (103, 103), 82, 12)
pygame.draw.circle(screen, yellow, (100, 100), 80)

#繪製圓弧
pygame.draw.arc(screen, aqua, (15, 10, 200, 185), 4.3, 2.0, 8)

#繪製線條
pygame.draw.line(screen, fuchsia, (70, 220), (100, 180), 20)
pygame.draw.line(screen, green, (198, 185), (280, 30), 6)
pygame.draw.line(screen, green, (280, 30), (380, 180), 6)

#繪製綠色矩形
pygame.draw.rect(screen, green, (30, 210, 140, 40))
pygame.draw.rect(screen, gray, (204, 198, 60, 40))
pygame.draw.rect(screen, gray, (304, 190, 60, 40))

#繪製三角形
pygame.draw.polygon(screen, gray, ((281, 53), (200, 205), (371, 187)))

#繪製橢圓形
pygame.draw.ellipse(screen, RosyBrown, (250, 230, 70, 30), 8)
pygame.draw.ellipse(screen, fuchsia, (240, 258, 65, 25), 5)

#繪製文字
#ft = pygame.font.SysFont('Malgun Gothic', 36)
ft = pygame.font.SysFont('微軟正黑體', 36)
wd1 = ft.render('Hello Python', False, red)
screen.blit(wd1, (10, 300))
#wd2 = ft.render('黃河之水天上來', True, green, yellow)
#screen.blit(wd2, (10, 80))

run_pygame()

print("------------------------------------------------------------")  # 60個

pygame.init()  # 初始化Pygame
screen = pygame.display.set_mode(screen_size)  # 創建屏幕
pygame.display.set_caption("畫圖綜合")

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

print("------------------------------------------------------------")  # 60個

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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


