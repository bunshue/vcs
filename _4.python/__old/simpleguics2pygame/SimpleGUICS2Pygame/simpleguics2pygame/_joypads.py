# -*- coding: latin-1 -*-

"""
simpleguics2pygame module: simpleguics2pygame/_joypads.

Dealing of joypads.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: November 29, 2020
"""

from __future__ import print_function

# print('IMPORT', __name__)


import os.path
import sys

import pygame
import pygame.joystick

pygame.joystick.init()


__all__ = tuple()  # type: tuple


#
# Private global constants
##########################
if not os.path.basename(sys.argv[0]).startswith('sphinx-build'):
    __PYGAME_JOYPADS = tuple(pygame.joystick.Joystick(i)
                             for i in range(pygame.joystick.get_count()))
else:
    __PYGAME_JOYPADS = tuple()
    """
    Tuple of all Pygame joypads found.

    **(Not available in SimpleGUI of CodeSkulptor.)**
    """


# Initialize each joypad
tuple(joypad.init() for joypad in __PYGAME_JOYPADS)  # type: ignore


_joypad_nb = len(__PYGAME_JOYPADS)  # pylint: disable=invalid-name
"""
Number of available joypads.

**(Not available in SimpleGUI of CodeSkulptor.)**
"""
