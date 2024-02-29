import pygame
import random

# 定義顏色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 初始化 Pygame
pygame.init()

# 設置視窗大小
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# 設置遊戲標題
pygame.display.set_caption("射擊遊戲")

# 設置遊戲時鐘
clock = pygame.time.Clock()

# 加載音效
shoot_sound = pygame.mixer.Sound("shoot.wav")

# 加載圖像
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()

bullet_image = pygame.image.load("bullet.png")
bullet_rect = bullet_image.get_rect()

enemy_image = pygame.image.load("enemy.png")
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

# 主遊戲循環
done = False
while not done:
    # 事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # 按下空格鍵發射子彈
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet_rect.x = player_rect.x + player_rect.width
            bullet_rect.y = player_rect.y + player_rect.height / 2 - bullet_rect.height / 2
            shoot_sound.play()

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
screen.fill(BLACK)

# 顯示玩家、子彈、敵人及分數
screen.blit(player_image, player_rect)
screen.blit(bullet_image, bullet_rect)
screen.blit(enemy_image, enemy_rect)
font = pygame.font.SysFont(None, 36)
text = font.render("Score: " + str(score), True, WHITE)
screen.blit(text, (10, 10))

# 更新畫面
pygame.display.flip()

clock.tick(60)
pygame.quit()
