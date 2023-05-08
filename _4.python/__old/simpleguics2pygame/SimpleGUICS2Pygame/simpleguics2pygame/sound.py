# -*- coding: latin-1 -*-

"""
simpleguics2pygame module: simpleguics2pygame/sound.

Class Sound.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2015-2016, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: November 29, 2020
"""

from __future__ import print_function

# print('IMPORT', __name__)


__all__ = ('_LocalSound', 'Sound',
           'create_sound', 'load_sound',
           '_load_local_sound')


try:
    from typing import Optional, Sequence, Union
except ImportError:
    pass

import pygame

from SimpleGUICS2Pygame.simpleguics2pygame._arguments import _CONFIG  # pylint: disable=no-name-in-module  # noqa

from SimpleGUICS2Pygame.simpleguics2pygame._media import _load_local_media, _load_media  # pylint: disable=no-name-in-module  # noqa


#
# "Private" function
####################
def _load_local_sound(filename):  # type: (str) -> '_LocalSound'
    """
    Create and return a sound by loading a file from `filename`.
    Not founded file and errors are ignored.

    I recommend to use only Internet resources
    with the `load_sound()` function.
    Then you can use your program **both**
    in standard Python and in CodeSkulptor.
    (See `Tips.html#download-medias`_ .)

    .. _`Tips.html#download-medias`: ../Tips.html#download-medias

    But if it is necessary,
    you can load local sound with this "private" function.

    Supported formats are the same as the `load_sound()` function.

    **(Not available in SimpleGUI of CodeSkulptor.)**

    :param filename: str (**only a valid filename**, not URL)

    :return: _LocalSound
    """
    assert isinstance(filename, str), type(filename)

    return _LocalSound(filename)


#
# Class
#######
class Sound:
    """Sound similar to SimpleGUI `Sound` of CodeSkulptor."""

    _dir_search_first = '_snd/'
    """
    `load_sound()` try **first** to loading sound from this directory,
    and next if failed, try to loading from URL.

    This local directory is relative to the directory of your program.
    """

    _load_disabled = _CONFIG['--no-load-sound']
    """
    If `True`
    then load sounds are disabled.
    """

    def __init__(self, url):  # type: (str) -> None
        """
        Set a sound (if not Sound._load_disabled).

        **Don't use directly**, use `load_sound()`.

        :param url: str
        """
        assert isinstance(url, str), type(url)

        self._pygame_channel = None  # type: Optional[pygame.mixer.Channel]
        self._pygame_sound = None  # type: Optional[pygame.mixer.Sound]
        if not Sound._load_disabled and (url != ''):
            self._pygame_sound = _load_media('Sound', url,  # type: ignore
                                             Sound._dir_search_first)

    def __repr__(self):  # type: () -> str
        """
        Return `'<Sound object>'`.

        :return: str
        """
        return '<Sound object>'

    def _get_length(self):  # type: () -> Union[int, float]
        """
        Return the length of this sound in seconds.

        (If initialization of this sound was failed
        then return `0`.)

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :return: int or float
        """
        return (self._pygame_sound.get_length()
                if (self._pygame_sound is not None)
                else 0)

    def pause(self):  # type: () -> None
        """
        Pause this sound.
        (Use `Sound.play()` to resume.)
        """
        if ((self._pygame_channel is not None) and
                (self._pygame_channel.get_sound() == self._pygame_sound)):
            self._pygame_channel.pause()

    def play(self):  # type: () -> None
        """
        If this sound is paused
        then resume the sound,
        else start the sound.
        """
        if self._pygame_channel is not None:
            assert self._pygame_sound is not None

            if self._pygame_channel.get_sound() == self._pygame_sound:
                self._pygame_channel.unpause()
            else:
                self._pygame_channel = self._pygame_sound.play()
        elif self._pygame_sound is not None:
            self._pygame_channel = self._pygame_sound.play()

    def rewind(self):  # type: () -> None
        """
        If this sound has already been started
        then stop the sound and rewind to the begining.
        """
        if ((self._pygame_channel is not None) and
                (self._pygame_channel.get_sound() == self._pygame_sound)):
            self._pygame_sound.stop()

    def set_volume(self, volume):  # type: (Union[int, float]) -> None
        """
        Change the volume of this sound.
        The default volume is `1` (maximum).

        :param volume: 0 <= int or float <= 1
        """
        assert isinstance(volume, (int, float)), type(volume)
        assert 0 <= volume <= 1, volume

        if self._pygame_sound is not None:
            self._pygame_sound.set_volume(volume)


#
# "Private" class
#################
class _LocalSound(Sound):
    """
    Child of Sound to load local file sound.

    **(Not available in SimpleGUI of CodeSkulptor.)**
    """

    def __init__(self, filename):  # pylint: disable=super-init-not-called
        # type: (str) -> None
        """
        Set a sound (if not Sound._load_disabled).

        **Don't use directly**, use `_local_load_sound()`.

        :param filename: str
        """
        assert isinstance(filename, str), type(filename)

        self._pygame_channel = None
        self._pygame_sound = None  # type: Optional[pygame.mixer.Sound]
        if not Sound._load_disabled and (filename != ''):
            self._pygame_sound = _load_local_media('Sound', filename)  # type: ignore  # noqa

    def __repr__(self):  # type: () -> str
        """
        Return `'<_LocalSound object>'`.

        :return: str
        """
        return '<_LocalSound object>'


#
# SimpleGUI functions
#####################
def create_sound(sound_data, sample_rate=8000, num_channels=1):
    # type: (Sequence[int], int, int) -> Sound
    """
    NOT YET IMPLEMENTED! (Return an empty `Sound`.)

    (Available in SimpleGUI of CodeSkulptor
    but *not in CodeSkulptor documentation*!)

    :param sound_data: (tuple or list) of (0 <= int < 256)
    :param sample_rate: int >= 0
    :param num_channels: int >= 0

    :return: Sound
    """
    assert isinstance(sound_data, (tuple, list)), type(sound_data)
    if __debug__:
        for data in sound_data:
            assert isinstance(data, int), type(data)
            assert 0 <= data < 256, data

    assert isinstance(sample_rate, int), type(sample_rate)
    assert sample_rate >= 0, sample_rate

    assert isinstance(num_channels, int), type(num_channels)
    assert num_channels >= 0, num_channels

    return Sound('')


def load_sound(url):  # type: (str) -> Sound
    """
    Create and return a sound by loading a file from `url`.
    Not founded URL and errors are ignored.

    SimpleGUICS2Pygame try **first** to loading sound
    from `Sound._dir_search_first` local directory (`_snd/` by default),
    and next if failed, try to loading from `url`.

    This local directory is relative to the directory of your program.

    For example,
    ``load_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/jump.ogg')``
    try first to loading from
    ``_snd/commondatastorage.googleapis.com/codeskulptor_assets/jump.ogg``.

    Supported formats: OGG, WAV and MP3.

    If MP3 sound failed on your system read `installation of audioread`_.

    .. _`installation of audioread`: ../index.html#package-audioread-required

    (Supported formats by CodeSkulptor are browser dependant.)

    (The sound can be started by `Sound.play()`.)

    :param url: str (**only a valid URL**, not local filename)

    :return: Sound
    """
    assert isinstance(url, str), type(url)

    return Sound(url)
