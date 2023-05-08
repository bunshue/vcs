#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test colors HTML in rgba() format.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2014, 2020-2021 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 5, 2021
"""

try:
    from user305_SXBsmszNiUxIeoV import rgba  # pytype: disable=import-error

    import simplegui  # pytype: disable=import-error

    SIMPLEGUICS2PYGAME = False
except ImportError:
    from SimpleGUICS2Pygame.codeskulptor_lib import rgba

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


TEST = 'test colors HTML rgba()'

WIDTH = 512
HEIGHT = 410

STATE_TRANSPARENCY = True


def draw(canvas):  # type: (simplegui.Canvas) -> None
    """
    Draw (with draw_line()) range of colors
    in rgba(red, blue, green, alpha) format.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    """
    for i in range(256):  # Format rgba(red, blue, green, alpha)
        for a in range(10):
            canvas.draw_line((i * 2, 10 + a * 10),
                             ((i + 1) * 2, 10 + a * 10), 10,
                             rgba(i, i, i, (a / 10.0 if STATE_TRANSPARENCY
                                            else 1)))

        for a in range(10):
            canvas.draw_line((i * 2, 110 + a * 10),
                             ((i + 1) * 2, 110 + a * 10), 10,
                             rgba(i, 0, 0, (a / 10.0 if STATE_TRANSPARENCY
                                            else 1)))

        for a in range(10):
            canvas.draw_line((i * 2, 210 + a * 10),
                             ((i + 1) * 2, 210 + a * 10), 10,
                             rgba(0, i, 0, (a / 10.0 if STATE_TRANSPARENCY
                                            else 1)))

        for a in range(10):
            canvas.draw_line((i * 2, 310 + a * 10),
                             ((i + 1) * 2, 310 + a * 10), 10,
                             rgba(0, 0, i, (a / 10.0 if STATE_TRANSPARENCY
                                            else 1)))


def switch_transparency():  # type: () -> None
    """Switch between transparency mode and opaque mode."""
    global STATE_TRANSPARENCY  # pylint: disable=global-statement

    STATE_TRANSPARENCY = not STATE_TRANSPARENCY


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
    frame.add_button('Switch transparency', switch_transparency)
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
