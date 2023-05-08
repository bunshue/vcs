# -*- coding: latin-1 -*-

"""
simplegui_lib_draw module.

Draw functions to help
in SimpleGUI of CodeSkulptor.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013, 2015, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 19, 2020
"""

# print('IMPORT', __name__)


try:
    import simplegui  # pytype: disable=import-error  # pylint: disable=unused-import  # noqa

    __SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore  # pylint: disable=unused-import  # noqa

    __SIMPLEGUICS2PYGAME = True

    try:
        from typing import Optional, Sequence, Union
    except ImportError:
        pass


#
# Functions
############
def draw_rect(canvas, pos, size,  # pylint: disable=too-many-arguments
              line_width, line_color, fill_color=None):
    # type: (simplegui.Canvas, Sequence[Union[int, float]], Sequence[Union[int, float]], int, str, str) -> None  # noqa
    """
    Draw a rectangle.

    :param canvas: simplegui.Canvas
    :param pos: (int or float, int or float) or [int or float, int or float]
    :param size: (int or float, int or float) or [int or float, int or float]
    :param line_width: int >= 0
    :param line_color: str
    :param fill_color: str
    """
    assert isinstance(pos, (tuple, list)), type(pos)
    assert len(pos) == 2, len(pos)
    assert isinstance(pos[0], (int, float)), type(pos[0])
    assert isinstance(pos[1], (int, float)), type(pos[1])

    assert isinstance(size, (tuple, list)), type(size)
    assert len(size) == 2, len(size)
    assert isinstance(size[0], (int, float)), type(size[0])
    assert isinstance(size[1], (int, float)), type(size[1])

    assert isinstance(line_width, (int, float)), type(line_width)
    assert line_width >= 0, line_width
    assert isinstance(line_color, str), type(str)
    assert (fill_color is None) or isinstance(fill_color, str), type(str)

    x0 = pos[0]
    y0 = pos[1]

    width = size[0] - 1
    height = size[1] - 1

    canvas.draw_polygon(((x0, y0),
                         (x0 + width, y0),
                         (x0 + width, y0 + height),
                         (x0, y0 + height)),
                        line_width, line_color, fill_color)


def draw_text_multi(canvas,  # pylint: disable=too-many-arguments
                    text, point,
                    font_size, font_color,
                    font_face='serif',
                    _font_size_coef=3.0 / 4):
    # type: (simplegui.Canvas, Union[str, Sequence[str]], Sequence[Union[int, float]], Union[int, float], str, str, Union[int, float]) -> None  # noqa
    """
    Draw the `text` (possibly with several lines) at the position `point`.

    If `text` is a str,
    then split it on each end of line.

    If `text` is a tuple or a list of str,
    then print each str on a separated line.

    See `simplegui.draw_text()`_ .

    .. _`simplegui.draw_text()`: simpleguics2pygame/canvas.html#SimpleGUICS2Pygame.simpleguics2pygame.canvas.Canvas.draw_text

    :param canvas: simplegui.Canvas
    :param text: str or (tuple of str) or (list of str)
    :param point: (int or float, int or float) or [int or float, int or float]
    :param font_size: (int or float) >= 0
    :param font_color: str
    :param font_face: str == 'monospace', 'sans-serif', 'serif'
    :param _font_size_coef: int or float

    :raise: ValueError if text contains unprintable whitespace character
    """  # noqa
    assert isinstance(text, (str, tuple, list)), type(text)

    assert isinstance(point, (tuple, list)), type(point)
    assert len(point) == 2, len(point)
    assert isinstance(point[0], (int, float)), type(point[0])
    assert isinstance(point[1], (int, float)), type(point[1])

    assert isinstance(font_size, (int, float)), type(font_size)
    assert font_size >= 0, font_size

    assert isinstance(font_color, str), type(font_color)
    assert isinstance(font_face, str), type(font_face)
    assert isinstance(_font_size_coef, (int, float)), type(_font_size_coef)

    if isinstance(text, str):
        # Convert each Window$ and M@c end of line to standard end of line
        # and then split
        text = text.replace('\n\r', '\n').replace('\r', '\n').split('\n')

    x, y = point

    for line in text:
        assert isinstance(line, str), type(line)

        if __SIMPLEGUICS2PYGAME:
            canvas.draw_text(line, (x, y), font_size, font_color, font_face,
                             _font_size_coef=_font_size_coef)
        else:
            canvas.draw_text(line, (x, y), font_size, font_color, font_face)

        y += font_size


