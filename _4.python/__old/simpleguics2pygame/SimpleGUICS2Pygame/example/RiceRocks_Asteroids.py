#!/usr/bin/env python
# -*- coding: latin-1 -*-
# pylint: disable=invalid-name,too-many-lines

"""
RiceRocks (Asteroids) game.

My retouched solution of the mini-project #8 of the MOOC
https://www.coursera.org/learn/interactive-python-2 (Coursera 2013).

Run on (maybe very slow on some browsers):
  - Python 2 and 3 with SimpleGUICS2Pygame: best environment
  - Chrome 31 on CodeSkulptor
  - Chromium 73.0 on CodeSkulptor and CodeSkulptor3: no OGG sounds
  - Firefox 26 on CodeSkulptor: probably slow
  - Firefox 68.5 on CodeSkulptor and CodeSkulptor3: probably slow
  - Opera 67.0 on CodeSkulptor and CodeSkulptor3: maybe slow
  - Safari 5.1.7 on CodeSkulptor: no OGG sounds

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2015, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 21, 2020
"""

import math
import random

try:
    from typing import Dict, List, Optional, Sequence, Tuple, Union
except ImportError:
    pass

try:
    from user305_SXBsmszNiUxIeoV import assert_position  # pytype: disable=import-error  # noqa
    from user305_tXfH4AcbNLtjfHy import FPS  # pytype: disable=import-error
    from user305_SZPJfNxJlVTjbAy import Loader  # pytype: disable=import-error

    import simplegui  # pytype: disable=import-error

    SIMPLEGUICS2PYGAME = False
except ImportError:
    from SimpleGUICS2Pygame.codeskulptor_lib import assert_position
    from SimpleGUICS2Pygame.simplegui_lib_fps import FPS
    from SimpleGUICS2Pygame.simplegui_lib_loader import Loader

    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore

    simplegui.Frame._hide_status = True  # pylint: disable=protected-access
    simplegui.Frame._keep_timers = False  # pylint: disable=protected-access

    SIMPLEGUICS2PYGAME = True


#
# Global constants
###################
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


#
# Global variables
###################
FRAME = None  # type: Optional[simplegui.Frame]

RICEROCKS = None  # type: Optional['RiceRocks']


#
# Helper functions
###################
def angle_to_vector(angle):  # type: (Union[int, float]) -> Tuple[float, float]
    """
    Return the vector corresponding to the angle expressed in radians.

    :param angle: int or float

    :return: (-1 <= float <= 1, -1 <= float <= 1)
    """
    assert isinstance(angle, (int, float)), type(angle)

    return (math.cos(angle), math.sin(angle))


def vector_to_angle(vector):  # type: (Sequence[Union[int, float]]) -> float
    """
    Return the angle (in radians) corresponding to the direction of vector.

    :param vector: (int or float, int or float)
                   or [int or float, int or float]

    :return: -math.pi <= float <= math.pi
    """
    assert_position(vector)

    return math.atan2(vector[1], vector[0])


