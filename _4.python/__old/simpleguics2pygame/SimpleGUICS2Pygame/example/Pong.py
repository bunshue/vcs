#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Pong game.

My retouched solution of the mini-project #4 of the MOOC
https://www.coursera.org/learn/interactive-python-1 (Coursera 2013).

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2014, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 20, 2020
"""

import math
import random

try:
    from typing import List, Optional, Tuple, Union
except ImportError:
    pass

try:
    import simplegui  # pytype: disable=import-error

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore
    import SimpleGUICS2Pygame.simpleguics2pygame._joypads as _joypads

    simplegui.Frame._cursor_auto_hide = True  # pylint: disable=protected-access  # noqa
    simplegui.Frame._hide_status = True  # pylint: disable=protected-access
    simplegui.Frame._keep_timers = False  # pylint: disable=protected-access

    SIMPLEGUICS2PYGAME = True


DEBUG = False
# DEBUG = True  # to help debug


PONG = None  # Optional['Pong']


# Classes
class Vector:
    """Vector (self.x, self.y)."""

    def __init__(self, x, y):
        # type: (Union[int, float], Union[int, float]) -> None
        """
        Initialize the vector.

        :param x: int or float
        :param y: int or float
        """
        assert isinstance(x, (int, float))
        assert isinstance(y, (int, float))

        self.x = x
        self.y = y

    def add(self, other):  # type: ('Vector') -> None
        """
        Add other to self.

        :param other: Vector
        """
        assert isinstance(other, Vector)

        self.x += other.x
        self.y += other.y

    def mul_scalar(self, scalar):  # type: (Union[int, float]) -> None
        """
        Multiply self by scalar.

        :param scalar: int or float
        """
        assert isinstance(scalar, (int, float))

        self.x *= scalar
        self.y *= scalar

    def distance(self, other):  # type: ('Vector') -> float
        """
        Return the distance between self and other.

        :param other: Vector

        :return: float >= 0
        """
        assert isinstance(other, Vector)

        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def same(self, other):  # type: ('Vector') -> bool
        """
        If (self.x, self.y) == (other.x, other.y)
        then return True,
        else return False.

        :param other: Vector
        """
        assert isinstance(other, Vector)

        return (self.x == other.x) and (self.y == other.y)

    def to_tuple(self):
        # type: () -> Tuple[Union[int, float], Union[int, float]]
        """
        Return the vector as a tuple.

        :return: (int or float, int or float)
        """
        return (self.x, self.y)


class Pong:
    """
    Game Pong.

    Size of the screen (Pong.WIDTH, Pong.HEIGHT).
    Half size: (Pong.HALF_WIDTH, Pong.HALF_HEIGHT)
    """

    WIDTH = 600
    HEIGHT = 400

    HALF_WIDTH = WIDTH // 2
    HALF_HEIGHT = HEIGHT // 2

    def __init__(self):  # type: () -> None
        """Initialize the game with one ball."""
        self.current_radius = 20

        self.balls = []  # type: List['Ball']
        self.balls_to_launch = [Ball(self.current_radius)]
        self.players = (Player(False, 'w', 's'), Player(True, 'up', 'down'))

        self.paused = False

    def add_ball(self, radius=None, right=None):
        # type: (Optional[int], Optional[bool]) -> None
        """
        Add a new ball.

        If radius is None
        then add a smaller ball (minimum radius == 10),
        else add a ball with radius.

        :param radius: int > 0
        :param right: None or bool
        """
        assert (radius is None) or (isinstance(radius, int) and (radius > 0))
        assert (right is None) or isinstance(right, bool)

        if radius is None:
            if self.current_radius >= 11:
                self.current_radius -= 1
            self.balls_to_launch.append(Ball(self.current_radius, right))
        else:
            self.balls_to_launch.append(Ball(radius, right))

    def pause(self):  # type: () -> None
        """Swicth on/off the pause."""
        self.paused = not self.paused


class MovingItem:
    """
    General moving item:
    self.pos: position Vector
    self.vel: velocity Vector
    """

    def __init__(self, position, velocity=None):
        # type: (Vector, Optional[Vector]) -> None
        """
        Initialize the position and the velocity.

        If velocity is None
        then set to Vector(0, 0).

        :param position: Vector
        :param velocity: None or Vector
        """
        assert isinstance(position, Vector)
        assert (velocity is None) or isinstance(velocity, Vector)

        self.pos = position
        self.vel = (Vector(0, 0) if velocity is None
                    else velocity)

    def bounce(self, horizontally=True, vertically=True):
        # type: (bool, bool) -> None
        """
        If horizontally
        then invert horizontal velocity.

        If vertically
        then invert vertical velocity.

        :param horizontally: bool
        :param vertically: bool
        """
        assert isinstance(horizontally, bool)
        assert isinstance(vertically, bool)

        if horizontally:
            self.vel.x = -self.vel.x
        if vertically:
            self.vel.y = -self.vel.y

    def same_pos(self, other):  # type: ('MovingItem') -> bool
        """
        If self and other are same position
        then return True,
        else return False.

        :param other: MovingItem
        """
        assert isinstance(other, MovingItem)

        return self.pos.same(other.pos)

    def same_vel_horizontal(self, other):  # type: ('MovingItem') -> bool
        """
        If self and other are the same horizontally direction
        then return True,
        else return False.

        :param other: MovingItem
        """
        assert isinstance(other, MovingItem)

        return ((self.vel.x > 0 and other.vel.x > 0) or
                (self.vel.x < 0 and other.vel.x < 0) or
                (self.vel.x == 0 and other.vel.x == 0))

    def same_vel_vertical(self, other):  # type: ('MovingItem') -> bool
        """
        If self and other are the same vertically direction
        then return True,
        else return False.

        :param other: MovingItem
        """
        assert isinstance(other, MovingItem)

        return ((self.vel.y > 0 and other.vel.y > 0) or
                (self.vel.y < 0 and other.vel.y < 0) or
                (self.vel.y == 0 and other.vel.y == 0))

    def update_pos(self):  # type: () -> None
        """Add self.vel to self.pos."""
        self.pos.add(self.vel)


class Ball(MovingItem):
    """Ball."""

    SPEED_MAX_X = 20
    SPEED_MAX_Y = 20

    def __init__(self, radius, right=None):
        # type: (int, Optional[bool]) -> None
        """
        Initialize the position at middle of screen
        and the velocity at random top up.

        If right is None
        then choice randomly a right.

        If right
        then velocity goes to right,
        else goes to left.

        :param radius: int > 0
        :param right: None or bool
        """
        assert isinstance(radius, int)
        assert radius > 0, radius

        if right is None:
            right = random.choice((False, True))

        assert isinstance(right, bool)

        vel_x = random.randrange(120, 240) / 60.0

        MovingItem.__init__(self,
                            Vector(Pong.HALF_WIDTH, Pong.HALF_HEIGHT),
                            Vector((vel_x if right
                                    else -vel_x),
                                   (random.randrange(60, 180) / 60.0 *
                                    random.choice((-1, 1)))))
        self.radius = radius

    def check_collision(self):  # pylint: disable=too-many-branches,too-many-statements  # noqa
        # type: () -> None
        """
        If the ball touch the top or the bottom of the screen
        then bounce vertically.

        If the ball touch the paddle
        then bounce horizontally and increase velocity,
        else if the ball touch gutter
        then increment the score and reinit the ball.

        If the ball touch *newest* ball
        then both "bounce".
        """
        assert isinstance(PONG, Pong)

        if self.vel.y < 0:    # top
            if self.pos.y <= self.radius:
                SOUND_BOUNCE_BORDER.play()
                self.bounce(False)
        elif self.vel.y > 0:  # bottom
            if self.pos.y >= Pong.HEIGHT - 1 - self.radius:
                SOUND_BOUNCE_BORDER.play()
                self.bounce(False)

        if self.vel.x < 0:    # left
            if self.pos.x <= Player.WIDTH + self.radius:
                if ((PONG.players[0].pos.y - Player.HALF_HEIGHT <=
                     self.pos.y <=
                     PONG.players[0].pos.y + Player.HALF_HEIGHT) or
                        PONG.players[0].protected):
                    SOUND_BOUNCE_PADDLE.play()
                    self.bounce(vertically=False)
                    self.faster()
                else:  # left player lost
                    SOUND_LOST.play()
                    PONG.players[1].score += 1
                    for i in range(len(PONG.balls)):
                        if PONG.balls[i] == self:
                            del PONG.balls[i]

                            break
                    PONG.add_ball(self.radius, True)
        elif self.vel.x > 0:  # right
            if self.pos.x >= Pong.WIDTH - 1 - self.radius - Player.WIDTH:
                if ((PONG.players[1].pos.y - Player.HALF_HEIGHT <=
                     self.pos.y <=
                     PONG.players[1].pos.y + Player.HALF_HEIGHT) or
                        PONG.players[1].protected):
                    SOUND_BOUNCE_PADDLE.play()
                    self.bounce(vertically=False)
                    self.faster()
                else:  # right player lost
                    SOUND_LOST.play()
                    PONG.players[0].score += 1
                    for i in range(len(PONG.balls)):
                        if PONG.balls[i] == self:
                            del PONG.balls[i]

                            break
                    PONG.add_ball(self.radius, False)

        if len(PONG.balls) > 1:
            founded = False
            for ball in PONG.balls:
                if founded:
                    if self.touch(ball):
                        # Elastic collision (with radius as mass)
                        SOUND_BALLS_COLLISION.play()
                        radius_sum = self.radius + ball.radius
                        radius_diff = self.radius - ball.radius

                        double = 2 * ball.radius
                        new_x = float(radius_diff * self.vel.x +
                                      double * ball.vel.x) / radius_sum
                        new_y = float(radius_diff * self.vel.y +
                                      double * ball.vel.y) / radius_sum

                        double = 2 * self.radius
                        ball.vel.x = (float(double * self.vel.x -
                                            radius_diff * ball.vel.x) /
                                      radius_sum)
                        ball.vel.y = (float(double * self.vel.y -
                                            radius_diff * ball.vel.y) /
                                      radius_sum)

                        self.vel.x = new_x
                        self.vel.y = new_y
                elif self.same_pos(ball):
                    founded = True

    def draw(self, canvas):  # type: (simplegui.Canvas) -> None
        """
        Draw the ball.

        :param canvas: simplegui.Canvas
        """
        for i in range(self.radius, 2, -2):
            color = 255 - 10 * i
            color_str = '#' + ('0' + hex(color)[-1] if color < 16
                               else hex(color)[-2:]) * 3
            canvas.draw_circle(self.pos.to_tuple(), i, 1, color_str, color_str)

        if DEBUG:
            canvas.draw_line((self.pos.x - self.radius, self.pos.y),
                             (self.pos.x + self.radius, self.pos.y), 1, 'Red')

    def faster(self):  # type: () -> None
        """
        Increase velocity by 10
        (with maximum (Ball.SPEED_MAX_X, Ball.SPEED_MAX_Y))
        """
        self.vel.mul_scalar(1.1)

        neg = (self.vel.x < 0)
        self.vel.x = min(Ball.SPEED_MAX_X, abs(self.vel.x))
        if neg:
            self.vel.x = -self.vel.x

        neg = (self.vel.y < 0)
        self.vel.y = min(Ball.SPEED_MAX_Y, abs(self.vel.y))
        if neg:
            self.vel.y = -self.vel.y

    def touch(self, other):  # type: (Ball) -> bool
        """
        If two balls touch
        then return True,
        else return False.

        :param other: Ball

        :return: bool
        """
        return self.pos.distance(other.pos) <= (self.radius + other.radius)


class Player(MovingItem):
    """
    Player left or right.

    Paddle of size (Player.WIDTH, Player.HEIGHT).
    Half size: (Player.HALF_WIDTH, Player.HALF_HEIGHT)

    Vertical velocity: Player.SPEED
    """

    WIDTH = 8
    HEIGHT = 80

    HALF_WIDTH = WIDTH // 2
    HALF_HEIGHT = HEIGHT // 2

    SPEED = 5

    def __init__(self, right, key_up, key_down):
        # type: (bool, str, str) -> None
        """
        Initialize the player (right or not) with his keys.

        :param right: bool
        :param key_up: str contains in simplegui.KEY_MAP
        :param key_down: str contains in simplegui.KEY_MAP
        """
        assert isinstance(right, bool)
        assert isinstance(key_up, str)
        assert isinstance(key_down, str)

        MovingItem.__init__(self, Vector((Pong.WIDTH - 1 - Player.HALF_WIDTH
                                          if right
                                          else Player.HALF_WIDTH),
                                         Pong.HALF_HEIGHT))

        self.key_up = simplegui.KEY_MAP[key_up]
        self.key_down = simplegui.KEY_MAP[key_down]

        self.key_up_active = False
        self.key_down_active = False

        self.score = 0

        self.protected = False

    def draw(self, canvas):  # type: (simplegui.Canvas) -> None
        """
        Draw the paddle.

        :param canvas: simplegui.Canvas
        """
        y1 = self.pos.y - Player.HALF_HEIGHT
        canvas.draw_line((self.pos.x, y1), (self.pos.x, y1 + Player.HEIGHT),
                         Player.WIDTH, 'White')

        if DEBUG:
            canvas.draw_line((self.pos.x - Player.WIDTH,
                              self.pos.y - Player.HALF_HEIGHT),
                             (self.pos.x + Player.WIDTH,
                              self.pos.y - Player.HALF_HEIGHT), 1, 'Red')
            canvas.draw_line((self.pos.x - Player.WIDTH,
                              self.pos.y + Player.HALF_HEIGHT),
                             (self.pos.x + Player.WIDTH,
                              self.pos.y + Player.HALF_HEIGHT), 1, 'Red')

    def protect(self):  # type: () -> None
        """Switch protected parameter."""
        self.protected = not self.protected

    def update_pos(self):  # type: () -> None
        """
        If possible
        then add self.vel to self.pos,
        else no move.
        """
        MovingItem.update_pos(self)

        if self.pos.y < Player.HALF_HEIGHT:
            self.pos.y = Player.HALF_HEIGHT
        elif self.pos.y > Pong.HEIGHT - 1 - Player.HALF_HEIGHT:
            self.pos.y = Pong.HEIGHT - 1 - Player.HALF_HEIGHT

    def update_vel(self):  # type: () -> None
        """
        If self.vel == 0 and a key is down
        then set the good velocity.
        """
        if self.vel.y == 0:
            if self.key_up_active:
                self.vel.y = -Player.SPEED
            elif self.key_down_active:
                self.vel.y = Player.SPEED


# Event handlers
def add_ball():  # type: () -> None
    """Add one ball to the game."""
    assert isinstance(PONG, Pong)

    PONG.add_ball()


def draw(canvas):  # type: (simplegui.Canvas) -> None
    """
    Event handler to draw all items.

    :param canvas: simplegui.Canvas
    """
    assert isinstance(PONG, Pong)

    # Mid line
    canvas.draw_line((Pong.HALF_WIDTH, 0), (Pong.HALF_WIDTH, Pong.HEIGHT),
                     1, 'White')

    # Gutters
    canvas.draw_line((Player.WIDTH, 0), (Player.WIDTH, Pong.HEIGHT),
                     1, ('Red' if PONG.players[0].protected
                         else 'White'))
    x = Pong.WIDTH - 1 - Player.WIDTH
    canvas.draw_line((x, 0), (x, Pong.HEIGHT),
                     1, ('Red' if PONG.players[1].protected
                         else 'White'))

    # Scores
    size = 60
    text = str(PONG.players[0].score)
    canvas.draw_text(text,
                     (Pong.HALF_WIDTH - 100 - FRAME.get_canvas_textwidth(text,
                                                                         size),
                      100),
                     size, 'Green')
    canvas.draw_text(str(PONG.players[1].score), (Pong.HALF_WIDTH + 100, 100),
                     size, 'Green')

    if not PONG.paused:
        # Players
        for player in PONG.players:
            player.update_pos()
            player.draw(canvas)

        # Ball
        for ball in PONG.balls:
            ball.update_pos()
            ball.draw(canvas)
            ball.check_collision()


def joypad_axe(joypad, axe, value):  # type: (int, int, float) -> None
    """
    Event handler to deal joypad axe.

    :param joypad: int >= 0
    :param axe: int >= 0
    :param value: -1 <= float <= 1
    """
    assert isinstance(PONG, Pong)

    if axe == 1:
        threshold = 0.7

        if joypad == 0:
            if value <= -threshold:   # player 0 up
                PONG.players[0].key_up_active = True
                PONG.players[0].vel.y = -Player.SPEED
                PONG.players[0].update_vel()
            elif value >= threshold:  # player 0 down
                PONG.players[0].key_down_active = True
                PONG.players[0].vel.y = Player.SPEED
                PONG.players[0].update_vel()
            else:                     # player 0 clear movement
                PONG.players[0].key_up_active = False
                PONG.players[0].key_down_active = False
                PONG.players[0].vel.y = 0
                PONG.players[0].update_vel()
        elif joypad == 1:
            if value <= -threshold:   # player 1 up
                PONG.players[1].key_up_active = True
                PONG.players[1].vel.y = -Player.SPEED
                PONG.players[1].update_vel()
            elif value >= threshold:  # player 1 down
                PONG.players[1].key_down_active = True
                PONG.players[1].vel.y = Player.SPEED
                PONG.players[1].update_vel()
            else:                     # player 1 clear movement
                PONG.players[1].key_up_active = False
                PONG.players[1].key_down_active = False
                PONG.players[1].vel.y = 0
                PONG.players[1].update_vel()


def joypad_up(joypad, button):  # type: (int, int) -> None
    """
    Event handler to deal joypad buttons.

    :param joypad: int >= 0
    :param button: int >= 0
    """
    if (joypad in (0, 1)) and (button == 0):
        add_ball()


def joypad_hat(joypad, hat, values):
    # type: (int, int, Tuple[int, int]) -> None
    """
    Event handler to deal joypad hat.

    :param joypad: int >= 0
    :param hat: int >= 0
    :param values: (a, b) with a and b == -1, 0 or 1
    """
    assert isinstance(PONG, Pong)

    if hat == 0:
        if joypad == 0:
            if values[1] == 1:     # player 0 up
                PONG.players[0].key_up_active = True
                PONG.players[0].vel.y = -Player.SPEED
                PONG.players[0].update_vel()
            elif values[1] == -1:  # player 0 down
                PONG.players[0].key_down_active = True
                PONG.players[0].vel.y = Player.SPEED
                PONG.players[0].update_vel()
            elif values[1] == 0:   # player 0 clear movement
                PONG.players[0].key_up_active = False
                PONG.players[0].key_down_active = False
                PONG.players[0].vel.y = 0
                PONG.players[0].update_vel()
        elif joypad == 1:
            if values[1] == 1:     # player 1 up
                PONG.players[1].key_up_active = True
                PONG.players[1].vel.y = -Player.SPEED
                PONG.players[1].update_vel()
            elif values[1] == -1:  # player 1 down
                PONG.players[1].key_down_active = True
                PONG.players[1].vel.y = Player.SPEED
                PONG.players[1].update_vel()
            elif values[1] == 0:   # player 1 clear movement
                PONG.players[1].key_up_active = False
                PONG.players[1].key_down_active = False
                PONG.players[1].vel.y = 0
                PONG.players[1].update_vel()


def keydown(key):  # type: (int) -> None
    """
    Event handler to deal key down.

    :param key: int >= 0
    """
    assert isinstance(PONG, Pong)

    if key == PONG.players[0].key_up:      # player 0 up
        PONG.players[0].key_up_active = True
        PONG.players[0].vel.y = -Player.SPEED
        PONG.players[0].update_vel()
    elif key == PONG.players[0].key_down:  # player 0 down
        PONG.players[0].key_down_active = True
        PONG.players[0].vel.y = Player.SPEED
        PONG.players[0].update_vel()
    elif key == PONG.players[1].key_up:    # player 1 up
        PONG.players[1].key_up_active = True
        PONG.players[1].vel.y = -Player.SPEED
        PONG.players[1].update_vel()
    elif key == PONG.players[1].key_down:  # player 1 down
        PONG.players[1].key_down_active = True
        PONG.players[1].vel.y = Player.SPEED
        PONG.players[1].update_vel()


def keyup(key):  # type: (int) -> None
    """
    Event handler to deal key up.

    :param key: int >= 0
    """
    assert isinstance(PONG, Pong)

    if key == PONG.players[0].key_up:      # player 0 clear up
        PONG.players[0].key_up_active = False
        PONG.players[0].vel.y = 0
        PONG.players[0].update_vel()
    elif key == PONG.players[0].key_down:  # player 0 clear down
        PONG.players[0].key_down_active = False
        PONG.players[0].vel.y = 0
        PONG.players[0].update_vel()
    elif key == PONG.players[1].key_up:    # player 1 clear up
        PONG.players[1].key_up_active = False
        PONG.players[1].vel.y = 0
        PONG.players[1].update_vel()
    elif key == PONG.players[1].key_down:  # player 1 clear down
        PONG.players[1].key_down_active = False
        PONG.players[1].vel.y = 0
        PONG.players[1].update_vel()


def launch_ball():  # type: () -> None
    """Add a prepared ball (if not in pause)."""
    assert isinstance(PONG, Pong)

    if PONG.balls_to_launch and not PONG.paused:
        PONG.balls.append(PONG.balls_to_launch.pop(0))


def pause():  # type: () -> None
    """Event handler to deal click on pause button."""
    assert isinstance(PONG, Pong)

    PONG.pause()
    BUTTON_PAUSE.set_text('Pause ' + ('off' if PONG.paused
                                      else 'on'))


def protect_left():  # type: () -> None
    """Event handler to deal click on protect left button."""
    assert isinstance(PONG, Pong)

    PONG.players[0].protect()
    BUTTON_PROTECT_LEFT.set_text(('Unprotect' if PONG.players[0].protected
                                  else 'Protect') + ' left player')


def protect_right():  # type: () -> None
    """Event handler to deal click on protect right button."""
    assert isinstance(PONG, Pong)

    PONG.players[1].protect()
    BUTTON_PROTECT_RIGHT.set_text(('Unprotect' if PONG.players[1].protected
                                   else 'Protect') + ' right player')


def quit_prog():  # type: () -> None
    """Stop timer and quit."""
    TIMER.stop()
    FRAME.stop()


def restart():  # type: () -> None
    """Event handler to deal click on restart button."""
    global PONG  # pylint: disable=global-statement

    PONG = Pong()
    BUTTON_PAUSE.set_text('Pause on')
    BUTTON_PROTECT_LEFT.set_text('Protect left player')
    BUTTON_PROTECT_RIGHT.set_text('Protect right player')

    if SIMPLEGUICS2PYGAME and (_joypads._joypad_nb > 0):  # pylint: disable=protected-access  # noqa
        protect_right()
    else:
        protect_left()


# Create frame
FRAME = simplegui.create_frame('Pong', Pong.WIDTH, Pong.HEIGHT)

# Sounds
SOUND_BALLS_COLLISION = simplegui.load_sound(
    'http://rpg.hamsterrepublic.com/wiki-images/7/72/Metal_Hit.ogg')
SOUND_BOUNCE_BORDER = simplegui.load_sound(
    'http://rpg.hamsterrepublic.com/wiki-images/2/21/Collision8-Bit.ogg')
SOUND_BOUNCE_PADDLE = simplegui.load_sound(
    'http://rpg.hamsterrepublic.com/wiki-images/d/d7/Oddbounce.ogg')
SOUND_LOST = simplegui.load_sound(
    'http://rpg.hamsterrepublic.com/wiki-images/d/db/Crush8-Bit.ogg')

# Register event handlers
FRAME.add_button('Restart', restart, 200)
FRAME.add_label('')
BUTTON_PAUSE = FRAME.add_button('Pause on', pause, 200)
FRAME.add_label('')
BUTTON_PROTECT_LEFT = FRAME.add_button('Protect left player',
                                       protect_left, 200)
BUTTON_PROTECT_RIGHT = FRAME.add_button('Protect right player',
                                        protect_right, 200)
FRAME.add_label('')
FRAME.add_button('Add ball', add_ball, 200)
FRAME.add_label('')
FRAME.add_button('Quit', quit_prog)
FRAME.add_label('')
FRAME.add_label('Left player keys: W (or Z), S')
FRAME.add_label('Right player keys: Up, Down')


FRAME.set_keydown_handler(keydown)
FRAME.set_keyup_handler(keyup)

if SIMPLEGUICS2PYGAME:
    if simplegui._joypads._joypad_nb > 0:  # pylint: disable=protected-access
        FRAME._set_joypadaxe_handler(joypad_axe)  # pylint: disable=protected-access  # noqa
        FRAME._set_joypadup_handler(joypad_up)  # pylint: disable=protected-access  # noqa
        FRAME._set_joypadhat_handler(joypad_hat)  # pylint: disable=protected-access  # noqa

    FRAME.add_label('')
    FRAME.add_label('%i joypad%s available' %
                    (simplegui._joypads._joypad_nb,  # pylint: disable=protected-access  # noqa
                     ('s' if simplegui._joypads._joypad_nb > 1  # pylint: disable=protected-access  # noqa
                      else '')))

FRAME.set_draw_handler(draw)

TIMER = simplegui.create_timer(1000, launch_ball)


# Main
restart()

TIMER.start()

FRAME.start()
