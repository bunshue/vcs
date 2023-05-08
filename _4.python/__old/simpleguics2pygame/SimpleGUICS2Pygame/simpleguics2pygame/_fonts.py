# -*- coding: latin-1 -*-

"""
simpleguics2pygame module: simpleguics2pygame/_fonts.

Fonts helpers.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2015, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: November 29, 2020
"""

from __future__ import print_function

# print('IMPORT', __name__)


__all__ = tuple()  # type: tuple


try:
    from typing import Dict, Optional, Tuple
except ImportError:
    pass

import pygame

from SimpleGUICS2Pygame.simpleguics2pygame._arguments import _CONFIG  # pylint: disable=no-name-in-module  # noqa


#
# Private global constant
#########################
_SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME = {
    'monospace': 'courier,couriernew',
    'sans-serif': 'arial,tahoma',
    'serif': 'timesnewroman,garamond,georgia'}
"""
Font faces using by SimpleGUI
to corresponding font names list used by Pygame.

**(Not available in SimpleGUI of CodeSkulptor.)**
"""


#
# Private global variables
##########################
__PYGAMEFONTS_CACHED = dict()  # type: Dict[Tuple[Optional[str], int], pygame.font.Font]  # noqa
"""
`Dict` {(`str` CodeSkulptor font face, `int` font size):
        `pygame.font.Font`}.

**(Not available in SimpleGUI of CodeSkulptor.)**
"""

_DEFAULT_FONT = _CONFIG['--default-font']
"""
If `True`
then use Pygame default font instead serif, monospace...

**(Not available in SimpleGUI of CodeSkulptor.)**
"""


#
# "Private" function
####################
def _simpleguifontface_to_pygamefont(font_face, font_size):  # pylint: disable=invalid-name  # noqa
    # type: (Optional[str], int) -> pygame.font.Font
    """
    Return a `pygame.font.Font` object
    corresponding to the SimpleGUI `font_face` name
    by using the `_SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME` dictionary.

    If font_face is None or the correponding font is not founded,
    then use the default `pygame.font.Font`.

    **(Not available in SimpleGUI of CodeSkulptor.)**

    Side effect:
    Each new font with new size is added to `__PYGAMEFONTS_CACHED`.
    See `Frame._pygamefonts_cached_clear()`.

    .. _`Frame._pygamefonts_cached_clear()`: frame.html#SimpleGUICS2Pygame.simpleguics2pygame.frame.Frame._pygamefonts_cached_clear

    :param font_face: None
                      or (str == key of _SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME)
    :param font_size: int > 0

    :return: pygame.font.Font
    """  # noqa
    font = __PYGAMEFONTS_CACHED.get((font_face, font_size))

    if font is None:
        assert ((font_face is None) or
                ((isinstance(font_face, str) and
                  (font_face in _SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME)))), \
            font_face
        assert isinstance(font_size, int), type(font_size)
        assert font_size > 0, font_size

        if (font_face is None) or _DEFAULT_FONT:  # pylint: disable=protected-access  # noqa
            font = pygame.font.SysFont(None, font_size)  # type: ignore
        else:
            try:
                font = pygame.font.SysFont(
                    _SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME[font_face],
                    font_size)
            except Exception:  # pylint: disable=broad-except
                font = pygame.font.SysFont(None, font_size)  # type: ignore

        assert font is not None

        __PYGAMEFONTS_CACHED[(font_face, font_size)] = font

    return font