#
# Classes
##########
class RiceRocks:  # pylint: disable=too-many-instance-attributes
    """General class dealing the game."""

    def __init__(self):  # type: () -> None
        """Set elements of the game."""
        self.loaded = False

        self.keydown_left = False
        self.keydown_right = False
        self.lives = 3
        self.my_ship = None  # type: Optional['Ship']
        self.nb_bombs = None  # type: Optional[int]
        self.score = 0
        self.started = False
        self.time = 0

        self.explosions = []  # type: List['Sprite']
        self.live_explosions = []  # type: List['Sprite']
        self.missiles = []  # type: List['Sprite']
        self.rocks = []  # type: List['Asteroid']

        self.animate_background_active = True
        self.music_active = True
        self.sounds_active = True
        self.timer = simplegui.create_timer(1000, self.rock_spawner)

        self.paused = False

        self.wait = False

        def wait_clear():
            """Disable waiting."""
            self.wait = False

        self.timer_wait = simplegui.create_timer(2000, wait_clear)

        self.img_infos = None  # type: Optional[Dict[str, 'ImageInfo']]
        self.medias = None

    def bomb_explode(self):  # type: () -> None
        """
        If it remains bomb
        then detonated a bomb that destroys all asteroids.
        """
        if self.nb_bombs:
            assert isinstance(self.medias, Loader)

            self.nb_bombs -= 1
            if self.sounds_active:
                self.medias.get_sound('bomb_explode').rewind()
                self.medias.get_sound('bomb_explode').play()
            for rock in self.rocks:
                self.explosions.append(Sprite(rock.position, rock.velocity,
                                              0, rock.angle_velocity,
                                              'asteroid_explosion'))
            self.rocks = []

    def draw_and_update(self, canvas):  # pylint: disable=too-many-locals,too-many-branches,too-many-statements  # noqa
        # type: (simplegui.Canvas) -> None
        """
        Draw and update all stuffs in each FPS cycle.

        :param canvas: simplegui.Canvas
        """
        assert isinstance(FRAME, simplegui.Frame)
        assert isinstance(self.img_infos, dict)
        assert isinstance(self.medias, Loader)
        assert isinstance(self.my_ship, Ship)

        self.time += 1

        # Draw static background
        if not SIMPLEGUICS2PYGAME:
            canvas.draw_image(self.medias.get_image('nebula'),
                              self.img_infos['nebula'].get_center(),
                              self.img_infos['nebula'].get_size(),
                              (SCREEN_WIDTH / 2.0, SCREEN_HEIGHT / 2.0),
                              (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Draw animated background
        if self.animate_background_active and not self.paused:
            center = self.img_infos['debris'].get_center()
            size_xy = self.img_infos['debris'].get_size()

            wtime = (self.time / 4.0) % SCREEN_WIDTH

            canvas.draw_image(self.medias.get_image('debris'),
                              center,
                              size_xy,
                              (wtime - SCREEN_WIDTH / 2.0,
                               SCREEN_HEIGHT / 2.0),
                              (SCREEN_WIDTH, SCREEN_HEIGHT))
            canvas.draw_image(self.medias.get_image('debris'),
                              center,
                              size_xy,
                              (wtime + SCREEN_WIDTH / 2.0,
                               SCREEN_HEIGHT / 2.0),
                              (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Draw missiles, ship, asteroids and explosions
        for missile in self.missiles:
            missile.draw(canvas)

        if self.lives > 0:
            self.my_ship.draw(canvas)

        for rock in self.rocks:
            rock.draw(canvas)

        for i in range(len(self.explosions) - 1, -1, -1):
            explosion = self.explosions[i]

            explosion.draw(canvas)
            explosion.update()
            if explosion.lifespan <= 0:  # explosion finished
                del self.explosions[i]

        if self.paused:
            return

        # Update ship
        self.my_ship.update()

        # Update missiles
        for i in range(len(self.missiles) - 1, -1, -1):  # pylint: disable=too-many-nested-blocks  # noqa
            missile = self.missiles[i]

            missile.update()
            if missile.lifespan <= 0:  # missile disappear
                del self.missiles[i]
            else:                      # active missile
                for j in range(len(self.rocks) - 1, -1, -1):
                    # Check collide with asteroids
                    rock = self.rocks[j]

                    if missile.collide(rock):  # collide
                        del self.missiles[i]
                        del self.rocks[j]

                        if not rock.little:
                            # Divide in two little asteroids
                            angle = vector_to_angle(missile.velocity)
                            mvel = math.sqrt(
                                (rock.velocity[0] * rock.velocity[0] +
                                 rock.velocity[1] * rock.velocity[1]) / 2.0)

                            vel = list(angle_to_vector(angle - math.pi / 4))
                            vel[0] *= mvel
                            vel[1] *= mvel
                            little1 = Asteroid(rock.position, vel,
                                               rock.angle_velocity * 2,
                                               rock.num, True)

                            vel = list(angle_to_vector(angle + math.pi / 4))
                            vel[0] *= mvel
                            vel[1] *= mvel
                            little2 = Asteroid(rock.position, vel,
                                               -rock.angle_velocity * 2,
                                               rock.num, True)

                            while True:
                                little1.position[0] += little1.velocity[0]
                                little1.position[1] += little1.velocity[1]
                                little2.position[0] += little2.velocity[0]
                                little2.position[1] += little2.velocity[1]
                                if not little1.collide(little2):
                                    break
                            self.rocks.extend((little1, little2))

                        self.score += 1
                        if self.score % 10 == 0:  # add a new bomb
                            assert isinstance(self.nb_bombs, int)

                            self.nb_bombs += 1
                            if self.sounds_active:
                                self.medias.get_sound('bomb_extra').rewind()
                                self.medias.get_sound('bomb_extra').play()
                            if self.score % 50 == 0:  # add a new live
                                self.lives += 1

                        self.explosions.append(Sprite(rock.position,
                                                      rock.velocity,
                                                      0, rock.angle_velocity,
                                                      'asteroid_explosion'))

                        break

        # Update asteroids
        for i in range(len(self.rocks) - 1, -1, -1):
            rock = self.rocks[i]

            rock.update()
            if self.my_ship.collide(rock):  # collide with ship
                del self.rocks[i]

                self.explosions.append(Sprite(rock.position, rock.velocity,
                                              0, rock.angle_velocity,
                                              'asteroid_collide_explosion'))
                self.live_explosions.append(Sprite((self.lives * 40, 40),
                                                   (0, 0),
                                                   -math.pi / 2, 0,
                                                   'live_explosion'))

                self.lives = max(0, self.lives - 1)
                if self.lives <= 0:  # game over  # pylint: disable=no-else-break  # noqa
                    self.stop()

                    self.explosions.append(Sprite(self.my_ship.position,
                                                  self.my_ship.velocity,
                                                  0,
                                                  self.my_ship.angle_velocity,
                                                  'ship_explosion'))

                    if self.sounds_active:
                        self.medias.get_sound('death').rewind()
                        self.medias.get_sound('death').play()

                    break
                else:
                    if self.sounds_active:
                        self.medias.get_sound('collide').rewind()
                        self.medias.get_sound('collide').play()
            else:
                for j in range(0, i):
                    other = self.rocks[j]
                    if rock.collide(other):
                        rock.position[0] = (rock.position[0] -
                                            rock.velocity[0]) % SCREEN_WIDTH
                        rock.position[1] = (rock.position[1] -
                                            rock.velocity[1]) % SCREEN_HEIGHT

                        other.position[0] = ((other.position[0] -
                                              other.velocity[0]) %
                                             SCREEN_WIDTH)
                        other.position[1] = ((other.position[1] -
                                              other.velocity[1]) %
                                             SCREEN_HEIGHT)

                        # Elastic collision (with radius*3 as mass)
                        # https://en.wikipedia.org/wiki/Elastic_collision
                        tmp_sum = (rock.radius + other.radius) * 3
                        tmp_diff = (rock.radius - other.radius) * 3

                        double = 2 * 3 * other.radius
                        new_x = (float(tmp_diff * rock.velocity[0] +
                                       double * other.velocity[0]) / tmp_sum)
                        new_y = (float(tmp_diff * rock.velocity[1] +
                                       double * other.velocity[1]) / tmp_sum)

                        double = 2 * 3 * rock.radius
                        other.velocity[0] = float(
                            double * rock.velocity[0] -
                            tmp_diff * other.velocity[0]) / tmp_sum
                        other.velocity[1] = float(
                            double * rock.velocity[1] -
                            tmp_diff * other.velocity[1]) / tmp_sum

                        rock.velocity[0] = new_x
                        rock.velocity[1] = new_y

        # Display number of lives
        if self.started:
            info = self.img_infos['ship']
            for i in range(self.lives):
                canvas.draw_image(self.medias.get_image('ship'),
                                  info.get_center(), info.get_size(),
                                  (40 + i * 40, 40), (40, 40),
                                  -math.pi / 2)

        # Draw and update live explosions
        for i in range(len(self.live_explosions) - 1, -1, -1):
            live_explosion = self.live_explosions[i]

            canvas.draw_image(live_explosion.image,
                              live_explosion.image_center,
                              live_explosion.image_size,
                              live_explosion.position, (40, 40),
                              -math.pi / 2)
            live_explosion.update()
            if live_explosion.lifespan <= 0:  # explosion finished
                del self.live_explosions[i]

        # Display number of bombs
        if self.started and self.nb_bombs:
            info = self.img_infos['bomb']
            for i in range(self.nb_bombs):
                canvas.draw_image(self.medias.get_image('bomb'),
                                  info.get_center(), info.get_size(),
                                  (40 + i * 40, 80), (20, 40),
                                  -math.pi / 2)

        # Display score
        text_size = 36
        font = 'sans-serif'

        text1 = 'Score'
        width1 = FRAME.get_canvas_textwidth(text1, text_size, font)
        text2 = str(self.score)
        width2 = FRAME.get_canvas_textwidth(text2, text_size, font)

        canvas.draw_text(text1, (SCREEN_WIDTH - 22 - width1,
                                 22 + text_size * 3.0 / 4),
                         text_size, 'Gray', font)
        canvas.draw_text(text2, (SCREEN_WIDTH - 22 - width2,
                                 22 + text_size * 7.0 / 4),
                         text_size, 'Gray', font)

        canvas.draw_text(text1, (SCREEN_WIDTH - 20 - width1,
                                 20 + text_size * 3.0 / 4),
                         text_size, 'White', font)
        canvas.draw_text(text2, (SCREEN_WIDTH - 20 - width2,
                                 20 + text_size * 7.0 / 4),
                         text_size, 'White', font)

        # Draw splash screen if game not started
        if not self.started:
            img_size = self.img_infos['splash'].get_size()
            canvas.draw_image(
                self.medias.get_image('splash'),
                self.img_infos['splash'].get_center(), img_size,
                (SCREEN_WIDTH / 2.0, SCREEN_HEIGHT / 2.0), img_size)

        # Update and draw FPS (if started)
        FPS_DRAWER.draw_fct(canvas)

    def load_medias(self):  # type: () -> None
        """
        Load images and sounds and waiting all is loaded,
        the set the general draw handler.
        """
        self.img_infos = {'asteroid-1': ImageInfo((45, 45), (90, 90), 40),
                          'asteroid-2': ImageInfo((45, 45), (90, 90), 40),
                          'asteroid-3': ImageInfo((45, 45), (90, 90), 38),
                          'asteroid_explosion': ImageInfo((64, 64), (128, 128),
                                                          17, 24, True),
                          'asteroid_collide_explosion': ImageInfo((64, 64),
                                                                  (128, 128),
                                                                  17, 24,
                                                                  True),
                          'bomb': ImageInfo((10, 10), (20, 20)),
                          'debris': ImageInfo((320, 240), (640, 480)),
                          'little-asteroid-1': ImageInfo((45, 45), (90, 90),
                                                         27, None, False,
                                                         (60, 60)),
                          'little-asteroid-2': ImageInfo((45, 45), (90, 90),
                                                         27, None, False,
                                                         (60, 60)),
                          'little-asteroid-3': ImageInfo((45, 45), (90, 90),
                                                         26, None, False,
                                                         (60, 60)),
                          'live_explosion': ImageInfo((64, 64), (128, 128),
                                                      17, 24, True),
                          'missile': ImageInfo((5, 5), (10, 10), 3, 50),
                          'nebula': ImageInfo((400, 300), (800, 600)),
                          'ship': ImageInfo((45, 45), (90, 90), 35),
                          'ship_explosion': ImageInfo((64, 64), (128, 128),
                                                      17, 24, True),
                          'splash': ImageInfo((200, 150), (400, 300))}

        def init():
            """Init the game after medias loaded."""
            assert isinstance(self.medias, Loader)

            if SIMPLEGUICS2PYGAME:
                FRAME._set_canvas_background_image(  # pylint: disable=protected-access  # noqa
                    self.medias.get_image('nebula'))

            self.medias._images['live_explosion'] = self.medias._images['ship_explosion']  # pylint: disable=protected-access  # noqa

            for i in range(1, 4):
                self.medias._images['little-asteroid-' + str(i)] = self.medias._images['asteroid-' + str(i)]  # pylint: disable=protected-access  # noqa

            self.medias._sounds['asteroid_collide_explosion'] = self.medias._sounds['asteroid_explosion']  # pylint: disable=protected-access  # noqa

            self.medias.get_sound('missile').set_volume(.5)

            self.my_ship = Ship((SCREEN_WIDTH / 2.0, SCREEN_HEIGHT / 2.0),
                                (0, 0),
                                -math.pi / 2, 'ship')

            FRAME.set_draw_handler(self.draw_and_update)

            if SIMPLEGUICS2PYGAME and (simplegui._joypads._joypad_nb > 0):  # pylint: disable=protected-access  # noqa
                FRAME._set_joypadaxe_handler(joypad_axe)  # pylint: disable=protected-access  # noqa
                FRAME._set_joypadup_handler(joypad_up)  # pylint: disable=protected-access  # noqa
                FRAME._set_joypadhat_handler(joypad_hat)  # pylint: disable=protected-access  # noqa

            FRAME.set_keydown_handler(keydown)
            FRAME.set_keyup_handler(keyup)

            FRAME.set_mouseclick_handler(click)

            if self.music_active:
                self.medias.get_sound('intro').play()

            self.loaded = True

        self.medias = Loader(FRAME, SCREEN_WIDTH, init)

        assert isinstance(self.medias, Loader)  # to avoid mypy false positives

        # Images by Kim Lathrop
        self.medias.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png',  # noqa
                              'asteroid-1')
        self.medias.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png',  # noqa
                              'asteroid-2')
        self.medias.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_brown.png',  # noqa
                              'asteroid-3')
        self.medias.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png',  # noqa
                              'asteroid_explosion')
        self.medias.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha2.png',  # noqa
                              'asteroid_collide_explosion')
        self.medias.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot3.png',  # noqa
                              'bomb')
        self.medias.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png',  # noqa
                              'debris')
        self.medias.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png',  # noqa
                              'missile')
        self.medias.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_brown.png',  # noqa
                              'nebula')
        self.medias.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png',  # noqa
                              'ship')
        self.medias.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_orange.png',  # noqa
                              'ship_explosion')
        self.medias.add_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png',  # noqa
                              'splash')

        # Sounds from http://www.sounddogs.com/ (not free)
        self.medias.add_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.ogg',  # noqa
                              'asteroid_explosion')
        self.medias.add_sound('http://rpg.hamsterrepublic.com/wiki-images/f/f4/StormMagic.ogg',  # noqa
                              'bomb_explode')
        self.medias.add_sound('http://commondatastorage.googleapis.com/codeskulptor-demos/pyman_assets/extralife.ogg',  # noqa
                              'bomb_extra')
        self.medias.add_sound('http://commondatastorage.googleapis.com/codeskulptor-demos/pyman_assets/eatedible.ogg',  # noqa
                              'collide')
        self.medias.add_sound('http://rpg.hamsterrepublic.com/wiki-images/5/58/Death.ogg',  # noqa
                              'death')
        self.medias.add_sound('http://commondatastorage.googleapis.com/codeskulptor-demos/pyman_assets/intromusic.ogg',  # noqa
                              'intro')
        self.medias.add_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.ogg',  # noqa
                              'soundtrack')
        self.medias.add_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.ogg',  # noqa
                              'missile')
        self.medias.add_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.ogg',  # noqa
                              'ship_thrust')

        self.medias.load()

        self.medias.wait_loaded()

    def pause_switch(self):  # type: () -> None
        """Pause on/off."""
        self.paused = not self.paused

    def rock_spawner(self):  # type: () -> None
        """
        If the maximum is not reached
        then spawns a rock (not too close to the ship).
        """
        if (len(self.rocks) < 10) and not self.paused:
            assert isinstance(self.my_ship, Ship)

            too_close = True

            def random_vel():
                """:return: int or float"""
                return (min(2,
                            (random.random() * (self.score / 10.0 + 0.1))) *
                        random.choice((-1, 1)))

            for _ in range(10):  # try 10 times
                rock_pos = (random.randrange(0, SCREEN_WIDTH),
                            random.randrange(0, SCREEN_HEIGHT))
                rock_vel = (random_vel(),
                            random_vel())
                rock_ang_vel = random.choice((-1, 1)) * (random.random() *
                                                         0.05 + 0.01)

                rock = Asteroid(rock_pos, rock_vel,
                                rock_ang_vel,
                                random.randint(1, 3))

                too_close = False
                for rock2 in self.rocks:
                    if rock2.collide(rock):
                        too_close = True

                        break

                too_close = (too_close or
                             (self.my_ship.distance(rock) <
                              (self.my_ship.radius + rock.radius) * 3))
                if not too_close:
                    break

            if not too_close:
                self.rocks.append(rock)

    def start(self):  # type: () -> None
        """Start the game."""
        if self.wait:
            return

        self.timer_wait.stop()

        if self.music_active:
            assert isinstance(self.medias, Loader)

            self.medias.get_sound('intro').rewind()
            self.medias.get_sound('soundtrack').play()

        self.keydown_left = False
        self.keydown_right = False
        self.lives = 3
        self.nb_bombs = 0
        self.score = 0

        self.my_ship = Ship((SCREEN_WIDTH / 2.0, SCREEN_HEIGHT / 2.0), (0, 0),
                            -math.pi / 2, 'ship')

        self.explosions = []
        self.missiles = []
        self.rocks = []

        self.timer.start()
        self.rock_spawner()

        self.paused = False
        self.started = True

        if SIMPLEGUICS2PYGAME:
            assert isinstance(FRAME, simplegui.Frame)

            FRAME._cursor_auto_hide = True  # pylint: disable=protected-access
            FRAME._set_cursor_visible(not FRAME._cursor_in_canvas())  # pylint: disable=protected-access  # noqa

    def stop(self):  # type: () -> None
        """Stop the game."""
        assert isinstance(self.my_ship, Ship)

        self.timer.stop()

        self.nb_bombs = None

        self.missiles = []
        self.rocks = []

        self.started = False

        self.my_ship.stop()

        if self.music_active:
            assert isinstance(self.medias, Loader)

            self.medias.get_sound('soundtrack').rewind()
            self.medias.get_sound('intro').play()

        if SIMPLEGUICS2PYGAME:
            assert isinstance(FRAME, simplegui.Frame)

            FRAME._cursor_auto_hide = False  # pylint: disable=protected-access
            FRAME._set_cursor_visible()  # pylint: disable=protected-access

        self.wait = True
        self.timer_wait.start()