def draw_text_side(frame, canvas,  # pylint: disable=too-many-arguments,too-many-locals  # noqa
                   text, point,
                   font_size, font_color,
                   font_face='serif',
                   font_size_coef=3.0 / 4,
                   rectangle_color=None, rectangle_fill_color=None,
                   side_x=-1, side_y=1):
    # type: (simplegui.Frame, simplegui.Canvas, str, Sequence[Union[int, float]], Union[int, float], str, str, Union[int, float], Optional[str], Optional[str], Union[int, float], Union[int, float]) -> None  # noqa
    """
    Draw the `text` string at the position `point`.

    See `simplegui.draw_text()`_ .

    .. _`simplegui.draw_text()`: simpleguics2pygame/canvas.html#SimpleGUICS2Pygame.simpleguics2pygame.canvas.Canvas.draw_text

    If `rectangle_color` != `None`
    then draw a rectangle around the text.

    If `rectangle_fill_color` != `None`
    then draw a filled rectangle under the text.

    | If `side_x`
    |   < 0 then `point[0]` is the left of the text,
    |  == 0 then `point[0]` is the center of the text,
    |   > 0 then `point[0]` is the right of the text.

    | If `side_y`
    |   < 0 then `point[1]` is the top of the text,
    |  == 0 then `point[1]` is the center of the text,
    |   > 0 then `point[1]` is the bottom of the text.

    :param frame: simplegui.Frame
    :param canvas: simplegui.Canvas
    :param text: str
    :param point: (int or float, int or float) or [int or float, int or float]
    :param font_size: (int or float) >= 0
    :param font_color: str
    :param font_face: str == 'monospace', 'sans-serif', 'serif'
    :param font_size_coef: int or float
    :param rectangle_color: None or str
    :param rectangle_fill_color: None or str
    :param side_x: int or float
    :param side_y: int or float
    """  # noqa
    assert isinstance(text, str), type(text)

    assert isinstance(point, (tuple, list)), type(point)
    assert len(point) == 2, len(point)
    assert isinstance(point[0], (int, float)), type(point[0])
    assert isinstance(point[1], (int, float)), type(point[1])

    assert isinstance(font_size, (int, float)), type(font_size)
    assert font_size >= 0, font_size

    assert isinstance(font_color, str), type(font_color)
    assert isinstance(font_face, str), type(font_face)

    assert (rectangle_color is None) or isinstance(rectangle_color, str), \
        type(rectangle_color)
    assert ((rectangle_fill_color is None) or
            isinstance(rectangle_fill_color, str)), \
        type(rectangle_fill_color)

    assert isinstance(side_x, (int, float)), type(side_x)
    assert isinstance(side_y, (int, float)), type(side_y)
    assert isinstance(font_size_coef, (int, float)), type(font_size_coef)

    text_width = (frame.get_canvas_textwidth(text, font_size)
                  if font_face is None
                  else frame.get_canvas_textwidth(text, font_size, font_face))

    text_height = font_size * font_size_coef

    if side_x < 0:
        x = point[0]
    elif side_x == 0:
        x = point[0] - text_width / 2.0
    else:
        x = point[0] - text_width

    if side_y < 0:
        y = point[1] + text_height
    elif side_y == 0:
        y = point[1] + text_height / 2.0
    else:
        y = point[1]

    if rectangle_color is not None:
        draw_rect(canvas, (x, y), (text_width, -text_height),
                  1, rectangle_color, rectangle_fill_color)
    elif rectangle_fill_color is not None:
        draw_rect(canvas, (x, y), (text_width, -text_height),
                  1, rectangle_fill_color, rectangle_fill_color)

    canvas.draw_text(text, (x, y), font_size, font_color, font_face)
