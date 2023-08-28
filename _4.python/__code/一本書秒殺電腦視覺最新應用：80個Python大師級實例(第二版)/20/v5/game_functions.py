
import sys
import pygame
from player import *

# 代表登录场景的常量
STAGE_LOGIN = 1
# 代表游戏场景的常量
STAGE_GAME = 2
# 代表失败场景的常量
STAGE_LOSE = 3

def check_events(screen, view_manager, player):
    ''' 响应按键和鼠标事件 '''
    for event in pygame.event.get():
        # 处理游戏退出（只有登录界面和失败界面才可退出）
        if event.type == pygame.QUIT and (view_manager.stage == STAGE_LOGIN \
            or view_manager.stage == STAGE_LOSE):
            sys.exit()
        # 处理登录场景下的鼠标按下事件
        if event.type == pygame.MOUSEBUTTONDOWN and view_manager.stage == STAGE_LOGIN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if on_button(view_manager, mouse_x, mouse_y):
                # 开始游戏
                view_manager.stage = STAGE_GAME
        # 处理失败场景下的鼠标按下事件
        if event.type == pygame.MOUSEBUTTONDOWN and view_manager.stage == STAGE_LOSE:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if on_button(view_manager, mouse_x, mouse_y):
                # 将角色生命值恢复到最大
                player.hp = MAX_HP
                # 进入游戏场景
                view_manager.stage = STAGE_GAME
        # 处理登录场景下的鼠标移动事件
        if event.type == pygame.MOUSEMOTION and view_manager.stage == STAGE_LOGIN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if on_button(view_manager, mouse_x, mouse_y):
                # 如果鼠标在按钮上方移动，控制按钮绘制高亮图片
                view_manager.start_image_index = 1
            else:
                view_manager.start_image_index = 0
            pygame.display.flip()
        # 处理游戏场景下按键被按下的事件
        if event.type == pygame.KEYDOWN and view_manager.stage == STAGE_GAME:
            if event.key == pygame.K_SPACE:
                # 当角色的left_shoot_time为0时（上一枪发射结束），角色才能发射下一枪。
                if player.left_shoot_time <= 0:
                    player.add_bullet(view_manager)
            # 用户按下向上键，表示跳起来
            if event.key == pygame.K_UP:
                player.is_jump = True
            # 用户按下向右键，表示向右移动
            if event.key == pygame.K_RIGHT:
                player.move = MOVE_RIGHT
            # 用户按下向右键，表示向左移动
            if event.key == pygame.K_LEFT:
                player.move = MOVE_LEFT
        # 处理游戏场景下按键被松开的事件
        if event.type == pygame.KEYUP and view_manager.stage == STAGE_GAME:
            # 用户松开向右键，表示向右站立
            if event.key == pygame.K_RIGHT:
                player.move = MOVE_STAND
            # 用户松开向左键，表示向左站立
            if event.key == pygame.K_LEFT:
                player.move = MOVE_STAND

# 判断当前鼠标是否在界面的按钮上
def on_button(view_manager, mouse_x, mouse_y):
    return view_manager.button_start_x < mouse_x < \
        view_manager.button_start_x + view_manager.again_image.get_width()\
        and view_manager.button_start_y < mouse_y < \
        view_manager.button_start_y + view_manager.again_image.get_height()

# 处理更新游戏界面的方法
def update_screen(screen, view_manager, mm, player):
    # 如果处于游戏登录场景
    if view_manager.stage == STAGE_LOGIN:
        view_manager.draw_login(screen)
    # 如果当前处于游戏场景
    elif view_manager.stage == STAGE_GAME:
        # 随机生成怪物
        mm.generate_monster(view_manager)
        # 处理角色的逻辑
        player.logic(screen)
        # 如果游戏角色已死，判断玩家失败
        if player.is_die():
            view_manager.stage = STAGE_LOSE
        # 检查所有怪物是否将要死亡
        mm.check_monster(view_manager, player)

        # 绘制游戏
        view_manager.draw_game(screen, mm, player)
    # 如果当前处于失败场景
    elif view_manager.stage == STAGE_LOSE:
        view_manager.draw_lose(screen)

    # 更新屏幕显示，放在最后一行
    pygame.display.flip()
