from functools import reduce

import cocos
import cocos.actions as ac

RIGHT = ac.RotateBy(90, 1)
LEFT = ac.RotateBy(-90, 1)


class Scenario(object):
    def __init__(self, tmx_map, turret_slots, bunker_position, enemy_start_position):
        self.tmx_map = tmx_map
        self.turret_slots = turret_slots
        self.bunker_position = bunker_position
        self.enemy_start_position = enemy_start_position
        self._actions = None

    def get_background(self):
        tmx_map = cocos.tiles.load('assets/tower_defense.tmx')
        bg = tmx_map['map0']
        bg.set_view(0, 0, bg.px_width, bg.px_height)
        return bg

    @property
    def actions(self):
        return self._actions

    @actions.setter
    def actions(self, actions):
        self._actions = ac.RotateBy(90, 0.5)
        self._actions = reduce((lambda x, y: x + y), actions)


def get_scenario():
    turret_slots = [(192, 352), (320, 352), (448, 352),
                    (192, 192), (320, 192), (448, 192),
                    (96, 32), (224, 32), (352, 32), (480, 32)]
    bunker_position = (528, 430)
    enemy_start_position = (-80, 110)
    sc = Scenario('map0', turret_slots, bunker_position, enemy_start_position)

    # Call the _action property's setter
    sc.actions = [move(610, 10), LEFT, move(0, 160),
                  LEFT, move(-415, 0), RIGHT,
                  move(0, 160), RIGHT, move(420, 0)]
    return sc


def move(x, y):
    dur = abs(x + y) / 100.0
    return ac.MoveBy((x, y), duration=dur)
