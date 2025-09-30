"""
pygame 測試大全

1. 一般
2. 畫圖畫字
3. 滑鼠鍵盤

最後再搬出





pygame提供的模組

color	提供色彩的設定
display	顯示螢幕
event	處理事件
image	處理圖片
key	處理鍵盤的按鈕
mouse	處理滑鼠訊息
movie	處理視訊播放
mixer	用來播放聲音
time	處理時間

pygame.display.set_mode()	建立視窗並初始化
pygame.display.set_caption()	在標題列顯示文字
pygame.display.flip()		更新畫面 將Surface全部更新後並顯示於畫面上
pygame.display.update()		依據軟體做部分畫面的更新



screen : 整個視窗
surface : 一個物件

"""

import sys
import time
import math
import random
import pygame

W, H = 800, 600
screen_size = (W, H)  # 設定屏幕尺寸
surface_size = (W - 50, H - 50)  # 設定surface尺寸

# pygame_顏色共同 R G B
RED = (255, 0, 0)  # R G B
GREEN = (0, 255, 0)  # R G B
BLUE = (0, 0, 255)  # R G B
CYAN = (0, 255, 255)  # R G B
MAGENTA = (255, 0, 255)  # R G B
YELLOW = (255, 255, 0)  # R G B
BLACK = (0, 0, 0)  # R G B
WHITE = (255, 255, 255)  # R G B
GRAY = (128, 128, 128)  # R G B
MAROON = (128, 0, 0)  # 栗色, Maroon
OLIVE = (128, 128, 0)  # 橄欖綠, Olive
LIME = (0, 128, 0)  # 綠色, Green
TEAL = (0, 128, 128)  # 藍綠色, Teal
NAVY = (0, 0, 128)  # 藏青色, Navy
PURPLE = (128, 0, 128)  # 紫色, Purple
SILVER = (192, 192, 192)  # 銀色, Silver
RosyBrown = (255, 193, 193)  # 玫紅色

# 設定顏色, same
RED = pygame.color.Color("#FF0000")
GREEN = pygame.color.Color("#00FF00")
BLUE = pygame.color.Color("#0000FF")
BLACK = pygame.color.Color("#000000")
WHITE = pygame.color.Color("#FFFFFF")

filename = "D:/_git/vcs/_4.python/_data/picture1.jpg"
font_filename = "C:/Windows/Fonts/mingliu.ttc"  # 新細明體


def randColor():
    r = random.randint(0, 255)  # 含頭尾
    g = random.randint(0, 255)  # 含頭尾
    b = random.randint(0, 255)  # 含頭尾
    return (r, g, b)


def init_pygame(name, color):
    print(name)
    pygame.init()  # 初始化Pygame

    screen = pygame.display.set_mode(screen_size)  # 產生視窗screen
    # screen = pygame.display.set_mode(screen_size, 0, 32)  # 產生視窗screen
    # screen = pygame.display.set_mode(screen_size, 0)  # 產生視窗screen

    pygame.display.set_caption(name)

    # print("取得screen參數 :", screen.get_size())

    # 利用screen物件來作為畫布，以fill()方法填上顏色
    screen.fill(color)
    return screen


def run_pygame():
    # 更新屏幕, 保持屏幕打開, 直到用戶退出, 偵測視窗是否被關閉(8)
    pygame.display.update()  # 繪製視窗顯示於螢幕上
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
                running = False
    pygame.quit()  # 關閉繪圖視窗


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 01 載入圖片"
pygame_name = "pygame 01 建立畫布"
pygame_name = "pygame 01 建立畫布 + 使用surface 載入圖片"

print("建立screen, 整個視窗")
screen = init_pygame(pygame_name, YELLOW)

print("建立surface, 一個物件")
# 產生Surface物件, 上色，繪製成形
surface = pygame.Surface((100, 100))
# print(surface.get_width(), surface.get_height())#取得surface參數
surface = surface.convert()  # 產生副本
surface.fill(GREEN)  # surface填滿指定色
print("將surface貼到screen上")
screen.blit(surface, (25, 25))  # 輸出到畫布上

