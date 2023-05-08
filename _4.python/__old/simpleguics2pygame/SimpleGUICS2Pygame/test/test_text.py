#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test draw text.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013, 2015, 2020-2021 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 5, 2021
"""

try:
    from user305_SaT1YKoOikl4ax9 import draw_text_multi, draw_text_side  # pytype: disable=import-error  # noqa

    import simplegui  # pytype: disable=import-error

    SIMPLEGUICS2PYGAME = False
except ImportError:
    from SimpleGUICS2Pygame.simplegui_lib_draw import draw_text_multi, draw_text_side  # noqa

    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore

    SIMPLEGUICS2PYGAME = True

    simplegui.Frame._hide_status = True  # pylint: disable=protected-access


if SIMPLEGUICS2PYGAME:
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


TEST = 'test text'

WIDTH = 800
HEIGHT = 300


def draw(canvas):  # type: (simplegui.Canvas) -> None
    """
    Draw handler.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    """
    for x in range(0, WIDTH, 20):
        canvas.draw_line((x, 0), (x, HEIGHT - 1), 1, 'silver')

    for y in range(0, HEIGHT, 20):
        canvas.draw_line((0, y), (WIDTH - 1, y), 1, 'silver')

    # Test canvas.draw_text()
    size = 80

    text = 'Text'
    y = 120

    canvas.draw_text(text, (0, y), size, 'rgba(255,255,255,.5)')
    canvas.draw_text(text, (200, y), size, 'white', 'serif')
    canvas.draw_text(text, (400, y), size, 'white', 'sans-serif')
    canvas.draw_text(text, (600, y), size, 'white', 'monospace')

    y = 240

    canvas.draw_text(text, (0, y), size, 'rgba(255,255,255,.5)')
    canvas.draw_text(text, (200, y), size, 'white', 'serif')
    canvas.draw_text(text, (400, y), size, 'white', 'sans-serif')
    canvas.draw_text(text, (600, y), size, 'white', 'monospace')

    # Test simplegui_lib_draw.draw_text_multi()
    size = 20

    draw_text_multi(canvas,
                    """line 1
line 2
line 3""", (200, size), size, 'white', 'serif')

    draw_text_multi(canvas,
                    ('item 1',
                     'item 2',
                     'item 3'), (300, size), size, 'white', 'serif')

    # Test simplegui_lib_draw.draw_text_side()
    size = 40

    draw_text_side(FRAME, canvas,
                   'Left top', (0, 0), size, 'red',
                   rectangle_color='orange',
                   side_x=-1, side_y=-1)

    draw_text_side(FRAME, canvas,
                   'Left bottom', (0, HEIGHT - 1), size, 'red',
                   rectangle_color='orange',
                   side_x=-1, side_y=1)

    draw_text_side(FRAME, canvas,
                   'Right top', (WIDTH - 1, 0), size, 'red',
                   rectangle_color='orange',
                   side_x=1, side_y=-1)

    draw_text_side(FRAME, canvas,
                   'Right bottom', (WIDTH - 1, HEIGHT - 1), size, 'red',
                   rectangle_color='orange',
                   side_x=1, side_y=1)

    draw_text_side(FRAME, canvas,
                   'Center', (WIDTH / 2, HEIGHT / 2), size, 'red',
                   rectangle_color='orange', rectangle_fill_color='yellow',
                   side_x=0, side_y=0)


# Main
FRAME = simplegui.create_frame(TEST, WIDTH, HEIGHT)

FRAME.add_label(TEST)
FRAME.add_label('')
FRAME.add_label(PYTHON_VERSION)
FRAME.add_label(GUI_VERSION)
FRAME.add_label(PYGAME_VERSION)
FRAME.add_label('')
FRAME.add_button('Quit', FRAME.stop)

FRAME.set_draw_handler(draw)

if SIMPLEGUICS2PYGAME:
    from sys import argv

    if len(argv) == 2:
        FRAME._save_canvas_and_stop(argv[1])  # pylint: disable=protected-access  # noqa


FRAME.start()
