#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test __repr__() et __str__() methods of objects.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013, 2015, 2020-2021 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 5, 2021
"""

try:
    import user305_SXBsmszNiUxIeoV as codeskulptor_lib  # pytype: disable=import-error  # noqa

    import simplegui  # pytype: disable=import-error

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore

    SIMPLEGUICS2PYGAME = True

    simplegui.Frame._hide_status = True  # pylint: disable=protected-access


if SIMPLEGUICS2PYGAME:
    from sys import version as python_version
    from SimpleGUICS2Pygame import _VERSION as GUI_VERSION
    from SimpleGUICS2Pygame.simpleguics2pygame import _PYGAME_VERSION  # pytype: disable=import-error  # pylint: disable=no-name-in-module  # noqa

    PYTHON_VERSION = 'Python ' + python_version.split()[0]
    PYGAME_VERSION = 'Pygame ' + str(_PYGAME_VERSION)
    GUI_VERSION = 'SimpleGUICS2Pygame ' + GUI_VERSION
else:
    PYTHON_VERSION = ('CodeSkulptor' +  # https://py2.codeskulptor.org/ or https://py3.codeskulptor.org/  # noqa
                      (' 2' if codeskulptor_lib.codeskulptor_version() == 2
                       else '3'))
    PYGAME_VERSION = ''
    GUI_VERSION = 'simplegui'


TEST = 'test objects'


def draw(canvas):  # type: (simplegui.Canvas) -> None
    """
    Print str representation of each SimpleGUI object.

    :param canvas: simpleguics2pygame.Canvas or simplegui.Canvas
    """
    image = simplegui.load_image('')
    sound = simplegui.load_sound('')
    timer = simplegui.create_timer(1000, lambda: None)
    timer.stop()

    for name, obj in (('button', BUTTON),
                      ('canvas', canvas),
                      ('frame', FRAME),
                      ('image', image),
                      ('input', INPUT),
                      ('label', LABEL),
                      ('sound', sound),
                      ('timer', timer)):
        print(name + str(type(obj)) + repr(obj) + str(obj))

    from sys import argv  # pylint: disable=import-outside-toplevel

    if len(argv) == 2:
        FRAME.stop()

    FRAME.set_draw_handler(lambda canvas: None)


# Main
FRAME = simplegui.create_frame(TEST, 0, 400, 400)

FRAME.add_label(TEST)
FRAME.add_label('')
FRAME.add_label(PYTHON_VERSION)
FRAME.add_label(GUI_VERSION)
FRAME.add_label(PYGAME_VERSION)

LABEL = FRAME.add_label('label')
BUTTON = FRAME.add_button('button', lambda: None)
INPUT = FRAME.add_input('input', lambda text: None, 50)

FRAME.set_draw_handler(draw)

FRAME.start()
