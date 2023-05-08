#!/usr/bin/env python
# -*- coding: latin-1 -*-
# pylint: disable=invalid-name

"""
Display results of Stress_Balls.py on my different environments.

See
https://bitbucket.org/OPiMedia/simpleguics2pygame/src/master/SimpleGUICS2Pygame/example/Stress_Balls/Stress_Balls.py

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013, 2018, 2020-2021 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 5, 2021
"""

try:
    from typing import Dict, Union
except ImportError:
    pass

try:
    # To avoid other simpleplot available in Python
    from codeskulptor import file2url    # pytype: disable=import-error  # pylint: disable=unused-import  # noqa
    import simpleplot  # pytype: disable=import-error

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleplot as simpleplot  # type: ignore

    SIMPLEGUICS2PYGAME = True


# Last results were evaluate on Intel Xeon W3530 Quad-Core 2.8 GHz 6 Gio
# All old results were evaluate on Pentium Dual-Core 2.7 GHz 2 Gio:
ALL_RESULTS = {
    # SimpleGUICS2Pygame on Debian
    'SimpleGUICS2Pygame 2.0.0 -O Python 2.7.13 pygame 1.9.6 Debian 9.12 Stretch':  # noqa
    ({1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 62, 400: 62, 500: 62, 750: 62,
      1000: 60, 1250: 52, 1500: 44, 1750: 38, 2000: 34},   # normal
     {1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 62, 400: 62, 500: 62, 750: 62,
      1000: 60, 1250: 51, 1500: 43, 1750: 38, 2000: 33}),  # REVERSE
    'SimpleGUICS2Pygame 2.0.0 -O Python 3.5.3 pygame 1.9.6 Debian 9.12 Stretch':  # noqa
    ({1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 62, 400: 62, 500: 62, 750: 62,
      1000: 61, 1250: 50, 1500: 44, 1750: 38, 2000: 34},   # normal
     {1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 62, 400: 62, 500: 62, 750: 62,
      1000: 60, 1250: 51, 1500: 43, 1750: 38, 2000: 33}),  # REVERSE
    'SimpleGUICS2Pygame 2.0.0 Python 2.7.13 pygame 1.9.6 Debian 9.12 Stretch':
    ({1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 62, 400: 62, 500: 62, 750: 60,
      1000: 48, 1250: 39, 1500: 34, 1750: 29, 2000: 25},   # normal
     {1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 62, 400: 62, 500: 62, 750: 60,
      1000: 48, 1250: 40, 1500: 33, 1750: 29, 2000: 26}),  # REVERSE
    'SimpleGUICS2Pygame 2.0.0 Python 3.5.3 pygame 1.9.6 Debian 9.12 Stretch':
    ({1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 62, 400: 62, 500: 62, 750: 61,
      1000: 48, 1250: 40, 1500: 33, 1750: 29, 2000: 26},   # normal
     {1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 62, 400: 62, 500: 62, 750: 60,
      1000: 49, 1250: 38, 1500: 34, 1750: 29, 2000: 26}),  # REVERSE

    # SimpleGUICS2Pygame on Window$
    'SimpleGUICS2Pygame 2.0.0 -O Python 2.7.17 pygame 1.9.6 Window$ 10':
    ({1: 57, 10: 60, 20: 59, 30: 59, 40: 59, 50: 59, 75: 59,
      100: 59, 200: 59, 300: 59, 400: 59, 500: 59, 750: 59,
      1000: 61, 1250: 51, 1500: 43, 1750: 37, 2000: 33},   # normal
     {1: 59, 10: 60, 20: 60, 30: 60, 40: 59, 50: 59, 75: 59,
      100: 59, 200: 59, 300: 59, 400: 59, 500: 59, 750: 59,
      1000: 60, 1250: 51, 1500: 43, 1750: 37, 2000: 32}),  # REVERSE
    'SimpleGUICS2Pygame 2.0.0 -O Python 3.8.2 pygame 1.9.6 Window$ 10':
    ({1: 60, 10: 59, 20: 59, 30: 60, 40: 59, 50: 59, 75: 60,
      100: 59, 200: 60, 300: 59, 400: 59, 500: 59, 750: 59,
      1000: 60, 1250: 56, 1500: 47, 1750: 39, 2000: 35},   # normal
     {1: 59, 10: 59, 20: 59, 30: 59, 40: 59, 50: 59, 75: 59,
      100: 60, 200: 60, 300: 60, 400: 59, 500: 59, 750: 59,
      1000: 60, 1250: 59, 1500: 49, 1750: 42, 2000: 36}),  # REVERSE
    'SimpleGUICS2Pygame 2.0.0 Python 2.7.17 pygame 1.9.6 Window$ 10':
    ({1: 59, 10: 59, 20: 59, 30: 59, 40: 59, 50: 59, 75: 59,
      100: 59, 200: 60, 300: 59, 400: 59, 500: 59, 750: 59,
      1000: 47, 1250: 38, 1500: 32, 1750: 27, 2000: 24},   # normal
     {1: 59, 10: 60, 20: 60, 30: 59, 40: 60, 50: 60, 75: 60,
      100: 60, 200: 59, 300: 59, 400: 59, 500: 60, 750: 57,
      1000: 44, 1250: 36, 1500: 30, 1750: 26, 2000: 23}),  # REVERSE
    'SimpleGUICS2Pygame 2.0.0 Python 3.8.2 pygame 1.9.6 Window$ 10':
    ({1: 59, 10: 60, 20: 60, 30: 60, 40: 60, 50: 60, 75: 60,
      100: 59, 200: 60, 300: 60, 400: 59, 500: 60, 750: 59,
      1000: 54, 1250: 43, 1500: 36, 1750: 31, 2000: 27},   # normal
     {1: 59, 10: 59, 20: 59, 30: 59, 40: 59, 50: 59, 75: 59,
      100: 60, 200: 59, 300: 59, 400: 59, 500: 59, 750: 60,
      1000: 57, 1250: 46, 1500: 36, 1750: 31, 2000: 28}),  # REVERSE

    # SimpleGUI in CodeSkulptor2 on Debian
    'CodeSkulptor2 Chromium 73.0 Debian 9.12 Stretch':
    ({1: 59, 10: 60, 20: 60, 30: 60, 40: 60, 50: 60, 75: 60,
      100: 60, 200: 58, 300: 37, 400: 24, 500: 20, 750: 13,
      1000: 10, 1250: 8, 1500: 7, 1750: 6, 2000: 5},   # normal
     {1: 60, 10: 60, 20: 60, 30: 60, 40: 60, 50: 60, 75: 60,
      100: 60, 200: 45, 300: 31, 400: 24, 500: 19, 750: 13,
      1000: 10, 1250: 8, 1500: 7, 1750: 6, 2000: 5}),  # REVERSE
    'CodeSkulptor2 Firefox 68.7 Debian 9.12 Stretch':
    ({1: 1, 10: 0, 20: 0, 30: 0, 40: 0, 50: 0, 75: 0,
      100: 0, 200: 0, 300: 0, 400: 0, 500: 0, 750: 0,
      1000: 0, 1250: 0, 1500: 0, 1750: 0, 2000: 0},   # normal
     {1: 0, 10: 0, 20: 0, 30: 0, 40: 0, 50: 0, 75: 0,
      100: 0, 200: 0, 300: 0, 400: 0, 500: 0, 750: 0,
      1000: 0, 1250: 0, 1500: 0, 1750: 0, 2000: 0}),  # REVERSE

    # SimpleGUI in CodeSkulptor3 on Debian
    'CodeSkulptor3 Chromium 73.0 Debian 9.12 Stretch':
    ({1: 60, 10: 60, 20: 60, 30: 60, 40: 60, 50: 60, 75: 60,
      100: 57, 200: 28, 300: 20, 400: 15, 500: 13, 750: 9,
      1000: 7, 1250: 5, 1500: 5, 1750: 4, 2000: 3},   # normal
     {1: 60, 10: 60, 20: 60, 30: 60, 40: 60, 50: 60, 75: 60,
      100: 52, 200: 22, 300: 17, 400: 15, 500: 12, 750: 8,
      1000: 6, 1250: 5, 1500: 4, 1750: 4, 2000: 3}),  # REVERSE
    'CodeSkulptor3 Firefox 68.7 Debian 9.12 Stretch':
    ({1: 60, 10: 60, 20: 60, 30: 60, 40: 60, 50: 60, 75: 48,
      100: 37, 200: 20, 300: 14, 400: 11, 500: 8, 750: 6,
      1000: 4, 1250: 4, 1500: 3, 1750: 3, 2000: 2},   # normal
     {1: 60, 10: 60, 20: 60, 30: 60, 40: 60, 50: 60, 75: 45,
      100: 35, 200: 18, 300: 12, 400: 9, 500: 8, 750: 5,
      1000: 4, 1250: 3, 1500: 3, 1750: 2, 2000: 2}),  # REVERSE

    # SimpleGUI in CodeSkulptor2 on Window$
    'CodeSkulptor2 Chrome 81.0 Window$ 10':
    ({1: 60, 10: 60, 20: 60, 30: 60, 40: 60, 50: 60, 75: 60,
      100: 60, 200: 55, 300: 37, 400: 28, 500: 22, 750: 15,
      1000: 12, 1250: 10, 1500: 8, 1750: 7, 2000: 6},   # normal
     {1: 60, 10: 60, 20: 60, 30: 60, 40: 60, 50: 60, 75: 60,
      100: 60, 200: 56, 300: 38, 400: 29, 500: 23, 750: 15,
      1000: 12, 1250: 9, 1500: 8, 1750: 7, 2000: 6}),  # REVERSE
    'CodeSkulptor2 Firefox 75.0 Window$ 10':
    ({1: 60, 10: 60, 20: 60, 30: 60, 40: 60, 50: 60, 75: 60,
      100: 60, 200: 41, 300: 28, 400: 21, 500: 18, 750: 12,
      1000: 10, 1250: 8, 1500: 7, 1750: 6, 2000: 5},   # normal
     {1: 59, 10: 60, 20: 60, 30: 60, 40: 60, 50: 60, 75: 60,
      100: 60, 200: 42, 300: 28, 400: 22, 500: 18, 750: 12,
      1000: 9, 1250: 8, 1500: 7, 1750: 6, 2000: 5}),  # REVERSE

    # SimpleGUI in CodeSkulptor3 on Window$
    'CodeSkulptor3 Chrome 81.0 Window$ 10':
    ({1: 60, 10: 60, 20: 60, 30: 60, 40: 60, 50: 60, 75: 60,
      100: 60, 200: 30, 300: 20, 400: 16, 500: 13, 750: 9,
      1000: 7, 1250: 5, 1500: 4, 1750: 4, 2000: 3},   # normal
     {1: 60, 10: 60, 20: 60, 30: 60, 40: 60, 50: 60, 75: 60,
      100: 56, 200: 29, 300: 20, 400: 15, 500: 13, 750: 8,
      1000: 6, 1250: 5, 1500: 4, 1750: 4, 2000: 3}),  # REVERSE
    'CodeSkulptor3 Firefox 75.0 Window$ 10':
    ({1: 60, 10: 60, 20: 60, 30: 60, 40: 60, 50: 60, 75: 56,
      100: 43, 200: 24, 300: 16, 400: 12, 500: 9, 750: 6,
      1000: 5, 1250: 4, 1500: 3, 1750: 3, 2000: 3},   # normal
     {1: 60, 10: 60, 20: 60, 30: 60, 40: 60, 50: 60, 75: 57,
      100: 43, 200: 23, 300: 15, 400: 11, 500: 9, 750: 6,
      1000: 5, 1250: 4, 1500: 3, 1750: 3, 2000: 2}),  # REVERSE

    # SimpleGUITk by David Holm on Debian, https://pypi.org/project/SimpleGUITk
    'SimpleGUITk 1.1.3 -O Python 2.7.13 Debian 9.12 Stretch':
    ({1: 77, 10: 73, 20: 70, 30: 69, 40: 67, 50: 65, 75: 61,
      100: 58, 200: 47, 300: 39, 400: 34, 500: 31, 750: 24,
      1000: 20, 1250: 17, 1500: 15, 1750: 13, 2000: 12},   # normal
     {1: 75, 10: 69, 20: 66, 30: 66, 40: 65, 50: 65, 75: 62,
      100: 60, 200: 49, 300: 43, 400: 37, 500: 33, 750: 26,
      1000: 21, 1250: 18, 1500: 15, 1750: 13, 2000: 12}),  # REVERSE
    'SimpleGUITk 1.1.3 -O Python 3.5.3 Debian 9.12 Stretch':
    ({1: 77, 10: 73, 20: 70, 30: 68, 40: 67, 50: 64, 75: 60,
      100: 58, 200: 45, 300: 38, 400: 33, 500: 29, 750: 23,
      1000: 19, 1250: 16, 1500: 14, 1750: 13, 2000: 11},   # normal
     {1: 79, 10: 69, 20: 66, 30: 66, 40: 65, 50: 64, 75: 61,
      100: 59, 200: 50, 300: 41, 400: 36, 500: 32, 750: 25,
      1000: 21, 1250: 17, 1500: 15, 1750: 13, 2000: 12}),  # REVERSE

    #
    # Old results
    #
    # SimpleGUICS2Pygame on Window$
    'old SimpleGUICS2Pygame 00.70.00 -O Python 2.7.5 Pygame 1.9.2pre Window$ 7':  # noqa
    ({1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 62, 400: 62, 500: 59, 750: 46,
      1000: 37, 1500: 26, 2000: 21},   # normal
     {1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 62, 400: 62, 500: 59, 750: 46,
      1000: 37, 1500: 27, 2000: 21}),  # REVERSE
    'old SimpleGUICS2Pygame 00.70.00 -O Python 3.3.2 Pygame 1.9.2pre Window$ 7':  # noqa
    ({1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 62, 400: 57, 500: 50, 750: 37,
      1000: 30, 1500: 21, 2000: 16},   # normal
     {1: 62, 10: 62, 20: 62, 30: 62, 40: 62, 50: 62, 75: 62,
      100: 62, 200: 62, 300: 61, 400: 56, 500: 48, 750: 35,
      1000: 28, 1500: 20, 2000: 15}),  # REVERSE

    # SimpleGUI in CodeSkulptor2 on Window$
    'old CodeSkulptor2 Chrome 27.0 Window$ 7':
    ({1: 40, 10: 40, 20: 38, 30: 35, 40: 33, 50: 35, 75: 35,
      100: 30, 200: 20, 300: 16, 400: 13, 500: 12, 750: 8,
      1000: 6, 1500: 5, 2000: 4},   # normal
     {1: 35, 10: 35, 20: 36, 30: 38, 40: 34, 50: 34, 75: 30,
      100: 30, 200: 20, 300: 15, 400: 13, 500: 12, 750: 8,
      1000: 6, 1500: 4, 2000: 4}),  # REVERSE
    'old CodeSkulptor2 Firefox 21.0 Window$ 7':
    ({1: 60, 10: 60, 20: 60, 30: 58, 40: 57, 50: 47, 75: 29,
      100: 22, 200: 12, 300: 8, 400: 6, 500: 5, 750: 3,
      1000: 2, 1500: 2, 2000: 1},   # normal
     {1: 60, 10: 60, 20: 59, 30: 58, 40: 48, 50: 41, 75: 30,
      100: 23, 200: 12, 300: 8, 400: 6, 500: 5, 750: 3,
      1000: 3, 1500: 2, 2000: 1}),  # REVERSE
    'old CodeSkulptor2 Safari 5.1.7 Window$ 7':
    ({1: 62, 10: 63, 20: 62, 30: 59, 40: 44, 50: 36, 75: 23,
      100: 19, 200: 12, 300: 8, 400: 7, 500: 6, 750: 5,
      1000: 4, 1500: 3, 2000: 3},   # normal
     {1: 63, 10: 63, 20: 63, 30: 55, 40: 42, 50: 35, 75: 23,
      100: 18, 200: 11, 300: 8, 400: 7, 500: 6, 750: 4,
      1000: 4, 1500: 3, 2000: 3}),  # REVERSE

    # SimpleGUITk by David Holm on Window$, https://pypi.org/project/SimpleGUITk  # noqa
    'old SimpleGUITk 1.1.1 Python 2 Window$ 7':
    ({1: 45, 10: 38, 20: 35, 30: 35, 40: 35, 50: 35, 75: 33,
      100: 31, 200: 24, 300: 20, 400: 17, 500: 15, 750: 11,
      1000: 9, 1500: 6, 2000: 5},   # normal
     {1: 44, 10: 38, 20: 37, 30: 35, 40: 35, 50: 34, 75: 33,
      100: 30, 200: 24, 300: 20, 400: 17, 500: 14, 750: 11,
      1000: 9, 1500: 6, 2000: 5}),  # REVERSE
    'old SimpleGUITk 1.1.1 Python 3 Window$ 7':
    ({1: 45, 10: 39, 20: 37, 30: 37, 40: 36, 50: 36, 75: 33,
      100: 31, 200: 24, 300: 20, 400: 17, 500: 15, 750: 11,
      1000: 9, 1500: 6, 2000: 5},  # normal
     {1: 45, 10: 38, 20: 35, 30: 36, 40: 34, 50: 35, 75: 33,
      100: 31, 200: 24, 300: 20, 400: 17, 500: 15, 750: 11,
      1000: 9, 1500: 6, 2000: 5})  # REVERSE
    }


