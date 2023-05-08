#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test draw buttons and labels in control panel.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2014, 2020-2021 Olivier Pirson
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


TEST = 'test button and label'


def button_handler():  # type: () -> None
    """Simple button handler function."""
    print('clic')


#
# Main
######
def main():  # type: () -> None
    """Create and start frame."""
    frame = simplegui.create_frame(TEST, 0, 850, 250)

    frame.add_label(TEST)
    frame.add_label('')
    frame.add_label(PYTHON_VERSION)
    frame.add_label(GUI_VERSION)
    frame.add_label(PYGAME_VERSION)
    frame.add_label('')
    frame.add_button('Quit', frame.stop)
    frame.add_label('')

    # Buttons
    frame.add_button('add_button()', button_handler)
    frame.add_button('add_button(, 200)', button_handler, 200)
    frame.add_button('add_button(, 50)', button_handler, 50)
    frame.add_button('add_button(, 30)', button_handler, 30)
    frame.add_button('add_button(, 0)', button_handler, 0)

    frame.add_button('', button_handler)
    frame.add_button('', button_handler, 50)

    frame.add_button('a b c', button_handler, 50)
    frame.add_button('a b c', button_handler, 40)

    # Labels
    frame.add_label('add_label()')
    frame.add_label('add_label(, 200)', 200)
    frame.add_label('add_label(, 50)', 50)
    frame.add_label('add_label(, 30)', 30)
    frame.add_label('add_label(, 0)', 0)

    frame.add_label('')
    frame.add_label('', 50)

    frame.add_label('a b c', 30)
    frame.add_label('a b c', 25)

    frame.start()


if __name__ == '__main__':
    main()
