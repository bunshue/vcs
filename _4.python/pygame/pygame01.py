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
pygame.display.set_caption()	設定視窗名稱
pygame.display.flip()		更新畫面 將Surface全部更新後並顯示於畫面上
pygame.display.update()		更新繪圖視窗, 依據軟體做部分畫面的更新

screen : 整個視窗
surface : 一個物件, 畫布
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
GRAY = (242, 242, 242)  # R G B 較淡
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

# colors
RED2 = pygame.color.Color("#FF8080")
BLUE2 = pygame.color.Color("#8080FF")

filename = "D:/_git/vcs/_4.python/_data/picture1.jpg"
font_filename = "C:/Windows/Fonts/mingliu.ttc"  # 新細明體


def randColor():
    # 獲得隨機顏色
    r = random.randint(0, 255)  # 含頭尾
    g = random.randint(0, 255)  # 含頭尾
    b = random.randint(0, 255)  # 含頭尾
    return (r, g, b)


def init_pygame(name, color, width=W, height=H):
    print(name)
    pygame.init()  # 初始化Pygame

    screen = pygame.display.set_mode((width, height))  # 產生視窗screen
    # screen = pygame.display.set_mode(screen_size, 0, 32)  # 產生視窗screen
    # screen = pygame.display.set_mode(screen_size, 0)  # 產生視窗screen

    pygame.display.set_caption(name)  # 設定視窗名稱

    # print("取得screen參數 :", screen.get_size())

    # 利用screen物件來作為畫布，以fill()方法填上顏色
    screen.fill(color)  # 設定視窗背景色
    return screen


def run_pygame():
    # 更新屏幕, 保持屏幕打開, 直到用戶退出, 偵測視窗是否被關閉(8)
    pygame.display.update()  # 更新繪圖視窗
    running = True
    while running:
        # 從消息隊列中獲取事件並對事件進行處理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
                running = False
    pygame.quit()  # 關閉繪圖視窗


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 01 基本架構1, 靜圖, 無fps"
screen = init_pygame(pygame_name, YELLOW)

surface = pygame.Surface((700, 500))  # 建立畫布
surface = surface.convert()
surface.fill(CYAN)  # 設定畫布顏色  # 設定surface背景色
screen.blit(surface, (50, 50))  # blit, 將畫布surface blit到視窗screen裏, 位置

