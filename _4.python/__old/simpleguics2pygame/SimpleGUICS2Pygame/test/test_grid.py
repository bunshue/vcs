#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test draw points, lines and polygons.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013, 2020-2021 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 5, 2021
"""

try:
    import simplegui  # pytype: disable=import-error

    SIMPLEGUICS2PYGAME = False
except ImportError:
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


TEST = 'test grid'

WIDTH = 400
HEIGHT = 300

SIZE = 80


STATE_COLORS = True
STATE_METHOD = 0


def draw(canvas):  # type: (simplegui.Canvas) -> None
    """
    Draw grid with 3 methods.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    """
    if STATE_COLORS:
        color1 = 'White'
        color2 = 'Gray'
        color3 = 'Yellow'
    else:
        color1 = color2 = color3 = 'White'

    if STATE_METHOD == 0:
        draw_grid1(canvas, 0, color1)
        draw_grid2(canvas, HEIGHT // 3, color2)
        draw_grid3(canvas, HEIGHT * 2 // 3, color3)
    elif STATE_METHOD == 1:
        draw_grid3(canvas, 0, color3)
        draw_grid1(canvas, HEIGHT // 3, color1)
        draw_grid2(canvas, HEIGHT * 2 // 3, color2)
    else:
        draw_grid2(canvas, 0, color2)
        draw_grid3(canvas, HEIGHT // 3, color3)
        draw_grid1(canvas, HEIGHT * 2 // 3, color1)


def draw_grid1(canvas, y_offset, color):
    # type: (simplegui.Canvas, int, str) -> None
    """
    Draw grid with points.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    :param y_offset: int >= 0
    :param color: str
    """
    text = 'points'
    width = FRAME.get_canvas_textwidth(text, SIZE)

    canvas.draw_text(text, ((WIDTH - width) // 2,
                            y_offset + (HEIGHT / 3 + SIZE / 4) / 2),
                     SIZE, color)

    for y in range(0, HEIGHT // 3, 20):
        y += y_offset
        for x in range(0, WIDTH):
            canvas.draw_point((x, y), color)

    for x in range(0, WIDTH, 40):
        for y in range(y_offset, y_offset + HEIGHT):
            canvas.draw_point((x, y), color)


def draw_grid2(canvas, y_offset, color):
    # type: (simplegui.Canvas, int, str) -> None
    """
    Draw grid with lines.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    :param y_offset: int >= 0
    :param color: str
    """
    text = 'lines'
    width = FRAME.get_canvas_textwidth(text, SIZE)

    canvas.draw_text(text, ((WIDTH - width) // 2,
                            y_offset + (HEIGHT / 3 + SIZE / 4) / 2),
                     SIZE, color)

    for y in range(0, HEIGHT // 3, 20):
        y += y_offset
        canvas.draw_line((0, y), (WIDTH - 1, y), 1, color)

    for x in range(0, WIDTH, 40):
        canvas.draw_line((x, y_offset), (x, y_offset + HEIGHT // 2 - 1),
                         1, color)


def draw_grid3(canvas, y_offset, color):
    # type: (simplegui.Canvas, int, str) -> None
    """
    Draw grid with polygons (rectangles).

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    :param y_offset: int >= 0
    :param color: str
    """
    text = 'rectangles'
    width = FRAME.get_canvas_textwidth(text, SIZE)

    canvas.draw_text(text, ((WIDTH - width) // 2,
                            y_offset + (HEIGHT / 3 + SIZE / 4) / 2),
                     SIZE, color)

    for y in range(0, HEIGHT // 3, 20):
        y += y_offset
        for x in range(0, WIDTH, 40):
            canvas.draw_polygon(((x, y), (x + 40, y),
                                 (x + 40, y + 20), (x, y + 20)),
                                1, color)


def switch_color():  # type: () -> None
    """Switch between 3 different colors and all in white."""
    global STATE_COLORS  # pylint: disable=global-statement

    STATE_COLORS = not STATE_COLORS


def switch_method():  # type: () -> None
    """Switch position of the 3 methods."""
    global STATE_METHOD  # pylint: disable=global-statement

    STATE_METHOD = (STATE_METHOD + 1) % 3


# Main
FRAME = simplegui.create_frame(TEST, WIDTH, HEIGHT)

FRAME.add_label(TEST)
FRAME.add_label('')
FRAME.add_label(PYTHON_VERSION)
FRAME.add_label(GUI_VERSION)
FRAME.add_label(PYGAME_VERSION)
FRAME.add_label('')
FRAME.add_button('Switch color', switch_color)
FRAME.add_button('Switch method', switch_method)
FRAME.add_label('')
FRAME.add_button('Quit', FRAME.stop)

FRAME.set_draw_handler(draw)

if SIMPLEGUICS2PYGAME:
    from sys import argv

    if len(argv) == 2:
        FRAME._save_canvas_and_stop(argv[1])  # pylint: disable=protected-access  # noqa


FRAME.start()
