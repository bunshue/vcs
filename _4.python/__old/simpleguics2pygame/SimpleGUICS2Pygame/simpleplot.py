# -*- coding: latin-1 -*-

"""
simpleplot module.

Replace the simpleplot module of CodeSkulptor.

Require matplotlib_
(and must be installed separately).

.. warning::
  With SimpleGUICS2Pygame,
  if your program is terminated,
  then windows opened by
  ``plot_bars()``, ``plot_lines()`` and ``plot_scatter()``
  will be closed automatically.
  You can use the specific function ``_block()``
  to block the program until closing all windows.
  See Tips_ to run specific code.

.. _Tips: Tips.html

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

.. _matplotlib: https://matplotlib.org/

:license: GPLv3 --- Copyright (C) 2013-2016, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 20, 2020
"""

from __future__ import print_function

# print('IMPORT', __name__)


try:
    from typing import Dict, Optional, Sequence, Union
except ImportError:
    pass


try:
    from matplotlib import __version__ as _MATPLOTLIB_VERSION

    import matplotlib.pyplot

    _MATPLOTLIB_AVAILABLE = True
    """
    `True` if matplotlib is available,
    else `False`.
    """
except ImportError:
    _MATPLOTLIB_AVAILABLE = False

    _MATPLOTLIB_VERSION = None
    """
    `matplotlib.__version__` if Pygame is available,
    else `None`.
    """


#
# Private global constant
##########################
_COLORS = ('#edc240', '#afd8f8', '#cb4b4b', '#4da74d',
           '#9440ed', '#bd9b33', '#8cacc6', '#a23c3c',
           '#3d853d', '#7633bd', '#ffe84c', '#d2ffff',
           '#f35a5a', '#5cc85c', '#b14cff', '#8e7426',
           '#698194', '#792d2d', '#2e642e', '#58268e',
           '#ffff59', '#f4ffff', '#ff6969', '#6be96b',
           '#cf59ff', '#5e4d19', '#455663', '#511d1d',
           '#1e421e', '#3b195e', '#ffff66', '#ffffff')
"""
Color used for each graph.

**(Not available in SimpleGUI of CodeSkulptor.)**
"""


#
# Functions
############
def _block():  # type: () -> None
    """
    If some plot windows are open
    then block the program until closing all windows.
    **(Not available in SimpleGUI of CodeSkulptor.)**
    """
    if _MATPLOTLIB_AVAILABLE:
        matplotlib.pyplot.show()


