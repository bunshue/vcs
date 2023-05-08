# -*- coding: latin-1 -*-

"""
simpleguics2pygame module: simpleguics2pygame/image.

Class Image.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2015-2016, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: November 29, 2020
"""

from __future__ import division
from __future__ import print_function

# print('IMPORT', __name__)


__all__ = ('Image', '_LocalImage',
           'load_image',
           '_load_local_image')

import collections  # noqa
import sys  # noqa

try:
    from typing import Optional, Tuple
except ImportError:
    pass

import pygame

from SimpleGUICS2Pygame.simpleguics2pygame._media import _load_local_media, _load_media  # pylint: disable=no-name-in-module  # noqa


#
# "Private" function
####################
def _load_local_image(filename):  # type: (str) -> '_LocalImage'
    """
    Create and return an image by loading a file from `filename`.
    Not founded file and errors are ignored.

    I recommend to use only Internet resources
    with the `load_image()` function.
    Then you can use your program **both**
    in standard Python and in CodeSkulptor.
    (See `Tips.html#download-medias`_ .)

    .. _`Tips.html#download-medias`: ../Tips.html#download-medias

    But if it is necessary,
    you can load local image with this "private" function.

    Supported formats are the same as the `load_image()` function.

    **(Not available in SimpleGUI of CodeSkulptor.)**

    :param filename: str (**only a valid filename**, not URL)

    :return: _LocalImage
    """
    assert isinstance(filename, str), type(filename)

    return _LocalImage(filename)


#
# Class
#######
class Image:
    """Image similar to SimpleGUI `Image` of CodeSkulptor."""

    _dir_search_first = '_img/'
    """
    `load_image()` try **first** to loading image from this directory,
    and next if failed, try to loading from URL.

    This local directory is relative to the directory of your program.
    """

    _pygamesurfaces_cache_default_max_size = 1000  # pylint: disable=invalid-name  # noqa
    """
    Default maximum number of Pygame surfaces
    in the `self._pygamesurfaces_cached`.
    """

    def __init__(self, url):  # type: (str) -> None
        """
        Set an image.

        **Don't use directly**, use `load_image()`.

        :param url: str
        """
        assert isinstance(url, str), type(url)

        self._url = url

        self._pygame_surface = None  # type: Optional[pygame.surface.Surface]
        if url != '':
            self._pygame_surface = _load_media('Image', url,  # type: ignore
                                               Image._dir_search_first)

        self._pygamesurfaces_cached = collections.OrderedDict()  # type: collections.OrderedDict[Tuple[int, ...], pygame.surface.Surface]  # noqa

        self._pygamesurfaces_cache_max_size = \
            Image._pygamesurfaces_cache_default_max_size

        if __debug__:
            self._pygamesurfaces_cached_counts = [0, 0]
            self._draw_count = 0

    def __repr__(self):  # type: () -> str
        """
        Return `'<Image object>'`.

        :return: str
        """
        return '<Image object>'

    def _print_stats_cache(self, text='', short_url=True):
        # type: (str, bool) -> None
        """
        Print to stderr some statistics of cached Pygame surfaces
        used by this image.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :param text: str
        :param short_url: bool
        """
        if __debug__:
            print('{}{:4} {:4}({:4},{:4})/{:4}={:2}% {}'
                  .format(text,
                          len(self._pygamesurfaces_cached),
                          sum(self._pygamesurfaces_cached_counts),
                          self._pygamesurfaces_cached_counts[0],
                          self._pygamesurfaces_cached_counts[1],
                          self._draw_count,
                          ((sum(self._pygamesurfaces_cached_counts) * 100 //
                            self._draw_count)
                           if self._draw_count != 0
                           else ''),
                          (self._url.split('/')[-1] if short_url
                           else self._url)),
                  file=sys.stderr)
        else:
            print('{}{:4} {}'.format(text,
                                     len(self._pygamesurfaces_cached),
                                     (self._url.split('/')[-1] if short_url
                                      else self._url)),
                  file=sys.stderr)

    def _pygamesurfaces_cached_clear(self):  # type: () -> None
        """
        Empty the cache of Pygame surfaces used by this image.

        **(Not available in SimpleGUI of CodeSkulptor.)**
        """
        self._pygamesurfaces_cached = collections.OrderedDict()

        if __debug__:
            self._pygamesurfaces_cached_counts = [0, 0]
            self._draw_count = 0

    def get_height(self):  # type: () -> int
        """
        Return the height ot this image.

        (If initialization of this image was failed
        then return `0`.)

        :return: int
        """
        return (self._pygame_surface.get_height()
                if self._pygame_surface is not None
                else 0)

    def get_width(self):  # type: () -> int
        """
        Return the width ot this image.

        (If initialization of this image was failed
        then return `0`.)

        :return: int
        """
        return (self._pygame_surface.get_width()
                if self._pygame_surface is not None
                else 0)


#
# "Private" class
#################
class _LocalImage(Image):
    """
    Child of Image to load local file image.

    **(Not available in SimpleGUI of CodeSkulptor.)**
    """

    def __init__(self, filename):  # pylint: disable=super-init-not-called
        # type: (str) -> None
        """
        Set an image.

        **Don't use directly**, use `_load_local_image()`.

        :param filename: str
        """
        assert isinstance(filename, str), type(filename)

        self._url = filename

        self._pygame_surface = None  # type: Optional[pygame.surface.Surface]
        if filename != '':
            self._pygame_surface = _load_local_media('Image', filename)  # type: ignore  # noqa

        self._pygamesurfaces_cached = collections.OrderedDict()

        self._pygamesurfaces_cache_max_size = \
            Image._pygamesurfaces_cache_default_max_size

        if __debug__:
            self._pygamesurfaces_cached_counts = [0, 0]
            self._draw_count = 0

    def __repr__(self):  # type: () -> str
        """
        Return `'<_LocalImage object>'`.

        :return: str
        """
        return '<_LocalImage object>'


#
# SimpleGUI function
####################
def load_image(url):  # type: (str) -> Image
    """
    Create and return an image by loading a file from `url`.
    Not founded URL and errors are ignored.

    SimpleGUICS2Pygame try **first** to loading image
    from `Image._dir_search_first` local directory (`_img/` by default),
    and next if failed, try to loading from `url`.

    This local directory is relative to the directory of your program.

    For example,
    ``load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png')``
    try first to loading from
    ``_img/commondatastorage.googleapis.com/codeskulptor_assets/lathrop/double_ship.png``.

    Supported formats are supported formats by Pygame to load:
    PNG, JPG, GIF (not animated)...
    (see https://www.pygame.org/docs/ref/image.html ).

    (CodeSkulptor may supported other formats,
    dependant on browser support.)

    I recommend PNG and JPG format.

    CodeSkulptor loads images **asynchronously**
    (the program continues without waiting for the images to be loaded).
    To handle this problem, you can use ``simplegui_lib_loader.Loader`` class.

    :param url: str (**only a valid URL**, not local filename)

    :return: Image
    """
    assert isinstance(url, str), type(url)

    return Image(url)