# 畫漸層色
color = pygame.color.Color("#FF0000")
row = 0
while row <= 250:
    pygame.draw.rect(screen, color, (0, row, W // 2, row + 1))
    pygame.display.flip()  # 更新畫面
    if color[2] + 1 < 255:
        color[2] = color[2] + 1  # 改變G通道
    row += 1

pygame.display.update()  # 更新繪圖視窗
run_pygame()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 01 基本架構2, 有fps"
screen = init_pygame(pygame_name, YELLOW)

# 設定每秒幀數fps幀，利用Clock()方法來確保動畫能持續進行
fps = 30  # 每秒的執行次數
clock = pygame.time.Clock()  # 建立時間元件

w, h = 80, 60

running = True
while running:
    # 從消息隊列中獲取事件並對事件進行處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False

    x = random.randint(0, W)  # 含頭尾
    y = random.randint(0, H)  # 含頭尾
    color = randColor()

    pygame.draw.rect(screen, color, (x, y, w, h), 2)
    pygame.draw.ellipse(screen, color, (x, y, w, h))
    pygame.display.flip()  # 更新畫面

    clock.tick(fps)  # 依fps的值來產生動畫, 每秒執行fps次

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 02 偵測滑鼠座標 鍵盤 AS123UDLR"
screen = init_pygame(pygame_name, YELLOW)

# 設定每秒幀數fps幀，利用Clock()方法來確保動畫能持續進行
fps = 30  # 每秒的執行次數
clock = pygame.time.Clock()  # 建立時間元件

running = True
while running:
    # screen.fill(YELLOW)  # 設定視窗背景色

    # 從消息隊列中獲取事件並對事件進行處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()  # 取得滑鼠座標
            # print("滑鼠", pos, end=" ")
            pygame.draw.circle(screen, RED, pos, 15)  # 實心圓

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        print("A", end=" ")
    if keys[pygame.K_s]:
        print("S", end=" ")
    if keys[pygame.K_1]:
        print("1", end=" ")
    if keys[pygame.K_2]:
        print("2", end=" ")
    if keys[pygame.K_3]:
        print("3", end=" ")

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            print("L", end=" ")
        elif event.key == pygame.K_RIGHT:
            print("R", end=" ")
        elif event.key == pygame.K_UP:
            print("U", end=" ")
        elif event.key == pygame.K_DOWN:
            print("D", end=" ")

    # 放掉鍵盤按鍵，回到原點
    # if event.type == pygame.KEYUP:
    # print('放開按鍵')

    pygame.display.flip()  # 更新畫面
    clock.tick(fps)  # 依fps的值來產生動畫, 每秒執行fps次

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 03 Animation 實現動畫效果"
screen = init_pygame(pygame_name, YELLOW)

# 設定每秒幀數fps幀，利用Clock()方法來確保動畫能持續進行
fps = 30  # 每秒的執行次數
clock = pygame.time.Clock()  # 建立時間元件

filename = "D:/_git/vcs/_1.data/______test_files1/__pic/_anime/_貓咪/cat3.png"
image = pygame.image.load(filename).convert()

pos_X, pos_Y = 50, 50  # 起始位置

running = True
while running:
    # 從消息隊列中獲取事件並對事件進行處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False

    # 清除畫面，並重畫
    screen.fill(YELLOW)  # 設定視窗背景色

    pos_X += 1
    pos_Y += 1
    if pos_X > 600 or pos_Y > 400:
        pos_X, pos_Y = 50, 50
    # screen.blit(image, (pos_X, pos_Y))  # blit, 將影像image blit到視窗screen裏, 位置
    pygame.draw.circle(screen, RED, (pos_X, pos_Y), 30, 0)  # 實心圓, 線寬0
    pygame.display.flip()  # 更新畫面

    pygame.display.update()  # 更新繪圖視窗
    clock.tick(fps)  # 依fps的值來產生動畫, 每秒執行fps次

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 03 水平移動"
screen = init_pygame(pygame_name, YELLOW)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)
ball = pygame.Surface((30, 30))  # 建立球矩形繪圖區
ball.fill(WHITE)  # 矩形區塊背景為白色
pygame.draw.circle(ball, BLUE, (15, 15), 15, 0)  # 畫藍色球
rect1 = ball.get_rect()  # 取得球矩形區塊
rect1.center = (320, H // 2)  # 球起始位置
x, y = rect1.topleft  # 球左上角坐標
dx = 3  # 球運動速度

# 設定每秒幀數fps幀，利用Clock()方法來確保動畫能持續進行
fps = 20  # 每秒的執行次數
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(30)  # 每秒執行30次
    # 從消息隊列中獲取事件並對事件進行處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False
    screen.blit(background, (0, 0))  # 清除繪圖視窗
    x += dx  # 改變水平位置
    rect1.center = (x, y)
    if rect1.left <= 0 or rect1.right >= screen.get_width():  # 到達左右邊界
        dx *= -1
    screen.blit(ball, rect1.topleft)
    pygame.display.update()  # 更新繪圖視窗

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 03 自由移動"
screen = init_pygame(pygame_name, YELLOW)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)

ball = pygame.Surface((30, 30))  # 建立球矩形繪圖區
ball.fill(WHITE)  # 矩形區塊背景為白色
pygame.draw.circle(ball, BLUE, (15, 15), 15, 0)  # 畫藍色球
rect1 = ball.get_rect()  # 取得球矩形區塊
rect1.center = (random.randint(100, 250), random.randint(150, 250))  # 球起始位置
x, y = rect1.topleft  # 球左上角坐標
direction = random.randint(20, 70)  # 起始角度
radian = math.radians(direction)  # 轉為弳度
dx = 5 * math.cos(radian)  # 球水平運動速度
dy = -5 * math.sin(radian)  # 球垂直運動速度

# 設定每秒幀數fps幀，利用Clock()方法來確保動畫能持續進行
fps = 20  # 每秒的執行次數
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(30)
    # 從消息隊列中獲取事件並對事件進行處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False
    screen.blit(background, (0, 0))  # 清除繪圖視窗
    x += dx  # 改變水平位置
    y += dy  # 改變垂直位置
    rect1.center = (x, y)
    if rect1.left <= 0 or rect1.right >= screen.get_width():  # 到達左右邊界
        dx *= -1  # 水平速度變號
    elif rect1.top <= 5 or rect1.bottom >= screen.get_height() - 5:  # 到達上下邊界
        dy *= -1  # 垂直速度變號
    screen.blit(ball, rect1.topleft)
    pygame.display.update()  # 更新繪圖視窗

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立screen, 整個視窗")

pygame_name = "pygame 04 建立畫布 + 載入圖片"
screen = init_pygame(pygame_name, YELLOW)

print("讀取圖片到記憶體")
# 方法load()載入圖片，convert()能提高圖片的處理速度
filename = "D:/_git/vcs/_4.python/_data/picture1.jpg"
image = pygame.image.load(filename)
image.convert()

print("建立物件surface")
# 產生Surface物件, 上色，繪製成形
surface = pygame.Surface((305 + 40, 400 + 40))  # 建立畫布
# print(surface.get_width(), surface.get_height())#取得surface參數
surface = surface.convert()  # 產生副本
surface.fill(GREEN)  # surface填滿指定色  # 設定surface背景色

print("將圖片blit到物件surface裏")
x_st, y_st = 20, 20
surface.blit(image, (x_st, y_st))  # blit, 將影像image blit到視窗screen裏, 位置

print("將物件surface貼到screen上")
screen.blit(surface, (25, 25))  # blit, 將畫布surface blit到視窗screen裏, 位置

print("建立物件surface2")
# 產生Surface2物件, 上色，繪製成形
surface2 = pygame.Surface((305 + 40, 400 + 40))  # 建立畫布
# print(surface2.get_width(), surface2.get_height())#取得surface2參數
surface2 = surface2.convert()  # 產生副本
surface2.fill(BLUE)  # surface2填滿指定色  # 設定surface背景色
print("將surface2貼到screen上")
screen.blit(surface2, (450, 25))  # blit, 將畫布surface blit到視窗screen裏, 位置

# 直接貼上圖片
x_st, y_st = 320, 180
screen.blit(image, (x_st, y_st))  # blit, 將影像image blit到視窗screen裏, 位置

# 改變圖片大小, 再貼上圖片
image = pygame.transform.scale(image, (300 * 3 // 4, 400 * 3 // 4))
x_st, y_st = 550, 20
screen.blit(image, (x_st, y_st))  # blit, 將影像image blit到視窗screen裏, 位置

run_pygame()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 05 滑鼠事件"
screen = init_pygame(pygame_name, YELLOW)

# 載入圖片
filename = "D:/_git/vcs/_1.data/______test_files1/__pic/_anime/_貓咪/cat3.png"
imageRect = pygame.image.load(filename).convert_alpha()

imageX, imageY = 0, 0  # 起始位置

running = True
while running:
    # 從消息隊列中獲取事件並對事件進行處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False

    screen.fill(YELLOW)  # 設定視窗背景色

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

    screen.blit(imageRect, (imageX, imageY))  # blit, 將影像imageRect blit到視窗screen裏, 位置
    pygame.display.update()  # 更新繪圖視窗

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 06 explosions 滑鼠控制"
screen = init_pygame(pygame_name, YELLOW)

# 設定每秒幀數fps幀，利用Clock()方法來確保動畫能持續進行
fps = 60  # 每秒的執行次數
clock = pygame.time.Clock()  # 建立時間元件

count = 0
click = False
limit = 30
pos = (0, 0)

running = True
while running:
    # screen.fill(BLACK)  # 設定視窗背景色

    if click and count < limit:
        pygame.draw.circle(screen, color, pos, count)
        count += 1
        if count >= limit:
            click = False

    # 從消息隊列中獲取事件並對事件進行處理
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()  # 取得滑鼠座標
            click = True
            count = 0
            color = randColor()
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False
    pygame.display.flip()  # 更新畫面
    clock.tick(fps)  # 依fps的值來產生動畫, 每秒執行fps次

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 07 偵測滑鼠位置"
screen = init_pygame(pygame_name, YELLOW)

# 設定每秒幀數fps幀，利用Clock()方法來確保動畫能持續進行
fps = 20  # 每秒的執行次數
clock = pygame.time.Clock()  # 建立時間元件

pos_list = []

pygame.display.update()  # 更新繪圖視窗

# 保持屏幕打開，直到用戶退出
# 偵測視窗是否被關閉

running = True
while running:
    # screen.fill(YELLOW)  # 設定視窗背景色

    # 從消息隊列中獲取事件並對事件進行處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:  # 滑鼠事件
            pos = pygame.mouse.get_pos()  # 取得滑鼠座標
            # print(pos)
            pos_list.append(pos)
            if len(pos_list) > 1:
                # pygame.draw.lines(screen, RED, False, pos_list)
                pygame.draw.lines(screen, RED, True, pos_list)

    pygame.display.flip()  # 更新畫面
    clock.tick(60)  # 依fps的值來產生動畫, 每秒執行fps次

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 08"
screen = init_pygame(pygame_name, YELLOW)

# 設定每秒幀數fps幀，利用Clock()方法來確保動畫能持續進行
fps = 20  # 每秒的執行次數
clock = pygame.time.Clock()  # 建立時間元件

pos_list = []

running = True
while running:
    # screen.fill(YELLOW)  # 設定視窗背景色

    # 從消息隊列中獲取事件並對事件進行處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False

    pos = pygame.mouse.get_pos()  # 取得滑鼠座標
    if pos[0] != 0 and pos[1] != 0:
        pos_list.append(pos)
    if len(pos_list) >= 20:
        del pos_list[0]

    if len(pos_list) > 2:
        pygame.draw.aalines(screen, RED, False, pos_list)

    pygame.display.flip()  # 更新畫面
    clock.tick(60)  # 依fps的值來產生動畫, 每秒執行fps次

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("畫圖畫字")
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 09 畫圖綜合 直接畫在screen上"
screen = init_pygame(pygame_name, YELLOW, 1000, 800)

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
pygame.draw.rect(screen, GREEN, (x_st, y_st, w, h))  # 實心矩形
pygame.draw.rect(screen, RED, (x_st, y_st, w, h), 5)  # 空心矩形, 設定線寬

y_st = y_st + 60
pygame.draw.rect(screen, BLUE, (x_st, y_st, w, h))  # 實心矩形

# 繪製綠框、內塗紅色矩形
pygame.draw.rect(screen, GREEN, (150, 235, 120, 120))  # 實心矩形
pygame.draw.rect(screen, RED, (140, 225, 140, 140), 10)  # 空心矩形, 設定線寬

# 圓
cx, cy = 400, 300
pygame.draw.circle(screen, RED, (cx, cy), 100, 10)  # 空心圓, 設定線寬
pygame.draw.circle(screen, GREEN, (cx, cy), 60)  # 實心圓
pygame.draw.circle(screen, BLUE, (cx, cy), 30, 0)  # 實心圓, 線寬0

# 繪製圓形
cx, cy = 650, 300
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
pygame.draw.ellipse(screen, MAGENTA, (x_st, y_st, w, h), 5)  # 空心矩形, 設定線寬
pygame.draw.rect(screen, CYAN, (x_st, y_st, w, h), 2)  # 空心矩形, 設定線寬

x_st, y_st, w, h = 150, 450, 200, 100
pygame.draw.ellipse(screen, YELLOW, [x_st, y_st, w, h])

# 繪製弧線
x_st, y_st = 400, 400
pygame.draw.arc(screen, CYAN, (x_st + 15, y_st + 10, 225, 180), 0, 1.6, 8)
pygame.draw.arc(screen, RED, (x_st + 20, y_st + 17, 212, 173), 0, 3.1, 8)
pygame.draw.arc(screen, MAGENTA, (x_st + 28, y_st + 27, 195, 157), 0, 4.7, 8)
pygame.draw.arc(screen, GREEN, (x_st + 38, y_st + 37, 173, 137), 0, 9.9, 8)
pygame.draw.arc(screen, CYAN, (x_st + 150, y_st, 200, 185), 4.3, 2.0, 8)

x_st, y_st, w, h = 260, 400, 150, 120
pygame.draw.arc(screen, RED, (x_st, y_st, w, h), 3.4, 6.1, 9)
pygame.draw.rect(screen, MAGENTA, (x_st, y_st, w, h), 2)  # 空心矩形, 設定線寬

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

x_st, y_st = 0, 400
lines = list()
for th in range(0, 361):
    y = 100 - 100 * math.sin(th * math.pi / 180)
    lines.append((x_st + th, y_st + y))
pygame.draw.lines(screen, BLUE, False, lines, 5)

print("------------------------------")  # 30個
print("繪製文字1, 直接blit到screen裏")

x_st, y_st = 20, 580
dx, dy = 400, 40
font_size = 30

ft = pygame.font.SysFont("Malgun Gothic", font_size)  # sugar有此字型 但kilo無
# ft = pygame.font.SysFont("Arial", font_size)#fail

wd = ft.render("Welcome to the United States", False, RED)
screen.blit(wd, (x_st + dx * 0, y_st + dy * 0))  # blit, 將wd blit到視窗screen裏, 位置

wd = ft.render("Welcome to the United States", True, RED)
screen.blit(wd, (x_st + dx * 0, y_st + dy * 1))  # blit, 將wd blit到視窗screen裏, 位置

wd = ft.render("Welcome to the United States", False, RED, GREEN)  # 背景綠色
screen.blit(wd, (x_st + dx * 0, y_st + dy * 2))  # blit, 將wd blit到視窗screen裏, 位置

wd = ft.render("黃河之水天上來", False, RED)
screen.blit(wd, (x_st + dx * 0, y_st + dy * 3))  # blit, 將wd blit到視窗screen裏, 位置

wd = ft.render("黃河之水天上來", True, RED, GREEN)  # 背景綠色
screen.blit(wd, (x_st + dx * 0, y_st + dy * 4))  # blit, 將wd blit到視窗screen裏, 位置

print("------------------------------")  # 30個
print("繪製文字2, 先畫在畫布surface上, 再blit到screen裏")

x_st, y_st = 20, 20
dx, dy = 400, 40
font_size = 30

# 產生Surface物件, 上色，繪製成形
surface = pygame.Surface((500, 100))  # 建立畫布
surface = surface.convert()  # 產生副本
surface.fill(WHITE)  # surface填滿指定色  # 設定surface背景色

font1 = pygame.font.Font(font_filename, font_size)

text1 = font1.render("黃河之水天上來", True, RED, WHITE)  # 中文,不同背景色
surface.blit(text1, (x_st + dx * 0, y_st + dy * 0))  # blit, 將text1 blit到畫布surface裏, 位置

text2 = font1.render("Welcome to the United States", True, BLUE, GREEN)  # 英文,相同背景色
surface.blit(text2, (x_st + dx * 0, y_st + dy * 1))  # blit, 將text2 blit到畫布surface裏, 位置

screen.blit(surface, (450, 660))  # blit, 將畫布surface blit到視窗screen裏, 位置

print("------------------------------")  # 30個

pygame.display.flip()  # 更新畫面
run_pygame()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 碰撞檢測
# 通常一個遊戲中會有很多對象出現，而這些對象之間的“碰撞”在所難免，
# 比如炮彈擊中了飛機、箱子撞到了地面等。
# 碰撞檢測在絕大多數的遊戲中都是一個必須得處理的至關重要的問題，
# pygame的sprite（動畫精靈）模塊就提供了對碰撞檢測的支持，
# 這裡我們暫時不介紹sprite模塊提供的功能，
# 因為要檢測兩個小球有沒有碰撞其實非常簡單，只需要檢查球心的距離有沒有小於兩個球的半徑之和。
# 為了製造出更多的小球，我們可以通過對鼠標事件的處理，
# 在點擊鼠標的位置創建顏色、大小和移動速度都隨機的小球，
# 當然要做到這一點，我們可以把之前學習到的面向對象的知識應用起來。


class Ball(object):
    # 球

    def __init__(self, x, y, radius, sx, sy, color=RED):
        # 初始化方法
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        # 移動
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        # 吃其他球
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = math.sqrt(dx**2 + dy**2)
            if distance < self.radius + other.radius and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        # 在窗口上繪製球
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)


# 事件處理

# 可以在事件循環中對鼠標事件進行處理，
# 通過事件對象的type屬性可以判定事件類型，
# 再通過pos屬性就可以獲得鼠標點擊的位置。
# 如果要處理鍵盤事件也是在這個地方，做法與處理鼠標事件類似。

pygame_name = "pygame 10 大球吃小球"
screen = init_pygame(pygame_name, YELLOW)

# 定義用來裝所有球的容器
balls = []

running = True
while running:
    # 從消息隊列中獲取事件並對事件進行處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False
        # 處理鼠標事件的代碼
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # print('滑鼠左鍵 :', event.pos)
            # 獲得點擊鼠標的位置
            x, y = event.pos
            radius = random.randint(10, 100)
            sx, sy = random.randint(-10, 10), random.randint(-10, 10)
            color = randColor()
            # 在點擊鼠標的位置創建一個球(大小、速度和顏色隨機)
            ball = Ball(x, y, radius, sx, sy, color)
            # 將球添加到列表容器中
            balls.append(ball)
            # print('滑鼠左鍵 :', event.pos)
            print("建立球 :", x, y, radius, sx, sy, color)
    screen.fill(YELLOW)  # 設定視窗背景色
    # 取出容器中的球 如果沒被吃掉就繪製 被吃掉了就移除
    for ball in balls:
        if ball.alive:
            ball.draw(screen)
        else:
            balls.remove(ball)
    pygame.display.flip()  # 更新畫面
    pygame.time.delay(50)  # delay 50毫秒  # 每隔50毫秒就改變球的位置再刷新窗口

    for ball in balls:
        ball.move(screen)
        # 檢查球有沒有吃到其他的球
        for other in balls:
            ball.eat(other)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 11 偵測鍵盤ASDW"
screen = init_pygame(pygame_name, YELLOW)

size = [400, 300]

# 設定每秒幀數fps幀，利用Clock()方法來確保動畫能持續進行
fps = 20  # 每秒的執行次數
clock = pygame.time.Clock()  # 建立時間元件

# player position
x = size[0] / 2
y = size[1] / 2

# ball position
ballX = random.randrange(0, size[0])
ballY = random.randrange(0, size[1])

# Goal position
goalX = size[0] / 2 - 10
goalY = size[1] / 2 - 10
goalW = 20
goalH = 20

# points
points = 0


def checkOffScreenX(x):
    if x > size[0]:
        x = 0
    elif x < 0:
        x = size[0]
    return x


def checkOffScreenY(y):
    if y > size[1]:
        y = 0
    elif y < 0:
        y = size[1]
    return y


def checkTouching():
    # Causes a mini explosion if the players are touching
    global x
    global ballX
    global y
    global ballY

    # Check player and ball are touching
    if -10 < y - ballY < 10 and -10 < x - ballX < 10:
        # draw an explosion
        pygame.draw.circle(screen, WHITE, [x, y], 15)

        xDiff = x - ballX
        yDiff = y - ballY

        # check ball on edge of screen
        if ballX == 0:
            xDiff -= 5
        elif ballX == size[0]:
            xDiff += 5
        if ballY == 0:
            yDiff -= 5
        elif ballY == size[1]:
            yDiff += 5

        # move the ball and player
        x += xDiff * 3
        ballX -= xDiff * 3

        y += yDiff * 3
        ballY -= yDiff * 3


# Game loop
done = False

# get current time
timeStart = pygame.time.get_ticks()

while not done:
    screen.fill(YELLOW)  # 設定視窗背景色

    # Draw the goal
    pygame.draw.rect(screen, GREEN, (goalX, goalY, goalW, goalH))

    keys = pygame.key.get_pressed()

    # player movement
    if keys[pygame.K_w]:
        y -= 1
    if keys[pygame.K_s]:
        y += 1
    if keys[pygame.K_a]:
        x -= 1
    if keys[pygame.K_d]:
        x += 1

    # Check off screen
    x = checkOffScreenX(x)
    y = checkOffScreenY(y)
    ballX = checkOffScreenX(ballX)
    ballY = checkOffScreenY(ballY)

    # Check player is touching the ball
    checkTouching()

    # Draw points
    for point in range(points):
        pointX = 0 + point * 5
        pygame.draw.rect(screen, WHITE, (pointX, 3, 4, 7))

    # draw player
    pygame.draw.circle(screen, RED2, [x, y], 6)

    # draw ball
    pygame.draw.circle(screen, BLUE2, [ballX, ballY], 6)

    # Check ball is in goal
    if goalX <= ballX <= goalX + goalH and goalY <= ballY <= goalY + goalH:
        points += 1
        ballX = random.randrange(0, size[0])
        ballY = random.randrange(0, size[0])

    pygame.display.flip()  # 更新畫面

    # 從消息隊列中獲取事件並對事件進行處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            done = True

    # 量測時間
    timeNow = pygame.time.get_ticks()
    if timeNow - timeStart >= 60000:
        done = True

    clock.tick(72)  # 依fps的值來產生動畫, 每秒執行fps次

pygame.quit()  # 關閉繪圖視窗

print("Total points: " + str(points))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 12 鍵盤事件"
screen = init_pygame(pygame_name, YELLOW)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)
ball = pygame.Surface((30, 30))  # 建立球矩形繪圖區
ball.fill(WHITE)  # 矩形區塊背景為白色
pygame.draw.circle(ball, BLUE, (15, 15), 15, 0)  # 畫藍色球
rect1 = ball.get_rect()  # 取得球矩形區塊
rect1.center = (320, H // 2)  # 球起始位置
x, y = rect1.topleft  # 球左上角坐標
dx = 5  # 球移動距離

# 設定每秒幀數fps幀，利用Clock()方法來確保動畫能持續進行
fps = 20  # 每秒的執行次數
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(30)  # 每秒執行30次
    # 從消息隊列中獲取事件並對事件進行處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False
    keys = pygame.key.get_pressed()  # 檢查按鍵被按
    if keys[pygame.K_RIGHT] and rect1.right < screen.get_width():  # 按向右鍵且未達右邊界
        rect1.centerx += dx  # 向右移動
    elif keys[pygame.K_LEFT] and rect1.left > 0:  # 按向左鍵且未達左邊界
        rect1.centerx -= dx  # 向左移動
    screen.blit(background, (0, 0))  # 清除繪圖視窗
    screen.blit(ball, rect1.topleft)
    pygame.display.update()  # 更新繪圖視窗

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# coinGameStart


def moveAnimation(image1, image2, count):
    if 10 < count % 20 <= 20:
        return image2
    else:
        return image1


def upClear(x, y):
    canMove = True

    if verticalDoorLeft <= x <= verticalDoorRight and y - 1 < topWall:
        canMove = True
    elif y - 1 < topWall:
        canMove = False
    elif (x < leftWall or x > rightWall) and y - 1 < middleDoorsTop:
        canMove = False

    if canMove:
        return 1
    else:
        return 0


def downClear(x, y):
    canMove = True

    if verticalDoorLeft <= x <= verticalDoorRight and bottomWall < y + 1:
        canMove = True
    elif bottomWall < y + 1:
        canMove = False
    elif (x < leftWall or x > rightWall) and y + 1 > middleDoorsBottom:
        canMove = False

    if canMove:
        return 1
    else:
        return 0


def leftClear(x, y):
    canMove = True

    if middleDoorsTop <= y <= middleDoorsBottom and x - 1 < leftWall:
        canMove = True
    elif x - 1 < leftWall:
        canMove = False
    elif (y > bottomWall or y < topWall) and x - 1 < verticalDoorLeft:
        canMove = False

    if canMove:
        return 1
    else:
        return 0


def rightClear(x, y):
    canMove = True

    if middleDoorsTop <= y <= middleDoorsBottom and x + 1 > rightWall:
        canMove = True
    elif x + 1 > rightWall:
        canMove = False
    elif (y > bottomWall or y < topWall) and x + 1 > verticalDoorRight:
        canMove = False

    if canMove:
        return 1
    else:
        return 0


def checkOffscreen(x, y):
    if x < -14:
        x = windowSize[0] - 14
    elif x > windowSize[0] - 14:
        x = -14

    if y < -20:
        y = windowSize[1] - 20
    elif y > windowSize[1] - 20:
        y = -20
    return x, y


def playersTouching():
    global pOneX, pOneY, pTwoX, pTwoY

    if -32 < pOneX - pTwoX < 32 and -40 < pOneY - pTwoY < 40:
        xDiff = pOneX - pTwoX
        yDiff = pOneY - pTwoY

        for dist in range(abs(xDiff) / 2):
            pOneMove = leftClear(pOneX, pOneY) + rightClear(pOneX, pOneY)
            pTwoMove = leftClear(pTwoX, pTwoY) + rightClear(pTwoX, pTwoY)
            if xDiff > 0:
                pOneX += pOneMove / 2 * xDiff / xDiff
                pTwoX -= pTwoMove / 2 * xDiff / xDiff
            else:
                pOneX -= pOneMove / 2 * xDiff / xDiff
                pTwoX += pTwoMove / 2 * xDiff / xDiff

        for dist in range(abs(yDiff) / 2):
            pOneMove = upClear(pOneX, pOneY) + downClear(pOneX, pOneY)
            pTwoMove = upClear(pTwoX, pTwoY) + downClear(pTwoX, pTwoY)
            if yDiff > 0:
                pOneY += pOneMove / 2 * yDiff / yDiff
                pTwoY -= pTwoMove / 2 * yDiff / yDiff
            else:
                pOneY -= pOneMove / 2 * yDiff / yDiff
                pTwoY += pTwoMove / 2 * yDiff / yDiff


def touchingCoin(x, y):
    return -32 < x - coinPos[0] < 20 and -40 < y - coinPos[1] < 20


def randomPosition():
    # return x and y
    x = random.randrange(32, windowSize[0] - 52)
    y = random.randrange(32, windowSize[1] - 52)
    return x, y


pygame_name = "pygame 13 coinGameStart"
width, height = 640, 384
screen = init_pygame(pygame_name, YELLOW, width, height)

windowSize = [width, height]

# 設定每秒幀數fps幀，利用Clock()方法來確保動畫能持續進行
fps = 20  # 每秒的執行次數
clock = pygame.time.Clock()

# Font for points
pointFont = pygame.font.SysFont("Monospace", 15)

# Variables for position etc.
pOneX = windowSize[0] / 4
pOneY = windowSize[1] / 2

pTwoX = windowSize[0] / 4 * 3
pTwoY = windowSize[1] / 2

coinPos = randomPosition()

pOnePoints = 0
pTwoPoints = 0

pOneCount = 0
pTwoCount = 0

pOneMoving = False
pTwoMoving = False

# Variables for walls
leftWall = 28
topWall = 16
rightWall = windowSize[0] - 60
bottomWall = 312

middleDoorsTop = 144
middleDoorsBottom = 182
verticalDoorLeft = 284
verticalDoorRight = verticalDoorLeft + 40

# Load images
background = pygame.image.load("data/background.png")
background = pygame.transform.scale(background, windowSize)

light = pygame.image.load("data/light.png")
light = pygame.transform.scale(light, windowSize)

pOneMove1 = pygame.image.load("data/sprite1_walking1.png")
pOneMove1 = pygame.transform.scale2x(pOneMove1)

pOneMove2 = pygame.image.load("data/sprite1_walking2.png")
pOneMove2 = pygame.transform.scale2x(pOneMove2)

pOneStanding = pygame.image.load("data/sprite1_standing.png")
pOneStanding = pygame.transform.scale2x(pOneStanding)

pTwoMove1 = pygame.image.load("data/sprite2_walking1.png")
pTwoMove1 = pygame.transform.scale2x(pTwoMove1)

pTwoMove2 = pygame.image.load("data/sprite2_walking2.png")
pTwoMove2 = pygame.transform.scale2x(pTwoMove2)

pTwoStanding = pygame.image.load("data/sprite2_standing.png")
pTwoStanding = pygame.transform.scale2x(pTwoStanding)

coin = pygame.image.load("data/coin.png")
coin = pygame.transform.scale2x(coin)

# Game loop
done = False
while not done:
    # Get movement
    # Player 1 movement
    pOneMoving = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        pOneY += downClear(pOneX, pOneY)
        pOneMoving = True
    if keys[pygame.K_w]:
        pOneY -= upClear(pOneX, pOneY)
        pOneMoving = True
    if keys[pygame.K_a]:
        pOneX -= leftClear(pOneX, pOneY)
        pOneMoving = True
    if keys[pygame.K_d]:
        pOneX += rightClear(pOneX, pOneY)
        pOneMoving = True

    pOneX, pOneY = checkOffscreen(pOneX, pOneY)

    # Player 1 animation
    if pOneMoving:
        pOneCount += 1
        pOneImage = moveAnimation(pOneMove1, pOneMove2, pOneCount)
    else:
        pOneImage = pOneStanding

    # Player 2 movement
    pTwoMoving = False
    if keys[pygame.K_DOWN]:
        pTwoY += downClear(pTwoX, pTwoY)
        pTwoMoving = True
    if keys[pygame.K_UP]:
        pTwoY -= upClear(pTwoX, pTwoY)
        pTwoMoving = True
    if keys[pygame.K_LEFT]:
        pTwoX -= leftClear(pTwoX, pTwoY)
        pTwoMoving = True
    if keys[pygame.K_RIGHT]:
        pTwoX += rightClear(pTwoX, pTwoY)
        pTwoMoving = True

    pTwoX, pTwoY = checkOffscreen(pTwoX, pTwoY)

    # Player 2 animation
    if pTwoMoving:
        pTwoCount += 1
        pTwoImage = moveAnimation(pTwoMove1, pTwoMove2, pTwoCount)
    else:
        pTwoImage = pTwoStanding

    # Check touching
    playersTouching()

    # Check touching coin
    if touchingCoin(pOneX, pOneY):
        pOnePoints += 1

    if touchingCoin(pTwoX, pTwoY):
        pTwoPoints += 1

    # Move coin if touching
    if touchingCoin(pOneX, pOneY) or touchingCoin(pTwoX, pTwoY):
        coinPos = randomPosition()

    # Render points for display
    pOnePointLabel = pointFont.render(str(pOnePoints), 1, WHITE)
    pTwoPointLabel = pointFont.render(str(pTwoPoints), 1, WHITE)

    # Update display
    screen.blit(background, (0, 0))
    screen.blit(coin, coinPos)
    screen.blit(pOneImage, [pOneX, pOneY])
    screen.blit(pTwoImage, [pTwoX, pTwoY])
    screen.blit(pOnePointLabel, [pOneX - 9, pOneY - 9])
    screen.blit(pTwoPointLabel, [pTwoX - 9, pTwoY - 9])
    screen.blit(light, (0, 0))

    pygame.display.flip()

    # 從消息隊列中獲取事件並對事件進行處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            done = True
    clock.tick(60)

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from threading import Thread
from time import sleep


class Car(object):
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    def move(self):
        if self._x + 80 < 950:
            self._x += random.randint(1, 10)

    def draw(self, screen):
        pygame.draw.rect(screen, self._color, (self._x, self._y, 80, 40), 0)


def main():
    class BackgroundTask(Thread):
        def run(self):
            while True:
                screen.fill(GRAY)
                pygame.draw.line(screen, BLACK, (130, 0), (130, 600), 4)
                pygame.draw.line(screen, BLACK, (950, 0), (950, 600), 4)
                for car in cars:
                    car.draw(screen)
                pygame.display.flip()
                sleep(0.05)
                for car in cars:
                    car.move()

    cars = []
    for index in range(5):
        temp = Car(50, 50 + 120 * index, randColor())
        cars.append(temp)

    # pygame_name = "xxxxxx"
    # screen = init_pygame(pygame_name, YELLOW)

    pygame.init()
    screen = pygame.display.set_mode((1000, 600))

    BackgroundTask(daemon=True).start()
    running = True
    while running:
        # 從消息隊列中獲取事件並對事件進行處理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
                running = False
    pygame.quit()  # 關閉繪圖視窗


if __name__ == "__main__":
    main()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 14 滑鼠滑動事件"
screen = init_pygame(pygame_name, YELLOW)

# pygame.init()
# screen = pygame.display.set_mode((640, 300))
# pygame.display.set_caption("滑鼠滑動事件")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)
ball = pygame.Surface((30, 30))  # 建立球矩形繪圖區
ball.fill(WHITE)  # 矩形區塊背景為白色
pygame.draw.circle(ball, BLUE, (15, 15), 15, 0)  # 畫藍色球
rect1 = ball.get_rect()  # 取得球矩形區塊
rect1.center = (320, 150)  # 球起始位置
x, y = rect1.topleft  # 球左上角坐標

# 設定每秒幀數fps幀，利用Clock()方法來確保動畫能持續進行
fps = 20  # 每秒的執行次數
clock = pygame.time.Clock()

running = True
playing = False  # 開始時球不能移動
while running:
    clock.tick(30)  # 每秒執行30次
    # 從消息隊列中獲取事件並對事件進行處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False
    buttons = pygame.mouse.get_pressed()
    if buttons[0]:  # 按滑鼠左鍵後球可移動
        playing = True
    elif buttons[2]:  # 按滑鼠右鍵後球不能移動
        playing = False
    if playing == True:  # 球可移動狀態
        mouses = pygame.mouse.get_pos()  # 取得滑鼠坐標
        rect1.centerx = mouses[0]  # 移動滑鼠
        rect1.centery = mouses[1]
    screen.blit(background, (0, 0))  # 清除繪圖視窗
    screen.blit(ball, rect1.topleft)
    pygame.display.update()  # 更新繪圖視窗

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# free motion

# collide


class Ball(pygame.sprite.Sprite):
    dx = 0  # x位移量
    dy = 0  # y位移量
    x = 0  # 球x坐標
    y = 0  # 球y坐標

    def __init__(self, speed, srx, sry, radium, color):
        pygame.sprite.Sprite.__init__(self)
        self.x = srx
        self.y = sry
        self.image = pygame.Surface([radium * 2, radium * 2])  # 繪製球體
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, color, (radium, radium), radium, 0)
        self.rect = self.image.get_rect()  # 取得球體區域
        self.rect.center = (srx, sry)  # 初始位置
        direction = random.randint(20, 70)  # 移動角度
        radian = math.radians(direction)  # 角度轉為弳度
        self.dx = speed * math.cos(radian)  # 球水平運動速度
        self.dy = -speed * math.sin(radian)  # 球垂直運動速度

    def update(self):
        self.x += self.dx  # 計算球新餘標
        self.y += self.dy
        self.rect.x = self.x  # 移動球圖形
        self.rect.y = self.y
        if self.rect.left <= 0 or self.rect.right >= screen.get_width():  # 到達左右邊界
            self.dx *= -1  # 水平速度變號
        elif (
            self.rect.top <= 5 or self.rect.bottom >= screen.get_height() - 5
        ):  # 到達上下邊界
            self.dy *= -1  # 垂直速度變號

    def collidebounce(self):
        self.dx *= -1


pygame_name = "pygame 15 角色碰撞"
screen = init_pygame(pygame_name, YELLOW)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)
allsprite = pygame.sprite.Group()  # 建立角色群組
ball1 = Ball(8, 100, 100, 15, BLUE)  # 建立藍色球物件
allsprite.add(ball1)  # 加入角色群組
ball2 = Ball(6, 200, 250, 15, RED)  # 建立紅色球物件
allsprite.add(ball2)

