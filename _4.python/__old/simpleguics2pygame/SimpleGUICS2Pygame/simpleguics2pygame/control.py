# -*- coding: latin-1 -*-

"""
simpleguics2pygame module: simpleguics2pygame/control.

Classes Control and TextAreaControl.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2015-2016, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: November 29, 2020
"""

from __future__ import division
from __future__ import print_function

# print('IMPORT', __name__)


__all__ = ('Control', 'TextAreaControl')


try:
    from typing import Any, Callable, Optional, Tuple, Union
except ImportError:
    pass

import pygame

from SimpleGUICS2Pygame.simpleguics2pygame._colors import _SIMPLEGUICOLOR_TO_PYGAMECOLOR  # pylint: disable=no-name-in-module  # noqa
from SimpleGUICS2Pygame.simpleguics2pygame._fonts import _simpleguifontface_to_pygamefont  # pylint: disable=no-name-in-module  # noqa


#
# "Private" function
####################
def _text_to_text_cut(text, width, pygame_font):
    # type: (str, int, pygame.font.Font) -> Tuple[str, ...]
    """
    Cut `text` in pieces smaller `width`.

    **(Not available in SimpleGUI of CodeSkulptor.)**

    :param text: str
    :param width: int >= 0
    :param pygame_font: pygame.font.Font

    :return: tuple of str
    """
    assert isinstance(text, str), type(text)

    assert isinstance(width, int), type(width)
    assert width >= 0, width

    assert isinstance(pygame_font, pygame.font.Font), type(pygame_font)

    text_cut = []

    line = ''
    tested = ''
    for piece in text.split():
        tested = (line + ' ' + piece if line
                  else piece)
        if pygame_font.size(tested)[0] <= width:
            line = tested
        else:
            if line:
                text_cut.append(line)
            line = piece

    if line:
        text_cut.append(line)

    return tuple(text_cut)