class ImageInfo:
    """Informations to use with Sprite."""

    def __init__(self, center, size,  # pylint: disable=too-many-arguments
                 radius=None, lifespan=None, animated=False,
                 draw_size=None):
        # type: (Sequence[Union[int, float]], Sequence[Union[int, float]], Optional[Union[int, float]], Optional[Union[int, float]], bool, Optional[Sequence[Union[int, float]]]) -> None  # noqa
        """
        Set informations.

        If radius is None
        then use maximum of size components.

        If lifespan is None
        then use infinity.

        If draw_size is None
        then use size value.

        :param center: (int or float, int or float)
                       or [int or float, int or float]
        :param size: ((int or float) > 0, (int or float) > 0)
                     or [(int or float) > 0, (int or float) > 0]
        :param radius: None or ((int or float) > 0)
        :param lifespan: None or ((int or float) > 0)
        :param animated: bool
        :param draw_size: None
                          or ((int or float) > 0, (int or float) > 0)
                          or [(int or float) > 0, (int or float) > 0]
        """
        assert_position(center)
        assert_position(size, True, True)
        assert ((radius is None) or
                (isinstance(radius, (int, float)) and
                 (radius > 0))), radius
        assert ((lifespan is None) or
                (isinstance(lifespan, (int, float)) and
                 (lifespan > 0))), lifespan
        assert isinstance(animated, bool), type(animated)

        if draw_size is None:
            draw_size = size

        assert_position(draw_size, True, True)

        self._center = list(center)
        self._size = list(size)
        self._radius = (max(size) if radius is None
                        else radius)
        self._lifespan = (lifespan if lifespan
                          else float('inf'))  # type: float
        self._animated = animated
        self._draw_size = list(draw_size)

    def get_animated(self):  # type: () -> bool
        """
        If is a animated image
        then return True,
        else return False.

        :return: bool
        """
        return self._animated

    def get_center(self):  # type: () -> List[Union[int, float]]
        """
        Return position of the center of image.

        :return: [int or float, int or float]
        """
        return list(self._center)

    def get_draw_size(self):  # type: () -> List[Union[int, float]]
        """
        Return draw size of image.

        :return: [(int or float) > 0, (int or float) > 0]
        """
        return list(self._draw_size)

    def get_lifespan(self):  # type: () -> Union[int, float]
        """
        Return lifespan of image.

        :return: (int or float) > 0
        """
        return self._lifespan

    def get_radius(self):  # type: () -> Union[int, float]
        """
        Return radius of image.

        :return: (int or float) > 0
        """
        return self._radius

    def get_size(self):  # type: () -> List[Union[int, float]]
        """
        Return size of image.

        :return: [(int or float) > 0, (int or float) > 0]
        """
        return list(self._size)