# 設定每秒幀數fps幀，利用Clock()方法來確保動畫能持續進行
fps = 20  # 每秒的執行次數
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(30)
    # 從消息隊列中獲取事件並對事件進行處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False
    screen.blit(background, (0, 0))  # 清除繪圖視窗
    ball1.update()  # 物件更新
    ball2.update()
    allsprite.draw(screen)
    result = pygame.sprite.collide_rect(ball1, ball2)
    if result == True:
        ball1.collidebounce()
        ball2.collidebounce()
    pygame.display.update()  # 更新繪圖視窗

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

"""
pygame之畫圖
draw.line()
draw.rect()
draw.polygon()
draw.circle()
draw.ellipse()
draw.arc()

pygame.mixer.music.rewind() #重新啟動音樂
#將當前音樂的播放重新設置為一開始
 
pygame.mixer.music.stop() #停止音樂播放

pygame.mixer.music.pause() #暫時停止音樂播放
pygame.mixer.music.unpause()   #恢復暫停音樂

print('音量0.5')
pygame.mixer.music.set_volume(0.5)  #調節音樂音量
#設置音樂播放的音量。值參數在0.0和1.0之間。當加載新音樂時，音量就會重置
time.sleep(30)
print('音量1')
pygame.mixer.music.set_volume(1)
time.sleep(30)
print('音量0.3')
pygame.mixer.music.set_volume(0.3)

b=pygame.mixer.music.get_volume() #返回當前音量
#值將在0.0和1.0之間

b=pygame.mixer.music.get_busy()   #檢查音樂流是否在播放
#當音樂流在積極播放時，就會返回True。當音樂空閑時，返回False
#暫停相當于在播放，返回True

b=pygame.mixer.get_init()  #測試混音器是否初始化
#如果混音器已初始化，則返回正在使用的播放參數。如果混音器尚未初始化，則返回None
#get_init() -> (frequency, format, channels)
#(22050, -16, 2)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# pygame 存圖命令
# pygame.image.save(screen, "tmp_save_pic.png")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pygame_name = "pygame 16 動畫基本架構"
screen = init_pygame(pygame_name, YELLOW)

surface = pygame.Surface(screen.get_size())  # 建立畫布
surface = pygame.Surface((600, 400))  # 建立畫布
surface = surface.convert()
surface.fill(RED)  # 設定畫布顏色  # 設定surface背景色

# 設定每秒幀數fps幀，利用Clock()方法來確保動畫能持續進行
fps = 20  # 每秒的執行次數
clock = pygame.time.Clock()  # 建立時間元件

running = True
while running:
    clock.tick(30)  # 依fps的值來產生動畫, 每秒執行fps次
    # 從消息隊列中獲取事件並對事件進行處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False
    screen.blit(surface, (0, 0))  # blit, 將畫布surface blit到視窗screen裏, 位置

    pygame.display.update()  # 更新繪圖視窗

pygame.quit()  # 關閉繪圖視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 在窗口上渲染圖像
screen.blit(ball_image, (50, 50))  # blit, 將影像ball_image blit到視窗screen裏, 位置

# 刷新當前窗口(渲染窗口將繪製的圖像呈現出來)
pygame.display.flip()  # 更新畫面

ddddddd
ball_image = pygame.image.load("./data/ball.png")

# 設置窗口的背景色(顏色是由紅綠藍三原色構成的元組)
screen.fill(GRAY)  # 設定視窗背景色

# 繪製一個圓(參數分別是: 屏幕, 顏色, 圓心位置, 半徑, 0表示填充圓)
pygame.draw.circle(screen, RED, (x, y), 30, 0)  # 實心圓, 線寬0

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


pygame.time.delay(100)  # delay 100毫秒


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" no  file

pygame_name = "pygame 17 xxxx"
screen = init_pygame(pygame_name, YELLOW)

# 初始化 Pygame
pygame.init()

# 設置視窗大小
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# 設置遊戲標題
pygame.display.set_caption("射擊遊戲")

# 設置遊戲時鐘
# 設定每秒幀數fps幀，利用Clock()方法來確保動畫能持續進行
fps = 20  # 每秒的執行次數
clock = pygame.time.Clock()

# 加載音效 no wave file
# shoot_sound = pygame.mixer.Sound("shoot.wav")

# 加載圖像
player_image = pygame.image.load("pygame1/pic/player.png")
player_rect = player_image.get_rect()

bullet_image = pygame.image.load("pygame1/pic/bullet.png")
bullet_rect = bullet_image.get_rect()

enemy_image = pygame.image.load("pygame1/pic/enemy.png")
enemy_rect = enemy_image.get_rect()

# 設置玩家初始位置
player_rect.x = 50
player_rect.y = SCREEN_HEIGHT / 2

# 設置子彈速度
bullet_speed = 5

# 設置敵人速度
enemy_speed = 3

# 設置分數
score = 0

running = True
while running:
    # 從消息隊列中獲取事件並對事件進行處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
            running = False

        # 按下空格鍵發射子彈
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet_rect.x = player_rect.x + player_rect.width
            bullet_rect.y = (
                player_rect.y + player_rect.height / 2 - bullet_rect.height / 2
            )
            # shoot_sound.play()

        # 移動玩家
        elif event.type == pygame.MOUSEMOTION:
            player_rect.y = pygame.mouse.get_pos()[1]

    # 移動子彈
    bullet_rect.x += bullet_speed

    # 如果子彈超出螢# 幕邊界，則將子彈重置
if bullet_rect.x > SCREEN_WIDTH:
    bullet_rect.x = -bullet_rect.width

# 移動敵人
enemy_rect.x -= enemy_speed

# 如果敵人超出螢幕邊界，則將敵人重置並隨機設置y軸位置
if enemy_rect.right < 0:
    enemy_rect.x = SCREEN_WIDTH
    enemy_rect.y = random.randint(0, SCREEN_HEIGHT - enemy_rect.height)

# 檢查是否擊中敵人
if bullet_rect.colliderect(enemy_rect):
    enemy_rect.x = SCREEN_WIDTH
    enemy_rect.y = random.randint(0, SCREEN_HEIGHT - enemy_rect.height)
    bullet_rect.x = -bullet_rect.width
    score += 1

# 畫面設置
screen.fill(BLACK)  # 設定視窗背景色

# 顯示玩家、子彈、敵人及分數
screen.blit(player_image, player_rect)  # blit, 將影像player_image blit到視窗screen裏, 位置
screen.blit(bullet_image, bullet_rect)  # blit, 將影像bullet_image blit到視窗screen裏, 位置
screen.blit(enemy_image, enemy_rect)  # blit, 將影像enemy_image blit到視窗screen裏, 位置

font = pygame.font.SysFont(None, 36)
text = font.render("Score: " + str(score), True, WHITE)
screen.blit(text, (10, 10))  # blit, 將text blit到視窗screen裏, 位置

# 更新畫面
pygame.display.flip()

clock.tick(60)

pygame.quit()  # 關閉繪圖視窗

"""  #  no  file
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pygame.locals import *

