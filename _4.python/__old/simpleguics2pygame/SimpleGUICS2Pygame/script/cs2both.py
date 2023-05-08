#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
script/cs2both.py script.

Script that change a CodeSkulptor program
to run in CodeSkulptor *and* Python SimpleGUICS2Pygame.

A file codeskulptor_program.py is copied
to codeskulptor_program.py.bak before changing.

Changes made :
- Add shebang '#!/usr/bin/env python'.
- Add '# -*- coding: latin-1 -*-'.
- Replace import simplegui
  by
  try:
      import simplegui
  except ImportError:
      import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
- *Try* to check if a timer is started *after* the start frame.

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

:license: GPLv3 --- Copyright (C) 2013-2014, 2020 Olivier Pirson
:author: Olivier Pirson --- http://www.opimedia.be/
:version: May 20, 2020
"""

from __future__ import print_function


import os
import os.path
import re
import sys


def main():  # pylint: disable=too-many-branches,too-many-statements
    # type: () -> None
    """Main function."""
    if (len(sys.argv) != 2) or (sys.argv[1][0] == '-'):
        help_and_exit()

    filename = os.path.abspath(os.path.expanduser(sys.argv[1]))

    if filename[-3:] != '.py':
        print("! '{}' have not '.py' extension.".format(filename))

        exit(1)  # pylint: disable=consider-using-sys-exit

    if not os.path.isfile(filename):
        print("! '{}' doesn't exist.".format(filename))

        exit(1)  # pylint: disable=consider-using-sys-exit

    if os.path.isfile(filename + '.bak'):
        print("! '{}.bak' alread exist.".format(filename))

        exit(1)  # pylint: disable=consider-using-sys-exit

    # Read
    with open(filename) as infile:
        lines = [line.rstrip() for line in infile]

    # Check
    if len(lines) < 2:
        print('"Empty" file.')

        exit()  # pylint: disable=consider-using-sys-exit

    add_shebang = lines[0][:2]
    add_coding = (not re.match(r'#\w*-\*- coding: \W+ -\*-$', lines[0]) and
                  not re.match(r'#\w*-\*- coding: \W+ -\*-$', lines[1]))

    change_import = False
    already_change_import = False

    end_blank_line = False

    while lines[-1] == '':
        end_blank_line = True
        lines.pop()

    if len(lines) < 2:
        print('"Empty" file.')

        exit()  # pylint: disable=consider-using-sys-exit

    for line in lines:
        if (not already_change_import and
                re.search(r'^\w*import SimpleGUICS2Pygame', line)):
            already_change_import = True

    if not already_change_import:
        for i, line in enumerate(lines):
            match = re.match(r'(\w)*import simplegui$', line)
            if match:
                change_import = True
                indent = (match.group(1) if match.group(1)
                          else '')
                lines[i] = '\n' + indent + ('\n' + indent).join(
                    ("# Automatically modified by 'cs2both.py'",
                     '# to run in CodeSkulptor *and* standard Python with SimpleGUICS2Pygame:',  # noqa
                     '# https://bitbucket.org/OPiMedia/simpleguics2pygame',
                     'try:',
                     '    import simplegui',
                     'except ImportError:',
                     '    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui')) + '\n'  # noqa

    # Write
    if add_shebang or add_coding or change_import or end_blank_line:
        os.rename(filename, filename + '.bak')
        print("File copied to {}.bak'".format(filename))

        with (open(filename, mode='w', encoding='latin_1', newline='\n')
              if sys.version_info[0] >= 3
              else open(filename, mode='w')) as outfile:
            if add_shebang:
                print('Add shebang.')
                print('#!/usr/bin/env python', file=outfile)

            if add_coding:
                print('Add coding latin-1.')
                print('# -*- coding: latin-1 -*-', file=outfile)

            if change_import:
                print('Change import simplegui.')

            if end_blank_line:
                print('End blank line deleted.')

            print('\n'.join(lines), file=outfile)
    else:
        print('Nothing changed.')

    while lines:
        line = lines.pop()
        if re.search(r'^\w*f(rame)?\.start\(\)', line):  # f.start() or frame.start()  # pylint: disable=no-else-break  # noqa
            break
        elif re.search(r'^\w*[^#]+\.start\(\)', line):   # other .start()
            print('Warning: Maybe a timer is started *after* the start frame.')

            break


def help_and_exit():  # type: () -> None
    """
    Print help message on error output
    and exit.
    """
    print("""cs2both.py codeskulptor_program.py

Make automatically little changes in codeskulptor_program.py
to run in CodeSkulptor *and* Python SimpleGUICS2Pygame.

The file codeskulptor_program.py is copied
to codeskulptor_program.py.bak before changing.

Changes made :
- Add shebang '#!/usr/bin/env python'.
- Add '# -*- coding: latin-1 -*-'.
- Replace import simplegui
  by
  try:
      import simplegui
  except ImportError:
      import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
- *Try* to check if a timer is started *after* the start frame.
""", file=sys.stderr)

    exit(1)  # pylint: disable=consider-using-sys-exit


########
# Main #
########
if __name__ == '__main__':
    main()
