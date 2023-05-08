# -*- coding: latin-1 -*-

"""
simpleguics2pygame module: simpleguics2pygame/timer.

Class Timer.

**Don't require Pygame.**

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2015, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 20, 2020
"""

from __future__ import division
from __future__ import print_function

# print('IMPORT', __name__)


__all__ = ('Timer',
           'create_timer')


import atexit
import threading

try:
    from typing import Any, Callable, Dict, Optional, Union
except ImportError:
    pass

from SimpleGUICS2Pygame.simpleguics2pygame._arguments import _CONFIG  # pylint: disable=no-name-in-module  # noqa


#
# "Private" variable
####################
_STOP_TIMERS = _CONFIG['--stop-timers']
"""
If `True`
then stop all timers when program ending.

If `False`
then timers keep running when program ending.
(This is the default behavior.)
"""


#
# "Private" function
####################
def __timer_exit():  # type: () -> None
    """
    If `_STOP_TIMERS` is True
    then stop all running timers,
    else do nothing.

    Automatically called when program ending.
    """
    if _STOP_TIMERS:
        Timer._stop_all()  # pylint: disable=protected-access


#
# Class
#######
class Timer:
    """
    Timer similar to SimpleGUI `Timer` of CodeSkulptor.

    **Don't require Pygame.**
    """

    _timers_running = dict()  # type: Dict[int, 'Timer']
    """
    `Dict` {(Timer id): `Timer`} of all timers are running.
    """

    @classmethod
    def _running_nb(cls):  # type: () -> int
        """
        Return the number of running timers.

        :return: int >= 0
        """
        return len(cls._timers_running)

    @classmethod
    def _running_some(cls):  # type: () -> bool
        """:return: True if at least one timer running, else False"""
        return bool(cls._timers_running)

    @classmethod
    def _stop_all(cls):  # type: () -> None
        """
        Stop all timers.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        Side effect: Empty `Timer._timers_running`.
        """
        for timer in tuple(cls._timers_running.values()):
            timer.stop()

    def __init__(self, interval, timer_handler):
        # type: (Union[int, float], Callable[[], Any]) -> None
        """
        Set a time.

        **Don't use directly**, use `create_timer()`.

        :param interval: int or float > 0
        :param timer_handler: function () -> *
        """
        assert isinstance(interval, (int, float)), type(interval)
        assert interval > 0, interval
        assert callable(timer_handler), type(timer_handler)

        self._interval = interval

        self._is_running = False
        self._timer = None  # type: Optional[threading.Timer]

        def repeat_handler():
            """Function to create and start a new timer."""
            Timer._timers_running[id(self)] = self
            self._timer = threading.Timer(self._interval / 1000, self._handler)
            self._timer.start()
            timer_handler()

        self._handler = repeat_handler

    def __repr__(self):  # type: () -> str
        """
        Return `'<Timer object>'`.

        :return: str
        """
        return '<Timer object>'

    def get_interval(self):  # type: () -> Union[int, float]
        """
        Return the interval of this timer.

        (Maybe available in SimpleGUI of CodeSkulptor
        but *not in CodeSkulptor documentation*!)

        :return: (int or float) > 0
        """
        return self._interval

    def is_running(self):  # type: () -> bool
        """
        If this timer is running
        then return `True`,
        else return `False`.

        :return: bool
        """
        return self._timer is not None

    def start(self):  # type: () -> None
        """
        Start this timer.

        .. warning::
           With SimpleGUICS2Pygame,
           ``Frame.start()`` is blocking
           until ``Frame.stop()`` execution or closing window.
           So timers must be started *before*,
           and states must be initialized *before*.
           (Or maybe after by a handler function.)

        (Side effect: Add `id(self)`: `self` in `Timer._timers_running`.)
        """
        if self._timer is None:
            Timer._timers_running[id(self)] = self
            self._timer = threading.Timer(self._interval / 1000, self._handler)
            self._timer.start()

    def stop(self):  # type: () -> None
        """
        Stop this timer.

        (Side effect: Remove `id(self)` of `Timer. _timers_running`.)
        """
        if self._timer is not None:
            self._timer.cancel()
            self._timer = None

            del Timer._timers_running[id(self)]


#
# SimpleGUI function
####################
def create_timer(interval, timer_handler):
    # type: (Union[int, float], Callable[[], Any]) -> Timer
    """
    Create and return a timer
    that will execute the function `timer_handler`
    every `interval` milliseconds.

    The first execution of `time_handler`
    will take place after the first period.

    (The timer can be started by `Timer.start()`.)

    :param interval: int or float > 0
    :param timer_handler: function () -> *

    :return: Timer
    """
    assert isinstance(interval, (int, float)), type(interval)
    assert interval > 0, interval
    assert callable(timer_handler), type(timer_handler)

    return Timer(interval, timer_handler)


#
# Main
######
atexit.register(__timer_exit)
