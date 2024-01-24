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
from pygame.sprite import Sprite
import player

# 定义代表子弹类型的常量（如果程序还需要增加更多子弹，只需在此处添加常量即可）
BULLET_TYPE_1 = 1
BULLET_TYPE_2 = 2
BULLET_TYPE_3 = 3
BULLET_TYPE_4 = 4

# 子弹类
class Bullet(Sprite):
    def __init__ (self, tipe, x, y, pdir):
        super().__init__()
        # 定义子弹的类型
        self.type = tipe
        # 子弹的X、Y坐标
        self.x = x
        self.y = y
        # 定义子弹的射击方向
        self.dir = pdir
        # 定义子弹在Y方向上的加速度
        self.y_accelate = 0
        # 子弹是否有效
        self.is_effect = True

    # 根据子弹类型获取子弹对应的图片
    def bitmap(self, view_manager): 
        return view_manager.bullet_images[self.type - 1]
    # 根据子弹类型来计算子弹在X方向上的速度
    def speed_x(self):
            # 根据玩家的方向来计算子弹方向和移动方向
            sign = 1 if self.dir == player.DIR_RIGHT else -1
            # 对于第1种子弹，以12为基数来计算它的速度
            if self.type == BULLET_TYPE_1:
                return 12 * sign
            # 对于第2种子弹，以8为基数来计算它的速度
            elif self.type == BULLET_TYPE_2:
                return 8 * sign
            # 对于第3种子弹，以8为基数来计算它的速度
            elif self.type == BULLET_TYPE_3:
                return 8 * sign
            # 对于第4种子弹，以8为基数来计算它的速度
            elif self.type == BULLET_TYPE_4:
                return 8 * sign
            else:
                return 8 * sign

    # 根据子弹类型来计算子弹在Y方向上的速度
    def speed_y(self):
        # 如果self.y_accelate不为0，则以self.y_accelate作为Y方向上的速度
        if self.y_accelate != 0:
            return self.y_accelate
        # 此处控制只有第3种子弹才有Y方向的速度（子弹会斜着向下移动）
        if self.type == BULLET_TYPE_1 or self.type == BULLET_TYPE_2 \
            or self.type == BULLET_TYPE_4:
            return 0
        elif self.type == BULLET_TYPE_3:
            return 6
    # 定义控制子弹移动的方法
    def move(self):
        self.x += self.speed_x()
        self.y += self.speed_y()
