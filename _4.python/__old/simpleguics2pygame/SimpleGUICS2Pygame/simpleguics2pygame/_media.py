# -*- coding: latin-1 -*-

"""
simpleguics2pygame module: simpleguics2pygame/_media.

Media (images and sounds) helpers.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2015, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: November 29, 2020
"""

from __future__ import print_function

# print('IMPORT', __name__)


__all__ = tuple()  # type: tuple


from io import BytesIO  # noqa
from os.path import abspath, dirname, expanduser, isdir, isfile, join, splitext  # noqa
from re import sub  # noqa
from sys import argv, stderr, version_info  # noqa

import atexit  # noqa
import os  # noqa

import pygame

if version_info[0] >= 3:
    from urllib.parse import urlsplit
    from urllib.request import urlopen
else:
    from urlparse import urlsplit  # type: ignore  # pylint: disable=import-error  # noqa
    from urllib2 import urlopen  # type: ignore  # pylint: disable=import-error  # noqa

try:
    from typing import Dict, List, Optional, Union
except ImportError:
    pass

from SimpleGUICS2Pygame.simpleguics2pygame._arguments import _CONFIG  # pylint: disable=wrong-import-position,no-name-in-module  # noqa


#
# Private global constant
#########################
_MIXER_FREQUENCY = 22050
"""
Sound frequency used by the mixer module of Pygame.
"""


_MIXER_INITIALIZED = False
"""
If `True`
then pygame.mixer is initialized.
"""


#
# Private global variables
##########################
_PRINT_LOAD_MEDIAS = _CONFIG['--print-load-medias']
"""
If `True`
then print URLs or locals filename loaded by `load_image()`
and `load_sound()`.
"""

__PYGAMEMEDIAS_CACHED = dict()  # type: Dict[str, Union[pygame.surface.Surface, pygame.mixer.Sound]]  # noqa
"""
`Dict` {`str` URL: `pygame.surface.Surface or pygame.mixer.Sound`}.
"""

_SAVE_DOWNLOADED_MEDIAS = _CONFIG['--save-downloaded-medias']
"""
If `True`
then save images and sounds downloaded from Web
that don't already exist in local directory.
See _SAVE_DOWNLOADED_MEDIAS_OVERWRITE.
"""

_SAVE_DOWNLOADED_MEDIAS_OVERWRITE = _CONFIG['--overwrite-downloaded-medias']
"""
If `True` and `_SAVE_DOWNLOADED_MEDIAS`
then download all images and sounds from Web
and save in local directory even if they already exist.
"""


__TMP_FILENAMES = []  # type: List[str]
"""List of filenames of temporary files that must be delete."""


#
# "Private" functions
#####################
def __delete_tmp_files():  # type: () -> None
    """
    Delete all temporary files in `__TMP_FILENAMES`.

    Automatically called when program ending.
    """
    for filename in __TMP_FILENAMES:
        os.remove(filename)


def _load_local_media(type_of_media, filename):
    # type: (str, str) -> Optional[Union[pygame.surface.Surface, pygame.mixer.Sound]]  # noqa
    """
    Load an image or a sound from local file `filename`.

    **Don't use directly**,
    this function is use by `_LocalImage` and `_LocalSound` classes.

    **(Not available in SimpleGUI of CodeSkulptor.)**

    Side effects:

    * If the media is a valid sound\
      then init the pygame.mixer and set _MIXER_INITIALIZED to `True`.

    :param type_of_media: 'Image' or 'Sound'
    :param filename: str

    :return: pygame.surface.Surface or pygame.mixer.Sound or None
    """
    assert type_of_media in ('Image', 'Sound'), type(type_of_media)
    assert isinstance(filename, str), type(filename)

    filename = abspath(expanduser(filename))

    media_is_image = (type_of_media == 'Image')

    if not media_is_image:
        __mixer_init()

    # Check if is correct sound extension
    if not media_is_image and (filename[-4:].lower() not in ('.mp3', '.ogg', '.wav')):  # noqa
        if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access
            print('Sound format not supported "{}"'.format(filename),
                  file=stderr)
            stderr.flush()

        return None

    # Load
    try:
        media = (pygame.image.load(filename) if media_is_image
                 else (__load_local_mp3_with_audioread(filename)
                       if filename[-4:].lower() == '.mp3'
                       else pygame.mixer.Sound(filename)))  # OGG or WAV
    except Exception as exc:  # pylint: disable=broad-except
        if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access
            print('{} Pygame local loading "{}" FAILED! {}'
                  .format(type_of_media, filename, exc),
                  file=stderr)
            stderr.flush()

        return None

    return media


