import sys
import pygame
from player import *

def check_events(screen, view_manager, player):
    ''' 响应按键和鼠标事件 '''
    for event in pygame.event.get():
        # 处理游戏退出
        if event.type == pygame.QUIT:
            sys.exit()
        # 处理按键被按下的事件
        if event.type == pygame.KEYDOWN:
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
        # 处理按键被松开的事件
        if event.type == pygame.KEYUP:
            # 用户松开向右键，表示向右站立
            if event.key == pygame.K_RIGHT:
                player.move = MOVE_STAND
            # 用户松开向左键，表示向左站立
            if event.key == pygame.K_LEFT:
                player.move = MOVE_STAND

# 处理更新游戏界面的方法    
def update_screen(screen, view_manager, mm, player):
    # 随机生成怪物
    mm.generate_monster(view_manager)
    # 处理角色的逻辑
    player.logic(screen)    #①
    # 如果游戏角色已死，判断玩家失败
    if player.is_die():   #②
        print('游戏失败!')   #③
    # 检查所有怪物是否将要死亡
    mm.check_monster(view_manager, player)

    # 绘制背景图
    screen.blit(view_manager.map, (0, 0))
    # 画角色
    player.draw(screen)   #③
    # 画怪物
    mm.draw_monster(screen, view_manager)
        
    # 更新屏幕显示，放在最后一行
    pygame.display.flip()
