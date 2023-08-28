import sys
import pygame

def check_events(screen, view_manager):
    ''' 响应按键和鼠标事件 '''
    for event in pygame.event.get():
        # 处理游戏退出
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(screen, view_manager, mm):
    ''' 处理更新游戏界面的方法 '''
    # 随机生成怪物
    mm.generate_monster(view_manager)
    # 绘制背景图
    screen.blit(view_manager.map, (0, 0))
    # 画怪物
    mm.draw_monster(screen, view_manager)

    # 更新屏幕显示，放在最后一行
    pygame.display.flip()
