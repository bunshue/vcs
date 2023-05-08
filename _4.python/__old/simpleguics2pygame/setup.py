#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
Setup of SimpleGUICS2Pygame package (May 19, 2020).

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2016, 2018, 2020 Olivier Pirson
http://www.opimedia.be/
"""

from __future__ import print_function


import io

import setuptools

try:
    from typing import List
except ImportError:
    pass

from SimpleGUICS2Pygame import _VERSION, _WEBSITE, _WEBSITE_DOC


def parse_requirements_file():  # type: () -> List[str]
    """
    Parse file "requirements.txt" and return the requirements list.

    :return: list of str
    """
    with open('requirements.txt') as fin:
        requirements = fin.readlines()

    return list(requirement.strip() for requirement in requirements)


REQUIREMENTS = parse_requirements_file()


print("""Warning!
If the installation failed, please see the online documentation
to upgrade installation system and to install requirements separately.
https://simpleguics2pygame.readthedocs.io/en/latest/#installation
Requirements:""")
for REQUIREMENT in REQUIREMENTS:
    print(' ', REQUIREMENT.replace('==', ' '))
print()


# https://packaging.python.org/guides/distributing-packages-using-setuptools/#setup-args
setuptools.setup(
    name='SimpleGUICS2Pygame',
    version=_VERSION,

    description='Primarily a standard Python (2 and 3) module reimplementing the SimpleGUI particular module of CodeSkulptor (a Python browser environment). In fact a package also with other modules adapted from CodeSkulptor.',  # noqa
    long_description=io.open('README.rst', encoding='utf-8').read(),
    long_description_content_type='text/x-rst',

    url=_WEBSITE_DOC,

    author='Olivier Pirson',
    author_email='olivier.pirson.opi@gmail.com',

    license='GPLv3',

    classifiers=(
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Natural Language :: English',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',

        'Topic :: Education',
        'Topic :: Games/Entertainment',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: pygame',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Widget Sets'
        ),

    platforms='any',

    keywords='CodeSkulptor SimpleGUI Pygame game education',

    project_urls={
        'Documentation': _WEBSITE_DOC,
        'Funding': 'http://www.opimedia.be/donate/',
        'Say Thanks!': 'http://www.opimedia.be',
        'Source': _WEBSITE
    },

    packages=('SimpleGUICS2Pygame', ),

    install_requires=REQUIREMENTS,

    python_requires='>=2.7',

    scripts=('SimpleGUICS2Pygame/script/cs2both.py',
             'SimpleGUICS2Pygame/script/pygame_check.py',
             'SimpleGUICS2Pygame/script/SimpleGUICS2Pygame_check.py'),

    # https://setuptools.readthedocs.io/en/latest/setuptools.html#new-and-changed-setup-keywords
    include_package_data=True
)
