#!/usr/bin/env python
# -*- coding: latin-1 -*-
# pylint: disable=invalid-name

"""
Nostalgic Basic Blitz game.

Old little game like those published in
"Jeux en BASIC sur TRS-80 couleur".
http://www.abebooks.fr/JEUX-BASIC-TRS-80-COULEUR-MONSAUT-Pierre/7821908154/bd

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2014, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: November 28, 2020
"""

import random

try:
    from typing import Optional, Tuple
except ImportError:
    pass

try:
    import simplegui  # pytype: disable=import-error
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore

    simplegui.Frame._cursor_auto_hide = True  # pylint: disable=protected-access  # noqa
    simplegui.Frame._hide_status = True  # pylint: disable=protected-access


#
# Global constants
###################
WIDTH = 59
HEIGHT = 20

SCALE = 2

CHAR_WIDTH = 6 * SCALE
CHAR_HEIGHT = 14 * SCALE

CANVAS_WIDTH = WIDTH * CHAR_WIDTH
CANVAS_HEIGHT = HEIGHT * CHAR_HEIGHT


#
# Global variables
###################
BLITZ = None  # type: Optional['Blitz']

FRAME = None  # type: Optional[simplegui.Frame]


#
# Classes
##########
class Bomb:
    """A bomb."""

    def __init__(self, x, y):  # type: (int, int) -> None
        """
        Set a bomb.

        :param x: int >= 0
        :param y: int >= 0
        """
        assert isinstance(x, int), type(x)
        assert x >= 0, x
        assert isinstance(y, int), type(y)
        assert y >= 0, y

        self.__x = x
        self.__pixel_y = y * CHAR_HEIGHT

    def draw(self, canvas):  # type: (simplegui.Canvas) -> None
        """
        Draw the bomb.

        :param canvas: simplegui.Canvas
        """
        assert isinstance(canvas, simplegui.Canvas), type(canvas)

        canvas.draw_line(((self.__x + 0.5) * CHAR_WIDTH - 1,
                          self.__pixel_y),
                         ((self.__x + 0.5) * CHAR_WIDTH - 1,
                          self.__pixel_y + CHAR_HEIGHT),
                         CHAR_WIDTH, 'Red')

    def landed(self):  # type: () -> bool
        """
        If the bomb touch the ground
        then return True,
        else return False.

        :return: bool
        """
        return self.__pixel_y + CHAR_HEIGHT >= CANVAS_HEIGHT

    def pos_x(self):  # type: () -> int
        """
        Return the horizontal position.

        :return: int >= 0
        """
        return self.__x

    def pos_y(self):  # type: () -> int
        """
        Return the vertical position.

        :return: int >= 0
        """
        return self.__pixel_y // CHAR_HEIGHT

    def update(self):  # type: () -> None
        """Update the bomb position."""
        self.__pixel_y += CHAR_HEIGHT // 3


