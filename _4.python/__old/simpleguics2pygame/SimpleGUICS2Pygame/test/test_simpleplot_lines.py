#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Test simpleplot lines.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2015, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 19, 2020
"""

try:
    from codeskulptor import file2url  # to avoid other simpleplot available in Python  # pytype: disable=import-error  # pylint: disable=unused-import  # noqa
    import simpleplot  # pytype: disable=import-error

    SIMPLEGUICS2PYGAME = False
except ImportError:
    import SimpleGUICS2Pygame.simpleplot as simpleplot  # type: ignore

    SIMPLEGUICS2PYGAME = True


#
# Main
######
def main():  # type: () -> None
    """Open two plots."""
    datalist = [(1, 2), (2, 3), (5, 4), (8, 3), (9, 2)]
    dataset = {1: 3, 2: 4, 5: 5, 8: 4, 9: 3}

    filename = None

    if SIMPLEGUICS2PYGAME:
        from sys import argv  # pylint: disable=import-outside-toplevel

        if len(argv) == 2:
            filename = argv[1]

    simpleplot.plot_lines('Test plot_lines 1', 400, 400, 'x', 'y',
                          (datalist, dataset))

    if filename is None:
        simpleplot.plot_lines('Test plot_lines 2', 400, 400, 'x', 'y',
                              (datalist, dataset),
                              True, ('datalist', 'dataset'))
    else:
        simpleplot.plot_lines('Test plot_lines 2', 400, 400, 'x', 'y',
                              (datalist, dataset),
                              True, ('datalist', 'dataset'),
                              _filename=filename)

    if SIMPLEGUICS2PYGAME and (len(argv) != 2):
        simpleplot._block()  # pylint: disable=protected-access


if __name__ == '__main__':
    main()