FPS = 40  # 每秒更換的速率

# 將圖片切割成3*3的圖塊
Squares = 3
gridNums = Squares * Squares


def main():
    pygame_name = "pygame 18 xxxxxxx"
    screen = init_pygame(pygame_name, YELLOW)

    # 初始化並設定時間元件
    pygame.init()
    # 設定每秒幀數fps幀，利用Clock()方法來確保動畫能持續進行
    fps = 20  # 每秒的執行次數
    mainClock = pygame.time.Clock()

    # 載入圖片並以get_rect()方法取得圖片大小
    gameImage = pygame.image.load("D:/_git/vcs/_4.python/pygame/pygame1/pic/bg02.jpg")
    gameRect = gameImage.get_rect()

    # 產生視窗
    screen = pygame.display.set_mode((gameRect.width, gameRect.height))
    pygame.display.set_caption("簡易拼圖遊戲")

    # 圖塊的大小依據圖片的寬和高再除以方塊數所得 width = 640/3
    gridWidth = int(gameRect.width / Squares)
    gridHeight = int(gameRect.height / Squares)
    # 函式startGame()遊戲後取得圖塊和空白方格的狀態
    picSlice, waitMoveSqr = startGame()

    # 播放音樂
    filename = "D:/_git/vcs/_1.data/______test_files1/_wav/harumi99.wav"
    pygame.mixer.music.load(filename)
    controlMusic = False

    finish = False  # 尚未啟動遊戲

    # 偵測遊戲的鍵盤和滑鼠
    while True:
        # 從消息隊列中獲取事件並對事件進行處理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 判斷事件的常數是否為QUIT常數
                finishGame()

            # 放開鍵盤事件
            if event.type == KEYUP:
                # 按鍵盤的m鍵來播放/停止音樂
                if event.key == K_v:
                    if controlMusic:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1, 0.0)
                    controlMusic = not controlMusic  # 當作切換開關

                # 按鍵盤的Esc鍵就會離開程式
                if event.key == K_ESCAPE:
                    finishGame()
                if finish:
                    continue

            # 配合左手，按下鍵盤的W、A、S、D來產生和方向鍵向上(W)、左(A)、下(S)、右(D)相同的效果
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    waitMoveSqr = moveLeft(picSlice, waitMoveSqr)
                if event.key == K_RIGHT or event.key == K_d:
                    waitMoveSqr = moveRight(picSlice, waitMoveSqr)
                if event.key == K_UP or event.key == K_w:
                    waitMoveSqr = moveUp(picSlice, waitMoveSqr)
                if event.key == K_DOWN or event.key == K_s:
                    waitMoveSqr = moveDown(picSlice, waitMoveSqr)

            # 是否按下滑鼠的按鈕，方法mouse.get_pos()取得位置
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()  # 取得滑鼠座標

                # 取得座標值之後，進一步找出滑鼠停留在圖塊的那個位置？
                posX = int(x / gridWidth)
                posY = int(y / gridHeight)
                index = posX + posY * Squares
                if (
                    index == waitMoveSqr - 1
                    or index == waitMoveSqr + 1
                    or index == waitMoveSqr - Squares
                    or index == waitMoveSqr + Squares
                ):
                    picSlice[waitMoveSqr], picSlice[index] = (
                        picSlice[index],
                        picSlice[waitMoveSqr],
                    )
                    waitMoveSqr = index

        if isFinished(picSlice, waitMoveSqr):
            picSlice[waitMoveSqr] = gridNums - 1
            finish = True

        screen.fill(WHITE)  # 設定視窗背景色

        for k in range(gridNums):
            rowDst = int(k / Squares)
            colDst = int(k % Squares)
            rectDst = pygame.Rect(
                colDst * gridWidth, rowDst * gridHeight, gridWidth, gridHeight
            )

            if picSlice[k] == -1:
                continue

            rowArea = int(picSlice[k] / Squares)
            colArea = int(picSlice[k] % Squares)
            rectArea = pygame.Rect(
                colArea * gridWidth, rowArea * gridHeight, gridWidth, gridHeight
            )
            screen.blit(
                gameImage, rectDst, rectArea
            )  # blit, 將影像gameImage blit到視窗screen裏, 位置

        for k in range(Squares + 1):
            pygame.draw.line(
                screen, GRAY, (k * gridWidth, 0), (k * gridWidth, gameRect.height)
            )
        for k in range(Squares + 1):
            pygame.draw.line(
                screen, GRAY, (0, k * gridHeight), (gameRect.width, k * gridHeight)
            )

        pygame.display.update()  # 更新繪圖視窗
        mainClock.tick(FPS)


