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

# 定义角色向右移动的常量
DIR_RIGHT = 1
# 定义角色向左移动的常量
DIR_LEFT = 2