def plot_bars(framename, width, height,  # pylint: disable=too-many-arguments,too-many-locals  # noqa
              xlabel, ylabel, datasets,
              legends=None,
              _block=False, _filename=None):
    # type: (str, int, int, str, str, Union[Sequence, Dict[Union[int, float], Union[int, float]]], Optional[Sequence], bool, Optional[str]) -> None  # noqa
    """
    Open a window titled `framename`
    and plot graphes with `datasets` data
    shown as vertical bars.

    `xlabel` and `ylabel` are labels of x-axis and y-axis.

    `datasets` must be a sequence of data.
    Each data must be:

    * Sequence (not empty) of pair x, y.
      Each point (x, y) is represented by a vertical bar of height y.

    * Or dict (not empty) x: y.
      Each point (x, y) is represented by a vertical bar of height y.

    If `legends` is not None
    then it must be a sequence of legend of each graph.

    If `_block`
    then block the program until closing the window
    else continue and close the window when program stop.
    **(Option not available in SimpleGUI of CodeSkulptor.)**

    If `_filename` is not None
    then save the image to this file.
    **(Option not available in SimpleGUI of CodeSkulptor.)**

    :param framename: str
    :param width: int > 0
    :param height: int > 0
    :param xlabel: str
    :param ylabel: str
    :param datasets: (list or tuple)
                     of (((list or tuple) of ([int or float, int or float]
                     or (int or float, int or float)))
                     or (dict (int or float): (int or float)))
    :param legends: None or ((list or tuple) of same length as datasets)
    :param _block: False
    :param _filename: None or str
    """
    assert isinstance(framename, str), type(framename)

    assert isinstance(width, int), type(width)
    assert width > 0, width

    assert isinstance(height, int), type(height)
    assert height > 0, height

    assert isinstance(xlabel, str), type(xlabel)
    assert isinstance(ylabel, str), type(ylabel)

    assert isinstance(datasets, (list, tuple)), type(datasets)
    if __debug__:
        for dataset in datasets:
            assert isinstance(dataset, (list, tuple, dict)), type(datasets)
            assert dataset
            for x, y in (dataset.items() if isinstance(dataset, dict)
                         else dataset):
                assert isinstance(x, (int, float)), (type(x), x)
                assert isinstance(y, (int, float)), (type(y), y)

    assert ((legends is None) or
            isinstance(legends, (list, tuple))), type(legends)
    assert (legends is None) or (len(legends) == len(datasets)), legends

    assert isinstance(_block, bool), type(_block)
    assert (_filename is None) or isinstance(_filename, str), type(_filename)

    if not _MATPLOTLIB_AVAILABLE:
        from sys import stderr  # pylint: disable=import-outside-toplevel

        print("""Fake 'plot_bars' function
because matplotlib is not available!
See https://simpleguics2pygame.readthedocs.io/en/latest/#installation""",
              file=stderr)

        return

    fig = matplotlib.pyplot.figure()
    fig.set_size_inches(width // fig.get_dpi(), height // fig.get_dpi(),
                        forward=True)

    fig.canvas.set_window_title(framename)
    matplotlib.pyplot.title(framename)

    from os.path import abspath, expanduser, sep  # pylint: disable=import-outside-toplevel  # noqa

    icon_path = __file__.split(sep)[:-1]
    try:
        icon_path.extend(('_img', 'SimpleGUICS2Pygame_32x32.ico'))
        matplotlib.pyplot.get_current_fig_manager().window.wm_iconbitmap(
            sep.join(icon_path))
    except Exception:  # pylint: disable=broad-except
        pass

    matplotlib.pyplot.xlabel(xlabel)
    matplotlib.pyplot.ylabel(ylabel)

    matplotlib.pyplot.grid()

    bar_width = 0.8 / len(datasets)
    for i, dataset in enumerate(datasets):
        bar_lefts, bar_heights = zip(*(sorted(dataset.items())
                                       if isinstance(dataset, dict)
                                       else dataset))
        matplotlib.pyplot.bar([x + bar_width * i for x in bar_lefts],
                              bar_heights,
                              width=bar_width,
                              color=_COLORS[i % len(_COLORS)],
                              edgecolor=_COLORS[i % len(_COLORS)],
                              figure=fig,
                              alpha=0.5)

    ymin, ymax = matplotlib.pyplot.ylim()
    matplotlib.pyplot.ylim(ymin, ymax + 1)

    if legends is not None:
        matplotlib.pyplot.legend(legends, loc='upper right')

    matplotlib.pyplot.show(block=_block)

    if _filename is not None:
        _filename = abspath(expanduser(_filename))
        matplotlib.pyplot.savefig(_filename)


