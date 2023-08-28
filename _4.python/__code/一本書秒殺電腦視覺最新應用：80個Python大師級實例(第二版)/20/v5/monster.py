import pygame
import sys
from random import randint
from pygame.sprite import Sprite
from pygame.sprite import Group
from bullet import *

# 控制怪物动画的速度
COMMON_SPEED_THRESHOLD = 10
MAN_SPEED_THRESHOLD = 8

# 定义代表怪物类型的常量（如果程序还需要增加更多怪物，只需在此处添加常量即可）
TYPE_BOMB = 1
TYPE_FLY = 2
TYPE_MAN = 3

class Monster(Sprite):
    def __init__ (self, view_manager, tp=TYPE_BOMB):
        super().__init__()
        # 定义怪物的种类
        self.type = tp
        # 定义怪物X、Y坐标的属性
        self.x = 0
        self.y = 0
        # 定义怪物是否已经死亡的旗标
        self.is_die = False
        # 绘制怪物图片的左上角的X坐标
        self.start_x = 0
        # 绘制怪物图片的左上角的Y坐标
        self.start_y = 0
        # 绘制怪物图片的右下角的X坐标
        self.end_x = 0
        # 绘制怪物图片的右下角的Y坐标
        self.end_y = 0
        # 该变量控制用于控制动画刷新的速度
        self.draw_count = 0
        # 定义当前正在绘制怪物动画的第几帧的变量
        self.draw_index = 0
        # 用于记录死亡动画只绘制一次，不需要重复绘制
        # 每当怪物死亡时，该变量会被初始化为等于死亡动画的总帧数
        # 当怪物的死亡动画帧播放完成时，该变量的值变为0。
        self.die_max_draw_count = sys.maxsize
        # 定义怪物射出的子弹
        self.bullet_list = Group()
        # -------下面代码根据怪物类型来初始化怪物X、Y坐标------
        # 如果怪物是炸弹（TYPE_BOMB）或敌人（TYPE_MAN）
        # 怪物的Y坐标与玩家控制的角色的Y坐标相同
        if self.type == TYPE_BOMB or self.type == TYPE_MAN:
            self.y = view_manager.Y_DEFALUT
        # 如果怪物是飞机，根据屏幕高度随机生成怪物的Y坐标
        elif self.type == TYPE_FLY:
            self.y = view_manager.screen_height * 50 / 100 - randint(0, 99)
        # 随机计算怪物的X坐标。
        self.x = view_manager.screen_width + randint(0, 
            view_manager.screen_width >> 1) - (view_manager.screen_width >> 2)

    # 画怪物的方法
    def draw(self, screen, view_manager):
        # 如果怪物类型是炸弹，绘制炸弹
        if self.type == TYPE_BOMB:
            # 死亡的怪物用死亡图片,活着的怪物用活着的图片
            self.draw_anim(screen, view_manager, view_manager.bomb2_images 
                if self.is_die else view_manager.bomb_images)
        # 如果怪物类型是飞机，绘制飞机
        elif self.type == TYPE_FLY:
            self.draw_anim(screen, view_manager, view_manager.fly_die_images 
                if self.is_die else view_manager.fly_images)
        # 如果怪物类型是人，绘制人
        elif self.type == TYPE_MAN:
            self.draw_anim(screen, view_manager, view_manager.man_die_images 
                if self.is_die else view_manager.man_images)
        else:
            pass

    # 根据怪物的动画帧图片来绘制怪物动画
    def draw_anim(self, screen, view_manager, bitmap_arr):
        # 如果怪物已经死，且没有播放过死亡动画
        #（self.die_max_draw_count等于初始值表明未播放过死亡动画）
        if self.is_die and self.die_max_draw_count == sys.maxsize:
            # 将die_max_draw_count设置与死亡动画的总帧数相等
            self.die_max_draw_count = len(bitmap_arr)    # ⑤
        self.draw_index %= len(bitmap_arr)
        # 获取当前绘制的动画帧对应的位图
        bitmap = bitmap_arr[self.draw_index]  # ①
        if bitmap == None:
            return
        draw_x = self.x
        # 对绘制怪物动画帧位图的X坐标进行微调
        if self.is_die:
            if type == TYPE_BOMB:
                draw_x = self.x - 50
            elif type == TYPE_MAN:
                draw_x = self.x + 50
        # 对绘制怪物动画帧位图的Y坐标进行微调
        draw_y = self.y - bitmap.get_height()
        # 画怪物动画帧的位图
        screen.blit(bitmap, (draw_x, draw_y))
        self.start_x = draw_x
        self.start_y = draw_y
        self.end_x = self.start_x + bitmap.get_width()
        self.end_y = self.start_y + bitmap.get_height()
        self.draw_count += 1
        # 控制人、飞机的发射子弹的速度
        if self.draw_count >= (COMMON_SPEED_THRESHOLD if type == TYPE_MAN
                else MAN_SPEED_THRESHOLD):  # ③
            # 如果怪物是人，只在第3帧才发射子弹
            if self.type == TYPE_MAN and self.draw_index == 2:
                self.add_bullet()
            # 如果怪物是飞机，只在最后一帧才发射子弹
            if self.type == TYPE_FLY and self.draw_index == len(bitmap_arr) - 1:
                self.add_bullet()
            self.draw_index += 1   # ②
            self.draw_count = 0    # ④
        # 每播放死亡动画的一帧，self.die_max_draw_count减1。
        # 当self.die_max_draw_count等于0时，表明死亡动画播放完成。
        if self.is_die:
            self.die_max_draw_count -= 1   # ⑥
        # 绘制子弹
        self.draw_bullets(screen, view_manager)

    # 判断怪物是否被子弹打中的方法
    def is_hurt(self, x, y): 
        return self.start_x < x < self.end_x and self.start_y < y < self.end_y

    # 根据怪物类型获取子弹类型，不同怪物发射不同的子弹
    # return 0代表这种怪物不发射子弹
    def bullet_type(self):
        if self.type == TYPE_BOMB:
            return 0
        elif self.type == TYPE_FLY:
            return BULLET_TYPE_3
        elif self.type == TYPE_MAN:
            return BULLET_TYPE_2
        else:
            return 0

    # 定义发射子弹的方法
    def add_bullet(self):
        # 如果没有子弹
        if self.bullet_type() <= 0:
            return
        # 计算子弹的X、Y坐标
        draw_x = self.x
        draw_y = self.y - 60
        # 如果怪物是飞机，重新计算飞机发射的子弹的Y坐标
        if self.type == TYPE_FLY:
            draw_y = self.y - 30
        # 创建子弹对象
        bullet = Bullet(self.bullet_type(), draw_x, draw_y, player.DIR_LEFT)
        # 将子弹添加到该怪物发射的子弹Group中
        self.bullet_list.add(bullet)

    # 更新所有子弹的位置：将所有子弹的X坐标减少shift距离（子弹左移）
    def update_shift(self, shift):
        self.x -= shift
        for bullet in self.bullet_list:
            if bullet != None:
                bullet.x -= shift

    # 绘制子弹的方法
    def draw_bullets(self, screen, view_manager) :
        # 遍历该怪物发射的所有子弹
        for bullet in self.bullet_list.copy():
             # 如果子弹已经越过屏幕
            if bullet.x <= 0 or bullet.x > view_manager.screen_width:
                # 删除已经移出屏幕的子弹
                self.bullet_list.remove(bullet)  # ⑦
        # 绘制所有子弹
        for bullet in self.bullet_list.sprites():
            # 获取子弹对应的位图
            bitmap = bullet.bitmap(view_manager)
            if bitmap == None:
                continue
            # 子弹移动
            bullet.move()
            # 绘制子弹的位图
            screen.blit(bitmap, (bullet.x, bullet.y))

    # 判断子弹是否与玩家控制的角色碰撞（判断子弹是否打中角色）
    def check_bullet(self, player):
        # 遍历所有子弹
        for bullet in self.bullet_list.copy():
            if bullet == None or not bullet.is_effect:
                continue
            # 如果玩家控制的角色被子弹打到
            if player.is_hurt(bullet.x, bullet.x, bullet.y, bullet.y):
                # 子弹设为无效
                bullet.isEffect = False
                # 将玩家的生命值减5
                player.hp = player.hp - 5
                # 删除已经击中玩家控制的角色的子弹
                self.bullet_list.remove(bullet)