#
# Classes
#########
class Control:  # pylint: disable=too-many-instance-attributes
    """Control similar to SimpleGUI `Control` (button and label) of CodeSkulptor."""  # noqa

    _button_background_pygame_color = _SIMPLEGUICOLOR_TO_PYGAMECOLOR['silver']
    """`pygame.Color` of the background in the button."""

    _button_selected_background_pygame_color = pygame.Color('#f0f0f0')   # pylint: disable=invalid-name  # noqa
    """`pygame.Color` of the background in the button when it has pressed."""

    _button_text_pygame_color = _SIMPLEGUICOLOR_TO_PYGAMECOLOR['black']
    """`pygame.Color` of text in the button."""

    _button_pygame_font = _simpleguifontface_to_pygamefont(None, 20)
    """`pygame.font.Font` of text in the button."""

    _button_padding_x = 5
    """Horizontal padding in the button."""

    _button_padding_y = 3
    """Vertical padding in the button."""

    _label_text_pygame_color = _button_text_pygame_color
    """`pygame.Color` of the label."""

    _label_pygame_font = _button_pygame_font
    """`pygame.font.Font` of the label."""

    def __init__(self,
                 frame,
                 text,
                 button_handler=None, width=None):
        # type: (pygame.Frame, str, Optional[Callable[[], Any]], Optional[int]) -> None  # noqa
        r"""
        Set a button (if button_handler is not None)
        or a label (if button_handler is None)
        in the control panel.

        **Don't use directly**,
        use `Frame.add_button()` or `Frame.add_label()`.

        :param frame: Frame
        :param text: str
        :param button_handler: None or (function () -> \*)
        :param width: None or int
        """
        assert isinstance(text, str), type(text)
        assert (button_handler is None) or callable(button_handler), \
            type(button_handler)
        assert (width is None) or isinstance(width, int), type(width)

        self._frame_parent = frame

        # If is None then it's a label, else it's a button
        self._button_handler = button_handler

        self._width = (max(0, int(round(width))) if width is not None
                       else None)

        self._text = text
        self._text_cut = _text_to_text_cut(
            text,
            (self._width if self._width is not None
             else self._frame_parent._control_width),  # pylint: disable=protected-access  # noqa
            (Control._label_pygame_font if button_handler is not None
             else Control._button_pygame_font))

        self._x1 = 0
        self._y1 = (frame._controls[-1]._y2 + 2 if frame._controls  # pylint: disable=protected-access  # noqa
                    else 0)
        self._x2 = 0
        self._y2 = 0

    def __repr__(self):  # type: () -> str
        """
        Return `'<Control object>'`.

        :return: str
        """
        return '<Control object>'

    def _mouse_left_button(self, pressed):  # type: (bool) -> None
        """
        Deal a click of left mouse button on the zone of this `Control`.

        If `pressed`
        then select this Control,
        else unselect and run the button handler (if exist).

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :param pressed: bool
        """
        assert isinstance(pressed, bool), type(pressed)

        self._frame_parent._control_selected = (self if pressed  # pylint: disable=protected-access  # noqa
                                                else None)
        self._frame_parent._draw_controlpanel()  # pylint: disable=protected-access  # noqa
        if (not pressed) and (self._button_handler is not None):
            self._button_handler()

    def _draw(self):  # type: () -> None
        """
        Draw the control object in the control panel.

        **(Not available in SimpleGUI of CodeSkulptor.)**
        """
        if self._button_handler is None:
            self._draw_label()
        else:
            self._draw_button()

    def _draw_button(self):  # type: () -> None
        """
        Draw the the control object as a button.

        **(Not available in SimpleGUI of CodeSkulptor.)**
        """
        # Prepare text
        seq = []

        width_max = 0
        height_total = 0
        for text in self._text_cut:
            pygame_surface_text = Control._button_pygame_font.render(
                text,
                True,
                Control._button_text_pygame_color)

            text_width, text_height = pygame_surface_text.get_size()
            width_max = max(width_max, text_width)
            height_total += text_height

            seq.append((pygame_surface_text, text_width, text_height))

        # Button
        width = (width_max + Control._button_padding_x * 2
                 if self._width is None
                 else max(self._width,
                          width_max + Control._button_padding_x * 2))

        height = height_total + Control._button_padding_y * 2

        pygame_surface_button = pygame.surface.Surface((width, height))  # pylint: disable=too-many-function-args  # noqa
        pygame_surface_button.fill(self._frame_parent._controlpanel_background_pygame_color)  # pylint: disable=protected-access  # noqa

        for i, color in enumerate(
                ((Control._button_selected_background_pygame_color
                  if self._frame_parent._control_selected == self  # pylint: disable=protected-access  # noqa
                  else Control._button_background_pygame_color),
                 Control._button_text_pygame_color)):
            pygame.draw.polygon(pygame_surface_button, color,
                                ((3, 0),
                                 (width - 4, 0),
                                 (width - 1, 3),
                                 (width - 1, height - 4),
                                 (width - 4, height - 1),
                                 (3, height - 1),
                                 (0, height - 4),
                                 (0, 3)),
                                i)  # button with rounded corners

        # Draw text
        y = Control._button_padding_y
        for pygame_surface_text, text_width, text_height in seq:
            pygame_surface_button.blit(pygame_surface_text,
                                       ((width - text_width) // 2,
                                        y))
            y += text_height

        # Draw complete button
        self._frame_parent._controlpanel_pygame_surface.blit(  # pylint: disable=protected-access  # noqa
            pygame_surface_button, (self._x1, self._y1))

        self._x2 = self._x1 + width
        self._y2 = self._y1 + height

    def _draw_label(self):  # type: () -> None
        """
        Draw the the control object as a label.

        **(Not available in SimpleGUI of CodeSkulptor.)**
        """
        if self._text_cut:
            width_max = 0

            self._y2 = self._y1

            for text in self._text_cut:
                pygame_surface_text = Control._label_pygame_font.render(
                    text, True, Control._label_text_pygame_color)

                width, height = pygame_surface_text.get_size()
                width_max = max(width_max, width)

                self._frame_parent._controlpanel_pygame_surface.blit(  # pylint: disable=protected-access  # noqa
                    pygame_surface_text, (self._x1, self._y2))
                self._y2 += height

            self._x2 = self._x1 + width_max
        else:
            self._x2 = self._x1
            self._y2 = self._y1 + Control._label_pygame_font.size('')[1]

    def _pos_in(self, x, y):
        # type: (Union[int, float], Union[int, float]) -> bool
        """
        If position (`x`, `y`) is on the zone of this `aControl`
        then return `True`,
        else return `False`.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :param x: int or float
        :param y: int or float

        :return: bool
        """
        assert isinstance(x, (int, float)), type(x)
        assert isinstance(y, (int, float)), type(y)

        return ((self._x1 <= x <= self._x2) and
                (self._y1 <= y <= self._y2))

    def get_text(self):  # type: () -> str
        """
        Return the text of the button or the label.

        :return: str
        """
        return self._text

    def set_text(self, text):  # type: (str) -> None
        """
        Change the text of the button or the label.

        :param text: str
        """
        assert isinstance(text, str), type(text)

        self._text = text
        self._text_cut = _text_to_text_cut(
            text,
            (self._width if self._width
             else self._frame_parent._control_width),  # pylint: disable=protected-access  # noqa
            (Control._label_pygame_font if self._button_handler is not None
             else Control._button_pygame_font))

        self._frame_parent._draw_controlpanel()  # pylint: disable=protected-access  # noqa


