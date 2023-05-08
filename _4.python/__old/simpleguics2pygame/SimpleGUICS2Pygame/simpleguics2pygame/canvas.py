# -*- coding: latin-1 -*-

"""
simpleguics2pygame module: simpleguics2pygame/canvas.

Class Canvas.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2015-2016, 2020-2021 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 4, 2021
"""

from __future__ import division
from __future__ import print_function

# print('IMPORT', __name__)


import math
import os.path
import re
import sys


__all__ = ('Canvas',
           'create_invisible_canvas')


try:
    from typing import Any, Callable, List, Optional, Sequence, Tuple, Union  # noqa
except ImportError:
    pass

import pygame

from SimpleGUICS2Pygame.simpleguics2pygame._colors import _SIMPLEGUICOLOR_TO_PYGAMECOLOR, _simpleguicolor_to_pygamecolor  # pylint: disable=wrong-import-position,no-name-in-module,ungrouped-imports  # noqa
from SimpleGUICS2Pygame.simpleguics2pygame._fonts import _SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME, _simpleguifontface_to_pygamefont  # pylint: disable=wrong-import-position,no-name-in-module,ungrouped-imports  # noqa
from SimpleGUICS2Pygame.simpleguics2pygame.image import Image  # pylint: disable=wrong-import-position,no-name-in-module,ungrouped-imports  # noqa


#
# Private global constants
##########################
_RADIAN_TO_DEGREE = 180 / math.pi
"""
Multiplicative constant to convert radian to degree.
"""


_RE_UNPRINTABLE_WHITESPACE_CHAR = re.compile('[\t\n\r\f\v]')
"""
Regular expression pattern to unprintable whitespace character.
"""


#
# "Private" function
####################
def _pos_round(position):
    # type: (Sequence[Union[int, float]]) -> Tuple[int, int]
    """
    Return the rounded `position`.

    **Don't require Pygame.**

    **(Not available in SimpleGUI of CodeSkulptor.)**

    :param position: (int or float, int or float)
                     or [int or float, int or float]

    :return: (int, int)
    """
    assert isinstance(position, (tuple, list)), type(position)
    assert len(position) == 2, len(position)
    assert isinstance(position[0], (int, float)), type(position[0])
    assert isinstance(position[1], (int, float)), type(position[1])

    return (int(round(position[0])), int(round(position[1])))