def plot_lines(framename, width, height,  # pylint: disable=too-many-arguments,too-many-locals  # noqa
               xlabel, ylabel, datasets,
               points=False, legends=None,
               _block=False, _filename=None):
    # type: (str, int, int, str, str, Union[Sequence, Dict[Union[int, float], Union[int, float]]], bool, Optional[Sequence], bool, Optional[str]) -> None  # noqa
    """
    Open a window titled `framename`
    and plot graphes with `datasets` data
    shown as connected lines.

    `xlabel` and `ylabel` are labels of x-axis and y-axis.

    `datasets` must be a sequence of data.
    Each data must be:

    * Sequence (not empty) of pair x, y.
      Each point (x, y) is plotted (in given order)
      and connected with line to previous and next points.

    * Or dict (not empty) x: y.
      Each point (x, y) is plotted (in ascending order of x value)
      and connected with line to previous and next points.

    If `points`
    then each point is highlighted by a small disc
    (a small circle in CodeSkulptor).

    If `legends` is not None
    then it must be a sequence of legend of each graph.

    If `_block`
    then block the program until closing the window
    else continue and close the window when program stop.
    **(Option not available in SimpleGUI of CodeSkulptor.)**

    If `_filename` is not None
    then save the image to this file.
    **(Option not available in SimpleGUI of CodeSkulptor.)**

    :param framename: str
    :param width: int > 0
    :param height: int > 0
    :param xlabel: str
    :param ylabel: str
    :param datasets: (list or tuple)
                     of (((list or tuple) of ([int or float, int or float]
                     or (int or float, int or float)))
                     or (dict (int or float): (int or float)))
    :param points: bool
    :param legends: None or ((list or tuple) of same length as datasets)
    :param _block: False
    :param _filename: None or str
    """
    assert isinstance(framename, str), type(framename)

    assert isinstance(width, int), type(width)
    assert width > 0, width

    assert isinstance(height, int), type(height)
    assert height > 0, height

    assert isinstance(xlabel, str), type(xlabel)
    assert isinstance(ylabel, str), type(ylabel)

    assert isinstance(datasets, (list, tuple)), type(datasets)
    if __debug__:
        for dataset in datasets:
            assert isinstance(dataset, (list, tuple, dict)), type(datasets)
            assert dataset
            for x, y in (dataset.items() if isinstance(dataset, dict)
                         else dataset):
                assert isinstance(x, (int, float)), (type(x), x)
                assert isinstance(y, (int, float)), (type(y), y)

    assert isinstance(points, bool), type(points)

    assert ((legends is None)
            or isinstance(legends, (list, tuple))), type(legends)
    assert (legends is None) or (len(legends) == len(datasets)), legends

    assert isinstance(_block, bool), type(_block)
    assert (_filename is None) or isinstance(_filename, str), type(_filename)

    if not _MATPLOTLIB_AVAILABLE:
        from sys import stderr  # pylint: disable=import-outside-toplevel

        print("""Fake 'plot_lines' function
because matplotlib is not available!
See https://simpleguics2pygame.readthedocs.io/en/latest/#installation""",
              file=stderr)

        return

    fig = matplotlib.pyplot.figure()
    fig.set_size_inches(width // fig.get_dpi(), height // fig.get_dpi(),
                        forward=True)

    fig.canvas.set_window_title(framename)
    matplotlib.pyplot.title(framename)

    from os.path import abspath, expanduser, sep  # pylint: disable=import-outside-toplevel  # noqa

    icon_path = __file__.split(sep)[:-1]
    try:
        icon_path.extend(('_img', 'SimpleGUICS2Pygame_32x32.ico'))
        matplotlib.pyplot.get_current_fig_manager().window.wm_iconbitmap(
            sep.join(icon_path))
    except Exception:  # pylint: disable=broad-except
        pass

    matplotlib.pyplot.xlabel(xlabel)
    matplotlib.pyplot.ylabel(ylabel)

    matplotlib.pyplot.grid()

    for i, dataset in enumerate(datasets):
        matplotlib.pyplot.plot(*zip(*(sorted(dataset.items())
                                      if isinstance(dataset, dict)
                                      else dataset)),
                               color=_COLORS[i % len(_COLORS)],
                               figure=fig,
                               marker=('o' if points
                                       else None))

    ymin, ymax = matplotlib.pyplot.ylim()
    matplotlib.pyplot.ylim(ymin - 1, ymax + 1)

    if legends is not None:
        matplotlib.pyplot.legend(legends, loc='upper right')

    matplotlib.pyplot.show(block=_block)

    if _filename is not None:
        _filename = abspath(expanduser(_filename))
        matplotlib.pyplot.savefig(_filename)


