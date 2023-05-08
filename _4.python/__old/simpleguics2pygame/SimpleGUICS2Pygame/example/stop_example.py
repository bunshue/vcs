#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Stop example.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2015, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 20, 2020
"""

try:
    import simplegui  # pytype: disable=import-error
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore

    simplegui.Frame._hide_status = True  # pylint: disable=protected-access
    simplegui.Frame._keep_timers = False  # pylint: disable=protected-access


CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300


def click():  # type: () -> None
    """Simple handler function to the timer."""
    print('click')


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


def stop_all():  # type: () -> None
    """Handler function to the Quit button."""
    TIMER.stop()
    SOUND.pause()
    FRAME.stop()


# Main
SOUND = simplegui.load_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg')  # noqa
SOUND.play()

FRAME = simplegui.create_frame('Stop example', CANVAS_WIDTH, CANVAS_HEIGHT)

FRAME.add_button('Quit', stop_all)

FRAME.set_draw_handler(draw)

TIMER = simplegui.create_timer(1000, click)
TIMER.start()

FRAME.start()