class Sprite:  # pylint: disable=too-many-instance-attributes
    """Sprite class"""

    def __init__(self, position,  # pylint: disable=too-many-arguments
                 velocity, angle, angle_velocity, media_name):
        # type: (Sequence[Union[int, float]], Sequence[Union[int, float]], Union[int, float], Union[int, float], str) -> None  # noqa
        """
        Set sprite.

        :param position: (int or float, int or float)
                         or [int or float, int or float]
        :param velocity: (int or float, int or float)
                         or [int or float, int or float]
        :param angle: int or float
        :param angle_velocity: int or float
        :param media_name: str
        """
        assert_position(position)
        assert_position(velocity)
        assert isinstance(angle, (int, float)), type(angle)
        assert isinstance(angle_velocity, (int, float)), type(angle_velocity)
        assert isinstance(media_name, str), type(media_name)

        self.position = list(position)
        self.velocity = list(velocity)
        self.angle = angle
        self.angle_velocity = angle_velocity

        assert isinstance(RICEROCKS, RiceRocks)
        assert isinstance(RICEROCKS.img_infos, dict)

        img_info = RICEROCKS.img_infos[media_name]
        self.animated = img_info.get_animated()
        self.image_center = img_info.get_center()
        self.image_draw_size = img_info.get_draw_size()
        self.image_size = img_info.get_size()
        self.lifespan = img_info.get_lifespan()
        self.radius = img_info.get_radius()
        self.image = None  # type: Optional[simplegui.Image]

        assert isinstance(RICEROCKS.medias, Loader)
        assert RICEROCKS.medias is not None  # to avoid mypy false positives

        self.image = RICEROCKS.medias.get_image(media_name)

        if (RICEROCKS.sounds_active and
                (media_name in RICEROCKS.medias._sounds)):  # pylint: disable=protected-access  # noqa
            sound = RICEROCKS.medias.get_sound(media_name)
            sound.rewind()
            sound.play()

    def collide(self, other_sprite):  # type: ('Sprite') -> bool
        """
        If this sprite collide with other_sprite
        then return True,
        else return False

        :param other_sprite: Sprite

        :return: bool
        """
        assert isinstance(other_sprite, Sprite), type(other_sprite)

        return (((self.position[0] - other_sprite.position[0])**2 +
                 (self.position[1] - other_sprite.position[1])**2) <=
                (self.radius + other_sprite.radius)**2)

    def distance(self, other_sprite):  # type: ('Sprite') -> float
        """
        Return the distance between this sprite and other_sprite.

        :param other_sprite: Sprite

        :return: float
        """
        assert isinstance(other_sprite, Sprite), type(other_sprite)

        return math.sqrt((self.position[0] - other_sprite.position[0])**2 +
                         (self.position[1] - other_sprite.position[1])**2)

    def draw(self, canvas):  # type: (simplegui.Canvas) -> None
        """
        Draw the sprite
        (if the associated image are not loaded, draw a red disc).

        :param canvas: simplegui.Canvas
        """
        if (self.image is not None) and (self.image.get_width() > 0):
            canvas.draw_image(self.image,
                              self.image_center, self.image_size,
                              self.position, self.image_draw_size,
                              self.angle)
        else:
            # Useful to debug
            canvas.draw_circle(self.position, self.radius, 1, 'Red', 'Red')

    def update(self):  # type: () -> None
        """
        Update position adding velocity,
        angle adding angle_velocity,
        lifespan and current image if animated.
        """
        self.angle += self.angle_velocity

        self.position[0] = (self.position[0] +
                            self.velocity[0]) % SCREEN_WIDTH
        self.position[1] = (self.position[1] +
                            self.velocity[1]) % SCREEN_HEIGHT

        if self.lifespan is not None:
            self.lifespan -= 1
            if self.animated:  # change the current image
                assert ((self.image is None) or
                        (self.image_center[0] < self.image.get_width()))

                self.image_center[0] += self.image_size[0]