def plot_scatter(framename, width, height,  # pylint: disable=too-many-arguments,too-many-locals  # noqa
                 xlabel, ylabel, datasets,
                 legends=None,
                 _block=False, _filename=None):
    # type: (str, int, int, str, str, Union[Sequence, Dict[Union[int, float], Union[int, float]]], Optional[Sequence], bool, Optional[str]) -> None  # noqa
    """
    Open a window titled `framename`
    and plot graphes with `datasets` data
    shown as scattered points.

    `xlabel` and `ylabel` are labels of x-axis and y-axis.

    `datasets` must be a sequence of data.
    Each data must be:

    * Sequence (not empty) of pair x, y.
      Each point (x, y) is represented by a circle.

    * Or dict (not empty) x: y.
      Each point (x, y) is represented by a circle.

    If `legends` is not None
    then it must be a sequence of legend of each graph.

    If `_block`
    then block the program until closing the window
    else continue and close the window when program stop.
    **(Option not available in SimpleGUI of CodeSkulptor.)**

    If `_filename` is not None
    then save the image to this file.
    **(Option not available in SimpleGUI of CodeSkulptor.)**

    :param framename: str
    :param width: int > 0
    :param height: int > 0
    :param xlabel: str
    :param ylabel: str
    :param datasets: (list or tuple)
                     of (((list or tuple) of ([int or float, int or float]
                     or (int or float, int or float)))
                     or (dict (int or float): (int or float)))
    :param legends: None or ((list or tuple) of same length as datasets)
    :param _block: False
    :param _filename: None or str
    """
    assert isinstance(framename, str), type(framename)

    assert isinstance(width, int), type(width)
    assert width > 0, width

    assert isinstance(height, int), type(height)
    assert height > 0, height

    assert isinstance(xlabel, str), type(xlabel)
    assert isinstance(ylabel, str), type(ylabel)

    assert isinstance(datasets, (list, tuple)), type(datasets)
    if __debug__:
        for dataset in datasets:
            assert isinstance(dataset, (list, tuple, dict)), type(datasets)
            assert dataset
            for x, y in (dataset.items() if isinstance(dataset, dict)
                         else dataset):
                assert isinstance(x, (int, float)), (type(x), x)
                assert isinstance(y, (int, float)), (type(y), y)

    assert ((legends is None) or
            isinstance(legends, (list, tuple))), type(legends)
    assert (legends is None) or (len(legends) == len(datasets)), legends

    assert isinstance(_block, bool), type(_block)
    assert (_filename is None) or isinstance(_filename, str), type(_filename)

    if not _MATPLOTLIB_AVAILABLE:
        from sys import stderr  # pylint: disable=import-outside-toplevel

        print("""Fake 'plot_scatter' function
because matplotlib is not available!
See https://simpleguics2pygame.readthedocs.io/en/latest/#installation""",
              file=stderr)

        return

    fig = matplotlib.pyplot.figure()
    fig.set_size_inches(width // fig.get_dpi(), height // fig.get_dpi(),
                        forward=True)

    fig.canvas.set_window_title(framename)
    matplotlib.pyplot.title(framename)

    from os.path import abspath, expanduser, sep  # pylint: disable=import-outside-toplevel  # noqa

    icon_path = __file__.split(sep)[:-1]
    try:
        icon_path.extend(('_img', 'SimpleGUICS2Pygame_32x32.ico'))
        matplotlib.pyplot.get_current_fig_manager().window.wm_iconbitmap(
            sep.join(icon_path))
    except Exception:  # pylint: disable=broad-except
        pass

    matplotlib.pyplot.xlabel(xlabel)
    matplotlib.pyplot.ylabel(ylabel)

    matplotlib.pyplot.grid()

    xmin = float('inf')
    xmax = float('-inf')

    for i, dataset in enumerate(datasets):
        xs, ys = zip(*(sorted(dataset.items())  # pylint: disable=invalid-name
                       if isinstance(dataset, dict)
                       else dataset))
        xmin = min(xmin, min(xs))
        xmax = max(xmax, max(xs))
        matplotlib.pyplot.scatter(xs,
                                  ys,
                                  color=_COLORS[i % len(_COLORS)],
                                  edgecolor=_COLORS[i % len(_COLORS)],
                                  figure=fig)

    matplotlib.pyplot.xlim(xmin, xmax)

    if legends is not None:
        matplotlib.pyplot.legend(legends, loc='upper right')

    matplotlib.pyplot.show(block=_block)

    if _filename is not None:
        _filename = abspath(expanduser(_filename))
        matplotlib.pyplot.savefig(_filename)


# Clean types use by static checking
if 'Sequence' in dir():
    del Dict
    del Optional
    del Sequence
    del Union
