import pygame
import sys
from random import randint
from pygame.sprite import Sprite
from pygame.sprite import Group
import pygame.font

from bullet import *
import monster_manager as mm

# 定义角色的最高生命值
MAX_HP = 50
# 定义控制角色动作的常量
# 此处只控制该角色包含站立、跑、跳等动作
ACTION_STAND_RIGHT = 1
ACTION_STAND_LEFT = 2
ACTION_RUN_RIGHT = 3
ACTION_RUN_LEFT = 4
ACTION_JUMP_RIGHT = 5
ACTION_JUMP_LEFT = 6
# 定义角色向右移动的常量
DIR_RIGHT = 1
# 定义角色向左移动的常量
DIR_LEFT = 2
# 定义控制角色移动的常量
# 此处控制该角色只包含站立、向右移动、向左移动三种移动方式
MOVE_STAND = 0
MOVE_RIGHT = 1
MOVE_LEFT = 2
MAX_LEFT_SHOOT_TIME = 6

class Player(Sprite):
    def __init__(self, view_manager, name, hp):
        super().__init__()
        self.name = name # 保存角色名字的成员变量
        self.hp = hp # 保存角色生命值的成员变量
        self.view_manager = view_manager
        # 保存角色所使用枪的类型（以后可考虑让角色能更换不同的枪）
        self.gun = 0
        # 保存角色当前动作的成员变量（默认向右站立）
        self.action = ACTION_STAND_RIGHT
        # 代表角色X坐标的属性
        self._x = -1
        # 代表角色Y坐标的属性
        self.y = -1
        # 保存角色射出的所有子弹
        self.bullet_list = Group()
        # 保存角色移动方式的成员变量
        self.move = MOVE_STAND
        # 控制射击状态的保留计数器
        # 每当用户发射一枪时，left_shoot_time会被设为MAX_LEFT_SHOOT_TIME，然后递减
        # 只有当left_shoot_time变为0时，用户才能发射下一枪
        self.left_shoot_time = 0
        # 保存角色是否跳动的属性
        self._is_jump = False
        # 保存角色是否跳到最高处的成员变量
        self.is_jump_max = False
        # 控制跳到最高处的停留时间
        self.jump_stop_count = 0
        # 当前正在绘制角色脚部动画的第几帧
        self.index_leg = 0
        # 当前正在绘制角色头部动画的第几帧
        self.index_head = 0
        # 当前绘制头部图片的X坐标
        self.current_head_draw_x = 0
        # 当前绘制头部图片的Y坐标
        self.current_head_draw_y = 0
        # 当前正在画的脚部动画帧的图片
        self.current_leg_bitmap = None
        # 当前正在画的头部动画帧的图片
        self.current_head_bitmap = None
        # 该变量控制用于控制动画刷新的速度
        self.draw_count = 0
        # 加载中文字体
        self.font = pygame.font.Font('images/msyh.ttf', 20)

    # 计算该角色当前方向：action成员变量为奇数代表向右
    def get_dir(self):
        return DIR_RIGHT if self.action % 2 == 1 else DIR_LEFT

    def get_x(self):
        return self._x
    def set_x(self, x_val):
            self._x = x_val % (self.view_manager.map.get_width() +
                self.view_manager.X_DEFAULT)
            # 如果角色移动到屏幕最左边
            if self._x < self.view_manager.X_DEFAULT:
                self._x = self.view_manager.X_DEFAULT
    x = property(get_x, set_x)

    def get_is_jump(self):
        return self._is_jump
    def set_is_jump(self, jump_val):
        self._is_jump = jump_val
        self.jump_stop_count = 6
    is_jump = property(get_is_jump, set_is_jump)


    # 返回该角色在游戏界面上的位移
    def shift(self):
        if self.x <= 0 or self.y <= 0:
            self.init_position()
        return self.view_manager.X_DEFAULT - self.x

    # 判断角色是否已经死亡
    def is_die(self):
        return self.hp <= 0

    # 初始化角色的初始化位置，角色能跳的最大高度
    def init_position(self):
        self.x = self.view_manager.screen_width * 15 / 100
        self.y = self.view_manager.screen_height * 75 / 100

    # 画角色的方法
    def draw(self, screen):
        # 绘制角色向右站立的动画图片
        if self.action == ACTION_STAND_RIGHT:
            self.draw_anim(screen, self.view_manager.leg_stand_images, 
                self.view_manager.head_stand_images, DIR_RIGHT)
        # 绘制角色向左站立的动画图片
        elif self.action == ACTION_STAND_LEFT:
            self.draw_anim(screen, self.view_manager.leg_stand_images, 
                self.view_manager.head_stand_images, DIR_LEFT)
        # 绘制角色向右跑动的动画图片
        elif self.action == ACTION_RUN_RIGHT:
            self.draw_anim(screen, self.view_manager.leg_run_images, 
                self.view_manager.head_run_images, DIR_RIGHT)
        # 绘制角色向左跑动的动画图片
        elif self.action == ACTION_RUN_LEFT:
            self.draw_anim(screen, self.view_manager.leg_run_images, 
                self.view_manager.head_run_images, DIR_LEFT)
        # 绘制角色向右跳动的动画图片
        elif self.action == ACTION_JUMP_RIGHT:
            self.draw_anim(screen, self.view_manager.leg_jump_images, 
                self.view_manager.head_jump_images, DIR_RIGHT)
        # 绘制角色向左跳动的动画图片
        elif self.action == ACTION_JUMP_LEFT:
            self.draw_anim(screen, self.view_manager.leg_jump_images, 
                self.view_manager.head_jump_images, DIR_LEFT)

    # 绘制角色的动画帧
    def draw_anim(self, screen, leg_arr, head_arr_from, pdir):
        head_arr = head_arr_from
        # 射击状态停留次数每次减1
        if self.left_shoot_time > 0:
            head_arr = self.view_manager.head_shoot_images
            self.left_shoot_time -= 1
        self.index_leg %= len(leg_arr)
        self.index_head %= len(head_arr)

        # 先画脚
        bitmap = leg_arr[self.index_leg]
        draw_x = self.view_manager.X_DEFAULT
        draw_y = self.y - bitmap.get_height()
        # 根据角色方向判断是否需要翻转图片
        if self.get_dir() == DIR_RIGHT:
            # 对图片执行镜像（第二个参数控制水平镜像，第三个参数控制垂直镜像）
            bitmap_mirror = pygame.transform.flip(bitmap, True, False)
            screen.blit(bitmap_mirror, (draw_x, draw_y))
        else:
            screen.blit(bitmap, (draw_x, draw_y))           
        self.current_leg_bitmap = bitmap

        # 再画头
        bitmap2 = head_arr[self.index_head]
        draw_x -= (bitmap2.get_width() - bitmap.get_width() >> 1)
        if self.action == ACTION_STAND_LEFT:
            draw_x += 6
        draw_y = draw_y - bitmap2.get_height() + 10
        # 根据角色方向判断是否需要翻转图片
        if self.get_dir() == DIR_RIGHT:
            # 对图片执行镜像（第二个参数控制水平镜像，第三个参数控制垂直镜像）
            bitmap2_mirror = pygame.transform.flip(bitmap2, True, False)
            screen.blit(bitmap2_mirror, (draw_x, draw_y))
        else:
            screen.blit(bitmap2, (draw_x, draw_y))  
        self.current_head_draw_x = draw_x
        self.current_head_draw_y = draw_y
        self.current_head_bitmap = bitmap2
        # self.draw_count控制该方法每调用4次才会切换到下一帧位图
        self.draw_count += 1
        if self.draw_count >= 4:
            self.draw_count = 0
            self.index_leg += 1
            self.index_head += 1
        # 画子弹
        self.draw_bullet(screen)
        # 画左上角的角色、名字、血量
        self.draw_head(screen)

    # 绘制左上角的角色、名字、生命值的方法
    def draw_head(self, screen):
        if self.view_manager.head == None:
            return
        # 对图片执行镜像（第二个参数控制水平镜像，第三个参数控制垂直镜像）
        head_mirror = pygame.transform.flip(self.view_manager.head, True, False)
        # 画头像
        screen.blit(head_mirror, (0, 0))
        # 将名字渲染成图像
        name_image = self.font.render(self.name, True, (230, 23, 23))
        # 画名字
        screen.blit(name_image, (self.view_manager.head.get_width(), 10))
        # 将生命值渲染成图像
        hp_image = self.font.render("HP:" + str(self.hp), True, (230, 23, 23))
        # 画生命值
        screen.blit(hp_image, (self.view_manager.head.get_width(), 30))

    # 判断该角色是否被子弹打中的方法
    def is_hurt(self, start_x, end_x, start_y, end_y):
        if self.current_head_bitmap == None or self.current_leg_bitmap == None:
            return False
        # 计算角色的图片所覆盖的矩形区域
        player_start_x = self.current_head_draw_x
        player_end_x = player_start_x + self.current_head_bitmap.get_width()
        player_start_y = self.current_head_draw_y
        player_end_y = player_start_y + self.current_head_bitmap.get_height() + \
            self.current_leg_bitmap.get_height()
        # 如果子弹出现的位置与角色图片覆盖的矩形区域有重叠，即可判断角色被子弹打中
        return (player_start_x < start_x < player_end_x \
            or player_start_x < end_x < player_end_x) \
            and (player_start_y < start_y < player_end_y \
            or player_start_y < end_y < player_end_y)

    # 发射子弹的方法
    def add_bullet(self, view_manager):
        # 计算子弹的初始X坐标
        bullet_x = self.view_manager.X_DEFAULT + 50 if self.get_dir() \
            == DIR_RIGHT else self.view_manager.X_DEFAULT - 50
        # 创建子弹对象
        bullet = Bullet(BULLET_TYPE_1, bullet_x, self.y - 60, self.get_dir())
        # 将子弹添加到用户发射的子弹Group中
        self.bullet_list.add(bullet)
        # 发射子弹时，将self.left_shoot_time设置为射击状态最大值
        self.left_shoot_time = MAX_LEFT_SHOOT_TIME
    # 画子弹
    def draw_bullet(self, screen):
        delete_list = []
        # 遍历角色发射的所有子弹
        for bullet in self.bullet_list.sprites():
            # 将所有越界的子弹收集到delete_list列表中
            if bullet.x < 0 or bullet.x > self.view_manager.screen_width:
                delete_list.append(bullet)
        # 清除所有越界的子弹
        self.bullet_list.remove(delete_list)
        # 遍历用户发射的所有子弹
        for bullet in self.bullet_list.sprites():
            # 获取子弹对应的位图
            bitmap = bullet.bitmap(self.view_manager)
            # 子弹移动
            bullet.move()
            # 画子弹，根据子弹方向判断是否需要翻转图片
            if bullet.dir == DIR_LEFT:
                # 对图片执行镜像（第二个参数控制水平镜像，第三个参数控制垂直镜像）
                bitmap_mirror = pygame.transform.flip(bitmap, True, False)
                screen.blit(bitmap_mirror, (bullet.x, bullet.y))
            else:
                screen.blit(bitmap, (bullet.x, bullet.y)) 

    # 处理角色移动的方法
    def move_position(self, screen):
        if self.move == MOVE_RIGHT:
            # 更新怪物的位置
            mm.update_posistion(screen, self.view_manager, self, 6)
            # 更新角色位置
            self.x += 6
            if not self.is_jump:
                # 不跳的时候，需要设置动作
                self.action = ACTION_RUN_RIGHT
        elif self.move == MOVE_LEFT:
            if self.x - 6 < self.view_manager.X_DEFAULT:
                # 更新怪物的位置
                mm.update_posistion(screen, self.view_manager, self, \
                    -(self.x - self.view_manager.X_DEFAULT))
            else:
                # 更新怪物的位置
                mm.update_posistion(screen, self.view_manager, self, -6)
            # 更新角色位置
            self.x -= 6
            if not self.is_jump:
                # 不跳的时候，需要设置动作
                self.action = ACTION_RUN_LEFT
        elif self.action != ACTION_JUMP_RIGHT and self.action != ACTION_JUMP_LEFT:
            if not self.is_jump:
                # 不跳的时候，需要设置动作
                self.action = ACTION_STAND_RIGHT

    # 处理角色移动与跳的逻辑关系
    def logic(self, screen):
        if not self.is_jump:
            self.move_position(screen)
            return
        # 如果还没有跳到最高点
        if not self.is_jump_max:
            self.action = ACTION_JUMP_RIGHT if self.get_dir() == \
                DIR_RIGHT else ACTION_JUMP_LEFT
            # 更新Y坐标
            self.y -= 8
            # 设置子弹在Y方向上具有向上的加速度
            self.set_bullet_y_accelate(-2)
            # 已经达到最高点
            if self.y <= self.view_manager.Y_JUMP_MAX:
                self.is_jump_max = True
        else:
            self.jump_stop_count -= 1
            # 如果在最高点停留次数已经使用完
            if self.jump_stop_count <= 0:
                # 更新Y坐标
                self.y += 8
                # 设置子弹在Y方向上具有向下的加速度
                self.set_bullet_y_accelate(2)
                # 已经掉落到最低点
                if self.y >= self.view_manager.Y_DEFALUT:
                    # 恢复Y坐标
                    self.y = self.view_manager.Y_DEFALUT
                    self.is_jump = False
                    self.is_jump_max = False
                    self.action = ACTION_STAND_RIGHT
                else:
                    # 未掉落到最低点，继续使用跳的动作
                    self.action = ACTION_JUMP_RIGHT if self.get_dir() == \
                    DIR_RIGHT else ACTION_JUMP_LEFT
        # 控制角色移动
        self.move_position(screen)

    # 更新子弹的位置（子弹位置同样会受到角色的位移的影响）
    def update_bullet_shift(self, shift):
        for bullet in self.bullet_list:
            bullet.x = bullet.x - shift
            
    # 给子弹设置垂直方向上的加速度
    # 游戏的设计是：当角色跳动时，子弹会具有垂直方向上的加速度
    def set_bullet_y_accelate(self, accelate):
        for bullet in self.bullet_list:
            if bullet.y_accelate == 0:
                bullet.y_accelate = accelate

        
