import pygame
import random

print("------------------------------------------------------------")  # 60個




"""
import pygame


def main():
    # 初始化導入的pygame中的模塊
    pygame.init()
    # 初始化用於顯示的窗口並設置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 設置當前窗口的標題
    pygame.display.set_caption('大球吃小球')
    running = True
    # 開啟一個事件循環處理髮生的事件
    while running:
        # 從消息隊列中獲取事件並對事件進行處理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()

"""


"""

import pygame


def main():
    # 初始化導入的pygame中的模塊
    pygame.init()
    # 初始化用於顯示的窗口並設置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 設置當前窗口的標題
    pygame.display.set_caption('大球吃小球')
    # 設置窗口的背景色(顏色是由紅綠藍三原色構成的元組)
    screen.fill((242, 242, 242))
    # 繪製一個圓(參數分別是: 屏幕, 顏色, 圓心位置, 半徑, 0表示填充圓)
    pygame.draw.circle(screen, (255, 0, 0,), (100, 100), 30, 0)
    # 刷新當前窗口(渲染窗口將繪製的圖像呈現出來)
    pygame.display.flip()
    running = True
    # 開啟一個事件循環處理髮生的事件
    while running:
        # 從消息隊列中獲取事件並對事件進行處理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()

"""

"""
#加載圖像

import pygame


def main():
    # 初始化導入的pygame中的模塊
    pygame.init()
    # 初始化用於顯示的窗口並設置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 設置當前窗口的標題
    pygame.display.set_caption('大球吃小球')
    # 設置窗口的背景色(顏色是由紅綠藍三原色構成的元組)
    screen.fill((255, 255, 255))
    # 通過指定的文件名加載圖像
    ball_image = pygame.image.load('./data/ball.png')
    # 在窗口上渲染圖像
    screen.blit(ball_image, (50, 50))
    # 刷新當前窗口(渲染窗口將繪製的圖像呈現出來)
    pygame.display.flip()
    running = True
    # 開啟一個事件循環處理髮生的事件
    while running:
        # 從消息隊列中獲取事件並對事件進行處理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
"""

"""
# 實現動畫效果

import pygame


def main():
    # 初始化導入的pygame中的模塊
    pygame.init()
    # 初始化用於顯示的窗口並設置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 設置當前窗口的標題
    pygame.display.set_caption('大球吃小球')
    # 定義變量來表示小球在屏幕上的位置
    x, y = 50, 50
    running = True
    # 開啟一個事件循環處理髮生的事件
    while running:
        # 從消息隊列中獲取事件並對事件進行處理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0,), (x, y), 30, 0)
        pygame.display.flip()
        # 每隔50毫秒就改變小球的位置再刷新窗口
        pygame.time.delay(50)
        x, y = x + 5, y + 5


if __name__ == '__main__':
    main()
"""

#碰撞檢測

#通常一個遊戲中會有很多對象出現，而這些對象之間的“碰撞”在所難免，比如炮彈擊中了飛機、箱子撞到了地面等。碰撞檢測在絕大多數的遊戲中都是一個必須得處理的至關重要的問題，pygame的sprite（動畫精靈）模塊就提供了對碰撞檢測的支持，這裡我們暫時不介紹sprite模塊提供的功能，因為要檢測兩個小球有沒有碰撞其實非常簡單，只需要檢查球心的距離有沒有小於兩個球的半徑之和。為了製造出更多的小球，我們可以通過對鼠標事件的處理，在點擊鼠標的位置創建顏色、大小和移動速度都隨機的小球，當然要做到這一點，我們可以把之前學習到的面向對象的知識應用起來。

from enum import Enum, unique
from math import sqrt
from random import randint

import pygame


@unique
class Color(Enum):
    """顏色"""

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """獲得隨機顏色"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):
    """球"""

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        """初始化方法"""
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        """移動"""
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        """吃其他球"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        """在窗口上繪製球"""
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)

#事件處理

#可以在事件循環中對鼠標事件進行處理，通過事件對象的type屬性可以判定事件類型，再通過pos屬性就可以獲得鼠標點擊的位置。如果要處理鍵盤事件也是在這個地方，做法與處理鼠標事件類似。

def main():
    # 定義用來裝所有球的容器
    balls = []
    # 初始化導入的pygame中的模塊
    pygame.init()
    # 初始化用於顯示的窗口並設置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 設置當前窗口的標題
    pygame.display.set_caption('大球吃小球')
    running = True
    # 開啟一個事件循環處理髮生的事件
    while running:
        # 從消息隊列中獲取事件並對事件進行處理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 處理鼠標事件的代碼
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 獲得點擊鼠標的位置
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                # 在點擊鼠標的位置創建一個球(大小、速度和顏色隨機)
                ball = Ball(x, y, radius, sx, sy, color)
                # 將球添加到列表容器中
                balls.append(ball)
        screen.fill((255, 255, 255))
        # 取出容器中的球 如果沒被吃掉就繪製 被吃掉了就移除
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        # 每隔50毫秒就改變球的位置再刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # 檢查球有沒有吃到其他的球
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




