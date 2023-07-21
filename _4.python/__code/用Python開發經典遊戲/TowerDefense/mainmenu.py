import cocos
import cocos.actions as ac
import cocos.menu
import pyglet
from cocos.director import director
from cocos.scenes.transitions import FadeTRTransition

import constants
from gamelayer import new_game


class MainMenu(cocos.menu.Menu):
    def __init__(self):
        super(MainMenu, self).__init__('Tower Defense')

        self.font_title['font_name'] = constants.OSWALD
        self.font_item['font_name'] = constants.OSWALD
        self.font_item_selected['font_name'] = constants.OSWALD

        self.menu_anchor_y = constants.CENTER
        self.menu_anchor_x = constants.CENTER

        items = list()
        items.append(cocos.menu.MenuItem('New Game', self.on_new_game))
        items.append(cocos.menu.ToggleMenuItem('Show FPS: ', self.show_fps, director.show_FPS))
        items.append(cocos.menu.MenuItem('Quit', pyglet.app.exit))

        self.create_menu(items, ac.ScaleTo(1.25, duration=0.25), ac.ScaleTo(1.0, duration=0.25))

    def on_new_game(self):
        director.push(FadeTRTransition(new_game(), duration=2))

    def show_fps(self, value):
        director.show_FPS = value


def new_menu():
    scene = cocos.scene.Scene()
    color_layer = cocos.layer.ColorLayer(205, 133, 63, 255)
    scene.add(MainMenu(), z=1)
    scene.add(color_layer, z=0)
    return scene