class City:
    """A city."""

    def __init__(self):  # type: () -> None
        """Set randomly a city."""
        heights = [random.randint(4, HEIGHT - 8) // 2
                   for _ in range((WIDTH - 5) // 2)]

        assert heights

        self.__heights = [0, 0]

        height = None

        for height in heights:
            height = height * 2 + 1
            self.__heights.extend((max(height, self.__heights[-1]),
                                   height))
        self.__heights.append(height)

    def check_collide(self, x, y):  # type: (int, int) -> bool
        """
        If plane collide with city
        then return True,
        else return False.

        :param x: int >= 0
        :param y: int >= 0

        :return: bool
        """
        assert isinstance(x, int), type(x)
        assert x >= 0, x
        assert isinstance(y, int), type(y)
        assert y >= 0, y

        return ((x < len(self.__heights)) and
                (self.__heights[x] > 0) and
                (y >= HEIGHT - self.__heights[x]))

    def draw(self, canvas):  # type: (simplegui.Canvas) -> None
        """
        Draw the city.

        :param canvas: simplegui.Canvas
        """
        assert isinstance(canvas, simplegui.Canvas), type(canvas)

        for i in range(len(self.__heights)):
            height = self.__heights[i]
            if height > 0:
                if i % 2 == 0:
                    canvas.draw_line(
                        ((i + 0.5) * CHAR_WIDTH - 1,
                         CANVAS_HEIGHT - 1 - height * CHAR_HEIGHT),
                        ((i + 0.5) * CHAR_WIDTH - 1,
                         CANVAS_HEIGHT - 1),
                        CHAR_WIDTH, 'Yellow')
                else:
                    for j in range(0, height, 2):
                        canvas.draw_line(
                            ((i + 0.5) * CHAR_WIDTH - 1,
                             CANVAS_HEIGHT - 1 - (j + 1) * CHAR_HEIGHT),
                            ((i + 0.5) * CHAR_WIDTH - 1,
                             CANVAS_HEIGHT - 1 - j * CHAR_HEIGHT),
                            CHAR_WIDTH, 'Yellow')

    def kill_column_top(self, x, y):  # type: (int, int) -> None
        """
        Kill top of column `x`.

        :param x: int >= 0
        :param y: int >= 0
        """
        assert isinstance(x, int), type(x)
        assert x >= 0, x
        assert isinstance(y, int), type(y)
        assert y >= 0, y

        if x < len(self.__heights):
            self.__heights[x] = min(max(0, HEIGHT - y - 1), self.__heights[x])

    def kill_columns(self, x):  # type: (int) -> None
        """
        Kill the column `x`.

        :param x: int >= 0
        """
        assert isinstance(x, int), type(x)
        assert x >= 0, x

        if x < len(self.__heights):
            self.__heights[x] = 0
            while self.__heights and (self.__heights[-1] <= 0):
                self.__heights.pop()

    def nb_remaining_columns(self):  # type: () -> int
        """
        Return the number of columns not killed.

        :return: int >= 0
        """
        nb_column = 0

        for height in self.__heights:
            if height > 0:
                nb_column += 1

        return nb_column


class Plane:
    """A plane."""

    def __init__(self):  # type: () -> None
        """Set a plane."""
        self.__pixel_x = 0
        self.__y = 0

        self.__crashed = False

    def crashed(self, crashed=None):  # type: (Optional[bool]) -> bool
        """
        If the plane crashed
        then return True,
        else return False.

        If `crashed` is True
        then crashed the plane.

        :param crashed: None or True

        :return: bool
        """
        assert (crashed is None) or (crashed is True), crashed

        if crashed:
            self.__crashed = True

        return self.__crashed

    def draw(self, canvas):  # type: (simplegui.Canvas) -> None
        """
        Draw the plane.

        :param canvas: simplegui.Canvas
        """
        assert isinstance(canvas, simplegui.Canvas), type(canvas)

        color = ('Orange' if self.__crashed
                 else 'Silver')
        pixel_y = self.__y * CHAR_HEIGHT
        canvas.draw_polygon(((self.__pixel_x,
                              pixel_y + CHAR_HEIGHT / 2),
                             (self.__pixel_x + CHAR_WIDTH,
                              pixel_y + CHAR_HEIGHT),
                             (self.__pixel_x + CHAR_WIDTH * 3,
                              pixel_y + CHAR_HEIGHT),
                             (self.__pixel_x + CHAR_WIDTH * 4,
                              pixel_y + CHAR_HEIGHT * 1.5),
                             (self.__pixel_x + CHAR_WIDTH * 3,
                              pixel_y + CHAR_HEIGHT * 2 - 3),
                             (self.__pixel_x,
                              pixel_y + CHAR_HEIGHT * 2 - 3)),
                            1, color, color)

        assert isinstance(BLITZ, Blitz)

        if not BLITZ.bomb_launched() and not self.__crashed:
            canvas.draw_line((self.__pixel_x + CHAR_WIDTH,
                              pixel_y + CHAR_HEIGHT * 2 - 3),
                             (self.__pixel_x + CHAR_WIDTH * 2,
                              pixel_y + CHAR_HEIGHT * 2 - 3),
                             3, 'Red')

    def launch_bomb(self):  # type: () -> Bomb
        """
        Launch a bomb.

        :return: Bomb
        """
        return Bomb(*self.launch_pos())

    def launch_pos(self):  # type: () -> Tuple[int, int]
        """
        Position of bomb launcher.

        :return: (int >= 0, int >= 0)
        """
        return (self.__pixel_x // CHAR_WIDTH + 1,
                self.__y + 2)

    def nose_pos(self):  # type: () -> Tuple[int, int]
        """
        Position of nose of the plane.

        :return: (int >= 0, int >= 0)
        """
        return (self.__pixel_x // CHAR_WIDTH + 3,
                self.__y + 1)

    def update(self):  # type: () -> None
        """Update plane position."""
        assert isinstance(BLITZ, Blitz)

        if (self.__y < HEIGHT - 2) and not self.__crashed:
            self.__pixel_x += 2
            if self.__pixel_x > CANVAS_WIDTH:
                self.__pixel_x = -CHAR_WIDTH * 4
                self.__y += 1
            elif BLITZ.won():
                self.__y += 1


class Blitz:
    """The Blitz game."""

    def __init__(self):  # type: () -> None
        """Set the game."""
        self.__bomb = None  # type: Optional['Bomb']
        self.__city = City()  # type: 'City'
        self.__plane = Plane()  # type: 'Plane'

    def bomb_launched(self):  # type: () -> bool
        """:return: True if a bomb is launched, False else."""
        return self.__bomb is not None

    def draw(self, canvas):  # type: (simplegui.Canvas) -> None
        """
        Draw all the game.

        :param canvas: simplegui.Canvas
        """
        assert isinstance(canvas, simplegui.Canvas), type(canvas)
        assert isinstance(FRAME, simplegui.Frame)

        self.__city.draw(canvas)
        self.__plane.draw(canvas)
        if self.__bomb is not None:
            self.__bomb.draw(canvas)

        text = str(self.__city.nb_remaining_columns())
        size = 30
        width = FRAME.get_canvas_textwidth(text, size)
        canvas.draw_text(text, (CANVAS_WIDTH - width - 10,
                                10 + size * 3.0 / 4),
                         size, 'White')

    def launch_bomb(self):  # type: () -> None
        """
        If not crashed and not already a bomb
        then launch a bomb.
        """
        if ((self.__bomb is None) and
                (0 <= self.__plane.launch_pos()[0] < WIDTH) and
                not self.__plane.crashed()):
            self.__bomb = self.__plane.launch_bomb()

    def update(self):  # type: () -> None
        """Update all the game"""
        self.__plane.update()

        if self.__bomb is not None:
            self.__bomb.update()
            if self.__bomb.landed():
                self.__city.kill_columns(self.__bomb.pos_x())
                self.__bomb = None
            else:
                assert isinstance(self.__bomb, Bomb)

                self.__city.kill_column_top(self.__bomb.pos_x(),
                                            self.__bomb.pos_y())

        x, y = self.__plane.nose_pos()
        if self.__city.check_collide(x + 1, y):
            self.__plane.crashed(True)

    def won(self):  # type: () -> bool
        """
        If won
        then return True,
        else return False.

        :return: bool
        """
        return ((self.__city.nb_remaining_columns() == 0) and
                not self.__plane.crashed())


#
# Handler functions
####################
def deal_keydown(key):  # type: (int) -> None
    """
    Deal key down.

    :param key: int >= 0
    """
    assert isinstance(key, int), type(key)
    assert key >= 0, key

    assert isinstance(BLITZ, Blitz)

    if key == simplegui.KEY_MAP['space']:
        BLITZ.launch_bomb()


def draw(canvas):  # type: (simplegui.Canvas) -> None
    """
    Display all.

    :param canvas: simplegui.Canvas
    """
    assert isinstance(canvas, simplegui.Canvas), type(canvas)
    assert isinstance(BLITZ, Blitz)

    BLITZ.draw(canvas)
    BLITZ.update()


def restart():  # type: () -> None
    """Restart the game."""
    global BLITZ  # pylint: disable=global-statement

    BLITZ = Blitz()


#
# Main
#######
FRAME = simplegui.create_frame('Nostalgic Basic Blitz)',
                               CANVAS_WIDTH, CANVAS_HEIGHT, 100)

FRAME.add_button('Restart', restart)
FRAME.add_label('')
FRAME.add_button('Quit', FRAME.stop)
FRAME.add_label('')
FRAME.add_label('Spacebar to launch bomb!')


restart()

FRAME.set_draw_handler(draw)

FRAME.set_keydown_handler(deal_keydown)


FRAME.start()
