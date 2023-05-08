# -*- coding: latin-1 -*-

"""
simplegui_lib_keys module.

A class to help manage keyboard handling
in SimpleGUI of CodeSkulptor.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2014, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 19, 2020
"""

# print('IMPORT', __name__)


try:
    from typing import Any, Callable, Dict, List, Optional
except ImportError:
    pass

try:
    import simplegui  # pytype: disable=import-error
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore


# Class
########
class Keys:
    """
    Keys handler.

    Set and catch keys handlers of SimpleGUICS2Pygame (and CodeSkulptor)
    to help.

    General note:
    Some keyboards can't handle more
    than two or three keys pressed simultaneously.
    See `Keyboard Ghosting Explained!`_
    and `Keyboard Ghosting Demonstration`_.

    .. _`Keyboard Ghosting Explained!`: http://www.microsoft.com/appliedsciences/antighostingexplained.mspx
    .. _`Keyboard Ghosting Demonstration`: http://www.microsoft.com/appliedsciences/content/projects/KeyboardGhostingDemo.aspx
    """  # noqa

    def __init__(self, frame, keys=None):
        # type: (simplegui.Frame, Optional[simplegui.Keys]) -> None
        """
        If keys is None
        then set an empty keys handler,
        else set a keys handler with key up and key down functions of keys.

        `active_handlers()`,
        `active_keydown_handler()` or `active_keyup_handler()`
        must be called to activate.

        :param frame: simplegui.Frame
        :param keys: None or Keys
        """
        assert isinstance(frame, simplegui.Frame), type(frame)
        assert (keys is None) or isinstance(keys, Keys), type(keys)

        self._frame = frame
        self._pressed_keys = dict()  # type: Dict[int, bool]

        if keys is None:
            self._keydown_fct = dict()  # type: Dict[int, Optional[Callable[[int], Any]]]  # noqa
            self._keyup_fct = dict()  # type: Dict[int, Optional[Callable[[int], Any]]]  # noqa
        else:
            self._keydown_fct = dict(keys._keydown_fct)
            self._keyup_fct = dict(keys._keyup_fct)

    def active_handlers(self):  # type: () -> None
        """Active key down and key up handlers."""
        self.active_keydown_handler()
        self.active_keyup_handler()

    def active_keydown_handler(self):  # type: () -> None
        """Active the key down handler."""
        def keydown(key_code):
            """Function handler dealt by frame."""
            self._pressed_keys[key_code] = True

            fct = self._keydown_fct.get(key_code)
            if fct is not None:
                fct(key_code)

        self._frame.set_keydown_handler(keydown)

    def active_keyup_handler(self):  # type: () -> None
        """Active the key up handler."""
        def keyup(key_code):
            """Function handler dealt by frame."""
            if key_code in self._pressed_keys:
                del self._pressed_keys[key_code]

            fct = self._keyup_fct.get(key_code)
            if fct is not None:
                fct(key_code)

        self._frame.set_keyup_handler(keyup)

    def is_pressed(self, key_code):  # type: (int) -> bool
        """
        If the key is pressed
        then return True,
        else return False.

        :param key_code: int >= 0

        :return: bool
        """
        assert isinstance(key_code, int), type(key_code)
        assert key_code >= 0, key_code

        return self._pressed_keys.get(key_code, False)

    def is_pressed_key_map(self, key_str):  # type: (str) -> bool
        """
        If the key is pressed
        then return True,
        else return False.

        :param key_str: str in `simplegui.KEY_MAP`

        :return: bool
        """
        assert isinstance(key_str, str), type(key_str)
        assert key_str in simplegui.KEY_MAP, key_str

        return self._pressed_keys.get(simplegui.KEY_MAP[key_str], False)

    def pressed_keys(self):  # type: () -> List[int]
        """
        Return a sorted list with code of all pressed keys.

        :return: list of (int >= 0)
        """
        return list(self._pressed_keys.keys())

    def set_keydown_fct(self, key_code, fct=None):
        # type: (int, Optional[Callable[[int], Any]]) -> None
        """
        If fct is None
        then erase the function key down handler to the specified key,
        else set the function key down handler to the specified key.

        :param key_code: int >= 0
        :param fct: (int) -> *
        """
        assert isinstance(key_code, int), type(key_code)
        assert key_code >= 0, key_code

        if fct is None:
            if key_code in self._keydown_fct:
                del self._keydown_fct[key_code]
        else:
            self._keydown_fct[key_code] = fct

    def set_keydown_fct_key_map(self, key_str, fct=None):
        # type: (str, Optional[Callable[[int], Any]]) -> None
        """
        If fct is None
        then erase the function key down handler to the specified key,
        else set the function key down handler to the specified key.

        :param key_str: str in `simplegui.KEY_MAP`
        :param fct: (int) -> *
        """
        assert isinstance(key_str, str), type(key_str)
        assert key_str in simplegui.KEY_MAP, key_str

        self.set_keydown_fct(simplegui.KEY_MAP[key_str], fct=fct)

    def set_keyup_fct(self, key_code, fct=None):
        # type: (int, Optional[Callable[[int], Any]]) -> None
        """
        If fct is None
        then erase the function key up handler to the specified key,
        else set the function key up handler to the specified key.

        :param key_code: int >= 0
        :param fct: (int) -> *
        """
        assert isinstance(key_code, int), type(key_code)
        assert key_code >= 0, key_code

        if fct is None:
            if key_code in self._keyup_fct:
                del self._keyup_fct[key_code]
        else:
            self._keyup_fct[key_code] = fct

    def set_keyup_fct_key_map(self, key_str, fct=None):
        # type: (str, Optional[Callable[[int], Any]]) -> None
        """
        If fct is None
        then erase the function key up handler to the specified key,
        else set the function key up handler to the specified key.

        :param key_str: str in `simplegui.KEY_MAP`

        :param key_code: int >= 0
        :param fct: (int) -> *
        """
        assert isinstance(key_str, str), type(key_str)
        assert key_str in simplegui.KEY_MAP, key_str

        self.set_keyup_fct(simplegui.KEY_MAP[key_str], fct=fct)
