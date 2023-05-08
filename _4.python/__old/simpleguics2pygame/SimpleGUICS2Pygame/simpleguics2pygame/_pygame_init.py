# -*- coding: latin-1 -*-

"""
simpleguics2pygame module: simpleguics2pygame/_pygame_init.

Initialize Pygame.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2015, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: November 29, 2020
"""

from __future__ import print_function

# print('IMPORT', __name__)


__all__ = ('_PYGAME_AVAILABLE', '_PYGAME_VERSION')


try:
    from pygame.version import ver as _PYGAME_VERSION

    _PYGAME_AVAILABLE = True
    """
    Always `True`. (Variable kept for backward compatibility.)
    """
except ImportError:
    import sys

    print("""Pygame not available!
See https://simpleguics2pygame.readthedocs.io/en/latest/#installation""",
          file=sys.stderr)

    sys.exit(1)


#
# Init Pygame
#############
import pygame
import pygame.font
import pygame.mixer
import pygame.transform

pygame.display.init()
pygame.font.init()
