# -*- coding: latin-1 -*-

"""
simpleguics2pygame module: simpleguics2pygame/keys.

Keys helpers.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2015, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: November 29, 2020
"""

from __future__ import print_function

# print('IMPORT', __name__)


import pygame.locals


__all__ = ('KEY_MAP', )


#
# Global constant
#################
KEY_MAP = {'space': 32,
           'left': 37,
           'up': 38,
           'right': 39,
           'down': 40,
           '0': 48,
           '1': 49,
           '2': 50,
           '3': 51,
           '4': 52,
           '5': 53,
           '6': 54,
           '7': 55,
           '8': 56,
           '9': 57,
           'A': 65,
           'B': 66,
           'C': 67,
           'D': 68,
           'E': 69,
           'F': 70,
           'G': 71,
           'H': 72,
           'I': 73,
           'J': 74,
           'K': 75,
           'L': 76,
           'M': 77,
           'N': 78,
           'O': 79,
           'P': 80,
           'Q': 81,
           'R': 82,
           'S': 83,
           'T': 84,
           'U': 85,
           'V': 86,
           'W': 87,
           'X': 88,
           'Y': 89,
           'Z': 90,
           'a': 65,
           'b': 66,
           'c': 67,
           'd': 68,
           'e': 69,
           'f': 70,
           'g': 71,
           'h': 72,
           'i': 73,
           'j': 74,
           'k': 75,
           'l': 76,
           'm': 77,
           'n': 78,
           'o': 79,
           'p': 80,
           'q': 81,
           'r': 82,
           's': 83,
           't': 84,
           'u': 85,
           'v': 86,
           'w': 87,
           'x': 88,
           'y': 89,
           'z': 90}
"""
SimpleGUI keyboard characters contants.
"""


#
# Private global constants
##########################
__PYGAMEKEY_TO_SIMPLEGUIKEY = {pygame.locals.K_SPACE: KEY_MAP['space'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_UP: KEY_MAP['up'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_DOWN: KEY_MAP['down'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_RIGHT: KEY_MAP['right'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_LEFT: KEY_MAP['left'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_LSHIFT: 17,  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_RSHIFT: 17,  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_LCTRL: 16,  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_RCTRL: 16,  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_LALT: 18,  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_RALT: 18,  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_0: KEY_MAP['0'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_1: KEY_MAP['1'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_2: KEY_MAP['2'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_3: KEY_MAP['3'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_4: KEY_MAP['4'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_5: KEY_MAP['5'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_6: KEY_MAP['6'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_7: KEY_MAP['7'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_8: KEY_MAP['8'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_9: KEY_MAP['9'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_KP0: KEY_MAP['0'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_KP1: KEY_MAP['1'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_KP2: KEY_MAP['2'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_KP3: KEY_MAP['3'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_KP4: KEY_MAP['4'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_KP5: KEY_MAP['5'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_KP6: KEY_MAP['6'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_KP7: KEY_MAP['7'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_KP8: KEY_MAP['8'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_KP9: KEY_MAP['9'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_a: KEY_MAP['A'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_b: KEY_MAP['B'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_c: KEY_MAP['C'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_d: KEY_MAP['D'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_e: KEY_MAP['E'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_f: KEY_MAP['F'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_g: KEY_MAP['G'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_h: KEY_MAP['H'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_i: KEY_MAP['I'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_j: KEY_MAP['J'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_k: KEY_MAP['K'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_l: KEY_MAP['L'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_m: KEY_MAP['M'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_n: KEY_MAP['N'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_o: KEY_MAP['O'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_p: KEY_MAP['P'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_q: KEY_MAP['Q'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_r: KEY_MAP['R'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_s: KEY_MAP['S'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_t: KEY_MAP['T'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_u: KEY_MAP['U'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_v: KEY_MAP['V'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_w: KEY_MAP['W'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_x: KEY_MAP['X'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_y: KEY_MAP['Y'],  # type: ignore  # pylint: disable=no-member  # noqa
                               pygame.locals.K_z: KEY_MAP['Z']}  # type: ignore  # pylint: disable=no-member  # noqa
"""
`Dict` {`int` Pygame key code : corresponding `int` SimpleGUI key code}.

**(Not available in SimpleGUI of CodeSkulptor.)**
"""


_SIMPLEGUIKEY_TO_STATUSKEY = {32: 'space',
                              37: 'Left',
                              38: 'Up',
                              39: 'Right',
                              40: 'Down',
                              48: '0',
                              49: '1',
                              50: '2',
                              51: '3',
                              52: '4',
                              53: '5',
                              54: '6',
                              55: '7',
                              56: '8',
                              57: '9',
                              65: 'a',
                              66: 'b',
                              67: 'c',
                              68: 'd',
                              69: 'e',
                              70: 'f',
                              71: 'g',
                              72: 'h',
                              73: 'i',
                              74: 'j',
                              75: 'k',
                              76: 'l',
                              77: 'm',
                              78: 'n',
                              79: 'o',
                              80: 'p',
                              81: 'q',
                              82: 'r',
                              83: 's',
                              84: 't',
                              85: 'u',
                              86: 'v',
                              87: 'w',
                              88: 'x',
                              89: 'y',
                              90: 'z'}
"""
`Dict` {`int` SimpleGUI key code : corresponding `str` status key}.

**(Not available in SimpleGUI of CodeSkulptor.)**
"""


#
# "Private" function
####################
def _pygamekey_to_simpleguikey(key):  # type: (int) -> int
    """
    Return the code use by SimpleGUI to representing
    the `key` expressed by Pygame.

    If `key` not in `__PYGAMEKEY_TO_SIMPLEGUIKEY`
    then return `key`.

    **(Not available in SimpleGUI of CodeSkulptor.)**

    :param key: int >= 0

    :return: int >= 0
    """
    assert isinstance(key, int), type(key)
    assert key >= 0, key

    return __PYGAMEKEY_TO_SIMPLEGUIKEY.get(key, key)
