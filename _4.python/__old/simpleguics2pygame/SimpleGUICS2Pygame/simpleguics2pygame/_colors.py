# -*- coding: latin-1 -*-

"""
simpleguics2pygame module: simpleguics2pygame/_colors.

Colors helpers.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2015, 2018, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: November 29, 2020
"""

from __future__ import division
from __future__ import print_function

# print('IMPORT', __name__)


__all__ = tuple()  # type: tuple


import colorsys  # noqa

try:
    from typing import Dict
except ImportError:
    pass

import pygame


#
# Private global constant
#########################
_SIMPLEGUICOLOR_TO_PYGAMECOLOR = {
    '_default': pygame.Color('#ff0000'),  # red, probably indicates error
    'transparent': pygame.Color('#00000000'),
    'aliceblue': pygame.Color('#f0f8ff'),
    'antiquewhite': pygame.Color('#faebd7'),
    'aqua': pygame.Color('#00ffff'),
    'aquamarine': pygame.Color('#7fffd4'),
    'azure': pygame.Color('#f0ffff'),
    'beige': pygame.Color('#f5f5dc'),
    'bisque': pygame.Color('#ffe4c4'),
    'black': pygame.Color('#000000'),
    'blanchedalmond': pygame.Color('#ffebcd'),
    'blue': pygame.Color('#0000ff'),
    'blueviolet': pygame.Color('#8a2be2'),
    'brown': pygame.Color('#a52a2a'),
    'burlywood': pygame.Color('#deb887'),
    'cadetblue': pygame.Color('#5f9ea0'),
    'chartreuse': pygame.Color('#7fff00'),
    'chocolate': pygame.Color('#d2691e'),
    'coral': pygame.Color('#ff7f50'),
    'cornflowerblue': pygame.Color('#6495ed'),
    'cornsilk': pygame.Color('#fff8dc'),
    'crimson': pygame.Color('#dc143c'),
    'cyan': pygame.Color('#00ffff'),
    'darkblue': pygame.Color('#00008b'),
    'darkcyan': pygame.Color('#008b8b'),
    'darkgoldenrod': pygame.Color('#b8860b'),
    'darkgray': pygame.Color('#a9a9a9'),
    'darkgrey': pygame.Color('#a9a9a9'),
    'darkgreen': pygame.Color('#006400'),
    'darkkhaki': pygame.Color('#bdb76b'),
    'darkmagenta': pygame.Color('#8b008b'),
    'darkolivegreen': pygame.Color('#556b2f'),
    'darkorange': pygame.Color('#ff8c00'),
    'darkorchid': pygame.Color('#9932cc'),
    'darkred': pygame.Color('#8b0000'),
    'darksalmon': pygame.Color('#e9967a'),
    'darkseagreen': pygame.Color('#8fbc8f'),
    'darkslateblue': pygame.Color('#483d8b'),
    'darkslategray': pygame.Color('#2f4f4f'),
    'darkslategrey': pygame.Color('#2f4f4f'),
    'darkturquoise': pygame.Color('#00ced1'),
    'darkviolet': pygame.Color('#9400d3'),
    'deeppink': pygame.Color('#ff1493'),
    'deepskyblue': pygame.Color('#00bfff'),
    'dimgray': pygame.Color('#696969'),
    'dimgrey': pygame.Color('#696969'),
    'dodgerblue': pygame.Color('#1e90ff'),
    'firebrick': pygame.Color('#b22222'),
    'floralwhite': pygame.Color('#fffaf0'),
    'forestgreen': pygame.Color('#228b22'),
    'fuchsia': pygame.Color('#ff00ff'),
    'gainsboro': pygame.Color('#dcdcdc'),
    'ghostwhite': pygame.Color('#f8f8ff'),
    'gold': pygame.Color('#ffd700'),
    'goldenrod': pygame.Color('#daa520'),
    'gray': pygame.Color('#808080'),
    'grey': pygame.Color('#808080'),
    'green': pygame.Color('#008000'),
    'greenyellow': pygame.Color('#adff2f'),
    'honeydew': pygame.Color('#f0fff0'),
    'hotpink': pygame.Color('#ff69b4'),
    'indianred': pygame.Color('#cd5c5c'),
    'indigo': pygame.Color('#4b0082'),
    'ivory': pygame.Color('#fffff0'),
    'khaki': pygame.Color('#f0e68c'),
    'lavender': pygame.Color('#e6e6fa'),
    'lavenderblush': pygame.Color('#fff0f5'),
    'lawngreen': pygame.Color('#7cfc00'),
    'lemonchiffon': pygame.Color('#fffacd'),
    'lightblue': pygame.Color('#add8e6'),
    'lightcoral': pygame.Color('#f08080'),
    'lightcyan': pygame.Color('#e0ffff'),
    'lightgoldenrodyellow': pygame.Color('#fafad2'),
    'lightgray': pygame.Color('#d3d3d3'),
    'lightgrey': pygame.Color('#d3d3d3'),
    'lightgreen': pygame.Color('#90ee90'),
    'lightpink': pygame.Color('#ffb6c1'),
    'lightsalmon': pygame.Color('#ffa07a'),
    'lightseagreen': pygame.Color('#20b2aa'),
    'lightskyblue': pygame.Color('#87cefa'),
    'lightslategray': pygame.Color('#778899'),
    'lightslategrey': pygame.Color('#778899'),
    'lightsteelblue': pygame.Color('#b0c4de'),
    'lightyellow': pygame.Color('#ffffe0'),
    'lime': pygame.Color('#00ff00'),
    'limegreen': pygame.Color('#32cd32'),
    'linen': pygame.Color('#faf0e6'),
    'magenta': pygame.Color('#ff00ff'),
    'maroon': pygame.Color('#800000'),
    'mediumaquamarine': pygame.Color('#66cdaa'),
    'mediumblue': pygame.Color('#0000cd'),
    'mediumorchid': pygame.Color('#ba55d3'),
    'mediumpurple': pygame.Color('#9370db'),
    'mediumseagreen': pygame.Color('#3cb371'),
    'mediumslateblue': pygame.Color('#7b68ee'),
    'mediumspringgreen': pygame.Color('#00fa9a'),
    'mediumturquoise': pygame.Color('#48d1cc'),
    'mediumvioletred': pygame.Color('#c71585'),
    'midnightblue': pygame.Color('#191970'),
    'mintcream': pygame.Color('#f5fffa'),
    'mistyrose': pygame.Color('#ffe4e1'),
    'moccasin': pygame.Color('#ffe4b5'),
    'navajowhite': pygame.Color('#ffdead'),
    'navy': pygame.Color('#000080'),
    'oldlace': pygame.Color('#fdf5e6'),
    'olive': pygame.Color('#808000'),
    'olivedrab': pygame.Color('#6b8e23'),
    'orange': pygame.Color('#ffa500'),
    'orangered': pygame.Color('#ff4500'),
    'orchid': pygame.Color('#da70d6'),
    'palegoldenrod': pygame.Color('#eee8aa'),
    'palegreen': pygame.Color('#98fb98'),
    'paleturquoise': pygame.Color('#afeeee'),
    'palevioletred': pygame.Color('#db7093'),
    'papayawhip': pygame.Color('#ffefd5'),
    'peachpuff': pygame.Color('#ffdab9'),
    'peru': pygame.Color('#cd853f'),
    'pink': pygame.Color('#ffc0cb'),
    'plum': pygame.Color('#dda0dd'),
    'powderblue': pygame.Color('#b0e0e6'),
    'purple': pygame.Color('#800080'),
    'red': pygame.Color('#ff0000'),
    'rosybrown': pygame.Color('#bc8f8f'),
    'royalblue': pygame.Color('#4169e1'),
    'saddlebrown': pygame.Color('#8b4513'),
    'salmon': pygame.Color('#fa8072'),
    'sandybrown': pygame.Color('#f4a460'),
    'seagreen': pygame.Color('#2e8b57'),
    'seashell': pygame.Color('#fff5ee'),
    'sienna': pygame.Color('#a0522d'),
    'silver': pygame.Color('#c0c0c0'),
    'skyblue': pygame.Color('#87ceeb'),
    'slateblue': pygame.Color('#6a5acd'),
    'slategray': pygame.Color('#708090'),
    'slategrey': pygame.Color('#708090'),
    'snow': pygame.Color('#fffafa'),
    'springgreen': pygame.Color('#00ff7f'),
    'steelblue': pygame.Color('#4682b4'),
    'tan': pygame.Color('#d2b48c'),
    'teal': pygame.Color('#008080'),
    'thistle': pygame.Color('#d8bfd8'),
    'tomato': pygame.Color('#ff6347'),
    'turquoise': pygame.Color('#40e0d0'),
    'violet': pygame.Color('#ee82ee'),
    'wheat': pygame.Color('#f5deb3'),
    'white': pygame.Color('#ffffff'),
    'whitesmoke': pygame.Color('#f5f5f5'),
    'yellow': pygame.Color('#ffff00'),
    'yellowgreen': pygame.Color('#9acd32')}