def __load_local_mp3_with_audioread(filename):
    # type: (str) -> Optional[pygame.mixer.Sound]
    """
    Load a MP3 sound from local file `filename`.

    **Required package `audioread`.**

    **Don't use directly**,
    this function is use by `_load_local_media` and `_load_media`.

    **(Not available in SimpleGUI of CodeSkulptor.)**

    Adapted from `audioread` example:
    https://github.com/beetbox/audioread/blob/177182e3f0301cd7d27e984ce45cee7436646db4/decode.py

    :param filename: str

    :return: pygame.mixer.Sound or None
    """  # noqa
    import contextlib  # pylint: disable=import-outside-toplevel
    import wave  # pylint: disable=import-outside-toplevel

    import audioread  # pylint: disable=import-outside-toplevel

    data = BytesIO()

    with contextlib.closing(wave.open(data, 'wb')) as fout:
        try:
            with audioread.audio_open(filename) as fin:
                fout.setnchannels(fin.channels)
                fout.setframerate(fin.samplerate)
                fout.setsampwidth(2)

                for buf in fin:
                    fout.writeframes(buf)
        except audioread.DecodeError:
            return None

    data.seek(0)

    return pygame.mixer.Sound(data)


def _load_media(type_of_media, url, local_dir):  # pylint: disable=too-many-branches,too-many-statements,too-many-return-statements,too-many-locals  # noqa
    # type: (str, str, str) -> Optional[Union[pygame.surface.Surface, pygame.mixer.Sound]]  # noqa
    """
    Load an image or a sound from Web or local directory,
    and save if asked with _SAVE_DOWNLOADED_MEDIAS
    and _SAVE_DOWNLOADED_MEDIAS_OVERWRITE.

    If local_dir don't exist it is created.

    **Don't use directly**,
    this function is use by `Image` and `Sound` classes.

    **(Not available in SimpleGUI of CodeSkulptor.)**

    Side effects:

    * Each new url is added to `__PYGAMEMEDIAS_CACHED`.
    * If the media is a valid sound\
      then init the pygame.mixer and set _MIXER_INITIALIZED to `True`.
    * If `_PRINT_LOAD_MEDIAS` then print loading informations to stderr.

    :param type_of_media: 'Image' or 'Sound'
    :param url: str
    :param local_dir: str

    :return: pygame.surface.Surface or pygame.mixer.Sound or None
    """
    assert type_of_media in ('Image', 'Sound'), type(type_of_media)
    assert isinstance(url, str), type(url)
    assert isinstance(local_dir, str), type(local_dir)

    media_is_image = (type_of_media == 'Image')

    if not media_is_image:
        __mixer_init()

    # Search in cache
    cached = __PYGAMEMEDIAS_CACHED.get(url)
    if cached is not None:
        # Already in cache
        media = (cached.copy() if media_is_image  # type: ignore
                 else pygame.mixer.Sound(cached))  # duplicate sound
        if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access
            print('{} "{}" got in cache'.format(type_of_media, url),
                  file=stderr)
            stderr.flush()

        return media

    # Build a "normalized" filename
    filename = __normalized_filename(url, local_dir)

    # Check if is correct sound extension
    if not media_is_image and (filename[-4:].lower() not in ('.mp3', '.ogg', '.wav')):  # noqa
        if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access
            print('Sound format not supported "{}"'.format(url),
                  file=stderr)
            stderr.flush()

        return None

    filename_exist = isfile(filename)

    # Load...
    if not _SAVE_DOWNLOADED_MEDIAS_OVERWRITE and filename_exist:
        try:
            # Load from local file
            media = (pygame.image.load(filename) if media_is_image
                     else (__load_local_mp3_with_audioread(filename)
                           if filename[-4:].lower() == '.mp3'
                           else pygame.mixer.Sound(filename)))  # OGG or WAV
            if _PRINT_LOAD_MEDIAS:
                print('{} loaded "{}" instead "{}"'.format(type_of_media,
                                                           filename, url),
                      file=stderr)
                stderr.flush()

            __PYGAMEMEDIAS_CACHED[url] = media  # type: ignore

            return media
        except Exception as exc:  # pylint: disable=broad-except
            if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access
                print('{} cache loading "{}" FAILED! {}'.format(type_of_media,
                                                                filename, exc),
                      file=stderr)
                stderr.flush()

    try:
        # Download from url
        media_data = urlopen(url).read()
        if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access
            print('{} downloaded "{}"'.format(type_of_media, url),
                  file=stderr)
            stderr.flush()
    except Exception as exc:  # pylint: disable=broad-except
        if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access
            print('{} downloading "{}" FAILED! {}'.format(type_of_media,
                                                          url, exc),
                  file=stderr)
            stderr.flush()

        return None

    try:
        if media_is_image or (filename[-4:].lower() != '.mp3'):  # image or OGG or WAV  # noqa
            media_bytesio = BytesIO(media_data)
            media = (pygame.image.load(media_bytesio) if media_is_image
                     else pygame.mixer.Sound(media_bytesio))  # OGG or WAV
        else:                                                    # MP3
            import tempfile  # pylint: disable=import-outside-toplevel

            # Create temporary file
            tmp_file, tmp_filename = tempfile.mkstemp(
                prefix='SimpleGUICS2Pygame_', suffix='.mp3')
            __TMP_FILENAMES.append(tmp_filename)
            os.close(tmp_file)

            # Write MP3 data in temporary file
            with open(tmp_filename, 'ab') as fout:
                fout.write(media_data)

            # Load MP3 sound from temporary file
            media = __load_local_mp3_with_audioread(tmp_filename)
    except Exception as exc:  # pylint: disable=broad-except
        if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access
            print('{} Pygame loading "{}" FAILED! {}'.format(type_of_media,
                                                             url, exc),
                  file=stderr)
            stderr.flush()

        return None

    if _SAVE_DOWNLOADED_MEDIAS:
        # Save copy locally
        if _SAVE_DOWNLOADED_MEDIAS_OVERWRITE or not filename_exist:
            if not isdir(dirname(filename)):
                try:
                    # Create local directory
                    os.makedirs(dirname(filename))
                    if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access  # noqa
                        print('      Created "{}" directory'
                              .format(dirname(filename)),
                              file=stderr)
                except Exception as exc:  # pylint: disable=broad-except
                    if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access  # noqa
                        print('      Creating "{}" directory FAILED!! {}'
                              .format(dirname(filename), exc),
                              file=stderr)

            try:
                # Save to local file
                with open(filename, 'wb') as outfile:
                    outfile.write(media_data)
                if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access  # noqa
                    print('      {} in "{}"'
                          .format(('Overwritten' if filename_exist
                                   else 'Saved'), filename),
                          file=stderr)
            except Exception as exc:  # pylint: disable=broad-except
                if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access  # noqa
                    print('      {} in "{}" FAILED! {}'
                          .format(('Overwriting' if filename_exist
                                   else 'Saving'), filename, exc),
                          file=stderr)
        elif _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access
            print('      Local file "{}" already exist'
                  .format(filename),
                  file=stderr)

    if _PRINT_LOAD_MEDIAS:  # pylint: disable=protected-access
        stderr.flush()

    __PYGAMEMEDIAS_CACHED[url] = media  # type: ignore

    return media


