#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test input dealing in control panel.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2015, 2020-2021 Olivier Pirson
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


TEST = 'test input'


INPUT_1 = ''
INPUT_2 = ''


def input_1_handler(text):  # type: (str) -> None
    """Simple input handler function."""
    global INPUT_1  # pylint: disable=global-statement

    INPUT_1 = text
    print('|' + INPUT_1 + '|')
    print('.' + INPUT_2 + '.')


def input_2_handler(text):  # type: (str) -> None
    """Simple input handler function."""
    global INPUT_2  # pylint: disable=global-statement

    INPUT_2 = text
    print('|' + INPUT_1 + '|')
    print('.' + INPUT_2 + '.')


#
# Main
######
def main():  # type: () -> None
    """Create and start frame."""
    frame = simplegui.create_frame(TEST, 0, 400, 400)

    frame.add_label(TEST)
    frame.add_label('')
    frame.add_label(PYTHON_VERSION)
    frame.add_label(GUI_VERSION)
    frame.add_label(PYGAME_VERSION)
    frame.add_label('')
    frame.add_button('Quit', frame.stop)
    frame.add_label('')

    # Buttons
    frame.add_input('Input 1:', input_1_handler, 400)
    frame.add_input('Input 2:', input_2_handler, 400)

    frame.start()


if __name__ == '__main__':
    main()
