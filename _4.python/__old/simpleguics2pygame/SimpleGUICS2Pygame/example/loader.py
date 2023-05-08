#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Example of simplegui_lib_loader.Loader use.

Documentation:
https://simpleguics2pygame.readthedocs.io/en/latest/simplegui_lib_loader.html

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2016, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 21, 2020
"""

try:
    import simplegui  # pytype: disable=import-error

    from user305_SZPJfNxJlVTjbAy import Loader  # pytype: disable=import-error

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore

    from SimpleGUICS2Pygame.simplegui_lib_loader import Loader

    SIMPLEGUICS2PYGAME = True

    simplegui.Frame._hide_status = True  # pylint: disable=protected-access


WIDTH = 400
HEIGHT = 200


def draw(canvas):  # type: (simplegui.Canvas) -> None
    """
    The real draw handler function.

    :param canvas: simplegui.Canvas
    """
    img = LOADER.get_image('asteroid')  # get an image by its name
    canvas.draw_image(img,
                      (img.get_width() / 2, img.get_height() / 2),
                      (img.get_width(), img.get_height()),
                      (img.get_width() / 2, img.get_height() / 2),
                      (img.get_width(), img.get_height()))

    img = LOADER.get_image('double_ship')  # get an image by its name
    canvas.draw_image(img,
                      (img.get_width() / 2, img.get_height() / 2),
                      (img.get_width(), img.get_height()),
                      (img.get_width() / 2, img.get_height() / 2 + 100),
                      (img.get_width(), img.get_height()))


# Main
FRAME = simplegui.create_frame('Loader example', WIDTH, HEIGHT, 50)


def init():  # type: () -> None
    """Init function called after image loaded."""
    # Init your stuff...
    FRAME.add_button('Quit', quit_prog)

    music = LOADER.get_sound('soundtrack')  # get a sound by its name
    music.play()

    snd = LOADER.get_sound('explosion')  # get a sound by its name
    snd.play()

    # Medias failed
    img = LOADER.get_image('incorrect url')  # get an image by its name

    assert img.get_width() == 0, img.get_width()

    snd = LOADER.get_sound('incorrect url')  # get a sound by its name
    snd.play()

    # Set the real draw handler
    FRAME.set_draw_handler(draw)


def quit_prog():  # type: () -> None
    """Stop sounds and frame"""
    LOADER.pause_sounds()  # stop all sounds
    FRAME.stop()
    if SIMPLEGUICS2PYGAME and FRAME._print_stats_cache:  # pylint: disable=protected-access  # noqa
        LOADER.print_stats_cache()


LOADER = Loader(FRAME,  # the frame
                WIDTH,  # the width frame
                init)   # the function to call after loading

# Specified images to load with its URL and give them a name.
LOADER.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png',  # noqa
                 'asteroid')
LOADER.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png',  # noqa
                 'double_ship')
LOADER.add_image('xxx',
                 'incorrect url')

# Specified sounds to load with its URL and give them a name.
LOADER.add_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.ogg',  # noqa
                 'explosion')
LOADER.add_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.ogg',  # noqa
                 'soundtrack')
LOADER.add_sound('xxx',
                 'incorrect url')


# Start loading images and sounds:
# - In standard Python with SimpleGUICS2Pygame:
#   draw a progression bar on canvas and wait until the loading is finished.
# - In SimpleGUI of CodeSkulptor: *don't* wait.
LOADER.load()

# Draw a progression bar on canvas
# and wait until all images and sounds are fully loaded.
# Then execute the function specified by Loader().
# (Abort if times out.)
LOADER.wait_loaded()

FRAME.start()