# 利用range()隨機產生圖片的分割
def startGame():
    board = []  # 空的List存放切割後的圖塊
    # 依切割後的圖塊數以append()方法加入board
    for k in range(gridNums):
        board.append(k)
    waitMoveSqr = gridNums - 1  # waitMoveSqr等待被移動的圖塊
    board[waitMoveSqr] = -1  # 表示List存放一個元素為-1，讓其他圖片能移動

    # 依據隨機值來決定圖片的移動方向並記錄移動圖塊和空白方格
    for k in range(100):
        direction = random.randint(0, 3)
        if direction == 0:
            waitMoveSqr = moveLeft(board, waitMoveSqr)
        elif direction == 1:
            waitMoveSqr = moveRight(board, waitMoveSqr)
        elif direction == 2:
            waitMoveSqr = moveUp(board, waitMoveSqr)
        elif direction == 3:
            waitMoveSqr = moveDown(board, waitMoveSqr)
    return board, waitMoveSqr


# 依傳入圖塊和空白格，將位於空白格左側的圖塊，移入空白格
def moveRight(board, waitMoveSqr):
    # print('1-', board, waitMoveSqr)
    if waitMoveSqr % Squares == 0:
        return waitMoveSqr
    board[waitMoveSqr - 1], board[waitMoveSqr] = (
        board[waitMoveSqr],
        board[waitMoveSqr - 1],
    )
    return waitMoveSqr - 1