"""
`Dict` {`str` color constant name: corresponding `pygame.Color`}.

**(Not available in SimpleGUI of CodeSkulptor.)**

See http://www.opimedia.be/DS/mementos/colors.htm ,
http://www.w3.org/TR/css3-color/#html4
and http://www.w3.org/TR/css3-color/#svg-color

List from https://www.w3schools.com/colors/colors_names.asp
"""


#
# Private global variable
#########################
_PYGAMECOLORS_CACHED = dict()  # type: Dict[str, pygame.Color]
"""
`Dict` {`str` CodeSkulptor color: `pygame.font.Color`}.

**(Not available in SimpleGUI of CodeSkulptor.)**
"""


#
# "Private" function
####################
def _simpleguicolor_to_pygamecolor(
        color,
        default_pygame_color=_SIMPLEGUICOLOR_TO_PYGAMECOLOR['_default']):
    # type: (str, pygame.Color) -> pygame.Color
    """
    Return a `pygame.Color` object
    corresponding to the SimpleGUI string `color` in format:

    * '#rrggbb',
    * '#rgb',
    * 'rgb(red, green, blue)',
    * 'rgba(red, green, blue, alpha)'
    * 'hsl(hue, saturation, lightness)'
    * 'hsla(hue, saturation, lightness, alpha)'
    * or constant name in `_SIMPLEGUICOLOR_TO_PYGAMECOLOR` \
      (`default_pygame_color` if the constant name are not founded).

    See http://www.opimedia.be/DS/mementos/colors.htm
    and http://www.w3.org/TR/css3-color/

    **(Not available in SimpleGUI of CodeSkulptor.)**

    Side effect: Each new color is added to `_PYGAMECOLORS_CACHED`.
    See `Frame._pygamecolors_cached_clear()`.

    .. _`Frame._pygamecolors_cached_clear()`: frame.html#SimpleGUICS2Pygame.simpleguics2pygame.frame.Frame._pygamecolors_cached_clear

    :param color: str
    :param default_pygame_color: pygame.Color

    :return: pygame.Color
    """  # noqa
    pygame_color = _PYGAMECOLORS_CACHED.get(color)  # pylint: disable=protected-access  # noqa
    if pygame_color is not None:  # already in cache
        return pygame_color

    assert isinstance(color, str), type(color)
    assert len(color) > 0

    # assert (((color[0] == '#') and (len(color) in (4, 7))) or
    #         (color[:4] == 'rgb(') or
    #         (color[:5] == 'rgba(') or
    #         (color[:4] == 'hsl(') or
    #         (color[:5] == 'hsla(') or
    #         (color.lower() in _SIMPLEGUICOLOR_TO_PYGAMECOLOR)), color

    color = color.lower()

    if color[0] == '#':  # format #rrggbb or #rgb
        # See http://www.w3.org/TR/css3-color/#numerical
        pygame_color = pygame.Color(
            color if len(color) == 7
            else '#' + color[1] * 2 + color[2] * 2 + color[3] * 2)
    elif color[:3] == 'rgb':
        if color[3] == '(':  # format rgb(red, green, blue)
            # See http://www.w3.org/TR/css3-color/#rgb-color
            assert color[-1] == ')', color

            channels = color[4:-1].split(',')

            assert len(channels) == 3, channels

            pygame_color = pygame.Color(max(0, min(255, int(channels[0]))),
                                        max(0, min(255, int(channels[1]))),
                                        max(0, min(255, int(channels[2]))))
        else:                # format rgba(red, green, blue, alpha)
            # See http://www.w3.org/TR/css3-color/#rgba-color
            assert color[3:5] == 'a(', color
            assert color[-1] == ')', color

            channels = color[5:-1].split(',')

            assert len(channels) == 4, channels

            pygame_color = pygame.Color(
                max(0, min(255, int(channels[0]))),
                max(0, min(255, int(channels[1]))),
                max(0, min(255, int(channels[2]))),
                max(0, min(255, int(round(float(channels[3]) * 255)))))
    elif color[:3] == 'hsl':
        if color[3] == '(':  # format hsl(hue, saturation, lightness)
            # See http://www.w3.org/TR/css3-color/#hsl-color
            assert color[-1] == ')', color

            datas = color[4:-1].split(',')

            assert len(datas) == 3, datas
            assert datas[1][-1] == '%', datas[1]
            assert datas[2][-1] == '%', datas[2]

            red, green, blue = colorsys.hls_to_rgb(
                max(0, min(1, (float(datas[0]) % 360) / 360)),
                max(0, min(1, float(datas[2][:-1]) / 100)),
                max(0, min(1, float(datas[1][:-1]) / 100)))

            pygame_color = pygame.Color(int(round(red * 255)),
                                        int(round(green * 255)),
                                        int(round(blue * 255)))
        else:                # format hsla(hue, saturation, lightness, alpha)
            # See http://www.w3.org/TR/css3-color/#hsla-color
            assert color[3:5] == 'a(', color
            assert color[-1] == ')', color

            datas = color[5:-1].split(',')

            assert len(datas) == 4, datas
            assert datas[1][-1] == '%', datas[1]
            assert datas[2][-1] == '%', datas[2]

            red, green, blue = colorsys.hls_to_rgb(
                max(0, min(1, (float(datas[0]) % 360) / 360)),
                max(0, min(1, float(datas[2][:-1]) / 100)),
                max(0, min(1, float(datas[1][:-1]) / 100)))

            pygame_color = pygame.Color(
                int(round(red * 255)),
                int(round(green * 255)),
                int(round(blue * 255)),
                max(0, min(255, int(round(float(datas[3]) * 255)))))
    else:                # constant name
        # See http://www.w3.org/TR/css3-color/#html4
        # and http://www.w3.org/TR/css3-color/#svg-color
        pygame_color = _SIMPLEGUICOLOR_TO_PYGAMECOLOR.get(color,
                                                          default_pygame_color)

    assert pygame_color is not None

    _PYGAMECOLORS_CACHED[color] = pygame_color

    return pygame_color
