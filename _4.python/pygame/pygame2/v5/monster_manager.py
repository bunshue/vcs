import pygame
from random import randint
from monster import *
from pygame.sprite import Sprite
from pygame.sprite import Group

# 保存所有死掉的怪物，保存它们是为了绘制死亡的动画，绘制完后清除这些怪物
die_monster_list = Group()
# 保存所有活着的怪物
monster_list = Group()

# 随机生成、并添加怪物的函数
def generate_monster(view_manager):
    if len(monster_list) < 3 + randint(0, 2):
        # 创建新怪物
        monster = Monster(view_manager, randint(1, 3))
        monster_list.add(monster)

# 更新怪物与子弹的坐标的函数
def update_posistion(screen, view_manager, player, shift):
    # 定义一个list列表，保存所有将要被删除的怪物
    del_list = []
    # 遍历怪物Group
    for monster in monster_list.sprites():
        monster.draw_bullets(screen, view_manager)
        # 更新怪物、怪物所有子弹的位置
        monster.update_shift(shift)  # ①
        # 如果怪物的X坐标越界，将怪物添加del_list列表中
        if monster.x < 0:
            del_list.append(monster)
    # 删除所有del_list列表中所有怪物
    monster_list.remove(del_list)
    del_list.clear()
    # 遍历所有已死的怪物Group
    for monster in die_monster_list.sprites():
        # 更新怪物、怪物所有子弹的位置
        monster.update_shift(shift)
        # 如果怪物的X坐标越界，将怪物添加del_list列表中
        if monster.x < 0:
            del_list.append(monster)
    # 删除所有del_list列表中所有怪物
    die_monster_list.remove(del_list)
    # 更新玩家控制的角色的子弹坐标
    player.update_bullet_shift(shift)

# 绘制所有怪物的函数
def draw_monster(screen, view_manager):
    # 遍历所有活着的怪物，绘制活着的怪物
    for monster in monster_list.sprites():
        # 画怪物
        monster.draw(screen, view_manager)
    del_list = []
    # 遍历所有已死亡的怪物，绘制已死亡的怪物
    for monster in die_monster_list.sprites():
        # 画怪物
        monster.draw(screen, view_manager)
        # 当怪物的die_max_draw_count返回0时，表明该怪物已经死亡，
        # 且该怪物的死亡动画所有帧都播放完成，将它们彻底删除。
        if monster.die_max_draw_count <= 0:
            del_list.append(monster)
    die_monster_list.remove(del_list)

# 检查怪物是否将要死亡的函数
def check_monster(view_manager, player):
    # 获取玩家发射的所有子弹
    bullet_list = player.bullet_list
    # 定义一个del_list列表，用于保存将要死亡的怪物
    del_list = []
    # 定义一个del_bullet_list列表，用于保存所有将要被删除的子弹
    del_bullet_list = []
    # 遍历所有怪物
    for monster in monster_list.sprites():
        # 如果怪物是炸弹
        if monster.type == TYPE_BOMB:
            # 角色被炸弹炸到
            if player.is_hurt(monster.x, monster.end_x,
                monster.start_y, monster.end_y):
                # 将怪物设置为死亡状态
                monster.is_die = True
                # 播放爆炸音效
                view_manager.sound_effect[1].play()
                # 将怪物（爆炸的炸弹）添加到del_list列表中
                del_list.append(monster)
                # 玩家控制的角色的生命值减10
                player.hp = player.hp - 10
            continue
        # 对于其他类型的怪物，则需要遍历角色发射的所有子弹
        # 只要任何一个子弹打中怪物，即可判断怪物即将死亡
        for bullet in bullet_list.sprites():
            if not bullet.is_effect:
                continue
            # 如果怪物被角色的子弹打到
            if monster.is_hurt(bullet.x, bullet.y):
                # 将子弹设为无效
                bullet.is_effect = False
                # 将怪物设为死亡状态
                monster.is_die = True
                # 如果怪物是飞机
                if monster.type == TYPE_FLY:
                    # 播放爆炸音效
                    view_manager.sound_effect[1].play()
                # 如果怪物是人
                if monster.type == TYPE_MAN:
                    # 播放惨叫音效
                    view_manager.sound_effect[2].play()
                # 将怪物（被子弹打中的怪物）添加到del_list列表中
                del_list.append(monster)
                # 将打中怪物的子弹添加到del_bullet_list列表中
                del_bullet_list.append(bullet)
        # 将del_bullet_list包含的所有子弹从bullet_list中删除
        bullet_list.remove(del_bullet_list)
        # 检查怪物子弹是否打到角色
        monster.check_bullet(player)
    # 将已死亡的怪物（保存在del_list列表中）添加到die_monster_list列表中
    die_monster_list.add(del_list)
    # 将已死亡的怪物（保存在del_list列表中）从monster_list中删除
    monster_list.remove(del_list)
