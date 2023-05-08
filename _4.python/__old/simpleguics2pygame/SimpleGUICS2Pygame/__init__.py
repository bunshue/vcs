# -*- coding: latin-1 -*-

"""
SimpleGUICS2Pygame package.

It is primarily a standard Python_ (**2 and 3**) module
reimplementing the SimpleGUI particular module of CodeSkulptor2_ and CodeSkulptor3_
(a Python browser environment).
This is in fact a package also with other modules adapted from CodeSkulptor.

Require Pygame_
(except for the Timer class)
(and must be installed separately).

Module simpleplot require matplotlib_ .


`Online HTML documentation`_ on Read The Docs.

| Sources and installers on Bitbucket: https://bitbucket.org/OPiMedia/simpleguics2pygame
| and on PyPI: https://pypi.org/project/SimpleGUICS2Pygame/ .

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

.. _CodeSkulptor2: https://py2.codeskulptor.org/
.. _CodeSkulptor3: https://py3.codeskulptor.org/
.. _matplotlib: https://matplotlib.org/
.. _`Online HTML documentation`: https://simpleguics2pygame.readthedocs.io/
.. _Pygame: https://www.pygame.org/
.. _Python: https://www.python.org/

:license: GPLv3 --- Copyright (C) 2013-2016, 2018, 2020-2021 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 4, 2021

* v.2.1.1 --- May 4, 2021
* v.2.1.0 --- November 29, 2020
* v.2.0.3 --- October 2, 2020
* v.2.0.2 --- May 23, 2020
* v.2.0.1 --- May 21, 2020
* v.2.0.0 --- April 18, 2020
* v.01.09.00 --- January 1st, 2015
* v.01.08.01 --- October 9, 2014
* v.01.08.00 --- October 4, 2014
* v.01.07.00 --- September 2, 2014
* v.01.06.03 --- July 24, 2014
* v.01.06.02 --- July 18, 2014
* v.01.06.01 --- July 17, 2014
* v.01.06.00 --- June 16, 2014
* v.01.05.00 --- May 25, 2014
* v.01.04.00 --- December 16, 2013
* v.01.03.00 --- December 13, 2013
* v.01.02.00 --- November 8, 2013
* v.01.01.00 --- November 1st, 2013
* v.01.00.02 --- October 31, 2013
* v.01.00.01 --- October 9, 2013
* v.01.00.00 --- July 13, 2013
* v.00.92.00 --- June 27, 2013
* v.00.91.00 --- June 23, 2013
* v.00.90.10 --- June 19, 2013
* v.00.90.00 --- June 13, 2013
* Started on May 21, 2013

`Complete changelog`_

.. _`Complete changelog`: https://simpleguics2pygame.readthedocs.io/en/latest/ChangeLog.html
"""  # noqa

from __future__ import print_function

# print('IMPORT', __name__)


_VERSION = '2.1.1'
"""Version of SimpleGUICS2Pygame package."""

_WEBSITE = 'https://bitbucket.org/OPiMedia/simpleguics2pygame/'
"""Website of the project."""

_WEBSITE_DOC = 'https://simpleguics2pygame.readthedocs.io/'
"""Website of the documentation."""


#
# GPLv3
# ------
# Copyright (C) 2013-2016, 2018, 2020-2021 Olivier Pirson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
