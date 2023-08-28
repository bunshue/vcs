import pygame
import sys
from view_manager import ViewManager
import game_functions as gf
import monster_manager as mm
from player import *

def run_game():
    # 初始化游戏
    pygame.init()
    # 创建ViewManager对象
    view_manager = ViewManager()
    # 设置显示屏幕，返回Surface对象
    screen = pygame.display.set_mode((view_manager.screen_width, 
        view_manager.screen_height))
    # 设置标题
    pygame.display.set_caption('合金弹头')
    # 创建玩家角色
    player = Player(view_manager, '孙悟空', MAX_HP)
    while(True):
        # 处理游戏事件
        gf.check_events(screen, view_manager, player)
        # 更新游戏屏幕
        gf.update_screen(screen, view_manager, mm, player)
run_game()