#
# Main
######
def main():  # pylint: disable=too-many-locals
    # type: () -> None
    """Calculate and print average, and open plot."""
    # Calculate average
    alls_nb_set = set()

    all_results = dict()

    for legend in ALL_RESULTS:
        data_a, data_b = ALL_RESULTS[legend]

        nb_shapes_a = list(data_a.keys())  # pytype: disable=attribute-error
        nb_shapes_a.sort()

        nb_shapes_b = list(data_b.keys())  # pytype: disable=attribute-error
        nb_shapes_b.sort()

        assert nb_shapes_a == nb_shapes_b, (nb_shapes_a, nb_shapes_b)

        results = dict()

        for nb in nb_shapes_b:
            alls_nb_set.add(nb)
            results[nb] = (data_a[nb] + data_b[nb]) / 2.0

        all_results[legend] = results

    # Sort results to display
    alls_nb = list(alls_nb_set)
    alls_nb.sort()

    legends = list(all_results.keys())
    legends.sort()

    datas = []
    datas_with_old = []

    for legend in legends:
        data = all_results[legend]

        nb_shapes = list(data.keys())  # pylint: disable=no-member
        nb_shapes.sort()

        r = []

        for nb in nb_shapes:
            r.append((nb, data[nb]))

        if not legend.startswith('old '):
            datas.append(r)
        datas_with_old.append(r)

    # Display
    print('|'.join(['%4d' % nb for nb in alls_nb]) + '|Environment')

    print('----+' * len(alls_nb) + '-----------')
    for legend in legends:
        data = all_results[legend]
        seq = []
        for nb in alls_nb:
            fps = data.get(nb, None)
            seq.append((('%2d  ' % fps
                         if int(fps) == fps
                         else '%4.1f' % fps)
                        if fps is not None
                        else ' ' * 4))
        print('|'.join(seq) + '|' + legend)

    # Graph
    try:
        simpleplot.plot_lines('Stress Balls results (with old results)',
                              800, 650, '# shapes', 'FPS',
                              datas_with_old, True, legends)
        simpleplot.plot_lines('Stress Balls results',
                              800, 650, '# shapes', 'FPS',
                              datas, True,
                              tuple(legend for legend in legends
                                    if not legend.startswith('old ')))
        if SIMPLEGUICS2PYGAME:
            simpleplot._block()  # pylint: disable=protected-access
    except Exception as e:  # pylint: disable=broad-except
        # To avoid fail if no simpleplot
        print('!simpleplot.plot_lines():' + str(e))


if __name__ == '__main__':
    main()