# 依傳入圖塊和空白格，將位於空白格右側的圖塊，移入空白格
def moveLeft(board, waitMoveSqr):
    if waitMoveSqr % Squares == Squares - 1:
        return waitMoveSqr
    board[waitMoveSqr + 1], board[waitMoveSqr] = (
        board[waitMoveSqr],
        board[waitMoveSqr + 1],
    )
    return waitMoveSqr + 1


# 依傳入圖塊和空白格，將位於空白格上方的圖塊，移入空白格
def moveDown(board, waitMoveSqr):
    if waitMoveSqr < Squares:
        return waitMoveSqr
    board[waitMoveSqr - Squares], board[waitMoveSqr] = (
        board[waitMoveSqr],
        board[waitMoveSqr - Squares],
    )
    return waitMoveSqr - Squares


# 依傳入圖塊和空白格，將位於空白格下方的圖塊，移入空白格
def moveUp(board, waitMoveSqr):
    if waitMoveSqr >= gridNums - Squares:
        return waitMoveSqr
    board[waitMoveSqr + Squares], board[waitMoveSqr] = (
        board[waitMoveSqr],
        board[waitMoveSqr + Squares],
    )
    return waitMoveSqr + Squares


# 是否完成
def isFinished(board, waitMoveSqr):
    for item in range(gridNums - 1):
        if board[item] != item:
            return False
    return True