#
# Private functions
###################
def __mixer_init():  # type: () -> None
    """Initialize Pygame mixer (if not already initialized)"""
    global _MIXER_INITIALIZED  # pylint: disable=global-statement

    if not _MIXER_INITIALIZED:
        _MIXER_INITIALIZED = True
        pygame.mixer.init(_MIXER_FREQUENCY)
        if pygame.display.get_surface() is None:
            # Workaround: Open a fake "empty" display
            # because on Window$ (and maybe other systems)
            # sound doesn't play if there is no display!
            pygame.display.set_mode((1, 1), flags=pygame.NOFRAME)  # pylint: disable=no-member  # noqa


def __normalized_filename(url, local_dir):  # type: (str, str) -> str
    """
    Build a "normalized" filename from url.

    :param url: str
    :param local_dir: str

    :return: str
    """
    assert isinstance(url, str), type(url)
    assert isinstance(local_dir, str), type(local_dir)

    urlsplitted = urlsplit(url)

    filename = join(dirname(argv[0]),
                    local_dir,
                    sub('[^._/0-9A-Za-z]', '_',
                        join(urlsplitted.netloc + '/',
                             urlsplitted.path[1:]).replace('\\', '/')))

    if urlsplitted.query != '':  # add "normalized" query part
        pieces = list(splitext(filename))
        pieces.insert(1, sub('[^._0-9A-Za-z]', '_', urlsplitted.query))
        filename = ''.join(pieces)

    return filename


#
# Main
######
atexit.register(__delete_tmp_files)