class Asteroid(Sprite):
    """Asteroid class"""

    def __init__(self, position,  # pylint: disable=too-many-arguments
                 velocity, angle_velocity, num, little=False):
        # type: (Sequence[Union[int, float]], Sequence[Union[int, float]], Union[int, float], int, bool) -> None  # noqa
        """
        Set an asteroid sprite.

        :param position: (int or float, int or float)
                         or [int or float, int or float]
        :param velocity: (int or float, int or float)
                         or [int or float, int or float]
        :param angle_velocity: int or float
        :param num: 1, 2 or 3
        :param litle: bool
        """
        assert_position(position)
        assert_position(velocity)
        assert isinstance(angle_velocity, (int, float)), type(angle_velocity)
        assert num in (1, 2, 3)
        assert isinstance(little, bool), type(little)

        Sprite.__init__(self, position, velocity,
                        0, angle_velocity,
                        ('little-asteroid-' if little
                         else 'asteroid-') + str(num))

        self.num = num
        self.little = little


class Ship(Sprite):
    """Ship class"""

    def __init__(self, position, velocity,
                 angle,
                 media_name):
        # type: (Sequence[Union[int, float]], Sequence[Union[int, float]], Union[int, float], str) -> None  # noqa
        """
        Set ship sprite.

        :param position: (int or float, int or float)
                         or [int or float, int or float]
        :param velocity: (int or float, int or float)
                         or [int or float, int or float]
        :param angle: int or float
        :param media_name: str
        """
        assert_position(position)
        assert_position(velocity)
        assert isinstance(angle, (int, float)), type(angle)
        assert isinstance(media_name, str), type(media_name)

        Sprite.__init__(self, position, velocity, angle,
                        0,
                        media_name)

        self.thrust = False

    def flip(self):  # type: () -> None
        """Flip the ship."""
        self.angle += math.pi

    def shot(self):  # type: () -> None
        """Launch a missile."""
        assert isinstance(RICEROCKS, RiceRocks)

        vector = angle_to_vector(self.angle)

        RICEROCKS.missiles.append(
            Sprite((self.position[0] + self.radius * vector[0],
                    self.position[1] + self.radius * vector[1]),
                   (self.velocity[0] + vector[0] * 6,
                    self.velocity[1] + vector[1] * 6),
                   self.angle, 0,
                   'missile'))

    def stop(self):  # type: () -> None
        """Stop the ship."""
        self.turn(None)
        if self.thrust:
            self.thrust_on_off()

    def thrust_on_off(self):  # type: () -> None
        """Switch activation of thrust."""
        assert isinstance(RICEROCKS, RiceRocks)
        assert isinstance(RICEROCKS.medias, Loader)

        self.thrust = not self.thrust

        if self.thrust:
            if RICEROCKS.sounds_active:
                RICEROCKS.medias.get_sound('ship_thrust').play()
            # Sprite image with actif thrust
            self.image_center[0] += self.image_size[0]
        else:
            if RICEROCKS.sounds_active:
                RICEROCKS.medias.get_sound('ship_thrust').rewind()
            # Sprite image with inactif thrust
            self.image_center[0] -= self.image_size[0]

    def turn(self, right):  # type: (Optional[bool]) -> None
        """
        Turn the ship
        (in fact change angle_velocity).

        :param right: None or bool
        """
        assert (right is None) or isinstance(right, bool), type(right)

        self.angle_velocity = {False: -0.05,
                               None: 0,
                               True: 0.05}[right]

    def update(self):  # type: () -> None
        """
        Update position adding velocity (and deal exit out of the canvas),
        decrease slightly velocity,
        and angle adding angle_velocity.

        Moreover if thrust is active then increase velocity.
        """
        # Update angle
        self.angle += self.angle_velocity

        # Update position
        self.position[0] = (self.position[0] +
                            self.velocity[0]) % SCREEN_WIDTH
        self.position[1] = (self.position[1] +
                            self.velocity[1]) % SCREEN_HEIGHT

        # Update velocity
        if self.thrust:
            acceleration = angle_to_vector(self.angle)
            self.velocity[0] += acceleration[0] * .25
            self.velocity[1] += acceleration[1] * .25

        self.velocity[0] *= .98
        self.velocity[1] *= .98


