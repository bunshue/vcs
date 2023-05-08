#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test draw arcs.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2020-2021 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 5, 2021
"""

import math

try:
    import simplegui  # pytype: disable=import-error

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore

    SIMPLEGUICS2PYGAME = True

    simplegui.Frame._hide_status = True  # pylint: disable=protected-access

if SIMPLEGUICS2PYGAME:
    try:
        from typing import Union
    except ImportError:
        pass

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

TEST = 'test arc'

WIDTH = 400
HEIGHT = 200


def draw(canvas):  # type: (simplegui.Canvas) -> None
    """
    Draw concentric arcs.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    """
    x = WIDTH // 3
    y = HEIGHT // 2

    line_width = 11

    for radius in range(1, WIDTH, 20):
        start_angle = radius // 20  # type: Union[int, float]
        end_angle = radius // 20 + math.pi
        canvas.draw_arc((WIDTH - 1 - x, y), radius,
                        start_angle, end_angle, line_width,
                        'rgba(0,255,0,.5)')
        canvas.draw_arc((WIDTH - 1 - x, y), radius,
                        start_angle, end_angle, 1, 'Lime')

    for radius in range(1, WIDTH, 20):
        start_angle = radius // 20 + math.pi / 2
        end_angle = radius // 20
        canvas.draw_arc((x, y), radius,
                        start_angle, end_angle, line_width, 'rgba(255,0,0,.5)')
        canvas.draw_arc((x, y), radius,
                        start_angle, end_angle, 1, 'Red')

    canvas.draw_circle((50, 50), 40, 10, 'Orange')
    canvas.draw_circle((110, 50), 40, 10, 'rgba(255,155,0,.5)')

    canvas.draw_circle((50, 110), 40, 5, 'rgba(0,155,255,.5)', 'Blue')
    canvas.draw_circle((110, 110), 40, 5, 'Aqua', 'rgba(0,255,255,.5)')

    canvas.draw_arc((50, 50), 30, 0, math.pi, 10, 'Fuchsia')
    canvas.draw_arc((50, 50), 30, math.pi * 5 / 4, math.pi * 7 / 4, 10, 'Red')
    canvas.draw_arc((110, 50), 30, math.pi, math.pi * 5 / 2, 10,
                    'rgba(255,0,255,.5)')

    canvas.draw_arc((50, 110), 20, 0, 1, 10, 'rgba(255,0,0,.5)')
    canvas.draw_arc((110, 110), 20, 1, 0, 10, 'rgba(255,0,0,.5)')


#
# Main
######
def main():  # type: () -> None
    """Create and start frame."""
    frame = simplegui.create_frame(TEST, WIDTH, HEIGHT)

    frame.add_label(TEST)
    frame.add_label('')
    frame.add_label(PYTHON_VERSION)
    frame.add_label(GUI_VERSION)
    frame.add_label(PYGAME_VERSION)
    frame.add_label('')
    frame.add_button('Quit', frame.stop)

    frame.set_draw_handler(draw)

    if SIMPLEGUICS2PYGAME:
        from sys import argv  # pylint: disable=import-outside-toplevel

        if len(argv) == 2:
            frame._save_canvas_and_stop(argv[1])  # pylint: disable=protected-access  # noqa

    frame.start()


if __name__ == '__main__':
    main()
