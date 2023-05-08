# -*- coding: latin-1 -*-

"""
simpleguics2pygame module: simpleguics2pygame/_arguments.

Read command line arguments.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2015-2016, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 19, 2020
"""

from __future__ import print_function

# print('IMPORT', __name__)


__all__ = tuple()  # type: tuple


import sys  # noqa


#
# "Private" variable
####################
_CONFIG = {'--default-font': False,
           '--display-fps': False,
           '--fps': 60,
           '--frame-padding': 2,
           '--fullscreen': False,
           '--keep-timers': False,
           '--no-border': False,
           '--no-controlpanel': False,
           '--no-load-sound': False,
           '--no-status': False,
           '--overwrite-downloaded-medias': False,
           '--print-load-medias': False,
           '--print-stats-cache': False,
           '--save-downloaded-medias': False,
           '--stop-timers': False}


#
# "Private" functions
#####################
def __help_quit(code=0):  # type: (int) -> None
    """
    Print help message in error output and quit.

    :param code: 0 <= int <= 255
    """
    assert isinstance(code, int), type(code)
    assert 0 <= code <= 255, code

    print("""Usage: python YOURPROGRAM.py [SimpleGUICS2Pygame arguments] [application arguments]

  --default-font        Use Pygame default font instead serif, monospace...
                          (this is faster if you display a lot of text).
  --display-fps         Display FPS average on the canvas.
  --fps N               Set Frame Per Second (default: 60 FPS).
  --frame-padding N     Set the padding in pixels found around the canvas
                          (default: 2).
  --fullscreen          Fullscreen mode.
  --help                Print help message and quit.
  --keep-timers         Keep running timers when close frame without asking
                          (default: ask before close). See also --stop-timers.
  --last                Mark this argument as the last SimpleGUICS2Pygame's
                          argument. (Do nothing else.)
  --no-border           Window without border.
  --no-controlpanel     Hide the control panel (and status boxes).
  --no-load-sound       Don't load any sound.
  --no-status           Hide two status boxes.
  --overwrite-downloaded-medias
                        Download all images and sounds from Web
                        and save in local directory even if they already exist.
  --print-application-args
                        Print remaining arguments transmit to application.
  --print-args          Print final configuration
                        from SimpleGUICS2Pygame's argument.
  --print-load-medias   Print URLs or local filenames loaded.
  --print-stats-cache   After frame stopped, print some statistics of caches.
  --save-downloaded-medias
                        Save images and sounds downloaded
                        from Web that don't already exist in local directory.
  --stop-timers         Stop all timers when ending program (default: running
                          timers continue, as in CodeSkulptor).
                          See also --keep-timers.
  --version             Print help message and quit.

If an argument is not in this list then it is ignored
 and all next arguments are ignored by SimpleGUICS2Pygame.

Arguments used by SimpleGUICS2Pygame is deleted to sys.argv.
Remaining arguments can used by your application.

SimpleGUICS2Pygame arguments are automatically read
when the module simpleguics2pygame is imported.

Examples:
  $ python YOURPROGRAM.py --no-controlpanel --stop-timers --foo --fullscreen
  Run YOURPROGRAM.py with the control panel hidden and timers will stoped.
  But SimpleGUICS2Pygame ignore --foo and --fullscreen.
  YOURPROGRAM.py application receive --foo --fullscreen arguments.

  $ python YOURPROGRAM.py --no-controlpanel --last --stop-timers --foo --fps 30
  Run YOURPROGRAM.py with the control panel hidden.
  But SimpleGUICS2Pygame ignore --stop-timers, --foo, --fps and 30.
  YOURPROGRAM.py application receive --stop-timers --foo --fps 30 arguments.""",  # noqa
          file=sys.stderr)

    exit(code)  # pylint: disable=consider-using-sys-exit


def __read_arguments():  # pylint: disable=too-many-branches,too-many-statements  # noqa
    # type: () -> None
    """
    Read arguments in sys.argv
    and set __CONFIG.

    See  `Tips.html#command-line-arguments`_
    for the list of arguments and usage examples.

    If an argument is not in this list
    then it is ignored and all next arguments are ignored.

    Arguments used by SimpleGUICS2Pygame is deleted to ``sys.argv``.

    This function is executed when the module is imported.

    .. _`Tips.html#command-line-arguments`: ../Tips.html#command-line-arguments

    **(Not available in SimpleGUI of CodeSkulptor.)**
    """
    def get_next_natural(option):  # pylint: disable=inconsistent-return-statements  # noqa
        """
        If one non negative integer argument is available
        then return it,
        else print error message and call __help_quit()

        :param option: str

        :return: int >= 0
        """
        assert isinstance(option, str), type(option)

        if len(sys.argv) >= 2:
            arg = sys.argv.pop(1)
            try:
                n = int(arg)
            except ValueError:
                print('Argument "{}" for option {} must be integer!'
                      .format(arg, option),
                      file=sys.stderr)
                __help_quit(2)

            if n >= 0:  # pylint: disable=no-else-return,inconsistent-return-statements  # noqa
                return n
            else:
                print('Argument "{}" for option {} must be >= 0!'
                      .format(arg, option),
                      file=sys.stderr)
                __help_quit(3)
        else:
            print('Missing argument for option {}!'.format(option),
                  file=sys.stderr)
            __help_quit(1)

    print_application_args = False
    print_args = False

    while len(sys.argv) >= 2:
        arg = sys.argv[1]
        if arg in ('--default-font',
                   '--display-fps',
                   '--fullscreen',
                   '--keep-timers',
                   '--no-border',
                   '--no-controlpanel',
                   '--no-load-sound',
                   '--no-status',
                   '--overwrite-downloaded-medias',
                   '--print-load-medias',
                   '--print-stats-cache',
                   '--save-downloaded-medias',
                   '--stop-timers'):
            sys.argv.pop(1)
            _CONFIG[arg] = True
        elif arg == '--fps':
            sys.argv.pop(1)
            _CONFIG[arg] = get_next_natural(arg)
        elif arg == '--frame-padding':
            sys.argv.pop(1)
            _CONFIG[arg] = get_next_natural(arg)
        elif arg == '--help':
            __help_quit()
        elif arg == '--print-application-args':
            sys.argv.pop(1)
            print_application_args = True
        elif arg == '--print-args':
            sys.argv.pop(1)
            print_args = True
        elif arg == '--version':
            from SimpleGUICS2Pygame import _VERSION  # pylint: disable=import-outside-toplevel  # noqa

            print('SimpleGUICS2Pygame {}'.format(_VERSION))

            exit()  # pylint: disable=consider-using-sys-exit
        else:  # --last or first argument not recognized by SimpleGUICS2Pygame
            if arg == '--last':
                sys.argv.pop(1)

            break

    if print_args:
        for option, value in _CONFIG.items():
            if value is True:
                print('SimpleGUICS2Pygame argument {}'.format(option))
            elif (value is not False) and (value is not None):
                print('SimpleGUICS2Pygame argument {} {}'
                      .format(option, value))
    if print_application_args:
        print('Application_arguments sys.argv={}'.format(sys.argv))


#
# Read arguments
################
__read_arguments()