class TextAreaControl:  # pylint: disable=too-many-instance-attributes
    """
    TextAreaControl similar
    to SimpleGUI `TextAreaControl` (input) of CodeSkulptor.
    """

    _input_background_pygame_color = _SIMPLEGUICOLOR_TO_PYGAMECOLOR['white']
    """`pygame.Color` of the background in the input box."""

    _input_mark_pygame_color = _SIMPLEGUICOLOR_TO_PYGAMECOLOR['lime']
    """`pygame.Color` of the end mark of text in the input box."""

    _input_padding_x = 5
    """Horizontal padding in the input box."""

    _input_padding_y = 3
    """Vertical padding in the input box."""

    _input_pygame_color = _SIMPLEGUICOLOR_TO_PYGAMECOLOR['black']
    """`pygame.Color` of the text in the input box."""

    _input_pygame_font = Control._label_pygame_font  # pylint: disable=protected-access  # noqa
    """`pygame.font.Font` of the text in the input box."""

    _input_selected_background_pygame_color = \
        _SIMPLEGUICOLOR_TO_PYGAMECOLOR['white']  # pylint: disable=invalid-name
    """`pygame.Color` of the background in the input box when it has focus."""

    _label_text_pygame_color = Control._label_text_pygame_color  # pylint: disable=protected-access  # noqa
    """`pygame.Color` of the label of the input box."""

    _label_pygame_font = _input_pygame_font
    """`pygame.font.Font` of the label of the input box."""

    def __init__(self,
                 frame,
                 label_text,
                 input_handler, input_width):
        # type: (pygame.Frame, str, Optional[Callable[[str], Any]], Union[int, float]) -> None  # noqa
        """
        Set a input box in the control panel.

        **Don't use directly**, use `Frame.add_input()`.

        :param frame: Frame
        :param label_text: str
        :param input_handler: function (str) -> *
        :param input_width: int or float
        """
        assert isinstance(label_text, str), type(label_text)
        assert callable(input_handler), type(input_handler)
        assert isinstance(input_width, (int, float)), type(input_width)

        self._frame_parent = frame

        self._input_handler = input_handler
        self._width = (int(round(input_width)) if input_width >= 0
                       else frame._control_width)  # pylint: disable=protected-access  # noqa

        self._label_text = label_text
        self._label_text_cut = _text_to_text_cut(
            label_text, frame._control_width,  # pylint: disable=protected-access  # noqa
            TextAreaControl._input_pygame_font)

        self._x1 = 0
        self._y1 = (frame._controls[-1]._y2 + 2 if frame._controls  # pylint: disable=protected-access  # noqa
                    else 0)
        self._x2 = 0
        self._y2 = 0

        self._input_pos = 0
        self._input_text = ''

    def __repr__(self):  # type: () -> str
        """
        Return `'<TextAreaControl object>'`.

        :return: str
        """
        return '<TextAreaControl object>'

    def _draw(self):  # pylint: disable=too-many-locals
        # type: () -> None
        """
        Draw the input box and his label.

        **(Not available in SimpleGUI of CodeSkulptor.)**
        """
        # Display the label
        label_width = 0

        self._y2 = self._y1

        for text in self._label_text_cut:
            pygame_surface_text = TextAreaControl._label_pygame_font.render(
                text, True, TextAreaControl._label_text_pygame_color)

            width, height = pygame_surface_text.get_size()
            label_width = max(label_width, width)

            self._frame_parent._controlpanel_pygame_surface.blit(  # pylint: disable=protected-access  # noqa
                pygame_surface_text, (self._x1, self._y2))
            self._y2 += height

        # Display the input text in the input box
        selected = (self._frame_parent._control_selected == self)  # pylint: disable=protected-access  # noqa

        pygame_surface_text = TextAreaControl._input_pygame_font.render(
            self._input_text, True, TextAreaControl._input_pygame_color)

        text_width, text_height = pygame_surface_text.get_size()

        if self._input_pos < len(self._input_text):
            pygame_surface_text_before_cursor = TextAreaControl._input_pygame_font.render(  # pylint: disable=invalid-name  # noqa
                self._input_text[:self._input_pos], True,
                TextAreaControl._input_pygame_color)

            text_before_cursor_width, _ = \
                pygame_surface_text_before_cursor.get_size()
        else:
            text_before_cursor_width = text_width

        rect_y = self._y2 + 2
        rect_height = text_height + 2 + TextAreaControl._input_padding_y * 2

        pygame.draw.rect(
            self._frame_parent._controlpanel_pygame_surface,  # pylint: disable=protected-access  # noqa
            (TextAreaControl._input_selected_background_pygame_color
             if selected
             else TextAreaControl._input_background_pygame_color),
            (self._x1, rect_y,
             self._width, rect_height),
            0)

        pygame.draw.rect(self._frame_parent._controlpanel_pygame_surface,  # pylint: disable=protected-access  # noqa
                         TextAreaControl._input_pygame_color,
                         (self._x1, rect_y,
                          self._width, rect_height),
                         1)

        text_x = self._x1 + 1 + TextAreaControl._input_padding_x
        text_y = rect_y + 1 + TextAreaControl._input_padding_y

        max_text_width = self._width - 2 - TextAreaControl._input_padding_x * 2
        offset_text_x = max(0, text_width - max_text_width)
        text_width = min(text_width, max_text_width)

        cursor_x = text_x - offset_text_x + text_before_cursor_width
        if (text_width >= max_text_width) and (text_x + 10 > cursor_x):
            diff = text_x + (10
                             if self._input_pos > 0
                             else 0) - cursor_x
            offset_text_x -= diff
            text_width += diff
            cursor_x += diff

        if selected:
            # Draw cursor
            pygame.draw.line(self._frame_parent._controlpanel_pygame_surface,  # pylint: disable=protected-access  # noqa
                             self._input_mark_pygame_color,
                             (cursor_x, text_y - 1),
                             (cursor_x, text_y + text_height + 1), 1)

        # Draw text
        self._frame_parent._controlpanel_pygame_surface.blit(  # pylint: disable=protected-access  # noqa
            pygame_surface_text,
            (text_x, text_y),
            (offset_text_x, 0, text_width, text_height))

        # Set bottom-right position
        self._x2 = self._x1 + max(label_width, self._width)
        self._y2 += rect_height

    def _key(self, pygame_event):  # pylint: disable=too-many-branches,too-many-statements,too-many-return-statements  # noqa
        # type: (pygame.event.Event) -> None
        """
        Deal key pressed
        when this `TextAreaControl` have focus.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :param pygame_event: pygame.Event KEYDOWN or KEYUP
        """
        assert 0 <= self._input_pos <= len(self._input_text), \
            (self._input_pos, len(self._input_text), self._input_text)

        if pygame_event.key == pygame.K_END:             # End  # pylint: disable=no-member,no-else-return  # noqa
            # Set position to end
            if self._input_pos < len(self._input_text):
                self._input_pos = len(self._input_text)
                self._frame_parent._draw_controlpanel()  # pylint: disable=protected-access  # noqa

            return
        elif pygame_event.key == pygame.K_ESCAPE:        # Escape  # pylint: disable=no-member  # noqa
            # Erase all
            if self._input_pos != '':
                self._input_pos = 0
                self._input_text = ''
                self._frame_parent._draw_controlpanel()  # pylint: disable=protected-access  # noqa

            return
        elif pygame_event.key == pygame.K_HOME:          # Home  # pylint: disable=no-member  # noqa
            # Set position to begining
            if self._input_pos > 0:
                self._input_pos = 0
                self._frame_parent._draw_controlpanel()  # pylint: disable=protected-access  # noqa

            return
        elif pygame_event.key == pygame.K_LEFT:          # Left  # pylint: disable=no-member  # noqa
            # Move backward position
            if self._input_pos > 0:
                self._input_pos = (
                    self._input_text[:self._input_pos].rstrip().rfind(' ') + 1
                    if pygame_event.mod & pygame.KMOD_CTRL  # pylint: disable=no-member  # noqa
                    else self._input_pos - 1)
                self._frame_parent._draw_controlpanel()  # pylint: disable=protected-access  # noqa

            return
        elif ((pygame_event.key == pygame.K_RETURN) or  # pylint: disable=no-member  # noqa
              (pygame_event.key == pygame.K_KP_ENTER)):  # Return  # pylint: disable=no-member  # noqa
            # Valid text and run handler
            self._frame_parent._control_selected = None  # pylint: disable=protected-access  # noqa
            self._frame_parent._draw_controlpanel()  # pylint: disable=protected-access  # noqa
            self._input_handler(self._input_text)

            return
        elif pygame_event.key == pygame.K_RIGHT:         # Right  # pylint: disable=no-member  # noqa
            # Move forward position
            if self._input_pos < len(self._input_text):
                if pygame_event.mod & pygame.KMOD_CTRL:  # pylint: disable=no-member  # noqa
                    i = self._input_pos
                    while ((i < len(self._input_text)) and
                           (self._input_text[i] == ' ')):
                        i += 1
                    i = self._input_text.find(' ', i)
                    self._input_pos = (i
                                       if i >= 0
                                       else len(self._input_text))
                else:
                    self._input_pos += 1
                self._frame_parent._draw_controlpanel()  # pylint: disable=protected-access  # noqa

            return
        elif pygame_event.key == pygame.K_TAB:           # Tab  # pylint: disable=no-member  # noqa
            # Give focus to the next input box (if exist)
            i = 0
            while self._frame_parent._controls[i] != self:  # pylint: disable=protected-access  # noqa
                i += 1
            i += 1
            while ((i < len(self._frame_parent._controls)) and  # pylint: disable=protected-access  # noqa
                   not isinstance(self._frame_parent._controls[i],  # pylint: disable=protected-access  # noqa
                                  TextAreaControl)):
                i += 1

            self._frame_parent._control_selected = (  # pylint: disable=protected-access  # noqa
                self._frame_parent._controls[i]  # pylint: disable=protected-access  # noqa
                if i < len(self._frame_parent._controls)  # pylint: disable=protected-access  # noqa
                else None)
            self._frame_parent._draw_controlpanel()  # pylint: disable=protected-access  # noqa

            return

        old = self._input_text

        if pygame_event.key == pygame.K_BACKSPACE:  # Backspace  # pylint: disable=no-member  # noqa
            # Delete previous character(s)
            new_pos = (
                self._input_text[:self._input_pos].rstrip().rfind(' ') + 1
                if pygame_event.mod & pygame.KMOD_CTRL  # pylint: disable=no-member  # noqa
                else self._input_pos - 1)
            self._input_text = (self._input_text[:new_pos] +
                                self._input_text[self._input_pos:])
            self._input_pos = new_pos
        elif pygame_event.key == pygame.K_DELETE:   # Delete  # pylint: disable=no-member  # noqa
            # Delete next character(s)
            if pygame_event.mod & pygame.KMOD_CTRL:  # pylint: disable=no-member  # noqa
                i = self._input_pos
                while ((i < len(self._input_text)) and
                       (self._input_text[i] == ' ')):
                    i += 1
                i = self._input_text.find(' ', i)
                self._input_text = (self._input_text[:self._input_pos] +
                                    (self._input_text[i:] if i >= 0
                                     else ''))
            else:
                self._input_text = (self._input_text[:self._input_pos] +
                                    self._input_text[self._input_pos + 1:])
        elif len(pygame_event.unicode) == 1:        # Other key
            # Add character
            self._input_text = (self._input_text[:self._input_pos] +
                                pygame_event.unicode +
                                self._input_text[self._input_pos:])
            self._input_pos += 1

        if self._input_text != old:
            # Text was modified
            try:
                # In Python 2, maybe self._input_text is unicode,
                # try to convert to str
                self._input_text = str(self._input_text)
                self._input_pos = min(self._input_pos, len(self._input_text))
            except Exception:  # pylint: disable=broad-except
                pass

            self._frame_parent._draw_controlpanel()  # pylint: disable=protected-access  # noqa

    def _mouse_left_button(self, pressed):  # type: (bool) -> None
        """
        Deal a click of left mouse button
        on the zone of this `TextAreaControl`.

        If `pressed`
        then give it the focus.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :param pressed: bool
        """
        assert isinstance(pressed, bool), type(pressed)

        if pressed:
            self._frame_parent._control_selected = self  # pylint: disable=protected-access  # noqa
            self._frame_parent._draw_controlpanel()  # pylint: disable=protected-access  # noqa

    def _pos_in(self, x, y):
        # type: (Union[int, float], Union[int, float]) -> bool
        """
        If position (`x`, `y`) is on the zone of this `TextAreaControl`
        then return `True`,
        else return `False`.

        **(Not available in SimpleGUI of CodeSkulptor.)**

        :param x: int or float
        :param y: int or float

        :return: bool
        """
        assert isinstance(x, (int, float)), type(x)
        assert isinstance(y, (int, float)), type(y)

        return ((self._x1 <= x <= self._x2) and
                (self._y1 <= y <= self._y2))

    def get_text(self):  # type: () -> str
        """
        Return the text of the input box.

        :return: str (or unicode in Python 2)
        """
        return self._input_text

    def set_text(self, input_text):  # type: (str) -> None
        """
        Change the text in the input box.

        :param input_text: str
        """
        assert isinstance(input_text, str), type(input_text)

        self._input_text = input_text

        self._frame_parent._draw_controlpanel()  # pylint: disable=protected-access  # noqa
