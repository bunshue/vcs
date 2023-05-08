#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
script/pygame_check.py script.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2015, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: April 14, 2020
"""

from __future__ import print_function

import sys


########
# Main #
########
if __name__ == '__main__':
    print("""script/pygame_check.py (April 14, 2020)
=======================================""")

    # Python
    print('python - version', sys.version, end='\n\n')

    # Pygame
    CMD = 'import pygame'
    try:
        import pygame

        print(CMD, 'ok - Version', pygame.version.ver)

        CMD = 'pygame.init()'
        try:
            SUCCESS, FAILED = pygame.init()  # pylint: disable=no-member

            if FAILED == 0:
                print(' ', CMD, SUCCESS, 'modules loaded ok')
            else:
                print(' ', CMD, SUCCESS, 'modules loaded',
                      FAILED, 'failed WARNING!')
        except Exception as exc:  # pylint: disable=broad-except
            print(' ', CMD, 'FAILED!', exc)
    except Exception as exc:  # pylint: disable=broad-except
        print(CMD, 'FAILED!', exc)