# 結束應用程式
def finishGame():
    pygame.quit()  # 關閉繪圖視窗
    sys.exit()


if __name__ == "__main__":
    main()  # 呼叫main()函式

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 設定使用參數
size = width, height = 500, 500
size = width, height = 560, 500
# 產生視窗，以Surface物件回傳
screen = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption("動畫")

# 設定使用參數
size = width, height = 600, 600

# 3030
print("------------------------------")  # 30個

w, h = 500, 500
x_st, y_st = (W - h) // 2, (H - h) // 2  # 左上角

pygame.draw.rect(screen, BLUE, [x_st, y_st, w, h])
# pygame.draw.rect(screen, BLUE, [x_st, y_st, w, h])
# 繪製矩形
# x_st, y_st, w, h = 20, 250, 100, 50
# pygame.draw.rect(screen, GREEN, (x_st, y_st, w, h))

# tick()方法依據fps之值讓移動圖片有動畫效果
# blit()不斷在畫布上繪製圖片
# update()進行動作的更新


# moveX, moveY = 5, -5 #設定圖片的移動速度會形成固定範圍
# 以隨機值來取得起始角度並轉為弧度
# 避免移動成固定範圍，以隨機值來取得起始角度並轉為弧度
posi = random.randint(45, 60)
angle = math.radians(posi)

# 設定圖片水平和垂直的移動速度
moveX = 5 * math.sin(angle)
moveY = -5 * math.cos(angle)

print("------------------------------")  # 30個

print("圖片屬性")
# 載入圖片，get_rect()取得矩形的移動區域
filename = "D:/_git/vcs/_1.data/______test_files1/__pic/_anime/_貓咪/cat3.png"
image = pygame.image.load(filename)

# 取得矩形的移動區域
imageRect = image.get_rect()
print("imageRect :", imageRect)
print("center :", imageRect.center)
print("topleft :", imageRect.topleft)
print("T :", imageRect.top)
print("B :", imageRect.bottom)
print("L :", imageRect.left)
print("R :", imageRect.right)
print("視窗屬性")
print("SW :", screen.get_width())
print("SH :", screen.get_height())

print("------------------------------")  # 30個

pygame.draw.ellipse(screen, RED, [x, y, width, height])


# Load music and sound
coinSound = pygame.mixer.Sound("data/coin.wav")
coinSound.play()

pygame.mixer.music.load("data/music.mp3")
pygame.mixer.music.play(-1)
