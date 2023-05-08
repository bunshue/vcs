# -*- coding: latin-1 -*-

"""
simpleguics2pygame module: simpleguics2pygame/__init__.

Standard Python_ (**2 and 3**) module
reimplementing the SimpleGUI particular module of CodeSkulptor2_ and CodeSkulptor3_
(a Python browser environment).

Require Pygame_
(except for the Timer class).

`Online HTML documentation`_ on Read The Docs.
(You can also see the online `SimpleGUI documentation on CodeSkulptor2`_
or `SimpleGUI documentation on CodeSkulptor3`_.)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

.. _CodeSkulptor2: https://py2.codeskulptor.org/
.. _CodeSkulptor3: https://py3.codeskulptor.org/
.. _`Online HTML documentation`: https://simpleguics2pygame.readthedocs.io/
.. _Pygame: https://www.pygame.org/
.. _Python: https://www.python.org/
.. _`SimpleGUI documentation on CodeSkulptor2`: https://py2.codeskulptor.org/docs.html#simplegui-create_frame
.. _`SimpleGUI documentation on CodeSkulptor3`: https://py3.codeskulptor.org/docs.html#simplegui-create_frame

:license: GPLv3 --- Copyright (C) 2013-2016, 2020-2021 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 5, 2021
"""  # noqa

from __future__ import print_function

# print('IMPORT', __name__)


import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

if 'os' in dir():
    del os


#
# Set arguments
###############
import SimpleGUICS2Pygame.simpleguics2pygame._arguments  # pylint: disable=wrong-import-position,no-name-in-module  # noqa

if '_arguments' in dir():
    del _arguments  # type: ignore  # pylint: disable=undefined-variable


#
# Import timer (Pygame is not required)
#######################################
from SimpleGUICS2Pygame.simpleguics2pygame.timer import *  # pylint: disable=wildcard-import,wrong-import-position,no-name-in-module  # noqa

if 'timer' in dir():
    del timer  # type: ignore  # pylint: disable=undefined-variable


#
# Init Pygame
#############
from SimpleGUICS2Pygame.simpleguics2pygame._pygame_init import *  # pylint: disable=no-name-in-module,wildcard-import,wrong-import-position  # noqa

if '_pygame_init' in dir():
    del _pygame_init  # type: ignore  # pylint: disable=undefined-variable


#
# Import all others (Pygame is required)
########################################
from SimpleGUICS2Pygame.simpleguics2pygame.keys import *  # pylint: disable=wildcard-import,wrong-import-position,no-name-in-module  # noqa

if 'keys' in dir():
    del keys  # type: ignore  # pylint: disable=undefined-variable

from SimpleGUICS2Pygame.simpleguics2pygame.control import *  # pylint: disable=wildcard-import,wrong-import-position,no-name-in-module  # noqa

if 'control' in dir():
    del control  # type: ignore  # pylint: disable=undefined-variable


from SimpleGUICS2Pygame.simpleguics2pygame.image import *  # pylint: disable=wildcard-import,wrong-import-position,no-name-in-module  # noqa

if 'image' in dir():
    del image  # type: ignore  # pylint: disable=undefined-variable

from SimpleGUICS2Pygame.simpleguics2pygame.sound import *  # pylint: disable=wildcard-import,wrong-import-position,no-name-in-module  # noqa

if 'sound' in dir():
    del sound  # type: ignore  # pylint: disable=undefined-variable


from SimpleGUICS2Pygame.simpleguics2pygame.canvas import *  # pylint: disable=wildcard-import,wrong-import-position,no-name-in-module  # noqa

if 'canvas' in dir():
    del canvas  # type: ignore  # pylint: disable=undefined-variable

from SimpleGUICS2Pygame.simpleguics2pygame.frame import *  # pylint: disable=wildcard-import,wrong-import-position,no-name-in-module  # noqa

if 'frame' in dir():
    del frame  # type: ignore  # pylint: disable=undefined-variable


#
# Clean
#######
if 'SimpleGUICS2Pygame' in dir():
    del SimpleGUICS2Pygame
