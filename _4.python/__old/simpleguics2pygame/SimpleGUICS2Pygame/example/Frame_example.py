#!/usr/bin/env python
# -*- coding: latin-1 -*-
# pylint: disable=invalid-name

"""
Frame example.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2014, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 21, 2020
"""

try:
    import user305_SXBsmszNiUxIeoV as codeskulptor_lib  # pytype: disable=import-error  # noqa

    import simplegui  # pytype: disable=import-error
except ImportError:
    import SimpleGUICS2Pygame.codeskulptor_lib as codeskulptor_lib  # type: ignore  # noqa

    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore

    simplegui.Frame._hide_status = True  # pylint: disable=protected-access


CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300


def draw(canvas):  # type: (simplegui.Canvas) -> None
    """
    Draw a simple text.

    :param canvas: simplegui.Canvas
    """
    text = 'Canvas'

    font_size = 40
    text_width = FRAME.get_canvas_textwidth(text, font_size)

    canvas.draw_text(text,
                     ((CANVAS_WIDTH - text_width) // 2,
                      CANVAS_HEIGHT // 2 + font_size // 4),
                     font_size, 'Green')


def save_canvas():  # type: () -> None
    """Download/save canvas image."""
    FRAME.download_canvas_image()


# Main
FRAME = simplegui.create_frame('Title', CANVAS_WIDTH, CANVAS_HEIGHT)

FRAME.add_label('Control Panel')

FRAME.add_label('')
if codeskulptor_lib.codeskulptor_version() != 2:
    FRAME.add_button(('Download canvas image'
                      if codeskulptor_lib.codeskulptor_is()
                      else 'Save canvas image'), save_canvas)

FRAME.add_label('')
FRAME.add_button('Quit', FRAME.stop)

FRAME.set_draw_handler(draw)

FRAME.start()