#
# Class
#######
class Canvas:
    """Canvas similar to SimpleGUI `Canvas` of CodeSkulptor."""

    _background_pygame_color = _SIMPLEGUICOLOR_TO_PYGAMECOLOR['black']
    """Default `pygame.Color` of the background of the canvas."""

    _bg_pygame_surface_image = None  # type: Optional[pygame.surface.Surface]
    """
    `pygame.surface.Surface` default background image
    replaces `_background_pygame_color`.
    """

    def __init__(self,
                 frame,
                 canvas_width, canvas_height):
        # type: (Optional[pygame.Frame], int, int) -> None  # noqa
        """
        Set the canvas.

        **Don't use directly**, a canvas is created by `Frame()`
        and reachable by handler defined by `Frame.set_draw_handler()`.

        :param frame: Frame (or None)
        :param canvas_width: int >= 0
        :param canvas_height: int >= 0
        """
        assert isinstance(canvas_width, int), type(canvas_width)
        assert canvas_width >= 0, canvas_width

        assert isinstance(canvas_height, int), type(canvas_height)
        assert canvas_height >= 0, canvas_height

        self._frame_parent = frame

        self._width = canvas_width
        self._height = canvas_height

        self._background_pygame_color = Canvas._background_pygame_color

        self._draw_handler = None  # type: Optional[Callable[[Canvas], Any]]

        self._pygame_surface = pygame.surface.Surface((canvas_width, canvas_height))  # pylint: disable=too-many-function-args  # noqa

    def __repr__(self):  # type: () -> str
        """
        Return `'<Canvas object>'`.

        :return: str
        """
        return '<Canvas object>'

    def _draw(self):  # type: () -> None
        """
        If `self._draw_handler` != `None`
        then call it and update display of the canvas.

        **(Not available in SimpleGUI of CodeSkulptor.)**
        """
        if ((self._draw_handler is not None) and
                (self._frame_parent is not None)):
            if self._bg_pygame_surface_image is None:
                if self._background_pygame_color.a == 255:
                    # Without alpha
                    self._pygame_surface.fill(self._background_pygame_color)
                elif self._background_pygame_color.a > 0:
                    # With alpha (not null)
                    s_alpha = pygame.surface.Surface((self._width, self._height),  # pylint: disable=too-many-function-args  # noqa
                                                     pygame.SRCALPHA)  # pylint: disable=no-member  # noqa
                    s_alpha.fill(self._background_pygame_color)
                    self._pygame_surface.blit(s_alpha, (0, 0))
            else:
                self._pygame_surface.blit(
                    self._bg_pygame_surface_image, (0, 0))

            self._draw_handler(self)

            if self._frame_parent._display_fps_average:  # pylint: disable=protected-access  # noqa
                self._pygame_surface.blit(
                    _simpleguifontface_to_pygamefont(None, 40)
                    .render(str(int(round(self._frame_parent._fps_average))),  # pylint: disable=protected-access  # noqa
                            True,
                            _SIMPLEGUICOLOR_TO_PYGAMECOLOR['red']),
                    (10, self._height - 40))

            self._frame_parent._pygame_surface.blit(  # pylint: disable=protected-access  # noqa
                self._pygame_surface,
                (self._frame_parent._canvas_x_offset,  # pylint: disable=protected-access  # noqa
                 self._frame_parent._canvas_y_offset))  # pylint: disable=protected-access  # noqa

            pygame.display.update((self._frame_parent._canvas_x_offset,  # pylint: disable=protected-access  # noqa
                                   self._frame_parent._canvas_y_offset,  # pylint: disable=protected-access  # noqa
                                   self._width,  # pylint: disable=protected-access  # noqa
                                   self._height))  # pylint: disable=protected-access  # noqa

    def _save(self, filename):  # type: (str) -> None
        """
        Save the canvas in `filename`.

        Supported formats are supported formats by Pygame to save:
        TGA, PNG, JPEG or BMP
        (see https://www.pygame.org/docs/ref/image.html#pygame.image.save ).

        If `filename` extension is not recognized
        then TGA format is used.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :param filename: str
        """
        assert isinstance(filename, str), type(filename)

        filename = os.path.abspath(os.path.expanduser(filename))
        pygame.image.save(self._pygame_surface, filename)

    def draw_arc(self,  # pylint: disable=too-many-arguments
                 center_point, radius,
                 start_angle, end_angle,
                 line_width, line_color):
        # type: (Sequence[Union[int, float]], Union[int, float], Union[int, float], Union[int, float], Union[int, float], str) -> None  # noqa
        """
        Draw an arc of circle, from `start_angle` to `end_angle`.
        Angles given in radians are clockwise
        and start from 0 at the 3 o'clock position.

        (Available in CodeSkulptor3 but *not in CodeSkulptor2*!)

        :param center_point: (int or float, int or float)
                             or [int or float, int or float]
        :param radius: (int or float) > 0
        :param start_angle: int or float
        :param end_angle: int or float
        :param line_width: (int or float) > 0
        :param line_color: str
        """
        assert isinstance(center_point, (tuple, list)), type(center_point)
        assert len(center_point) == 2, len(center_point)
        assert isinstance(center_point[0], (int, float)), type(center_point[0])
        assert isinstance(center_point[1], (int, float)), type(center_point[1])

        assert isinstance(radius, (int, float)), type(radius)
        assert radius > 0, radius

        assert isinstance(start_angle, (int, float)), (start_angle)
        assert isinstance(end_angle, (int, float)), type(end_angle)

        assert isinstance(line_width, (int, float)), type(line_width)
        assert line_width > 0, line_width

        assert isinstance(line_color, str), type(line_color)

        line_width = (1 if line_width <= 1
                      else int(round(line_width)))

        radius = int(round(radius)) + int(round(line_width // 2))

        # Adapt Codeskulptor angles to Pygame
        if start_angle == end_angle:
            return

        start_angle = -start_angle
        end_angle = -end_angle
        start_angle, end_angle = end_angle, start_angle

        double_pi = math.pi * 2
        start_angle %= double_pi
        end_angle %= double_pi

        if start_angle == end_angle:
            return

        # Draw
        if radius > 1:
            pygamecolor = _simpleguicolor_to_pygamecolor(line_color)

            if pygamecolor.a > 0:
                diameter = radius * 2
                s_tmp = pygame.surface.Surface((diameter, diameter),  # pylint: disable=too-many-function-args  # noqa
                                               pygame.SRCALPHA)  # pylint: disable=no-member  # noqa

                pygame.draw.arc(s_tmp, pygamecolor,
                                s_tmp.get_rect(),
                                start_angle, end_angle,
                                min(line_width, radius))

                self._pygame_surface.blit(s_tmp,
                                          (center_point[0] - radius,
                                           center_point[1] - radius))
        elif radius > 0:  # == 1
            self.draw_point(center_point, line_color)

    def draw_circle(self,  # pylint: disable=too-many-arguments
                    center_point, radius,
                    line_width, line_color,
                    fill_color=None):
        # type: (Sequence[Union[int, float]], Union[int, float], Union[int, float], str, Optional[str]) -> None  # noqa
        """
        Draw a circle.

        If `fill_color` != `None`
        then fill with this color.

        :param center_point: (int or float, int or float)
                             or [int or float, int or float]
        :param radius: (int or float) > 0
        :param line_width: (int or float) > 0
        :param line_color: str
        :param fill_color: None or str
        """
        assert isinstance(center_point, (tuple, list)), type(center_point)
        assert len(center_point) == 2, len(center_point)
        assert isinstance(center_point[0], (int, float)), type(center_point[0])
        assert isinstance(center_point[1], (int, float)), type(center_point[1])

        assert isinstance(radius, (int, float)), type(radius)
        assert radius > 0, radius

        assert isinstance(line_width, (int, float)), type(line_width)
        assert line_width > 0, line_width

        assert isinstance(line_color, str), type(line_color)
        assert (fill_color is None) or isinstance(fill_color, str), \
            type(fill_color)

        line_width = (1 if line_width <= 1
                      else int(round(line_width)))

        radius = int(round(radius)) + int(round(line_width // 2))

        if radius > 1:
            pygamecolor = _simpleguicolor_to_pygamecolor(line_color)
            pygamefillcolor = (None if fill_color is None
                               else _simpleguicolor_to_pygamecolor(fill_color))

            center_point_rounded = _pos_round(center_point)

            if ((pygamecolor.a == 255) and
                    ((pygamefillcolor is None) or (pygamefillcolor.a == 255))):
                # Without alpha
                if pygamefillcolor is not None:
                    pygame.draw.circle(self._pygame_surface, pygamefillcolor,
                                       center_point_rounded, radius,
                                       0)
                if pygamecolor != pygamefillcolor:
                    pygame.draw.circle(self._pygame_surface, pygamecolor,
                                       center_point_rounded, radius,
                                       min(line_width, radius))
            elif ((pygamecolor.a > 0) or
                  ((pygamefillcolor is not None) and (pygamefillcolor.a > 0))):
                # With one or two alpha (not null)
                diameter = radius * 2
                s_alpha = pygame.surface.Surface((diameter, diameter),  # pylint: disable=too-many-function-args  # noqa
                                                 pygame.SRCALPHA)  # pylint: disable=no-member  # noqa

                if (pygamefillcolor is not None) and (pygamefillcolor.a > 0):
                    pygame.draw.circle(s_alpha, pygamefillcolor,
                                       (radius, radius), radius,
                                       0)
                if (pygamecolor != pygamefillcolor) and (pygamecolor.a > 0):
                    pygame.draw.circle(s_alpha, pygamecolor,
                                       (radius, radius), radius,
                                       min(line_width, radius))

                self._pygame_surface.blit(s_alpha,
                                          (center_point_rounded[0] - radius,
                                           center_point_rounded[1] - radius))
        elif radius > 0:  # == 1
            self.draw_point(center_point, line_color)

    def draw_image(self,  # pylint: disable=too-many-arguments,too-many-locals,too-many-branches,too-many-statements  # noqa
                   image,
                   center_source, width_height_source,
                   center_dest, width_height_dest,
                   rotation=0):
        # type: (Image, Sequence[Union[int, float]], Sequence[Union[int, float]], Sequence[Union[int, float]], Sequence[Union[int, float]], Union[int, float]) -> None  # noqa
        """
        Draw `image` on the canvas.

        Specify center position and size of the source (`image`)
        and center position and size of the destination (the canvas).

        Size of the source allow get a piece of `image`.
        If `width_height_source` is bigger than `image`
        then draw nothing.

        Size of the destination allow rescale the drawed image.

        `rotation` specify a clockwise rotation in radians.

        Each new Pygame surface used
        is added to `image._pygamesurfaces_cached`.
        See `Image._pygamesurfaces_cached_clear()`_ .

        .. _`Image._pygamesurfaces_cached_clear()`: image.html#SimpleGUICS2Pygame.simpleguics2pygame.image.Image._pygamesurfaces_cached_clear

        If number of surfaces in this caches
        is greater than `image._pygamesurfaces_cache_max_size`
        then remove the oldest surface.

        :param image: Image
        :param center_source: (int or float, int or float)
                              or [int or float, int or float]
        :param width_height_source: ((int or float) >= 0, (int or float) >= 0)
                                 or [(int or float) >= 0, (int or float) >= 0]
        :param center_dest: (int or float, int or float)
                            or [int or float, int or float]
        :param width_height_dest: ((int or float) >= 0, (int or float) >= 0)
                                  or [(int or float) >= 0, (int or float) >= 0]
        :param rotation: int or float
        """  # noqa
        assert isinstance(image, Image), type(image)

        assert isinstance(center_source, (tuple, list)), \
            type(center_source)
        assert len(center_source) == 2, len(center_source)
        assert isinstance(center_source[0], (int, float)), \
            type(center_source[0])
        assert isinstance(center_source[1], (int, float)), \
            type(center_source[1])

        assert isinstance(width_height_source, (tuple, list)), \
            type(width_height_source)
        assert len(width_height_source) == 2, len(width_height_source)
        assert isinstance(width_height_source[0], (int, float)), \
            type(width_height_source[0])
        assert width_height_source[0] >= 0, width_height_source[0]
        assert isinstance(width_height_source[1], (int, float)), \
            type(width_height_source[1])
        assert width_height_source[1] >= 0, width_height_source[1]

        assert isinstance(center_dest, (tuple, list)), type(center_dest)
        assert len(center_dest) == 2, len(center_dest)
        assert isinstance(center_dest[0], (int, float)), type(center_dest[0])
        assert isinstance(center_dest[1], (int, float)), type(center_dest[1])

        assert isinstance(width_height_dest, (tuple, list)), \
            type(width_height_dest)
        assert len(width_height_dest) == 2, len(width_height_dest)
        assert isinstance(width_height_dest[0], (int, float)), \
            type(width_height_dest[0])
        assert width_height_dest[0] >= 0, width_height_dest[0]
        assert isinstance(width_height_dest[1], (int, float)), \
            type(width_height_dest[1])
        assert width_height_dest[1] >= 0, width_height_dest[1]

        assert isinstance(rotation, (int, float)), type(rotation)

        if image._pygame_surface is None:  # pylint: disable=protected-access
            return

        # Calculate parameters
        width_source, height_source = width_height_source

        x0_source = center_source[0] - width_source / 2
        y0_source = center_source[1] - height_source / 2

        if x0_source >= 0:
            x0_source = int(round(x0_source))
        elif -1 < x0_source:  # rounding error correcting
            width_source -= x0_source
            x0_source = 0
        else:                 # outside of source image
            return

        if y0_source >= 0:
            y0_source = int(round(y0_source))
        elif -1 < y0_source:  # rounding error correcting
            height_source -= y0_source
            y0_source = 0
        else:                 # outside of source image
            return

        width_source = int(round(width_source))
        height_source = int(round(height_source))

        if ((x0_source + width_source > image.get_width() + 1) or
                (y0_source + height_source > image.get_height() + 1)):
            # Bigger than source image
            return

        if x0_source + width_source > image.get_width():
            # Keep this image (seem too big, maybe rounding error)
            width_source -= 1

        if y0_source + height_source > image.get_height():
            # Keep this image (seem too big, maybe rounding error)
            height_source -= 1

        width_height_dest = _pos_round(width_height_dest)

        rotation = int(round(-rotation * _RADIAN_TO_DEGREE)) % 360

        # Get in cache or build Pygame surface
        if sys.version_info[:2] >= (3, 2):
            move_to_end = image._pygamesurfaces_cached.move_to_end  # pylint: disable=protected-access  # noqa
        else:
            def move_to_end(key):  # type: (int) -> None
                """
                Move the `key` item to the newest place of the surfaces cache.

                :param key: tuple of 7 (int >= 0)
                """
                del image._pygamesurfaces_cached[key]  # pylint: disable=protected-access  # noqa

                image._pygamesurfaces_cached[key] = pygame_surface_image  # pylint: disable=protected-access  # noqa

        key = (x0_source, y0_source, width_source, height_source,
               width_height_dest[0], width_height_dest[1],
               rotation)
        pygame_surface_image = image._pygamesurfaces_cached.get(key)  # type: Optional[pygame.surface.Surface]  # pylint: disable=protected-access  # noqa

        if pygame_surface_image is not None:  # Result available
            move_to_end(key)
            if __debug__:
                image._pygamesurfaces_cached_counts[0] += 1  # pylint: disable=protected-access  # noqa
        else:                                 # Build result
            key_0 = key[:-1] + (0, )
            if rotation != 0:  # Get not rotated surface in cache
                pygame_surface_image = image._pygamesurfaces_cached.get(key_0)  # pylint: disable=protected-access  # noqa

            if pygame_surface_image is not None:  # Not rotated available
                move_to_end(key_0)
                if __debug__:
                    image._pygamesurfaces_cached_counts[1] += 1  # pylint: disable=protected-access  # noqa
            else:                                 # Build piece and/or resize
                if ((x0_source == 0) and (y0_source == 0) and
                        (width_source == image.get_width()) and
                        (height_source == image.get_height())):
                    pygame_surface_image = image._pygame_surface  # pylint: disable=protected-access  # noqa
                else:  # Get a piece in source
                    pygame_surface_image = image._pygame_surface.subsurface(  # pylint: disable=protected-access  # noqa
                        (x0_source, y0_source,
                         width_source, height_source))

                if ((width_height_dest[0] != width_source) or
                        (width_height_dest[1] != height_source)):
                    # Resize to destination dimensions
                    pygame_surface_image = pygame.transform.scale(
                        pygame_surface_image, width_height_dest)

                image._pygamesurfaces_cached[key_0] = pygame_surface_image  # pylint: disable=protected-access  # noqa

                if (self._frame_parent and  # pylint: disable=protected-access
                        self._frame_parent._print_stats_cache and  # pylint: disable=protected-access  # noqa
                        (len(image._pygamesurfaces_cached) == image._pygamesurfaces_cache_max_size)):  # pylint: disable=protected-access  # noqa
                    image._print_stats_cache(  # pylint: disable=protected-access  # noqa
                        'Surfaces full cache              ')
                elif len(image._pygamesurfaces_cached) > image._pygamesurfaces_cache_max_size:  # pylint: disable=protected-access  # noqa
                    image._pygamesurfaces_cached.popitem(False)  # pylint: disable=protected-access  # noqa

            if rotation != 0:  # Rotate
                pygame_surface_image = pygame.transform.rotate(
                    pygame_surface_image, rotation)

                image._pygamesurfaces_cached[key] = pygame_surface_image  # pylint: disable=protected-access  # noqa

                if (self._frame_parent and  # pylint: disable=protected-access
                        self._frame_parent._print_stats_cache and  # pylint: disable=protected-access  # noqa
                        (len(image._pygamesurfaces_cached) == image._pygamesurfaces_cache_max_size)):  # pylint: disable=protected-access  # noqa
                    image._print_stats_cache(  # pylint: disable=protected-access  # noqa
                        'Surfaces full cache with rotated ')
                elif len(image._pygamesurfaces_cached) > image._pygamesurfaces_cache_max_size:  # pylint: disable=protected-access  # noqa
                    image._pygamesurfaces_cached.popitem(False)  # pylint: disable=protected-access  # noqa

        # Draw the result
        self._pygame_surface.blit(
            pygame_surface_image,
            (int(round(center_dest[0] - pygame_surface_image.get_width() /
                       2)),
             int(round(center_dest[1] - pygame_surface_image.get_height() /
                       2))))
        if __debug__:
            image._draw_count += 1

    def draw_line(self,
                  point1, point2,
                  line_width, line_color):
        # type: (Sequence[Union[int, float]], Sequence[Union[int, float]], Union[int, float], str) -> None  # noqa
        """
        Draw a line segment from point1 to point2.

        :param point1: (int or float, int or float)
                       or [int or float, int or float]
        :param point2: (int or float, int or float)
                       or [int or float, int or float]
        :param line_width: (int or float) > 0
        :param line_color: str
        """
        assert isinstance(point1, (tuple, list)), type(point1)
        assert len(point1) == 2, len(point1)
        assert isinstance(point1[0], (int, float)), type(point1[0])
        assert isinstance(point1[1], (int, float)), type(point1[1])

        assert isinstance(point2, (tuple, list)), type(point2)
        assert len(point2) == 2, len(point2)
        assert isinstance(point2[0], (int, float)), type(point2[0])
        assert isinstance(point2[1], (int, float)), type(point2[1])

        assert isinstance(line_width, (int, float)), type(line_width)
        assert line_width > 0, line_width

        assert isinstance(line_color, str), type(line_color)

        pygamecolor = _simpleguicolor_to_pygamecolor(line_color)

        if pygamecolor.a == 255:  # without alpha
            pygame.draw.line(self._pygame_surface, pygamecolor,
                             _pos_round(point1), _pos_round(point2),
                             int(round(line_width)))
        elif pygamecolor.a > 0:   # with alpha (not null)
            x1, y1 = _pos_round(point1)
            x2, y2 = _pos_round(point2)  # pylint: disable=invalid-name  # noqa

            width = abs(x2 - x1) + line_width * 2
            height = abs(y2 - y1) + line_width * 2

            x_min = min(x1, x2)
            y_min = min(y1, y2)

            s_alpha = pygame.surface.Surface((width, height), pygame.SRCALPHA)  # pylint: disable=too-many-function-args,no-member  # noqa
            pygame.draw.line(s_alpha, pygamecolor,
                             (x1 - x_min + line_width,
                              y1 - y_min + line_width),
                             (x2 - x_min + line_width,
                              y2 - y_min + line_width),
                             int(round(line_width)))
            self._pygame_surface.blit(s_alpha,
                                      (x_min - line_width, y_min - line_width))

    def draw_point(self, position, color):
        # type: (Sequence[Union[int, float]], str) -> None
        """
        Draw a point.

        :param position: (int or float, int or float)
                         or [int or float, int or float]
        :param color: str
        """
        assert isinstance(position, (tuple, list)), type(position)
        assert len(position) == 2, len(position)
        assert isinstance(position[0], (int, float)), type(position[0])
        assert isinstance(position[1], (int, float)), type(position[1])

        assert isinstance(color, str), type(color)

        pygamecolor = _simpleguicolor_to_pygamecolor(color)

        if pygamecolor.a == 255:  # without alpha
            self._pygame_surface.set_at(_pos_round(position), pygamecolor)
        elif pygamecolor.a > 0:   # with alpha (not null)
            s_alpha = pygame.surface.Surface((1, 1), pygame.SRCALPHA)  # pylint: disable=too-many-function-args,no-member  # noqa
            s_alpha.set_at((0, 0), pygamecolor)
            self._pygame_surface.blit(s_alpha, _pos_round(position))

    def draw_polygon(self,
                     point_list,
                     line_width, line_color,
                     fill_color=None):
        # type: (Sequence[Sequence[Union[int, float]]], Union[int, float], str, Optional[str]) -> None  # noqa
        """
        Draw a polygon from a list of points.
        A segment is automatically drawed
        between the last point and the first point.

        If `fill color` is not None
        then fill with this color.

        If `line_width` > 1, ends are poorly made!

        :param point_list: not empty (tuple or list)
                           of ((int or float, int or float)
                           or [int or float, int or float])
        :param line_width: (int or float) > 0
        :param line_color: str
        :param fill_color: None or str
        """
        assert isinstance(point_list, (tuple, list)), type(point_list)
        assert len(point_list) > 0, len(point_list)

        if __debug__:
            for point in point_list:
                assert isinstance(point, (tuple, list)), type(point)
                assert len(point) == 2, len(point)
                assert isinstance(point[0], (int, float)), type(point[0])
                assert isinstance(point[1], (int, float)), type(point[1])

        assert isinstance(line_width, (int, float)), type(line_width)
        assert line_width >= 0, line_width

        assert isinstance(line_color, str), type(line_color)
        assert (fill_color is None) or isinstance(fill_color, str), \
            type(fill_color)

        if len(point_list) == 1:
            return

        pygamecolor = _simpleguicolor_to_pygamecolor(line_color)
        pygamefillcolor = (None if fill_color is None
                           else _simpleguicolor_to_pygamecolor(fill_color))

        point_list_rounded = [_pos_round(point) for point in point_list]

        del point_list

        line_width = int(round(line_width))

        if ((pygamecolor.a == 255) and
                ((pygamefillcolor is None) or (pygamefillcolor.a == 255))):
            # Without alpha
            if pygamefillcolor is not None:
                pygame.draw.polygon(self._pygame_surface, pygamefillcolor,
                                    point_list_rounded, 0)
            if pygamecolor != pygamefillcolor:
                pygame.draw.lines(self._pygame_surface, pygamecolor, True,
                                  point_list_rounded, line_width)
        elif ((pygamecolor.a > 0) or
              ((pygamefillcolor is not None) and (pygamefillcolor.a > 0))):
            # With one or two alpha (not null)
            s_alpha = pygame.surface.Surface((self._width, self._height),  # pylint: disable=too-many-function-args  # noqa
                                             pygame.SRCALPHA)  # pylint: disable=no-member  # noqa

            if (pygamefillcolor is not None) and (pygamefillcolor.a > 0):
                pygame.draw.polygon(s_alpha, pygamefillcolor,
                                    point_list_rounded, 0)
            if (pygamecolor != pygamefillcolor) and (pygamecolor.a > 0):
                pygame.draw.lines(s_alpha, pygamecolor, True,
                                  point_list_rounded, line_width)

            self._pygame_surface.blit(s_alpha, (0, 0))

    def draw_polyline(self,
                      point_list,
                      line_width, line_color):
        # type: (Sequence[Sequence[Union[int, float]]], Union[int, float], str) -> None  # noqa
        """
        Draw line segments between a list of points.

        If `line_width` > 1, ends are poorly made!

        :param point_list: not empty (tuple or list)
                           of ((int or float, int or float)
                           or [int or float, int or float])
        :param line_width: (int or float) > 0
        :param line_color: str
        """
        assert isinstance(point_list, (tuple, list)), type(point_list)
        assert len(point_list) > 0, len(point_list)

        if __debug__:
            for point in point_list:
                assert isinstance(point, (tuple, list)), type(point)
                assert len(point) == 2, len(point)
                assert isinstance(point[0], (int, float)), type(point[0])
                assert isinstance(point[1], (int, float)), type(point[1])

        assert isinstance(line_width, (int, float)), type(line_width)
        assert line_width > 0, line_width

        assert isinstance(line_color, str), type(line_color)

        if len(point_list) == 1:
            return

        pygamecolor = _simpleguicolor_to_pygamecolor(line_color)

        point_list_rounded = [_pos_round(point) for point in point_list]

        del point_list

        line_width = int(round(line_width))

        if pygamecolor.a == 255:  # without alpha
            pygame.draw.lines(self._pygame_surface, pygamecolor, False,
                              point_list_rounded, line_width)
        elif pygamecolor.a > 0:   # with alpha (not null)
            s_alpha = pygame.surface.Surface((self._width, self._height),  # pylint: disable=too-many-function-args  # noqa
                                             pygame.SRCALPHA)  # pylint: disable=no-member  # noqa

            pygame.draw.lines(s_alpha, pygamecolor, False,
                              point_list_rounded, line_width)

            self._pygame_surface.blit(s_alpha, (0, 0))

    def draw_text(self,  # pylint: disable=too-many-arguments
                  text, point,
                  font_size, font_color,
                  font_face='serif',
                  _font_size_coef=3 / 4):
        # type: (str, Sequence[Union[int, float]], Union[int, float], str, str, Union[int, float]) -> None  # noqa
        """
        Draw the `text` string at the position `point`.

        (`point[0]` is the left of the text,
        `point[1]` is the bottom of the text.)

        If correponding font in Pygame is not founded,
        then use the default `pygame.font.Font`.

        `_font_size_coef` is used to adjust the vertical positioning.
        **(This paramater is not available in SimpleGUI of CodeSkulptor.)**

        :warning: This method can't draw multiline text.

        To draw multiline text, see `simplegui_lib_draw.draw_text_multi()`_ .

        .. _`simplegui_lib_draw.draw_text_multi()`: ../simplegui_lib_draw.html#SimpleGUICS2Pygame.simplegui_lib_draw.draw_text_multi

        :param text: str
        :param point: (int or float, int or float)
                      or [int or float, int or float]
        :param font_size: (int or float) >= 0
        :param font_color: str
        :param font_face: str == 'monospace', 'sans-serif', 'serif'
        :param _font_size_coef: int or float

        :raise: ValueError if text contains unprintable whitespace character

        **(Alpha color channel don't work!!!)**
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
        assert font_face in _SIMPLEGUIFONTFACE_TO_PYGAMEFONTNAME, font_face

        assert isinstance(_font_size_coef, (int, float)), type(_font_size_coef)

        if text == '':
            return

        if _RE_UNPRINTABLE_WHITESPACE_CHAR.search(text):
            raise ValueError('text may not contain non-printing characters')

        pygamecolor = _simpleguicolor_to_pygamecolor(font_color)
        font_size = int(round(font_size))

        if (pygamecolor.a > 0) and (font_size > 0):
            pygame_surface_text = _simpleguifontface_to_pygamefont(
                font_face, font_size).render(text, True, pygamecolor)

            # if pygamecolor.a == 255:  # without alpha
            self._pygame_surface.blit(
                pygame_surface_text,
                (point[0],
                 (point[1] -
                  pygame_surface_text.get_height() * _font_size_coef)))
            # else:                     # with alpha (not null)
            #     # Don't work!!!
            #     s_alpha = pygame.surface.Surface((pygame_surface_text.get_width(),  # noqa
            #                                       pygame_surface_text.get_height()),  # noqa
            #                                      pygame.SRCALPHA)
            #     s_alpha.blit(pygame_surface_text, (0, 0))
            #     self._pygame_surface.blit(
            #         s_alpha,
            #         (point[0],
            #          (point[1] -
            #           pygame_surface_text.get_height() * _font_size_coef)))


#
# SimpleGUI function
####################
def create_invisible_canvas(width, height):  # type: (int, int) -> Canvas
    """
    NOT IMPLEMENTED!
    (Return a "weak" `Canvas`.)

    (Available in SimpleGUI of CodeSkulptor
    but *not in CodeSkulptor documentation*!)

    :param width: int >= 0
    :param height: int >= 0

    :return: Canvas
    """
    assert isinstance(width, int), type(width)
    assert width >= 0, width

    assert isinstance(height, int), type(height)
    assert height >= 0, height

    return Canvas(None, width, height)
