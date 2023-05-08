#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Memory.
  Game with 8 x (2 indentical cards)
         or 4 x (4 indentical cards).

My retouched solution of the mini-project #5 of the MOOC
https://www.coursera.org/learn/interactive-python-2 (Coursera 2013).

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2015, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 21, 2020
"""

import random

try:
    from typing import List, Optional, Sequence, Union
except ImportError:
    pass

try:
    import simplegui  # pytype: disable=import-error

    from user305_SXBsmszNiUxIeoV import assert_position  # pytype: disable=import-error  # noqa
    from user305_SaT1YKoOikl4ax9 import draw_rect  # pytype: disable=import-error  # noqa
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore

    from SimpleGUICS2Pygame.codeskulptor_lib import assert_position
    from SimpleGUICS2Pygame.simplegui_lib_draw import draw_rect

    simplegui.Frame._hide_status = True  # pylint: disable=protected-access


USE_IMAGES = True  # change to False to avoid images


# Globals variables
if USE_IMAGES:
    CARD_IMAGES = tuple(
        simplegui.load_image(url)
        for url in ('https://i.imgur.com/kQbx35z.jpg',  # Guido van Rossum
                    'https://i.imgur.com/Rr1jAAn.jpg',  # Python
                    'https://i.imgur.com/ybaQQfu.jpg',  # SimpleGUICS2Pygame
                    'https://i.imgur.com/svHUOV2.jpg',  # CodeSkulptor
                    'https://i.imgur.com/kvuSM04.jpg',  # Joe Warren
                    'https://i.imgur.com/8CVSH15.jpg',  # Scott Rixner
                    'https://i.imgur.com/HXJ6906.jpg',  # John Greiner
                    'https://i.imgur.com/Nlpl5R3.jpg',  # Stephen Wong
                    'https://i.imgur.com/z0ezFNN.jpg'))  # Memory (verso)
else:
    CARD_IMAGES = (simplegui.load_image(''), ) * 9  # 9 (same) failed images

MEMORY = None  # the principal variable, instance of Memory  # type: Optional['Memory']  # noqa

NB_IMAGES_LOADED = 0
NB_TEST_IMAGES_LOADED = 20

LABEL_GAME = None  # type: Optional[simplegui.Control]
LABEL_MOVES = None  # type: Optional[simplegui.Control]


# Helper function
def draw_border(canvas, pos, size,  # pylint: disable=too-many-arguments
                line_width, color, shift=4):
    # type: (simplegui.Canvas, Sequence[Union[int, float]], Sequence[Union[int, float]], int, str, int) -> None  # noqa
    """
    Draw a rounded rectangle.

    :param canvas: simplegui.Canvas
    :param pos: (int or float, int or float) or [int or float, int or float]
    :param size: (int or float, int or float) or [int or float, int or float]
    :param line_width: int >= 0
    :param color: str
    :param shift: int
    """
    assert_position(pos)
    assert_position(size)
    assert isinstance(line_width, (int, float)), type(line_width)
    assert line_width >= 0, line_width
    assert isinstance(color, str), type(str)
    assert isinstance(shift, int), type(shift)

    x0 = pos[0]
    y0 = pos[1]

    width = size[0] - 1
    height = size[1] - 1

    canvas.draw_polygon(((x0, y0 + shift),
                         (x0 + shift, y0),
                         (x0 + width - shift, y0),
                         (x0 + width, y0 + shift),
                         (x0 + width, y0 + height - shift),
                         (x0 + width - shift, y0 + height),
                         (x0 + shift, y0 + height),
                         (x0, y0 + height - shift)),
                        line_width, color)


# Classes
class Card:
    """A card (with an identification number and a drawing position)."""

    WIDTH = 50
    HEIGHT = 100

    def __init__(self, num, image):  # type: (int, simplegui.Image) -> None
        """
        Initialize the card.

        :param num: int >= 0
        :param image: simplegui.Image
        """
        assert isinstance(num, int), type(num)
        assert num >= 0, num

        self.num = num
        self.image = image

        self.pos_x = 0
        self.pos_y = 0
        self.exposed = False
        self.selected = False

    def draw(self, canvas):  # type: (simplegui.Canvas) -> None
        """
        Draw the card.

        :param canvas: simplegui.canvas
        """
        if self.exposed:
            self.draw_recto(canvas)
        else:
            self.draw_verso(canvas)

    def draw_recto(self, canvas):  # type: (simplegui.Canvas) -> None
        """
        Draw recto of the card
        (CARD_IMAGES[self.num] images if loaded).

        :param canvas: simplegui.canvas
        """
        if self.image.get_width() > 0:  # draw image
            canvas.draw_image(self.image,
                              (self.image.get_width() / 2.0,
                               self.image.get_height() / 2.0),
                              (self.image.get_width(),
                               self.image.get_height()),
                              (self.pos_x + self.image.get_width() / 2.0,
                               self.pos_y + self.image.get_height() / 2.0),
                              (self.image.get_width(),
                               self.image.get_height()))
        else:                           # draw text number
            size = 50
            text = str(self.num)
            width = FRAME.get_canvas_textwidth(text, 50)
            canvas.draw_text(text,
                             (self.pos_x + (Card.WIDTH - width) // 2,
                              (self.pos_y + (Card.HEIGHT - size) / 2.0 +
                               size * 3.0 / 4)),
                             size, 'white')

        if self.selected or (self.image.get_width() == 0):
            draw_border(canvas,
                        (self.pos_x, self.pos_y), (Card.WIDTH, Card.HEIGHT),
                        3, ('yellow' if self.selected
                            else 'white'))

    def draw_verso(self, canvas):  # type: (simplegui.Canvas) -> None
        """
        Draw verso of the card
        (CARD_IMAGES[-1] images if loaded).

        :param canvas: simplegui.canvas
        """
        img = CARD_IMAGES[-1]

        if img.get_width() > 0:  # draw image
            canvas.draw_image(img,
                              (img.get_width() / 2.0, img.get_height() / 2.0),
                              (img.get_width(), img.get_height()),
                              (self.pos_x + img.get_width() / 2.0,
                               self.pos_y + img.get_height() / 2.0),
                              (img.get_width(), img.get_height()))
        else:                    # draw simple rectangle
            canvas.draw_line((self.pos_x + Card.WIDTH / 2.0 - 1,
                              self.pos_y),
                             (self.pos_x + Card.WIDTH / 2.0 - 1,
                              self.pos_y + Card.HEIGHT - 1),
                             Card.WIDTH, 'green')
            draw_rect(canvas,
                      (self.pos_x + 3, self.pos_y + 3),
                      (Card.WIDTH - 6, Card.HEIGHT - 6),
                      1, 'red')

    def in_pos(self, pos):  # type: (Sequence[Union[int, float]]) -> bool
        """
        If pos is in this card
        then return True,
        else return False.

        :param pos: (int or float, int or float)
                      or [int or float, int or float]

        :return: bool
        """
        assert_position(pos)

        return ((self.pos_x <= pos[0] < self.pos_x + Card.WIDTH) and
                (self.pos_y <= pos[1] < self.pos_y + Card.HEIGHT))


class Memory:
    """Memory game (list of cards)"""

    def __init__(self, nb_different_cards=8, nb_repeat_cards=2):
        # type: (int, int) -> None
        """
        Initialize the game.

        :param nb_different_cards: 0 < int <= len(CARD_IMAGES) - 2
        :param nb_repeat_cards: int > 0
        """
        assert isinstance(nb_different_cards, int), type(nb_different_cards)
        assert nb_different_cards > 0, nb_different_cards

        assert isinstance(nb_repeat_cards, int), type(nb_repeat_cards)
        assert 0 < nb_repeat_cards <= len(CARD_IMAGES) - 2, nb_repeat_cards

        assert nb_different_cards * nb_repeat_cards == 16, \
            (nb_different_cards, nb_repeat_cards)

        self.nb_different_cards = nb_different_cards
        self.nb_repeat_cards = nb_repeat_cards

        self.nb_moves = 0
        self.nb_founded = 0
        self.new_founded = False

        self.deck = [Card(i % nb_different_cards,
                          CARD_IMAGES[i % nb_different_cards])
                     for i in range(nb_different_cards * nb_repeat_cards)]
        random.shuffle(self.deck)

        for i, card in enumerate(self.deck):
            card.pos_x = (10 +
                          ((i % (nb_different_cards * nb_repeat_cards // 2)) *
                           (Card.WIDTH + 10)))
            card.pos_y = (10 +
                          ((i // (nb_different_cards * nb_repeat_cards // 2)) *
                           (Card.HEIGHT + 10)))

        self.selected_cards = []  # type: List[Card]

        assert isinstance(LABEL_MOVES, simplegui.Control)

        LABEL_MOVES.set_text('Nb moves: 0')  # type: ignore

    def draw(self, canvas):  # type: (simplegui.Canvas) -> None
        """
        Draw all cards.

        :param canvas: simplegui.canvas
        """
        for card in self.deck:
            card.draw(canvas)

    def expose(self, pos):  # type: (Sequence[Union[int, float]]) -> None
        """
        Expose the card pointed by position pos,
        and check if good cards are exposed.

        :param pos: (int or float, int or float)
                      or [int or float, int or float]
        """
        assert_position(pos)

        for card in self.deck:  # pylint: disable=too-many-nested-blocks
            if card.in_pos(pos):  # this is the pointed card
                if not card.exposed:
                    if len(self.selected_cards) == self.nb_repeat_cards:
                        # Good number of exposed cards
                        # Reinit exposed cards
                        for c in self.selected_cards:  # pylint: disable=invalid-name  # noqa
                            c.selected = False
                            if not self.new_founded:  # but not good cards
                                c.exposed = False

                        self.selected_cards = []

                    # Expose the pointed card
                    card.exposed = True
                    card.selected = True
                    self.selected_cards.append(card)

                    if len(self.selected_cards) == self.nb_repeat_cards:
                        # Good number of exposed cards
                        # Update the moves counter
                        self.nb_moves += 1

                        assert isinstance(LABEL_MOVES, simplegui.Control)

                        LABEL_MOVES.set_text('Nb moves: ' + str(self.nb_moves))

                        # If all exposed cards and pointed card are the same
                        self.new_founded = all(
                            [c.num == self.selected_cards[0].num
                             for c in self.selected_cards[1:]])
                        if self.new_founded:  # good cards are exposed
                            self.nb_founded += 1
                            if self.nb_founded == self.nb_different_cards:
                                # Completed game
                                for c in self.selected_cards:  # pylint: disable=invalid-name  # noqa
                                    c.selected = False

                break


# Event handlers
def draw(canvas):  # type: (simplegui.Canvas) -> None
    """
    Event handler to draw all cards.

    :param canvas: simplegui.Canvas
    """
    assert isinstance(MEMORY, Memory)

    MEMORY.draw(canvas)


def draw_wait_images(canvas):  # type: (simplegui.Canvas) -> None
    """
    Draw waiting message when images loading.

    :param canvas: simplegui.Canvas
    """
    percent = NB_IMAGES_LOADED * 100.0 / len(CARD_IMAGES)

    canvas.draw_line((0, 150), (490, 150), 20, 'white')
    canvas.draw_line((0, 150), (490 * percent / 100.0, 150), 20, 'green')

    size = 50
    canvas.draw_text('Loading... %d%%' % int(percent),
                     (10, 80 + size * 30.0 / 4),
                     size, 'white')


def mouseclick(pos):  # type: (Sequence[Union[int]]) -> None
    """
    Event handler to deal clic on a card.

    :param pos: (int >= 0, int >= 0)
    """
    assert isinstance(MEMORY, Memory)

    MEMORY.expose(pos)


def restart_4x4():  # type: () -> None
    """
    Event handler to deal click on restart 4x4 button.

    Global change: MEMORY
    """
    global MEMORY  # pylint: disable=global-statement

    assert isinstance(LABEL_GAME, simplegui.Control)

    LABEL_GAME.set_text('4 x (4 indentical cards)')
    MEMORY = Memory(4, 4)


def restart_8x2():  # type: () -> None
    """
    Event handler to deal click on restart 8x2 button.

    Global change: MEMORY
    """
    global MEMORY  # pylint: disable=global-statement

    assert isinstance(LABEL_GAME, simplegui.Control)

    LABEL_GAME.set_text('8 x (2 indentical cards)')
    MEMORY = Memory(8, 2)


def start():  # type: () -> None
    """Event handler to deal start after loading images."""
    restart_8x2()

    FRAME.set_mouseclick_handler(mouseclick)
    FRAME.set_draw_handler(draw)


def test_images_loaded():  # type: () -> None
    """
    Check the number of images already loaded.

    Global change: NB_IMAGES_LOADED
                   NB_TEST_IMAGES_LOADED
    """
    global NB_IMAGES_LOADED  # pylint: disable=global-statement
    global NB_TEST_IMAGES_LOADED  # pylint: disable=global-statement

    NB_IMAGES_LOADED = sum([1 for img in CARD_IMAGES if img.get_width() > 0])

    if (NB_TEST_IMAGES_LOADED <= 0) or (NB_IMAGES_LOADED == len(CARD_IMAGES)):
        TIMER.stop()
        start()

    NB_TEST_IMAGES_LOADED -= 1


# Create frame
FRAME = simplegui.create_frame('Memory', 490, 230, 160)

# Control panel
LABEL_GAME = FRAME.add_label('8x2 game')
LABEL_MOVES = FRAME.add_label('Nb moves: 0')
FRAME.add_label('')
FRAME.add_button('Restart 8x2', restart_8x2)
FRAME.add_button('Restart 4x4', restart_4x4)
FRAME.add_label('')
FRAME.add_button('Quit', FRAME.stop)

# Register event handlers
FRAME.set_draw_handler(draw_wait_images)

TIMER = simplegui.create_timer(100, test_images_loaded)
TIMER.start()

test_images_loaded()


# Main
FRAME.start()
