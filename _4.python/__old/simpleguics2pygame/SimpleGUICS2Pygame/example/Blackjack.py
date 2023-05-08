#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Blackjack game.

My retouched solution of the mini-project #6 of the MOOC
https://www.coursera.org/learn/interactive-python-2 (Coursera 2013).

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2014, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 20, 2020
"""

import random

try:
    from typing import List, Optional, Sequence, Union
except ImportError:
    pass

try:
    import simplegui  # pytype: disable=import-error
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore

    simplegui.Frame._hide_status = True  # pylint: disable=protected-access
    simplegui.Frame._keep_timers = False  # pylint: disable=protected-access


# Global constants
##################
DEBUG = False
# DEBUG = True  # to help debug

# Cards sprite 949x392 (source: www.jfitz.com/cards/ )
CARDS_IMAGE = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png')  # noqa
CARD_BACK = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png')  # noqa

CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)

CARD_SPACE = 5

FONT_SIZE = 40

FRAME_WIDTH = 800
FRAME_HEIGHT = 600

DEALER_POS = ((FRAME_WIDTH - CARD_SPACE) / 2.0 - CARD_SIZE[0], 100)
PLAYER_POS = (DEALER_POS[0], 400)

GREEN = 'Green'
GREEN_LIGHT = '#40d040'
GREEN_DARK = '#007000'

NB_IMAGES_TO_LOAD = 2


# Global variables
##################
DECK = None  # type: Optional['Deck']

HAND_DEALER = None  # type: Optional['Hand']
HAND_PLAYER = None  # type: Optional['Hand']

IN_PLAY = False

MAX_TEST_IMAGES_LOADED = 20
NB_IMAGES_LOADED = 0

OUTCOME = None

SCORE_DEALER = 0
SCORE_PLAYER = 0


# Helper functions
##################
def assert_pos(pos):  # type: (Sequence[Union[int, float]]) -> None
    """
    Assertions to check valid position:
    (int or float, int or float) or [int or float, int or float]
    """
    assert isinstance(pos, (tuple, list)), type(pos)
    assert len(pos) > 0, len(pos)

    assert isinstance(pos[0], (int, float)), type(pos[0])
    assert pos[0] >= 0, pos

    assert isinstance(pos[1], (int, float)), type(pos[1])
    assert pos[1] >= 0, pos


def draw_rect(canvas, pos, size,  # pylint: disable=too-many-arguments
              line_width, line_color, fill_color=None):
    # type: (simplegui.Canvas, Sequence[Union[int, float]], Sequence[Union[int, float]], int, str, Optional[str]) -> None  # noqa
    """
    Draw a rectangle.

    :param canvas: simplegui.Canvas
    :param pos: (int or float, int or float) or [int or float, int or float]
    :param size: (int or float, int or float) or [int or float, int or float]
    :param line_width: int >= 0
    :param line_color: str
    :param fill_color: str or None
    """
    assert_pos(pos)
    assert_pos(size)
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


# Classes
#########
class Card:
    """Card."""

    _VALUES = {'A': 1,
               '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'T': 10,
               'J': 10, 'Q': 10, 'K': 10}

    def __init__(self, suit, rank):  # type: (str, str) -> None
        """
        Set a card.

        :param suit: str in Deck._SUITS
        :param rank: str in Deck._RANKS
        """
        assert isinstance(suit, str), type(suit)
        assert suit in Deck._SUITS, suit  # pylint: disable=protected-access
        assert isinstance(rank, str), type(rank)
        assert rank in Deck._RANKS, rank  # pylint: disable=protected-access

        self._suit = suit
        self._rank = rank

    def __str__(self):  # type: () -> str
        """
        Return a representation of card.

        :return: str
        """
        return self._suit + self._rank

    def draw(self, canvas, pos, hide):
        # type: (simplegui.Canvas, Sequence[Union[int, float]], bool) -> None
        """
        Draw the card at the position.

        If hide
        then the first card are drawed face down.

        If the images CARDS_IMAGE or CARD_BACK are not loaded
        then draw rectangle instead.

        :param canvas: simplegui.Canvas
        :param pos: (int or float, int or float)
                      or [int or float, int or float]
        :param hide: bool
        """
        assert_pos(pos)
        assert isinstance(hide, bool), type(hide)

        drawed = False

        if hide:
            if CARD_BACK.get_width() > 0:
                canvas.draw_image(CARD_BACK,
                                  CARD_BACK_CENTER, CARD_BACK_SIZE,
                                  (pos[0] + CARD_BACK_CENTER[0],
                                   pos[1] + CARD_BACK_CENTER[1]), CARD_SIZE)
                drawed = True
        else:
            if CARDS_IMAGE.get_width() > 0:
                canvas.draw_image(
                    CARDS_IMAGE,
                    ((CARD_CENTER[0] + CARD_SIZE[0] *
                      Deck._RANKS.index(self._rank)),  # pylint: disable=protected-access  # noqa
                     (CARD_CENTER[1] + CARD_SIZE[1] *
                      Deck._SUITS.index(self._suit))),  # pylint: disable=protected-access  # noqa
                    CARD_SIZE,
                    (pos[0] + CARD_CENTER[0],
                     pos[1] + CARD_CENTER[1]), CARD_SIZE)
                drawed = True

        if not drawed:
            draw_rect(canvas, pos, CARD_SIZE, 3, 'Black', ('Maroon' if hide
                                                           else 'White'))
            if not hide:
                text = str(self)
                canvas.draw_text(
                    text,
                    (pos[0] + (CARD_SIZE[0] -
                               FRAME.get_canvas_textwidth(text,
                                                          FONT_SIZE)) / 2.0,
                     pos[1] + CARD_SIZE[1] / 2.0 + FONT_SIZE / 4.0),
                    FONT_SIZE, ('Red' if self.get_suit() in ('H', 'D')
                                else 'Black'))

    def get_rank(self):  # type: () -> str
        """
        Return the rank of the card.

        :return: str
        """
        return self._rank

    def get_suit(self):  # type: () -> str
        """
        Return the suit of the card.

        :return: str
        """
        return self._suit

    def get_value(self):  # type: () -> int
        """
        Return the value of the card.

        :return: 1 <= int <= 10
        """
        return Card._VALUES[self._rank]


class Deck:
    """Deck."""

    _SUITS = ('C',  # Clubs (trèfle en français)
              'S',  # Spades (pique)
              'H',  # Heart (coeur)
              'D')  # Diamond (carreau)

    _RANKS = ('A',
              '2', '3', '4', '5', '6', '7', '8', '9',
              'T',  # ten
              'J',  # Jack (valet)
              'Q',  # Queen (dame)
              'K')  # King (roi)

    def __init__(self):  # type: () -> None
        """Set a deck, list of 52 classic cards."""
        self._cards = []

        for suit in Deck._SUITS:
            for rank in Deck._RANKS:
                self._cards.append(Card(suit, rank))

    def __str__(self):  # type: () -> str
        """
        Return the sequence of cards.

        :return: str
        """
        return ' '.join([str(card) for card in self._cards])

    def deal_card(self):  # type: () -> Card
        """
        Return a card and remove of the deck.

        :return: Card
        """
        assert len(self._cards) > 0

        return self._cards.pop()

    def shuffle(self):  # type: () -> None
        """Shuffle the deck."""
        random.shuffle(self._cards)


class Hand:
    """Hand (of dealer or player)."""

    def __init__(self, is_dealer=False):  # type: (bool) -> None
        """
        Set an empty hand.

        :param is_dealer: bool
        """
        assert isinstance(is_dealer, bool), type(is_dealer)

        self._is_dealer = is_dealer
        self._cards = []  # type: List[Card]

    def __str__(self):  # type: () -> str
        """
        Return the sequence of cards.

        :return: str
        """
        return ' '.join([str(card) for card in self._cards])

    def add_card(self, card):  # type: (Card) -> None
        """
        Add the card in the hand.

        :param card: Card
        """
        assert isinstance(card, Card), type(card)

        self._cards.append(card)

    def draw(self, canvas, pos):
        # type: (simplegui.Canvas, Sequence[Union[int, float]]) -> None
        """
        Draw all cards of the hand.

        :param canvas: simplegui.Canvas
        :param pos: (int or float, int or float)
                      or [int or float, int or float]
        """
        assert_pos(pos)

        if DEBUG:
            canvas.draw_text(str(self.get_value()),
                             (pos[0] - 50, pos[1] + FONT_SIZE),
                             FONT_SIZE, 'Black')

        for i, card in enumerate(self._cards):
            card.draw(canvas, [pos[0] + i * (CARD_SIZE[0] + CARD_SPACE),
                               pos[1]],
                      (i == 0) and self._is_dealer and IN_PLAY)

    def get_value(self):  # type: () -> int
        """
        Return value of the hand.

        :return: int >= 0
        """
        ace_founded = False

        value = 0
        for card in self._cards:
            value += card.get_value()
            if card.get_rank() == 'A':
                ace_founded = True

        return (value + 10 if ace_founded and (value + 10 <= 21)
                else value)


# Event handlers
################
def deal():  # type: () -> None
    """Start a new round."""
    global DECK  # pylint: disable=global-statement
    global HAND_DEALER  # pylint: disable=global-statement
    global HAND_PLAYER  # pylint: disable=global-statement
    global IN_PLAY  # pylint: disable=global-statement
    global OUTCOME  # pylint: disable=global-statement
    global SCORE_DEALER  # pylint: disable=global-statement

    if IN_PLAY:
        SCORE_DEALER += 1
        OUTCOME = 'YOU LOOSE!'
    else:
        IN_PLAY = True
        OUTCOME = None

    DECK = Deck()
    DECK.shuffle()

    HAND_DEALER = Hand(True)
    HAND_PLAYER = Hand()

    for _ in range(2):
        HAND_PLAYER.add_card(DECK.deal_card())
        HAND_DEALER.add_card(DECK.deal_card())


def draw(canvas):  # type: (simplegui.Canvas) -> None
    """
    Draw all the game.

    :param canvas: simplegui.Canvas
    """
    canvas.draw_circle((FRAME_WIDTH / 2.0,
                        FRAME_HEIGHT - FRAME_WIDTH * 3 / 2.0 - 25),
                       FRAME_WIDTH * 3 / 2.0, 50, '#803020', GREEN)

    canvas.draw_text('DEALER', (DEALER_POS[0], DEALER_POS[1] - 10),
                     FONT_SIZE, GREEN_LIGHT)

    canvas.draw_text('PLAYER', (PLAYER_POS[0], PLAYER_POS[1] - 10),
                     FONT_SIZE, GREEN_LIGHT)
    draw_rect(canvas,
              (PLAYER_POS[0] - CARD_SPACE, PLAYER_POS[1] - CARD_SPACE),
              (CARD_SIZE[0] * 2 + CARD_SPACE * 3,
               CARD_SIZE[1] + CARD_SPACE * 2),
              2, GREEN_LIGHT, GREEN_DARK)

    canvas.draw_text('BLACKJACK', (20, 20 + FONT_SIZE * 3 / 4.0), FONT_SIZE,
                     'Red')
    canvas.draw_text('BLACK', (20, 20 + FONT_SIZE * 3 / 4.0), FONT_SIZE,
                     'Black')

    y = PLAYER_POS[1] - 70
    canvas.draw_line((20, y - FONT_SIZE - 10),
                     (FRAME_WIDTH - 20, y - FONT_SIZE - 10), 3, GREEN_LIGHT)
    canvas.draw_line((20, y), (FRAME_WIDTH - 20, y), 3, GREEN_LIGHT)

    text = ('HIT OR STAND?' if IN_PLAY
            else 'NEW DEAL?')
    canvas.draw_text(text,
                     ((FRAME_WIDTH -
                       FRAME.get_canvas_textwidth(text, FONT_SIZE)) / 2.0,
                      y - FONT_SIZE / 4.0 - 3),
                     FONT_SIZE, GREEN_LIGHT)

    if OUTCOME is not None:
        canvas.draw_text(
            OUTCOME,
            ((FRAME_WIDTH -
              FRAME.get_canvas_textwidth(OUTCOME, FONT_SIZE)) / 2.0,
             250), FONT_SIZE, 'WHITE')

    if DECK is not None:
        text = 'SCORE: %d | %d' % (SCORE_DEALER, SCORE_PLAYER)
        canvas.draw_text(text,
                         ((FRAME_WIDTH -
                           FRAME.get_canvas_textwidth(text, FONT_SIZE) - 20),
                          20 + FONT_SIZE * 3 / 4.0),
                         FONT_SIZE, 'Black')

        assert isinstance(HAND_DEALER, Hand)
        assert isinstance(HAND_PLAYER, Hand)

        HAND_DEALER.draw(canvas, DEALER_POS)
        HAND_PLAYER.draw(canvas, PLAYER_POS)


def draw_wait_images(canvas):  # type: (simplegui.Canvas) -> None
    """
    Draw waiting message when images loading.

    :param canvas: simplegui.Canvas
    """
    percent = NB_IMAGES_LOADED * 100.0 / NB_IMAGES_TO_LOAD

    canvas.draw_line((0, 150), (FRAME_WIDTH, 150), 20, 'White')
    if percent > 0:
        canvas.draw_line((0, 150), (FRAME_WIDTH * percent / 100.0, 150),
                         20, 'Green')

    size = 50
    canvas.draw_text('Loading... %d%%' % int(percent),
                     (10, 80 + size * 3 / 4.0),
                     size, 'White')


def hit():  # type: () -> None
    """
    Give a new card to the player
    and deal his value.
    """
    global IN_PLAY  # pylint: disable=global-statement
    global OUTCOME  # pylint: disable=global-statement
    global SCORE_DEALER  # pylint: disable=global-statement

    assert isinstance(DECK, Deck)
    assert isinstance(HAND_PLAYER, Hand)

    OUTCOME = None

    if IN_PLAY:
        HAND_PLAYER.add_card(DECK.deal_card())

        if HAND_PLAYER.get_value() > 21:
            IN_PLAY = False
            OUTCOME = 'YOU HAVE BUSTED'
            SCORE_DEALER += 1
    elif (DECK is not None) and (HAND_PLAYER.get_value() > 21):
        OUTCOME = 'YOU HAVE BUSTED'


def stand():  # type: () -> None
    """
    The player stand.
    Deal the dealer logic and test who win.
    """
    global IN_PLAY  # pylint: disable=global-statement
    global OUTCOME  # pylint: disable=global-statement
    global SCORE_DEALER  # pylint: disable=global-statement
    global SCORE_PLAYER  # pylint: disable=global-statement

    assert isinstance(DECK, Deck)
    assert isinstance(HAND_DEALER, Hand)
    assert isinstance(HAND_PLAYER, Hand)

    OUTCOME = None

    if IN_PLAY:
        while HAND_DEALER.get_value() < 17:
            HAND_DEALER.add_card(DECK.deal_card())

        IN_PLAY = False

        if HAND_PLAYER.get_value() <= HAND_DEALER.get_value() <= 21:
            OUTCOME = 'YOU LOOSE'
            SCORE_DEALER += 1
        else:
            OUTCOME = 'YOU WIN'
            SCORE_PLAYER += 1
    elif (DECK is not None) and (HAND_PLAYER.get_value() > 21):
        OUTCOME = 'YOU HAVE BUSTED'


def test_images_loaded():  # type: () -> None
    """
    Check the number of images already loaded.

    Global change: NB_IMAGES_LOADED
    """
    global MAX_TEST_IMAGES_LOADED  # pylint: disable=global-statement
    global NB_IMAGES_LOADED  # pylint: disable=global-statement

    NB_IMAGES_LOADED = sum([1 for img in [CARD_BACK, CARDS_IMAGE]
                            if img.get_width() > 0])

    if ((NB_IMAGES_LOADED == NB_IMAGES_TO_LOAD) or
            (MAX_TEST_IMAGES_LOADED <= 0)):
        TIMER.stop()
        FRAME.set_draw_handler(draw)

    MAX_TEST_IMAGES_LOADED -= 1


# Main
######
if __name__ == '__main__':
    # Create frame
    FRAME = simplegui.create_frame('Blackjack', FRAME_WIDTH, FRAME_HEIGHT, 100)

    # Control panel
    FRAME.add_button('Deal', deal, 100)
    FRAME.add_label('')
    FRAME.add_button('Hit', hit, 100)
    FRAME.add_label('')
    FRAME.add_button('Stand', stand, 100)
    FRAME.add_label('')
    FRAME.add_label('')
    FRAME.add_button('Quit', FRAME.stop)

    # Register event handlers
    FRAME.set_draw_handler(draw_wait_images)

    TIMER = simplegui.create_timer(100, test_images_loaded)
    TIMER.start()
    test_images_loaded()

    deal()

    FRAME.start()
