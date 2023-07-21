import os
from pathlib import Path

import cocos
import pyglet


def setup():
    cocos.director.director.init()
    have_pyglet_point_to_CocosInvaders_folder()


def have_pyglet_point_to_CocosInvaders_folder():
    pyglet.resource.path = [str(Path(os.path.realpath(__file__)).parent)]
    pyglet.resource.reindex()
