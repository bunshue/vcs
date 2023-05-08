#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
presentation: simple example that displays some information.

Little application that draw
a short presentation of SimpleGUICS2Pygame package.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2016, 2018, 2020-2021 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 4, 2021
"""

try:
    import user305_SXBsmszNiUxIeoV as codeskulptor_lib  # pytype: disable=import-error  # noqa

    import simplegui  # pytype: disable=import-error
except ImportError:
    import SimpleGUICS2Pygame.codeskulptor_lib as codeskulptor_lib  # type: ignore  # noqa

    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui  # type: ignore

    simplegui.Frame._hide_status = True  # pylint: disable=protected-access


#
# Main function
###############
def main():  # pylint: disable=too-many-statements
    # type: () -> None
    """Main function."""
    if codeskulptor_lib.codeskulptor_is():
        def open_new_tab(url):  # type: (str) -> None
            """
            Print ``url``.

            Fake replacement of ``webbrowser.open_new_tab()`` function.
            """
            print(url)

        _VERSION = ''  # pylint: disable=invalid-name
        _WEBSITE = 'https://bitbucket.org/OPiMedia/simpleguics2pygame/'  # pylint: disable=invalid-name  # noqa
        _WEBSITE_DOC = 'https://simpleguics2pygame.readthedocs.io/'  # pylint: disable=invalid-name  # noqa
    else:
        from sys import version  # pylint: disable=import-outside-toplevel
        from webbrowser import open_new_tab  # type: ignore  # pylint: disable=import-outside-toplevel  # noqa

        from SimpleGUICS2Pygame import _VERSION, _WEBSITE, _WEBSITE_DOC  # type: ignore  # pylint: disable=import-outside-toplevel  # noqa

    width = 560
    height = 540

    def draw_about_handler(canvas):
        """
        Draw a short presentation of this package.

        :param canvas: simplegui.Canvas
        """
        size = 40
        canvas.draw_line((0, size / 2),
                         (width - 1, size / 2),
                         size * 1.75, '#f2f2f2')
        canvas.draw_text('SimpleGUICS2Pygame ' + _VERSION,
                         (10, size), size, 'Black')
        canvas.draw_image(logo_opi, (20.5, 17), (41, 34),
                          (30.5, height - 27), (41, 34))
        canvas.draw_image(logo_gpl, (44, 15.5), (88, 31),
                          (width / 2, height - 25.5), (88, 31))
        canvas.draw_image(logo, (32, 32), (64, 64),
                          (width - 42, height - 42), (64, 64))

        size = 20

        for i, line in enumerate(
                ('It is primarily a standard Python (2 and 3) module',
                 'reimplementing the SimpleGUI particular module',
                 'of CodeSkulptor (a Python browser environment).',
                 'This is in fact a package also with other modules',
                 'adapted from CodeSkulptor.',
                 None,
                 None,
                 'Require Pygame for simpleguics2pygame.',
                 'Require audioread for MP3 sounds.',
                 'Require malplotlib for simpleplot.',
                 None,
                 None,
                 None,
                 None,
                 'GPLv3',
                 'Copyright (C) 2013 - 2021 Olivier Pirson',
                 'Olivier Pirson OPi --- http://www.opimedia.be/',
                 'olivier.pirson.opi@gmail.com')):
            if line is not None:
                canvas.draw_text(line, (10, 80 + size * (i + 3 / 4)),
                                 size, 'Black')

    if codeskulptor_lib.codeskulptor_is():
        logo = simplegui.load_image('https://bitbucket.org/OPiMedia/simpleguics2pygame/raw/42359d3aa63aa0b6ea2c663652a60579c7ba80f8/SimpleGUICS2Pygame/_img/SimpleGUICS2Pygame_64x64_t.png')  # noqa
        logo_opi = simplegui.load_image('https://bitbucket.org/OPiMedia/simpleguics2pygame/raw/42359d3aa63aa0b6ea2c663652a60579c7ba80f8/SimpleGUICS2Pygame/_img/OPi_t.png')  # noqa
        logo_gpl = simplegui.load_image('https://bitbucket.org/OPiMedia/simpleguics2pygame/raw/42359d3aa63aa0b6ea2c663652a60579c7ba80f8/SimpleGUICS2Pygame/_img/gplv3-88x31.png')  # noqa
    else:
        from os.path import dirname, join  # pylint: disable=import-outside-toplevel  # noqa
        from sys import argv  # pylint: disable=import-outside-toplevel

        logo = simplegui._load_local_image(  # pylint: disable=protected-access,no-member  # noqa
            join(dirname(argv[0]),
                 '../_img/SimpleGUICS2Pygame_64x64_t.png'))
        logo_opi = simplegui._load_local_image(join(dirname(argv[0]),  # pylint: disable=protected-access,no-member  # noqa
                                                    '../_img/OPi_t.png'))
        logo_gpl = simplegui._load_local_image(join(dirname(argv[0]),  # pylint: disable=protected-access,no-member  # noqa
                                                    '../_img/gplv3-88x31.png'))

    frame = simplegui.create_frame(
        'SimpleGUICS2Pygame: short presentation of this package',
        width, height)
    frame.set_canvas_background('White')

    frame.add_label('Go to websites:')
    frame.add_button('SimpleGUICS2Pygame',
                     lambda: open_new_tab(_WEBSITE), 180)
    frame.add_button('online documentation',
                     lambda: open_new_tab(_WEBSITE_DOC), 180)
    frame.add_button('Olivier Pirson OPi',
                     lambda: open_new_tab('http://www.opimedia.be/'), 180)
    frame.add_button('Donate',
                     lambda: open_new_tab('http://www.opimedia.be/donate'),
                     180)

    frame.add_label('')
    frame.add_button('CodeSkulptor2',
                     lambda: open_new_tab('https://py2.codeskulptor.org/'),
                     180)
    frame.add_button('CodeSkulptor3',
                     lambda: open_new_tab('https://py3.codeskulptor.org/'),
                     180)

    frame.add_label('')
    frame.add_button('Pygame',
                     lambda: open_new_tab('https://www.pygame.org/'), 180)
    frame.add_button('audioread',
                     lambda: open_new_tab(
                         'https://github.com/beetbox/audioread'),
                     180)
    frame.add_button('matplolib',
                     lambda: open_new_tab('https://matplotlib.org/'), 180)

    frame.add_label('')
    frame.add_button('GPL',
                     lambda: open_new_tab(
                         'https://www.gnu.org/licenses/gpl-3.0.html'),
                     180)

    frame.add_label('')
    frame.add_button('Quit', frame.stop)

    frame.add_label('')
    if codeskulptor_lib.codeskulptor_is():
        frame.add_label('CodeSkulptor' +
                        (' 2' if codeskulptor_lib.codeskulptor_version() == 2
                         else '3'))
    else:
        frame.add_label('Pygame ' + simplegui._PYGAME_VERSION)  # pylint: disable=protected-access,no-member  # noqa
        frame.add_label('')
        frame.add_label('Python ' + version)

    frame.set_draw_handler(draw_about_handler)

    frame.start()


#
# Main
######
if __name__ == '__main__':
    main()