#
# Event handlers
#################
def click(pos):  # pylint: disable=unused-argument
    # type: (Tuple[int, int]) -> None
    """
    If click on splash screen
    then start the game.

    :param pos: (int >= 0, int >= 0)
    """
    assert isinstance(RICEROCKS, RiceRocks)

    if not RICEROCKS.started:
        RICEROCKS.wait = False
        RICEROCKS.start()


def fps_on_off():  # type: () -> None
    """Active or inactive the calculation and drawing of FPS."""
    if FPS_DRAWER.is_started():
        FPS_DRAWER.stop()
        BUTTON_FPS.set_text('FPS on')
    else:
        FPS_DRAWER.start()
        BUTTON_FPS.set_text('FPS off')


def joypad_axe(joypad, axe, value):  # type: (int, int, float) -> None
    """
    Event handler to deal joypad axe.

    :param joypad: int >= 0
    :param axe: int >= 0
    :param value: -1 <= float <= 1
    """
    assert isinstance(RICEROCKS, RiceRocks)

    if (joypad == 0) and RICEROCKS.started:
        assert isinstance(RICEROCKS.my_ship, Ship)

        threshold = 0.9

        if axe == 0:
            if value <= -threshold:   # left
                RICEROCKS.keydown_left = True
                RICEROCKS.my_ship.turn(False)
            elif value >= threshold:  # right
                RICEROCKS.keydown_right = True
                RICEROCKS.my_ship.turn(True)
            else:                     # clear horizontal
                RICEROCKS.keydown_left = False
                RICEROCKS.keydown_right = False
                RICEROCKS.my_ship.turn(None)
        elif axe == 1:
            if value <= -threshold:         # forward
                if not RICEROCKS.my_ship.thrust:
                    RICEROCKS.my_ship.thrust_on_off()
            elif RICEROCKS.my_ship.thrust:  # clear vertical
                RICEROCKS.my_ship.thrust_on_off()


