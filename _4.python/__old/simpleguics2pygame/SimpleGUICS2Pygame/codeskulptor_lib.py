# -*- coding: latin-1 -*-

"""
codeskulptor_lib module.

Some miscellaneous functions to help in CodeSkulptor.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2014, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 19, 2020
"""

# print('IMPORT', __name__)


try:
    from typing import Union
except ImportError:
    pass


# Private global variables
##########################
__CODESKULPTOR_IS = None
"""
Used to memoization by codeskulptor_is().
"""


__CODESKULPTOR_VERSION = None
"""
Used to memoization by codeskulptor_version().
"""


# Functions
###########
def assert_position(position, non_negative=False, non_zero=False):
    # type: (Union[int, float], bool, bool) -> None
    """
    Assertions to check valid `position`.

    If non_negative
    then each `int` or `float` must be >= 0.

    If non_zero
    then each `int` or `float` must be != 0.

    :param position: (int or float, int or float) or [int or float, int or float]
    :param non_negative: bool
    """  # noqa
    assert isinstance(non_negative, bool), type(non_negative)
    assert isinstance(non_zero, bool), type(non_zero)

    assert isinstance(position, (tuple, list)), type(position)
    assert len(position) == 2, len(position)

    assert isinstance(position[0], (int, float)), type(position[0])
    assert isinstance(position[1], (int, float)), type(position[1])

    if non_negative:
        assert position[0] >= 0, position
        assert position[1] >= 0, position

    if non_zero:
        assert position[0] != 0, position
        assert position[1] != 0, position


def codeskulptor_is():  # type: () -> bool
    """
    If run in CodeSkulptor environment
    then return `True`,
    else return `False`.

    :return: bool
    """
    # CodeSkulptor require global in top of function
    global __CODESKULPTOR_IS  # pylint: disable=global-statement

    if __CODESKULPTOR_IS is None:
        try:
            # Try import to check if running in CodeSkulptor environment
            from codeskulptor import file2url  # pytype: disable=import-error  # pylint: disable=import-outside-toplevel,unused-import  # noqa
            from simplegui import KEY_MAP  # pytype: disable=import-error  # pylint: disable=import-outside-toplevel,unused-import  # noqa

            __CODESKULPTOR_IS = True
        except ImportError:
            __CODESKULPTOR_IS = False

    return __CODESKULPTOR_IS


def codeskulptor_version():  # type: () -> Union[bool, int]
    """
    If run in CodeSkulptor environment
    then return 2 if CodeSkulptor or 3 if CodeSkulptor3
    else return `False`.

    :return: False, 2 or 3
    """
    # CodeSkulptor require global in top of function
    global __CODESKULPTOR_VERSION  # pylint: disable=global-statement

    if __CODESKULPTOR_VERSION is None:
        if codeskulptor_is():
            try:
                # Try import to check if running in CodeSkulptor version 2
                from urllib2 import urlopen  # pytype: disable=import-error  # pylint: disable=import-outside-toplevel,unused-import  # noqa

                __CODESKULPTOR_VERSION = 2
            except ImportError:
                __CODESKULPTOR_VERSION = 3
        else:
            __CODESKULPTOR_VERSION = False

    return __CODESKULPTOR_VERSION


def hex2(n, uppercase=True):  # pylint: disable=invalid-name
    # type: (int, bool) -> str
    """
    Return 2 characters corresponding to the hexadecimal representation of `n`.

    :param n: 0 <= int < 256
    :param uppercase: bool

    :return: str (length == 2)
    """
    assert isinstance(n, int)
    assert 0 <= n < 256
    assert isinstance(uppercase, bool), type(uppercase)

    return hex_fig(n // 16) + hex_fig(n % 16)


def hex_fig(n, uppercase=True):  # pylint: disable=invalid-name
    # type: (int, bool) -> str
    """
    Return the hexadecimal figure of `n`.

    :param n: 0 <= int < 16
    :param uppercase: bool

    :return: str (one character from 0123456789ABCDEF or 0123456789abcdef)
    """
    assert isinstance(n, int), type(n)
    assert 0 <= n < 16
    assert isinstance(uppercase, bool), type(uppercase)

    return (str(n) if n < 10
            else chr((ord('A' if uppercase
                          else 'a') + n - 10)))


def hsl(hue, saturation, lightness):
    # type: (Union[int, float], Union[int, float], Union[int, float]) -> str
    """
    Return the string HTML representation of the color
    in 'hsl(hue, lightness, saturation)' format.

    :param hue: float or int
    :param saturation: 0 <= float or int <= 100
    :param lightness: 0 <= float or int <= 100

    :return: str
    """
    assert isinstance(hue, (float, int))

    assert isinstance(saturation, (float, int))
    assert 0 <= saturation <= 100

    assert isinstance(lightness, (float, int))
    assert 0 <= lightness <= 100

    # %s to avoid CodeSkulptor %% bug
    return 'hsla(%d, %d%s, %d%s)' % (hue % 360,
                                     saturation, '%',
                                     lightness, '%')


def hsla(hue, saturation, lightness, alpha=1):
    # type: (Union[int, float], Union[int, float], Union[int, float], Union[int, float]) -> str  # noqa
    """
    Return the string HTML representation of the color
    in 'hsla(hue, lightness, saturation, alpha)' format.

    :param hue: float or int
    :param saturation: 0 <= float or int <= 100
    :param lightness: 0 <= float or int <= 100
    :param alpha: 0 <= float or int <= 1

    :return: str
    """
    assert isinstance(hue, (float, int))

    assert isinstance(saturation, (float, int))
    assert 0 <= saturation <= 100

    assert isinstance(lightness, (float, int))
    assert 0 <= lightness <= 100

    assert isinstance(alpha, (float, int))
    assert 0 <= alpha <= 1

    # %s to avoid CodeSkulptor %% bug
    return 'hsla(%d, %d%s, %d%s, %f)' % (hue % 360,
                                         saturation, '%',
                                         lightness, '%',
                                         alpha)


def rgb(red, green, blue):  # type: (int, int, int) -> str
    """
    Return the string HTML representation of the color
    in 'rgb(red, blue, green)' format.

    :param red:   0 <= int <= 255
    :param green: 0 <= int <= 255
    :param blue:  0 <= int <= 255

    :return: str
    """
    assert isinstance(red, int)
    assert 0 <= red < 256

    assert isinstance(green, int)
    assert 0 <= green < 256

    assert isinstance(blue, int)
    assert 0 <= blue < 256

    return 'rgba(%d, %d, %d)' % (red, green, blue)


def rgba(red, green, blue, alpha=1):
    # type: (int, int, int, Union[int, float]) -> str
    """
    Return the string HTML representation of the color
    in 'rgba(red, blue, green, alpha)' format.

    :param red:   0 <= int <= 255
    :param green: 0 <= int <= 255
    :param blue:  0 <= int <= 255
    :param alpha: 0 <= float or int <= 1

    :return: str
    """
    assert isinstance(red, int)
    assert 0 <= red < 256

    assert isinstance(green, int)
    assert 0 <= green < 256

    assert isinstance(blue, int)
    assert 0 <= blue < 256

    assert isinstance(alpha, (float, int))
    assert 0 <= alpha <= 1

    return 'rgba(%d, %d, %d, %f)' % (red, green, blue, alpha)
