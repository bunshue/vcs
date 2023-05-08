#!/usr/bin/env python
# -*- coding: latin-1 -*-
# pylint: disable=invalid-name

"""
Mandelbrot Set simple computation.

See http://en.wikipedia.org/wiki/Mandelbrot_set#Computer_drawings .

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2014, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 21, 2020
"""

import math

try:
    from typing import List, Optional, Tuple
except ImportError:
    pass

try:
    from user305_SXBsmszNiUxIeoV import codeskulptor_is, hex2  # pytype: disable=import-error  # noqa

    import simplegui  # pytype: disable=import-error

    from codeskulptor import set_timeout  # pytype: disable=import-error

    set_timeout(10)
except ImportError:
    from SimpleGUICS2Pygame.codeskulptor_lib import codeskulptor_is, hex2

    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore

    simplegui.Frame._hide_status = True  # pylint: disable=protected-access


#
# Global constants
###################
# draw FPS average (only with SimpleGUICS2Pygame)
_FPS_AVERAGE = not codeskulptor_is()

CANVAS_WIDTH = 256
CANVAS_HEIGHT = 256


#
# Global variables
###################
COLORS = None  # type:  Optional[Tuple[str, ...]]

GRID = None  # type: Optional[List[List[List]]]

NB_ITER_MAX = 50
NB_ITER = 0

Z0_REAL = -2.0
Z0_IMAG = 1.5

Z1_REAL = 1.0
Z1_IMAG = -1.5


#
# Functions
############
def draw_and_calculate(canvas):  # pylint: disable=too-many-branches
    # type: (simplegui.Canvas) -> None
    """
    Draw and calculate image of Mandelbrot set from GRID.

    :param canvas: simplegui.Canvas
    """
    global NB_ITER  # pylint: disable=global-statement

    assert isinstance(COLORS, tuple)
    assert isinstance(GRID, list)

    print(NB_ITER)
    NB_ITER += 1

    for y, line in enumerate(GRID):
        contiguous_color = None
        contiguous_x0 = 0

        for x, point in enumerate(line):
            color = point[3]
            if color is None:
                z = point[0]

                z_real2 = z[0] * z[0]
                z_imag2 = z[1] * z[1]
                z_abs2 = z_real2 + z_imag2

                if z_abs2 > 4:
                    color = point[2] % len(COLORS)  # color
                    point[3] = color
                else:
                    color = None
                    c = point[1]
                    point[0] = (z_real2 - z_imag2 + c[0],  # z
                                z[0] * z[1] * 2 + c[1])
                    point[2] += 1  # number of iterations

            if contiguous_color != color:
                if contiguous_color is not None:
                    contiguous_color_str = COLORS[contiguous_color]
                    if contiguous_x0 + 1 == x:
                        canvas.draw_point((contiguous_x0, y),
                                          contiguous_color_str)
                        canvas.draw_point((contiguous_x0, CANVAS_HEIGHT - y),
                                          contiguous_color_str)
                    else:
                        draw_hline(canvas,
                                   contiguous_x0, x - 1, y,
                                   contiguous_color_str)
                        draw_hline(canvas,
                                   contiguous_x0, x - 1, CANVAS_HEIGHT - y,
                                   contiguous_color_str)

                contiguous_color = color
                contiguous_x0 = x

        if contiguous_color is not None:
            contiguous_color_str = COLORS[contiguous_color]
            if contiguous_x0 + 1 == len(line):
                canvas.draw_point((contiguous_x0, y),
                                  contiguous_color_str)
                canvas.draw_point((contiguous_x0, CANVAS_HEIGHT - y),
                                  contiguous_color_str)
            else:
                draw_hline(canvas,
                           contiguous_x0, len(line) - 1, y,
                           contiguous_color_str)
                draw_hline(canvas,
                           contiguous_x0, len(line) - 1, CANVAS_HEIGHT - y,
                           contiguous_color_str)

    if NB_ITER >= NB_ITER_MAX:
        frame.set_draw_handler(draw_only)
        print('\nEnd.')

    if _FPS_AVERAGE:
        canvas.draw_text('{:.3}'.format(frame._get_fps_average()),  # pylint: disable=protected-access  # noqa
                         (5, 20), 20, 'Black')


