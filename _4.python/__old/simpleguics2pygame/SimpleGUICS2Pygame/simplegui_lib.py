# -*- coding: latin-1 -*-

"""
simplegui_lib module.

Some functions and classes to help
in SimpleGUI of CodeSkulptor,
from `simplegui_lib_draw`,
`simplegui_lib_fps`,
`simplegui_lib_keys`
and `simplegui_lib_loader`.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2015, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 21, 2020
"""

# print('IMPORT', __name__)


try:
    from user305_SaT1YKoOikl4ax9 import draw_rect, draw_text_multi, draw_text_side  # pytype: disable=import-error  # pylint: disable=unused-import  # noqa
    from user305_tXfH4AcbNLtjfHy import FPS  # pytype: disable=import-error  # pylint: disable=unused-import  # noqa
    from user305_EtIUDiM87dN1mD2 import Keys  # pytype: disable=import-error  # pylint: disable=unused-import  # noqa
    from user305_SZPJfNxJlVTjbAy import Loader  # pytype: disable=import-error  # pylint: disable=unused-import  # noqa
except ImportError:
    from SimpleGUICS2Pygame.simplegui_lib_draw import draw_rect, draw_text_multi, draw_text_side  # noqa
    from SimpleGUICS2Pygame.simplegui_lib_fps import FPS
    from SimpleGUICS2Pygame.simplegui_lib_keys import Keys
    from SimpleGUICS2Pygame.simplegui_lib_loader import Loader