def joypad_up(joypad, button):  # type: (int, int) -> None
    """
    Event handler to deal joypad buttons.

    :param joypad: int >= 0
    :param button: int >= 0
    """
    assert isinstance(RICEROCKS, RiceRocks)

    if joypad == 0:
        if RICEROCKS.started:
            assert isinstance(RICEROCKS.my_ship, Ship)

            if button == 0:    # shoot
                RICEROCKS.my_ship.shot()
            elif button == 1:  # bomb
                RICEROCKS.bomb_explode()
            elif button == 2:  # flip
                RICEROCKS.my_ship.flip()
        else:
            RICEROCKS.start()


def joypad_hat(joypad, hat, values):
    # type: (int, int, Tuple[int, int]) -> None
    """
    Event handler to deal joypad hat.

    :param joypad: int >= 0
    :param hat: int >= 0
    :param values: (a, b) with a and b == -1, 0 or 1
    """
    assert isinstance(RICEROCKS, RiceRocks)

    if (joypad == 0) and (hat == 0) and RICEROCKS.started:
        assert isinstance(RICEROCKS.my_ship, Ship)

        if values[0] == -1:   # left
            RICEROCKS.keydown_left = True
            RICEROCKS.my_ship.turn(False)
        elif values[0] == 1:  # right
            RICEROCKS.keydown_right = True
            RICEROCKS.my_ship.turn(True)
        else:                 # clear horizontal
            RICEROCKS.keydown_left = False
            RICEROCKS.keydown_right = False
            RICEROCKS.my_ship.turn(None)

        if values[1] == 1:              # forward
            if not RICEROCKS.my_ship.thrust:
                RICEROCKS.my_ship.thrust_on_off()
        elif values[1] == -1:           # flip
            RICEROCKS.my_ship.flip()
        elif RICEROCKS.my_ship.thrust:  # clear vertical
            RICEROCKS.my_ship.thrust_on_off()


def keydown(key):  # type: (int) -> None
    """
    Event handler to deal key down.

    :param key: int >= 0
    """
    assert isinstance(RICEROCKS, RiceRocks)

    if RICEROCKS.started:
        assert isinstance(RICEROCKS.my_ship, Ship)

        if key == simplegui.KEY_MAP['left']:     # left
            RICEROCKS.keydown_left = True
            RICEROCKS.my_ship.turn(False)
        elif key == simplegui.KEY_MAP['right']:  # right
            RICEROCKS.keydown_right = True
            RICEROCKS.my_ship.turn(True)
        elif key == simplegui.KEY_MAP['up']:     # forward
            RICEROCKS.my_ship.thrust_on_off()
        elif key == simplegui.KEY_MAP['down']:   # flip
            RICEROCKS.my_ship.flip()
        elif key == simplegui.KEY_MAP['space']:  # shoot
            RICEROCKS.my_ship.shot()
        elif key == simplegui.KEY_MAP['B']:      # bomb
            RICEROCKS.bomb_explode()
        elif key == simplegui.KEY_MAP['P']:      # pause
            RICEROCKS.pause_switch()
    else:
        RICEROCKS.start()