if codeskulptor_is():
    def draw_hline(canvas, x0, x1, y, color):
        # type: (simplegui.Canvas, int, int, int, str) -> None
        """
        Draw a horizontal line
        (point by point
        because CodeSkulptor draw_line() is problematic with line_width=1).

        :param canvas: simplegui.Canvas
        :param x0: int >= 0
        :param x1: int >= 0
        :param y: int >= 0
        :param color: str
        """
        for x in range(x0, x1 + 1):
            canvas.draw_point((x, y), color)
else:
    def draw_hline(canvas, x0, x1, y, color):
        # type: (simplegui.Canvas, int, int, int, str) -> None
        """
        Draw a horizontal line.

        :param canvas: simplegui.Canvas
        :param x0: int >= 0
        :param x1: int >= 0
        :param y: int >= 0
        :param color: str
        """
        canvas.draw_line((x0, y), (x1, y), 1, color)


def draw_only(canvas):  # type: (simplegui.Canvas) -> None
    """
    Draw image of Mandelbrot set from GRID.

    :param canvas: simplegui.Canvas
    """
    assert isinstance(COLORS, tuple)
    assert isinstance(GRID, list)

    for y, line in enumerate(GRID):
        contiguous_color = None
        contiguous_x0 = 0

        for x, point in enumerate(line):
            color = point[3]
            if contiguous_color != color:
                if contiguous_color is not None:
                    contiguous_color_str = COLORS[contiguous_color]
                    if contiguous_x0 + 1 == x:
                        canvas.draw_point((contiguous_x0, y),
                                          contiguous_color_str)
                        canvas.draw_point((contiguous_x0, CANVAS_HEIGHT - y),
                                          contiguous_color_str)
                    else:
                        draw_hline(canvas,
                                   contiguous_x0, x - 1, y,
                                   contiguous_color_str)
                        draw_hline(canvas,
                                   contiguous_x0, x - 1, CANVAS_HEIGHT - y,
                                   contiguous_color_str)

                contiguous_color = color
                contiguous_x0 = x

        assert isinstance(contiguous_color, int)

        contiguous_color_str = COLORS[contiguous_color]
        if contiguous_x0 + 1 == len(line):
            canvas.draw_point((contiguous_x0, y),
                              contiguous_color_str)
            canvas.draw_point((contiguous_x0, CANVAS_HEIGHT - y),
                              contiguous_color_str)
        else:
            draw_hline(canvas,
                       contiguous_x0, len(line) - 1, y,
                       contiguous_color_str)
            draw_hline(canvas,
                       contiguous_x0, len(line) - 1, CANVAS_HEIGHT - y,
                       contiguous_color_str)

    if _FPS_AVERAGE:
        canvas.draw_text('{:.3}'.format(frame._get_fps_average()),  # pylint: disable=protected-access  # noqa
                         (5, 20), 20, 'Black')


def init():  # type: () -> None
    """
    Set a GRID of point information :
    [z, C, numbers of iterations, None or color number]
    """
    global COLORS  # pylint: disable=global-statement
    global GRID  # pylint: disable=global-statement
    global NB_ITER  # pylint: disable=global-statement

    print('Init.')

    assert NB_ITER_MAX < 256, NB_ITER_MAX

    COLORS = tuple(['#%s%s%s'
                    % (hex2(255 - 256 * int(math.log10(i) // NB_ITER_MAX)),
                       hex2(255 - 256 * i // NB_ITER_MAX),
                       hex2(255 - 256 * i // NB_ITER_MAX))
                    for i in range(1, NB_ITER_MAX)])

    NB_ITER = 0

    coef_c_real = (Z1_REAL - Z0_REAL) / (CANVAS_WIDTH - 1)
    coef_c_imag = (Z0_IMAG - Z1_IMAG) / (CANVAS_HEIGHT - 1)

    GRID = []
    for y in range(CANVAS_HEIGHT // 2 + 1):
        c_imag = Z0_IMAG - coef_c_imag * y

        line = []
        for x in range(CANVAS_WIDTH):
            c_real = Z0_REAL + coef_c_real * x
            line.append([(0, 0),            # z
                         (c_real, c_imag),  # C
                         0,                 # number of iterations
                         None])             # color number

        GRID.append(line)

    print('\nNumber of iterations:')


#
# Main
#######
init()

frame = simplegui.create_frame('Mandelbrot Viewer',
                               CANVAS_WIDTH, CANVAS_HEIGHT, 50)

frame.add_button('Quit', frame.stop)

frame.set_draw_handler(draw_and_calculate)

frame.start()