print("建立surface2, 一個物件")
# 產生Surface2物件, 上色，繪製成形
surface2 = pygame.Surface((150, 150))
# print(surface2.get_width(), surface2.get_height())#取得surface2參數
surface2 = surface2.convert()  # 產生副本
surface2.fill(BLUE)  # surface2填滿指定色
print("將surface2貼到screen上")
screen.blit(surface2, (150, 25))  # 輸出到畫布上

print("讀取圖片貼到surface上")
# 方法load()載入圖片，convert()能提高圖片的處理速度
filename = "D:/_git/vcs/_1.data/______test_files1/__pic/_anime/_貓咪/cat3.png"
image = pygame.image.load(filename)
image.convert()
x_st, y_st = 320, 30
screen.blit(image, (x_st, y_st))


filename = "D:/_git/vcs/_4.python/_data/picture1.jpg"
# 方法load()載入圖片，convert()能提高圖片的處理速度
image = pygame.image.load(filename)
image.convert()

# 直接貼上圖片
x_st, y_st = 25, 180
screen.blit(image, (x_st, y_st))

# 改變圖片大小
image = pygame.transform.scale(image, (300 * 3 // 4, 400 * 3 // 4))
x_st, y_st = 500, 250
screen.blit(image, (x_st, y_st))

run_pygame()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 02 Animation"
screen = init_pygame(pygame_name, YELLOW)

filename = "D:/_git/vcs/_1.data/______test_files1/__pic/_anime/_貓咪/cat3.png"

fps = 30  # 每秒的執行次數, 設定每秒畫格30，利用Clock()方法來確保動畫能持續進行

# 載入圖片，get_rect()取得矩形區域
image = pygame.image.load(filename)
pos_X, pos_Y = 5, 5  # 設定開始移動的X、Y座標
move = "Down"
clock = pygame.time.Clock()  # 建立時間元件

# tick()方法依據fps之值讓移動圖片有動畫效果
# blit()不斷在畫布上繪製圖片
# update()進行動作的更新

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False

    screen.fill(YELLOW)

    if move == "Down":
        pos_Y += 5
        if pos_Y == 230:
            move = "Right"
    elif move == "Right":
        pos_X += 5
        if pos_X == 315:
            move = "Up"
    elif move == "Up":
        pos_Y -= 5
        if pos_Y == 10:
            move = "Left"
    elif move == "Left":
        pos_X -= 5
        if pos_X == 10:
            move = "Down"

    # print('移動座標:', pos_X, pos_Y)
    # blit()方法在畫布上繪製圖片
    screen.blit(image, (pos_X, pos_Y))
    pygame.display.update()  # 繪製視窗顯示於螢幕上
    clock.tick(fps)  # 依fps的值來產生動畫, 每秒執行fps次

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 03 按鍵事件"
screen = init_pygame(pygame_name, YELLOW)

filename = "D:/_git/vcs/_1.data/______test_files1/__pic/_anime/_貓咪/cat3.png"

from pygame.locals import *

# 載入圖片並設座標
surface = pygame.image.load(filename).convert()
pos_X, pos_Y = 0, 0  # 起始位置
Xmove, Ymove = 0, 0  # 移動座標

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False

        screen.fill((YELLOW))

        # 判斷那個按鍵被按？
        if event.type == KEYDOWN:
            # 向左方向鍵，減少座標值
            if event.key == pygame.K_LEFT:
                pos_X -= 5
            # 向右方向鍵，增加座標值
            elif event.key == pygame.K_RIGHT:
                pos_X += 5
            # 向上下向鍵，減少座標值
            elif event.key == pygame.K_UP:
                pos_Y -= 5
            # 向下方向鍵，增加座標值
            elif event.key == pygame.K_DOWN:
                pos_Y += 5

        # 放掉鍵盤按鍵，回到原點
        # if event.type == pygame.KEYUP:
        #   print('放開按鍵')

        screen.blit(surface, (pos_X, pos_Y))  # 輸出到畫布上
        pygame.display.update()  # 繪製視窗顯示於螢幕上

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 04 滑鼠事件"
screen = init_pygame(pygame_name, YELLOW)

filename = "D:/_git/vcs/_1.data/______test_files1/__pic/_anime/_貓咪/cat3.png"
# 載入圖片
imageRect = pygame.image.load(filename).convert_alpha()

imageX, imageY = 0, 0  # 起始位置

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False
    # screen.fill(BLACK)

    # 偵測滑鼠的按鈕
    buts = pygame.mouse.get_pressed()

    # 按下滑鼠左鍵才能移動圖片
    if buts[0]:
        moving = True
        # 取得滑鼠座標
        imageX, imageY = pygame.mouse.get_pos()  # 取得滑鼠座標

        # 取得座標讓圖片不要超過視窗範圍
        imageX -= imageRect.get_width() / 2
        imageY -= imageRect.get_height() / 2
        # print(imageX, imageY)
    else:
        moving = False

    screen.blit(imageRect, (imageX, imageY))
    pygame.display.update()  # 繪製視窗顯示於螢幕上

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "D:/_git/vcs/_1.data/______test_files1/__pic/_anime/_貓咪/cat3.png"

pygame_name = "pygame 05 碰撞的偵測"
screen = init_pygame(pygame_name, YELLOW)

# 設定每秒畫格20，利用Clock()方法來確保動畫能持續進行
fps = 20  # 每秒的執行次數

clock = pygame.time.Clock()  # 建立時間元件

# 載入圖片，get_rect()取得矩形的移動區域
image = pygame.image.load(filename)
imageRect = image.get_rect()

# 屬性center-設定圖片要開始移動的中心點
imageRect.center = 400, 400

# 屬性topleft取得圖片移動區域左上角到畫布的位置
pos_X, pos_Y = imageRect.topleft

# moveX, moveY = 5, -5 #設定圖片的移動速度會形成固定範圍
# 避免移動成固定範圍，以隨機值來取得起始角度並轉為弧度
posi = random.randint(45, 60)
angle = math.radians(posi)
# 設定圖片水平和垂直的移動速度
moveX = 5 * math.sin(angle)
moveY = -5 * math.cos(angle)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False

    screen.fill(YELLOW)
    clock.tick(fps)  # 依fps的值來產生動畫, 每秒執行fps次

    # 改變水平、垂直位置並重設物件的中心點
    pos_X += moveX
    pos_Y += moveY
    imageRect.center = pos_X, pos_Y

    # 偵測水平、垂直方向的移動是否會碰到畫布的左、右或上、下邊界
    # 碰到時改變moveX、moveY為正值並改變方向
    if (imageRect.left <= 0) or (imageRect.right >= screen.get_width()):
        moveX *= -1
        print(moveX, moveY)
    elif (imageRect.top <= 5) or (imageRect.bottom >= screen.get_height() - 5):
        moveY *= -1
    screen.blit(image, imageRect.topleft)
    pygame.display.update()  # 繪製視窗顯示於螢幕上

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 06"
screen = init_pygame(pygame_name, YELLOW)

clock = pygame.time.Clock()  # 建立時間元件

w = W / 10
h = H / 10
N = 10
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False
    r = random.randint(0, 255)  # 含頭尾
    g = random.randint(0, 255)  # 含頭尾
    b = random.randint(0, 255)  # 含頭尾
    x = N * random.randint(0, (W) // N)  # 含頭尾
    y = N * random.randint(0, (H) // N)  # 含頭尾

    # pygame.draw.rect(screen, (r, g, b), (x, y, w, h))
    pygame.draw.ellipse(screen, (r, g, b), (x, y, w, h))
    pygame.display.flip()  # 更新畫面

    clock.tick(10)  # 依fps的值來產生動畫, 每秒執行fps次

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 07"
screen = init_pygame(pygame_name, YELLOW)

clock = pygame.time.Clock()  # 建立時間元件

width = 200
height = 200
x = W / 2 - width / 2
y = H / 2 - height / 2

color = pygame.color.Color("#FF0000")

count = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False

    screen.fill(LIME)
    pygame.draw.ellipse(screen, color, [x, y, width, height])
    width += math.cos(count) * 10
    x -= (math.cos(count) * 10) / 2
    height += math.sin(count) * 10
    y -= (math.sin(count) * 10) / 2
    count += 0.5

    pygame.display.flip()  # 更新畫面

    clock.tick(20)  # 依fps的值來產生動畫, 每秒執行fps次

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 08 製作一個按鈕, 測試按鈕事件"
screen = init_pygame(pygame_name, YELLOW)

clock = pygame.time.Clock()  # 建立時間元件

w = 200
h = 150
x_st = 100
y_st = 100

toggled = False
pos = (0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()  # 取得滑鼠座標
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False

    # 改變視窗背景色
    if toggled:
        screen.fill(RED)
    else:
        screen.fill(GREEN)

    pygame.draw.rect(screen, BLUE, [x_st, y_st, w, h])
    # pygame.draw.rect(screen, BLUE, [x_st, y_st, w, h])
    # 繪製矩形
    # x_st, y_st, w, h = 20, 250, 100, 50
    # pygame.draw.rect(screen, GREEN, (x_st, y_st, w, h))

    if x_st <= pos[0] <= x_st + w and y_st <= pos[1] <= y_st + h:
        print("你按了按鈕", pos)
        toggled = not toggled
        pos = (0, 0)

    pygame.display.flip()  # 更新畫面
    clock.tick(10)  # 依fps的值來產生動畫, 每秒執行fps次

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# movingTarget.py

pygame_name = "pygame 09"
screen = init_pygame(pygame_name, YELLOW)

clock = pygame.time.Clock()  # 建立時間元件

windowSize = [400, 300]
btnWidth = 50
btnLength = 20
btnX = (windowSize[0] - btnWidth) / 2
btnY = (windowSize[1] - btnLength) / 2

toggled = False
pos = (0, 0)

points = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()  # 取得滑鼠座標
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False

    # 改變視窗背景色
    if toggled:
        screen.fill(BLACK)
    else:
        screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, [btnX, btnY, btnWidth, btnLength])

    if btnX <= pos[0] <= btnX + btnWidth and btnY <= pos[1] <= btnY + btnLength:
        toggled = not toggled
        pos = (0, 0)
        points += 1

    btnX += random.randint(-1 - points, 1 + points)
    btnY += random.randint(-1 - points, 1 + points)

    pygame.display.flip()  # 更新畫面
    clock.tick(10)  # 依fps的值來產生動畫, 每秒執行fps次

pygame.quit()  # 關閉繪圖視窗

print(points)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# explosions.py

pygame_name = "pygame 10"
screen = init_pygame(pygame_name, YELLOW)

clock = pygame.time.Clock()  # 建立時間元件

count = 0
click = False
limit = 30
pos = (0, 0)

running = True
while running:
    # screen.fill(BLACK)

    if click and count < limit:
        pygame.draw.circle(screen, color, pos, count)
        count += 1
        if count >= limit:
            click = False

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()  # 取得滑鼠座標
            click = True
            count = 0
            color = randColor()
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False
    pygame.display.flip()  # 更新畫面
    clock.tick(60)  # 依fps的值來產生動畫, 每秒執行fps次

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 11 偵測滑鼠位置"
screen = init_pygame(pygame_name, YELLOW)

clock = pygame.time.Clock()  # 建立時間元件

pos_list = []

# 更新屏幕
pygame.display.update()  # 繪製視窗顯示於螢幕上

# 保持屏幕打開，直到用戶退出
# 偵測視窗是否被關閉

running = True
while running:
    # screen.fill(YELLOW)
    pygame.draw.rect(screen, BLACK, [0, 0, 0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:  # 滑鼠事件
            pos = pygame.mouse.get_pos()  # 取得滑鼠座標
            print(pos)
            pos_list.append(pos)
            if len(pos_list) > 1:
                # pygame.draw.lines(screen, RED, False, pos_list)
                pygame.draw.lines(screen, RED, True, pos_list)

    pygame.display.flip()  # 更新畫面
    clock.tick(10)  # 依fps的值來產生動畫, 每秒執行fps次

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# mesh.py

pygame_name = "pygame 11"
screen = init_pygame(pygame_name, YELLOW)

clock = pygame.time.Clock()  # 建立時間元件

windowSize = [400, 300]
points = []

running = True
while running:
    # screen.fill(BLACK)
    if len(points) > 10:
        del points[0]
    if len(points) > 1:
        pygame.draw.lines(screen, RED, True, points)
    for point in points:
        pygame.draw.line(screen, RED, point, [point[0], windowSize[1]])

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()  # 取得滑鼠座標
            points.append(pos)
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False
    pygame.display.flip()  # 更新畫面
    clock.tick(60)  # 依fps的值來產生動畫, 每秒執行fps次

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# mouseTrails.py

pygame_name = "pygame 12"
screen = init_pygame(pygame_name, YELLOW)

clock = pygame.time.Clock()  # 建立時間元件

points = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False

    # screen.fill(BLACK)
    pos = pygame.mouse.get_pos()  # 取得滑鼠座標
    if pos[0] != 0 and pos[1] != 0:
        points.append(pos)
    if len(points) >= 20:
        del points[0]

    if len(points) > 2:
        pygame.draw.aalines(screen, RED, False, points)

    pygame.display.flip()  # 更新畫面
    clock.tick(30)  # 依fps的值來產生動畫, 每秒執行fps次

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("畫圖畫字")
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 13 畫圖綜合"
screen = init_pygame(pygame_name, YELLOW)

# pygame.display.flip()  # 更新畫面

print("畫直線")
line_width = 10  # 線寬
x1, y1 = 50, 50
x2, y2 = 250, 50
# 畫直線 色 起 終 寬
pygame.draw.line(screen, RED, (x1, y1), (x2, y2), line_width)
pygame.draw.line(screen, RED, (x1, y1 + 50), (x2, y2 + 50), 30)
pygame.draw.line(screen, RED, (x1, y1 + 100), (x2, y2 + 100), 15)
pygame.draw.line(screen, RED, (x1, y1 + 150), (x2, y2 + 150))  # 無line_width, 即 1 點

# 反鋸齒直線
pygame.draw.aaline(screen, BLACK, [10, 10], [30 + 200, 25 + 200])
pygame.draw.aaline(screen, BLACK, [40, 10], [60 + 200, 25 + 200])

# 繪製矩形
x_st, y_st, w, h = 20, 250, 100, 50
pygame.draw.rect(screen, GREEN, (x_st, y_st, w, h))

y_st = y_st + 60
pygame.draw.rect(screen, BLUE, (x_st, y_st, w, h))

# 繪製綠框、內塗紅色矩形
pygame.draw.rect(screen, GREEN, (150, 235, 120, 120))
pygame.draw.rect(screen, RED, (140, 225, 140, 140), 10)

# 繪製五個同心圓
cx = 400
cy = 300
radius_1 = 100
radius_2 = 80
radius_3 = 60
radius_4 = 40
radius_5 = 20
pygame.draw.circle(screen, WHITE, (cx, cy), radius_1)
pygame.draw.circle(screen, RED, (cx, cy), radius_2)
pygame.draw.circle(screen, GREEN, (cx, cy), radius_3)
pygame.draw.circle(screen, BLUE, (cx, cy), radius_4)
pygame.draw.circle(screen, YELLOW, (cx, cy), radius_5)

# 繪製圓形
cx = 650
cy = 300
pygame.draw.circle(screen, RED, (cx, cy), 20, 10)
pygame.draw.circle(screen, YELLOW, (cx, cy), 40, 10)
pygame.draw.circle(screen, GREEN, (cx, cy), 60, 10)
pygame.draw.circle(screen, CYAN, (cx, cy), 80, 10)
pygame.draw.circle(screen, MAGENTA, (cx, cy), 100, 10)
pygame.draw.circle(screen, BLUE, (cx, cy), 120, 10)
pygame.draw.circle(screen, GRAY, (cx, cy), 140, 10)

pygame.draw.circle(screen, RED, [500, 500], 100)

# 繪製半徑為40的黃色實心圓形
pygame.draw.circle(screen, RED, (103 + 300, 103), 82, 12)
pygame.draw.circle(screen, YELLOW, (100 + 300, 100), 80)

# 繪製橢圓形
x_st, y_st, w, h = 50, 450, 70, 30
pygame.draw.ellipse(screen, RosyBrown, (x_st, y_st, w, h), 8)

x_st, y_st, w, h = 50, 500, 65, 25
pygame.draw.ellipse(screen, MAGENTA, (x_st, y_st, w, h), 5)

x_st, y_st, w, h = 150, 450, 200, 100
pygame.draw.ellipse(screen, YELLOW, [x_st, y_st, w, h])

# 繪製弧線
x_st, y_st = 400, 400
pygame.draw.arc(screen, CYAN, (x_st + 15, y_st + 10, 225, 180), 0, 1.6, 8)
pygame.draw.arc(screen, RED, (x_st + 20, y_st + 17, 212, 173), 0, 3.1, 8)
pygame.draw.arc(screen, MAGENTA, (x_st + 28, y_st + 27, 195, 157), 0, 4.7, 8)
pygame.draw.arc(screen, GREEN, (x_st + 38, y_st + 37, 173, 137), 0, 9.9, 8)
pygame.draw.arc(screen, CYAN, (x_st + 150, y_st, 200, 185), 4.3, 2.0, 8)

# 畫多邊形
x_st, y_st = 550, 20
pygame.draw.polygon(
    screen, RED, ((x_st, y_st), (x_st + 50, y_st + 100), (x_st - 50, y_st + 100))
)

x_st, y_st = 550, 0
pygame.draw.polygon(
    screen,
    BLUE,
    [
        (x_st + 15, y_st + 120),
        (x_st + 65, y_st + 35),
        (x_st + 185, y_st + 35),
        (x_st + 230, y_st + 120),
        (x_st + 130, y_st + 180),
    ],
    6,
)
pygame.display.flip()  # 更新畫面

run_pygame()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

x_st, y_st = 20, 20
dx, dy = 400, 40
font_size = 30

pygame_name = "pygame 14 畫圖綜合 繪製文字"
screen = init_pygame(pygame_name, YELLOW)

# 產生Surface物件, 上色，繪製成形
surface = pygame.Surface(screen.get_size())
# print(surface.get_width(), surface.get_height())
surface = surface.convert()  # 產生副本
surface.fill(WHITE)  # surface填滿指定色

font1 = pygame.font.Font(font_filename, font_size)
text1 = font1.render("顯示中文", True, RED, WHITE)  # 中文,不同背景色
surface.blit(text1, (x_st + dx * 0, y_st + dy * 0))

text2 = font1.render("Welcome to the United States 1", True, BLUE, GREEN)  # 英文,相同背景色
surface.blit(text2, (x_st + dx * 0, y_st + dy * 1))
screen.blit(surface, (0, 0))

ft = pygame.font.SysFont("Malgun Gothic", font_size)  # sugar有此字型 但kilo無

wd1 = ft.render("Welcome to the United States 2", False, CYAN)
screen.blit(wd1, (x_st + dx * 0, y_st + dy * 2))

wd2 = ft.render("黃河之水天上來", True, GREEN, YELLOW)
screen.blit(wd2, (x_st + dx * 0, y_st + dy * 3))

ft = pygame.font.SysFont("Malgun Gothic", font_size)  # sugar有此字型 但kilo無
wd1 = ft.render("萬象更新", False, GREEN)
screen.blit(wd1, (x_st + dx * 0, y_st + dy * 4))

wd2 = ft.render("Welcome to the United States 3", True, RED)
screen.blit(wd2, (x_st + dx * 0, y_st + dy * 5))

ft = pygame.font.SysFont("Malgun Gothic", font_size)  # sugar有此字型 但kilo無
# ft = pygame.font.SysFont("Arial", font_size)#fail
wd1 = ft.render("Welcome to the United States 4", False, BLUE, CYAN)
screen.blit(wd1, (x_st + dx * 0, y_st + dy * 6))

wd2 = ft.render("百科全書", True, RED, CYAN)
screen.blit(wd2, (x_st + dx * 0, y_st + dy * 7))

wd1 = ft.render("Welcome to the United States 5", False, BLUE, CYAN)
screen.blit(wd1, (x_st + dx * 0, y_st + dy * 8))

wd2 = ft.render("世界大同", True, RED, CYAN)
screen.blit(wd2, (x_st + dx * 0, y_st + dy * 9))

wd1 = ft.render("Welcome to the United States 6", False, BLUE, CYAN)
screen.blit(wd1, (x_st + dx * 0, y_st + dy * 10))

wd2 = ft.render("追劇", True, RED, CYAN)
screen.blit(wd2, (x_st + dx * 0, y_st + dy * 11))

run_pygame()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 15 畫圖綜合 背景漸層色"
screen = init_pygame(pygame_name, YELLOW)

width = 800
height = 800

color = pygame.color.Color("#F54455")

row = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False
    increment = 255 / 100
    while row <= height:
        pygame.draw.rect(screen, color, (0, row, width, row + increment))
        pygame.display.flip()  # 更新畫面
        if color[2] + increment < 255:
            color[2] = color[2] + int(increment)
        row += increment

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# pygame 存圖命令
# pygame.image.save(screen, "tmp_save_pic.png")
# pygame.image.save(screen, "circle" + str(fileNo) + ".png")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# 基本架構

pygame.init()  # 啟動Pygame

screen = pygame.display.set_mode((640, 320))  # 建立繪圖視窗
pygame.display.set_caption("基本架構")  # 繪圖視窗標題

background = pygame.Surface(screen.get_size())  # 建立畫布
background = background.convert()
background.fill(WHITE)  # 畫布為白色
screen.blit(background, (0, 0))  # 在繪圖視窗繪製畫布

pygame.display.update()  # 更新繪圖視窗
running = True
while running:  # 無窮迴圈
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 使用者按關閉鈕
            running = False

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("基本繪圖")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)

pygame.draw.circle(background, BLACK, (150, 150), 130, 4)
pygame.draw.circle(background, BLUE, (100, 120), 25, 0)
pygame.draw.circle(background, BLUE, (200, 120), 25, 0)
pygame.draw.ellipse(background, MAGENTA, [135, 130, 30, 80], 0)
pygame.draw.arc(background, RED, [80, 130, 150, 120], 3.4, 6.1, 9)
screen.blit(background, (0, 0))

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame.init()

screen = pygame.display.set_mode((640, 320))
pygame.display.set_caption("動畫基本架構")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)

clock = pygame.time.Clock()  # 建立時間元件

running = True
while running:
    clock.tick(30)  # 依fps的值來產生動畫, 每秒執行fps次
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))  # 清除繪圖視窗

    pygame.display.update()  # 更新繪圖視窗

pygame.quit()  # 關閉繪圖視窗


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
# https://gamedevacademy.org/pygame-time-clock-tutorial-complete-guide/
#Tracking Frames Per Second (FPS)

pygame.init()

clock = pygame.time.Clock()  # 建立時間元件
cnt = 0
while True:
    clock.tick(60)  # 依fps的值來產生動畫, 每秒執行fps次
    cnt += 1
    if cnt % 60 == 0:
        print('a')
    if cnt > 1000:
        break


print("程式執行完畢！")
"""

print("pygame 讀取 鍵盤輸入")

pygame.init()

windowSize = [400, 300]
pygame.display.set_mode(windowSize)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_1]:
        print("你按了鍵盤 1")

    if keys[pygame.K_2]:
        print("你按了鍵盤 2")

    if keys[pygame.K_3]:
        print("你按了鍵盤 3")

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
