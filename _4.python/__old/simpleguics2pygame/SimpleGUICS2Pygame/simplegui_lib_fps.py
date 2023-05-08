# -*- coding: latin-1 -*-

"""
simplegui_lib_fps module.

A class to calculate and display FPS (Frames Per Second)
in SimpleGUI of CodeSkulptor.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2014, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 19, 2020
"""

# print('IMPORT', __name__)


try:
    from typing import Optional, Union
except ImportError:
    pass

try:
    import simplegui  # pytype: disable=import-error  # pylint: disable=unused-import  # noqa
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore  # pylint: disable=unused-import  # noqa


# Class
########
class FPS:  # pylint: disable=too-many-instance-attributes
    """
    Calculate and display FPS (Frames Per Second).

    How to use:

    * Create an instance of FPS: ``fps = FPS()``
    * Start: ``fps.start()``
    * And put the ``draw_fct()``
      in the end of your canvas' draw handler: ``fps.draw_fct(canvas)``
    """

    def __init__(self, x=10, y=10, font_color='Red', font_size=40):
        # type: (Union[int, float], Union[int, float], str, int) -> None
        """
        Set an instance to calculate FPS and drawing on position (x, y).

        :param x: int or float
        :param y: int or float
        :param font_color: str
        :param font_size: int > 0
        """
        assert isinstance(x, (int, float)), type(x)
        assert isinstance(y, (int, float)), type(y)
        assert isinstance(font_color, str), type(font_color)
        assert font_size > 0, font_size

        self._font_color = font_color
        self._font_size = font_size
        self._x = x
        self._y = y

        self._fps = None  # type: Optional[int]
        self._nb_frames_drawed = None  # type: Optional[int]
        self._nb_seconds = None  # type: Optional[int]
        self._timer = None  # type: Optional[simplegui.Timer]

    def draw_fct(self, canvas):  # type: (simplegui.Canvas) -> None
        """
        Update the number of frames drawn
        and draw the FPS.

        This method **must be** called from the canvas' draw handler
        (the function passed as a parameter
        to `simplegui.Frame.set_draw_handler()`).

        :param canvas: simplegui.Canvas
        """
        if self._timer is not None:
            assert isinstance(self._nb_frames_drawed, int)

            self._nb_frames_drawed += 1

            canvas.draw_text(str(self._fps),
                             (self._x, self._y + self._font_size * 3 // 4),
                             self._font_size, self._font_color)

    def is_started(self):  # type: () -> bool
        """
        If FPS is active
        then return True,
        else return False.
        """
        return self._timer is not None

    def start(self):  # type: () -> None
        """
        Start calculation and drawing.

        See `draw_fct()`.
        """
        if self._timer is not None:
            self.stop()

        self._fps = 0
        self._nb_frames_drawed = 0
        self._nb_seconds = 0

        def update():
            """Update counters."""
            if self._timer is not None:
                assert isinstance(self._fps, int)
                assert isinstance(self._nb_frames_drawed, int)
                assert isinstance(self._nb_seconds, int)

                self._nb_seconds += 1
                self._fps = int(round(float(self._nb_frames_drawed) /
                                      self._nb_seconds))

        self._timer = simplegui.create_timer(1000, update)

        self._timer.start()

    def stop(self):  # type: () -> None
        """Stop calculation and drawing."""
        if self._timer is not None:
            self._timer.stop()
            self._timer = None