def keyup(key):  # type: (int) -> None
    """
    Event handler to deal key up.

    :param key: int >= 0
    """
    assert isinstance(RICEROCKS, RiceRocks)

    if RICEROCKS.started:
        assert isinstance(RICEROCKS.my_ship, Ship)

        if key == simplegui.KEY_MAP['left']:
            RICEROCKS.keydown_left = False
            RICEROCKS.my_ship.turn(True if RICEROCKS.keydown_right
                                   else None)
        elif key == simplegui.KEY_MAP['right']:
            RICEROCKS.keydown_right = False
            RICEROCKS.my_ship.turn(False if RICEROCKS.keydown_left
                                   else None)
        elif key == simplegui.KEY_MAP['up']:
            RICEROCKS.my_ship.thrust_on_off()
        elif key == 27:  # Escape
            quit_prog()


def quit_prog():  # type: () -> None
    """Stop timer and sounds, and quit."""
    assert isinstance(RICEROCKS, RiceRocks)

    if RICEROCKS.loaded:
        assert isinstance(FRAME, simplegui.Frame)
        assert isinstance(RICEROCKS.medias, Loader)

        RICEROCKS.stop()
        RICEROCKS.medias.pause_sounds()
        FRAME.stop()
        if SIMPLEGUICS2PYGAME and FRAME._print_stats_cache:  # pylint: disable=protected-access  # noqa
            RICEROCKS.medias.print_stats_cache()


def stop():  # type: () -> None
    """Stop the game."""
    assert isinstance(RICEROCKS, RiceRocks)

    if RICEROCKS.loaded:
        RICEROCKS.stop()


def switch_animate_background():  # type: () -> None
    """Switch animate background on/off."""
    assert isinstance(RICEROCKS, RiceRocks)

    RICEROCKS.animate_background_active = (not
                                           RICEROCKS.animate_background_active)
    BUTTON_ANIMATE_BACKGROUND.set_text('Static background'
                                       if RICEROCKS.animate_background_active
                                       else 'Animate background')


def switch_music():  # type: () -> None
    """Switch music on/off."""
    assert isinstance(RICEROCKS, RiceRocks)
    assert isinstance(RICEROCKS.medias, Loader)

    RICEROCKS.music_active = not RICEROCKS.music_active

    if RICEROCKS.music_active:
        BUTTON_MUSIC.set_text('Music off')
        if RICEROCKS.started:
            RICEROCKS.medias.get_sound('soundtrack').play()
        else:
            RICEROCKS.medias.get_sound('intro').play()
    else:
        BUTTON_MUSIC.set_text('Music on')
        RICEROCKS.medias.get_sound('intro').rewind()
        RICEROCKS.medias.get_sound('soundtrack').rewind()


def switch_sounds():  # type: () -> None
    """Switch sounds on/off."""
    assert isinstance(RICEROCKS, RiceRocks)

    RICEROCKS.sounds_active = not RICEROCKS.sounds_active
    BUTTON_SOUNDS.set_text('Sounds off' if RICEROCKS.sounds_active
                           else 'Sounds on')


#
# Main
#######
if __name__ == '__main__':
    FRAME = simplegui.create_frame('RiceRocks (Asteroids)',
                                   SCREEN_WIDTH, SCREEN_HEIGHT, 200)

    FPS_DRAWER = FPS(x=0, y=0, font_size=32)

    RICEROCKS = RiceRocks()
    RICEROCKS.load_medias()

    FRAME.add_button('Stop this game', stop)
    FRAME.add_label('')
    BUTTON_MUSIC = FRAME.add_button('Music off', switch_music)
    BUTTON_SOUNDS = FRAME.add_button('Sounds off', switch_sounds)
    if SIMPLEGUICS2PYGAME:
        FRAME.add_label('')
    BUTTON_ANIMATE_BACKGROUND = FRAME.add_button('Static background',
                                                 switch_animate_background)
    if SIMPLEGUICS2PYGAME:
        FRAME.add_label('')
    FRAME.add_button('Quit', quit_prog)
    FRAME.add_label('')
    FRAME.add_label('Turn: Left and Right')
    FRAME.add_label('Accelerate: Up')
    FRAME.add_label('Flip: Down')
    FRAME.add_label('Fire: Space')
    FRAME.add_label('Bomb: B')
    FRAME.add_label('Pause: P')
    FRAME.add_label('Esc: Quit')

    if SIMPLEGUICS2PYGAME:
        FRAME.add_label('')
        FRAME.add_label('%i joypad%s available' %
                        (simplegui._joypads._joypad_nb,  # pylint: disable=protected-access  # noqa
                         ('s' if simplegui._joypads._joypad_nb > 1  # pylint: disable=protected-access  # noqa
                          else '')))

    FRAME.add_label('')
    FRAME.add_label('One bomb for every 10')
    FRAME.add_label('asteroids destroyed.')
    FRAME.add_label('')
    FRAME.add_label('One live for every 50')
    FRAME.add_label('asteroids destroyed.')

    FRAME.add_label('')
    FRAME.add_label('Useful to test:')
    BUTTON_FPS = FRAME.add_button('FPS on', fps_on_off)

    if not SIMPLEGUICS2PYGAME:
        FRAME.add_label('')
        FRAME.add_label('If the game is too slow,')
        FRAME.add_label('try with the browser Chrome.')

    FRAME.start()
