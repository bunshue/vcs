# coding: utf-8
#########################################################################
# 网站: <a href="http:#www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2018, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
import pygame

# 管理图片加载和图片绘制的工具类
class ViewManager:
    # 加载所有游戏图片、声音的方法
    def __init__ (self):
        self.screen_width = 1200
        self.screen_height = 600
        # 保存角色生命值的成员变量
        x = self.screen_width * 15 / 100
        y = self.screen_height * 75 / 100
        # 控制角色的默认坐标
        self.X_DEFAULT = x
        self.Y_DEFALUT = y
        self.Y_JUMP_MAX = self.screen_height * 50 / 100

        self.map = pygame.image.load("images/map.jpg")
        self.map_back = pygame.image.load("images/game_back.jpg")
        self.map_back = pygame.transform.scale(self.map_back, (1200, 600))
        # 加载角色站立时腿部动画帧的图片
        self.leg_stand_images = []
        self.leg_stand_images.append(pygame.image.load("images/leg_stand.png"))
        # 加载角色站立时头部动画帧的图片
        self.head_stand_images = []
        self.head_stand_images.append(pygame.image.load("images/head_stand_1.png"))
        self.head_stand_images.append(pygame.image.load("images/head_stand_2.png"))
        self.head_stand_images.append(pygame.image.load("images/head_stand_3.png"))
        # 加载角色跑动时腿部动画帧的图片
        self.leg_run_images = []
        self.leg_run_images.append(pygame.image.load("images/leg_run_1.png"))
        self.leg_run_images.append(pygame.image.load("images/leg_run_2.png"))
        self.leg_run_images.append(pygame.image.load("images/leg_run_3.png"))
        # 加载角色跑动时头部动画帧的图片
        self.head_run_images = []
        self.head_run_images.append(pygame.image.load("images/head_run_1.png"))
        self.head_run_images.append(pygame.image.load("images/head_run_2.png"))
        self.head_run_images.append(pygame.image.load("images/head_run_3.png"))
        # 加载角色跳跃时腿部动画帧的图片
        self.leg_jump_images = []
        self.leg_jump_images.append(pygame.image.load("images/leg_jum_1.png"))
        self.leg_jump_images.append(pygame.image.load("images/leg_jum_2.png"))
        self.leg_jump_images.append(pygame.image.load("images/leg_jum_3.png"))
        self.leg_jump_images.append(pygame.image.load("images/leg_jum_4.png"))
        self.leg_jump_images.append(pygame.image.load("images/leg_jum_5.png"))
        # 加载角色跳跃时头部动画帧的图片
        self.head_jump_images = []
        self.head_jump_images.append(pygame.image.load("images/head_jump_1.png"))
        self.head_jump_images.append(pygame.image.load("images/head_jump_2.png"))
        self.head_jump_images.append(pygame.image.load("images/head_jump_3.png"))
        self.head_jump_images.append(pygame.image.load("images/head_jump_4.png"))
        self.head_jump_images.append(pygame.image.load("images/head_jump_5.png"))
        # 加载角色射击时头部动画帧的图片
        self.head_shoot_images = []
        self.head_shoot_images.append(pygame.image.load("images/head_shoot_1.png"))
        self.head_shoot_images.append(pygame.image.load("images/head_shoot_2.png"))
        self.head_shoot_images.append(pygame.image.load("images/head_shoot_3.png"))
        self.head_shoot_images.append(pygame.image.load("images/head_shoot_4.png"))
        self.head_shoot_images.append(pygame.image.load("images/head_shoot_5.png"))
        self.head_shoot_images.append(pygame.image.load("images/head_shoot_6.png"))
        # 加载子弹的图片
        self.bullet_images = []
        self.bullet_images.append(pygame.image.load("images/bullet_1.png"))
        self.bullet_images.append(pygame.image.load("images/bullet_2.png"))
        self.bullet_images.append(pygame.image.load("images/bullet_3.png"))
        self.bullet_images.append(pygame.image.load("images/bullet_4.png"))
        self.head = pygame.image.load("images/head.png")
        # 加载第一种怪物（炸弹）未爆炸时动画帧的图片
        self.bomb_images = []
        self.bomb_images.append(pygame.image.load("images/bomb_1.png"))
        self.bomb_images.append(pygame.image.load("images/bomb_2.png"))
        # 加载第一种怪物（炸弹）爆炸时的图片
        self.bomb2_images = []
        self.bomb2_images.append(pygame.image.load("images/bomb2_1.png"))
        self.bomb2_images.append(pygame.image.load("images/bomb2_2.png"))
        self.bomb2_images.append(pygame.image.load("images/bomb2_3.png"))
        self.bomb2_images.append(pygame.image.load("images/bomb2_4.png"))
        self.bomb2_images.append(pygame.image.load("images/bomb2_5.png"))
        self.bomb2_images.append(pygame.image.load("images/bomb2_6.png"))
        self.bomb2_images.append(pygame.image.load("images/bomb2_7.png"))
        self.bomb2_images.append(pygame.image.load("images/bomb2_8.png"))
        self.bomb2_images.append(pygame.image.load("images/bomb2_9.png"))
        self.bomb2_images.append(pygame.image.load("images/bomb2_10.png"))
        self.bomb2_images.append(pygame.image.load("images/bomb2_11.png"))
        self.bomb2_images.append(pygame.image.load("images/bomb2_12.png"))
        self.bomb2_images.append(pygame.image.load("images/bomb2_13.png"))
        # 加载第二种怪物（飞机）的动画帧的图片
        self.fly_images = []
        self.fly_images.append(pygame.image.load("images/fly_1.gif"))
        self.fly_images.append(pygame.image.load("images/fly_2.gif"))
        self.fly_images.append(pygame.image.load("images/fly_3.gif"))
        self.fly_images.append(pygame.image.load("images/fly_4.gif"))
        self.fly_images.append(pygame.image.load("images/fly_5.gif"))
        self.fly_images.append(pygame.image.load("images/fly_6.gif"))
        # 加载第二种怪物（飞机）爆炸时的动画帧的图片
        self.fly_die_images = []
        self.fly_die_images.append(pygame.image.load("images/fly_die_1.png"))
        self.fly_die_images.append(pygame.image.load("images/fly_die_2.png"))
        self.fly_die_images.append(pygame.image.load("images/fly_die_3.png"))
        self.fly_die_images.append(pygame.image.load("images/fly_die_4.png"))
        self.fly_die_images.append(pygame.image.load("images/fly_die_5.png"))
        self.fly_die_images.append(pygame.image.load("images/fly_die_6.png"))
        self.fly_die_images.append(pygame.image.load("images/fly_die_7.png"))
        self.fly_die_images.append(pygame.image.load("images/fly_die_8.png"))
        self.fly_die_images.append(pygame.image.load("images/fly_die_9.png"))
        self.fly_die_images.append(pygame.image.load("images/fly_die_10.png"))
        # 加载第三种怪物（人）活着时的动画帧的图片
        self.man_images = []
        self.man_images.append(pygame.image.load("images/man_1.png"))
        self.man_images.append(pygame.image.load("images/man_2.png"))
        self.man_images.append(pygame.image.load("images/man_3.png"))
        # 加载第三种怪物（人）死亡时的动画帧的图片
        self.man_die_images = []
        self.man_die_images.append(pygame.image.load("images/man_die_1.png"))
        self.man_die_images.append(pygame.image.load("images/man_die_2.png"))
        self.man_die_images.append(pygame.image.load("images/man_die_3.png"))
        self.man_die_images.append(pygame.image.load("images/man_die_4.png"))
        self.man_die_images.append(pygame.image.load("images/man_die_5.png"))
