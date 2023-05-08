#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test draw images.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2016, 2020-2021 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 5, 2021
"""

import math

try:
    from user305_tXfH4AcbNLtjfHy import FPS  # pytype: disable=import-error
    from user305_SZPJfNxJlVTjbAy import Loader  # pytype: disable=import-error

    import simplegui  # pytype: disable=import-error

    SIMPLEGUICS2PYGAME = False
except ImportError:
    from SimpleGUICS2Pygame.simplegui_lib_fps import FPS
    from SimpleGUICS2Pygame.simplegui_lib_loader import Loader

    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore

    SIMPLEGUICS2PYGAME = True

    simplegui.Frame._hide_status = True  # pylint: disable=protected-access
    simplegui.Frame._keep_timers = False  # pylint: disable=protected-access


if SIMPLEGUICS2PYGAME:
    from sys import argv
    from sys import version as python_version
    from pygame.version import ver as pygame_version
    from SimpleGUICS2Pygame import _VERSION as GUI_VERSION  # pylint: disable=ungrouped-imports  # noqa

    PYTHON_VERSION = 'Python ' + python_version.split()[0]
    PYGAME_VERSION = 'Pygame ' + pygame_version
    GUI_VERSION = 'SimpleGUICS2Pygame ' + GUI_VERSION
else:
    PYTHON_VERSION = 'CodeSkulptor'  # https://py2.codeskulptor.org/ or https://py3.codeskulptor.org/  # noqa
    PYGAME_VERSION = ''
    GUI_VERSION = 'simplegui'


TEST = 'test image'

WIDTH = 360
HEIGHT = 270


def draw(canvas):  # type: (simplegui.Canvas) -> None
    """
    Draw a ship image several times.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    """
    canvas.draw_line((0, 0), (WIDTH - 1, HEIGHT - 1), 1, 'Blue')
    canvas.draw_line((0, HEIGHT - 1), (WIDTH, 0), 1, 'Blue')

    img = LOADER.get_image('double_ship')

    # The complete image with ship twice
    canvas.draw_image(img,
                      (img.get_width() / 2, img.get_height() / 2),
                      (img.get_width(), img.get_height()),
                      (img.get_width() / 2, img.get_height() / 2),
                      (img.get_width(), img.get_height()))

    # The ship without thrust
    canvas.draw_image(img,
                      (img.get_width() / 4, img.get_height() / 2),
                      (img.get_width() / 2, img.get_height()),
                      (img.get_width() / 4, img.get_height() * 3 / 2),
                      (img.get_width() / 2, img.get_height()))
    # The ship with thrust
    canvas.draw_image(img,
                      (img.get_width() * 3 / 4, img.get_height() / 2),
                      (img.get_width() / 2, img.get_height()),
                      (img.get_width() * 3 / 4, img.get_height() * 3 / 2),
                      (img.get_width() / 2, img.get_height()))

    # The rotated ship without thrust
    canvas.draw_image(img,
                      (img.get_width() / 4, img.get_height() / 2),
                      (img.get_width() / 2, img.get_height()),
                      (img.get_width() / 4, img.get_height() * 5 / 2),
                      (img.get_width() / 2, img.get_height()),
                      -math.pi / 2)
    # The rotated ship with thrust
    canvas.draw_image(img,
                      (img.get_width() * 3 / 4, img.get_height() / 2),
                      (img.get_width() / 2, img.get_height()),
                      (img.get_width() * 3 / 4, img.get_height() * 5 / 2),
                      (img.get_width() / 2, img.get_height()),
                      -math.pi / 2)

    # The big ship with thrust
    canvas.draw_image(img,
                      (img.get_width() * 3 / 4, img.get_height() / 2),
                      (img.get_width() / 2, img.get_height()),
                      (img.get_width() * 6 / 4, img.get_height() * 3 / 2),
                      (img.get_width(), img.get_height() * 4))

    # The little ship with thrust
    canvas.draw_image(img,
                      (img.get_width() * 3 / 4, img.get_height() / 2),
                      (img.get_width() / 2, img.get_height()),
                      (img.get_width() * 15 / 8, img.get_height() / 2),
                      (img.get_width() / 4, img.get_height()))

    canvas.draw_image(img,
                      (img.get_width() * 3 / 4, img.get_height() / 2),
                      (img.get_width() / 2, img.get_height()),
                      (img.get_width() * 7 / 4, img.get_height() * 11 / 4),
                      (img.get_width() / 2, img.get_height() / 2))

    canvas.draw_image(LOGO,
                      (32, 32), (64, 64),
                      (WIDTH / 2, HEIGHT / 2), (64, 64))

    # Update and draw FPS (if started)
    FPS_DRAWER.draw_fct(canvas)


def fps_on_off():  # type: () -> None
    """Active or inactive the calculation and drawing of FPS."""
    if FPS_DRAWER.is_started():
        FPS_DRAWER.stop()
        BUTTON_FPS.set_text('FPS on')
    else:
        FPS_DRAWER.start()
        BUTTON_FPS.set_text('FPS off')


def init():  # type: () -> None
    """Init after image loaded."""
    if not SIMPLEGUICS2PYGAME:
        global LOGO  # pylint: disable=global-statement

        LOGO = LOADER.get_image('logo')

    FRAME.set_draw_handler(draw)

    if SIMPLEGUICS2PYGAME:
        if len(argv) == 2:
            FRAME._save_canvas_and_stop(argv[1])  # pylint: disable=protected-access  # noqa


# Main
FRAME = simplegui.create_frame(TEST, WIDTH, HEIGHT)

FPS_DRAWER = FPS()

FRAME.add_label(TEST)
FRAME.add_label('')
FRAME.add_label(PYTHON_VERSION)
FRAME.add_label(GUI_VERSION)
FRAME.add_label(PYGAME_VERSION)
FRAME.add_label('')
BUTTON_FPS = FRAME.add_button('FPS on', fps_on_off)
FRAME.add_label('')
FRAME.add_button('Quit', FRAME.stop)


LOADER = Loader(FRAME, WIDTH, init)
LOADER.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png',  # noqa
                 'double_ship')
if not SIMPLEGUICS2PYGAME:
    LOADER.add_image('https://simpleguics2pygame.readthedocs.io/en/latest/_images/SimpleGUICS2Pygame_64x64_t.png',  # noqa
                     'logo')
LOADER.load()

LOADER.wait_loaded()

if SIMPLEGUICS2PYGAME:
    from os.path import dirname, join

    LOGO = simplegui._load_local_image(  # pylint: disable=protected-access,no-member  # noqa
        join(dirname(argv[0]), '../_img/SimpleGUICS2Pygame_64x64_t.png'))

FRAME.start()
if SIMPLEGUICS2PYGAME and FRAME._print_stats_cache:  # pylint: disable=protected-access  # noqa
    LOADER.print_stats_cache()
