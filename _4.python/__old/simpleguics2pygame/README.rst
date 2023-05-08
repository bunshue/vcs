.. -*- restructuredtext -*-

==================
SimpleGUICS2Pygame
==================

It is primarily a standard Python_ (**2 and 3**) module
reimplementing the SimpleGUI particular module of CodeSkulptor2_ and CodeSkulptor3_
(a Python browser environment).
This is in fact a package also with other modules adapted from CodeSkulptor.

Simply change

.. code-block:: python

   import simplegui

by

.. code-block:: python

    try:
        import simplegui
    except ImportError:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

in your CodeSkulptor program
and your program **run both** in CodeSkulptor
and *standard Python* with this module (and Pygame).

|SimpleGUICS2Pygame|

`Online HTML documentation`_ on **Read The Docs**.
(You can also see the online `SimpleGUI documentation on CodeSkulptor2`_
or `SimpleGUI documentation on CodeSkulptor3`_.)

| **Sources** and installers on Bitbucket: https://bitbucket.org/OPiMedia/simpleguics2pygame
| and on **PyPI**: https://pypi.org/project/SimpleGUICS2Pygame/ .

.. _CodeSkulptor2: https://py2.codeskulptor.org/
.. _CodeSkulptor3: https://py3.codeskulptor.org/
.. _`Online HTML documentation`: https://simpleguics2pygame.readthedocs.io/
.. _Python: https://www.python.org/
.. _`SimpleGUI documentation on CodeSkulptor2`: https://py2.codeskulptor.org/docs.html
.. _`SimpleGUI documentation on CodeSkulptor3`: https://py3.codeskulptor.org/docs.html

.. |SimpleGUICS2Pygame| image:: https://simpleguics2pygame.readthedocs.io/en/latest/_images/SimpleGUICS2Pygame_64x64_t.png

|



If you have some problem
========================
First, read this short main `documentation page`_,
this Compatibility_ page
and this Tips_ page.

If you have problem with some command,
you can see its documentation in the `modules page`_.

Next, you can search in Stack Overflow.
If you don't find answer, you can ask question like this_.

Finally you can email me.
I will try to help you with pleasure.

.. _`documentation page`: https://simpleguics2pygame.readthedocs.io/
.. _Compatibility: https://simpleguics2pygame.readthedocs.io/en/latest/Compatibility.html
.. _`modules page`: https://simpleguics2pygame.readthedocs.io/en/latest/modules.html
.. _this: https://stackoverflow.com/questions/16387770/how-to-integrate-simplegui-with-python-2-7-and-3-0-shell
.. _Tips: https://simpleguics2pygame.readthedocs.io/en/latest/Tips.html

|



Installation
============
Installation requires that Python tools are up to date.
If not, then see the `Online HTML documentation`_.
Else, simply do:

.. code-block:: sh

   $ python -m pip install SimpleGUICS2Pygame --user

Note that ``$`` represents the prompt and do *not* be entered by you.

If several Python implementations are installed,
maybe you must use something like ``python2`` or ``python3`` instead ``python`` command.

With the ``--user`` option
the installation is made in the user directory
and doesn't require administrator rights.


Normally all **requirements are automatically installed**.
But for that you need have ``pip`` and other installation packages installed
and up to date.

.. warning::
   If you have some installation problem
   see the complete information in `Online HTML documentation`_.



On Arch Linux you can use this package installation script (written by Danny Fajardo):
`Arch_Linux/PKGBUILD`_.

.. _`Arch_Linux/PKGBUILD`: https://bitbucket.org/OPiMedia/simpleguics2pygame/src/master/GNU_Linux/Arch_Linux/PKGBUILD

|



Examples of CodeSkulptor and SimpleGUICS2Pygame use
===================================================
You can see examples in `SimpleGUICS2Pygame/example/`_ subdirectory from the sources archives.

.. _`SimpleGUICS2Pygame/example/`: https://bitbucket.org/OPiMedia/simpleguics2pygame/src/master/SimpleGUICS2Pygame/example/

Or online:
`Python programs running in CodeSkulptor`_ .

Two simple online examples:
  * `Frame_example.py`_: very simple canvas example
  * `presentation.py`_: little draw images and texts

.. _`Frame_example.py`: https://py3.codeskulptor.org/#user305_ELuwGUIuxh7hmlE.py
.. _`presentation.py`: https://py3.codeskulptor.org/#user306_QDvMS3LY8vYOaZ5.py
.. _`Python programs running in CodeSkulptor`: https://simpleguics2pygame.readthedocs.io/en/latest/_static/links/prog_links.html

|



Message to developers
=====================
This is a **free software**, so you can download it, **modify it** and **submit your modifications**.
You can also **redistribute** your own version (keeping the GPL license).

Complete **sources** on Bitbucket: https://bitbucket.org/OPiMedia/simpleguics2pygame

See developers_'page.

.. _developers: https://simpleguics2pygame.readthedocs.io/en/latest/Developers.html

|



Author: 🌳 Olivier Pirson — OPi |OPi| 🇧🇪🇫🇷🇬🇧 🐧 👨‍💻 👨‍🔬
=================================================================
🌐 Website: http://www.opimedia.be/

💾 Bitbucket: https://bitbucket.org/OPiMedia/

* 📧 olivier.pirson.opi@gmail.com
* Mastodon: https://mamot.fr/@OPiMedia — Twitter: https://twitter.com/OPirson
* 👨‍💻 LinkedIn: https://www.linkedin.com/in/olivierpirson/ — CV: http://www.opimedia.be/CV/English.html
* other profiles: http://www.opimedia.be/about/

.. |OPi| image:: http://www.opimedia.be/_png/OPi.png

|



Support me
==========
This program is a **free software** (GPL license).
It is **completely free** (like "free speech" *and* like "free beer").
However you can **support me** financially by donating.

Click to this link |Donate|
**Thank you!**

.. |Donate| image:: http://www.opimedia.be/donate/_png/Paypal_Donate_92x26_t.png
   :target: http://www.opimedia.be/donate/

|



License: GPLv3_ |GPLv3|
=======================
Copyright (C) 2013-2016, 2018, 2020-2021 Olivier Pirson

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

.. _GPLv3: https://www.gnu.org/licenses/gpl-3.0.html

.. |GPLv3| image:: https://www.gnu.org/graphics/gplv3-88x31.png

|



Note that
=========
* `SimpleGUI of CodeSkulptor2`_ (Scott Rixner) is a specific module of CodeSkulptor2_, written in JavaScript.

  CodeSkulptor is a Python implementation running **in a browser**.
  It implements a subset of Python **2**.
  It is the environment used in the course
  `An Introduction to Interactive Programming in Python`_
  (Rice University, Coursera).

* `SimpleGUI of CodeSkulptor3`_ (Scott Rixner) is the same in the new version CodeSkulptor3_
  that implements a subset of Python **3**.

* **SimpleGUICS2Pygame** (Olivier Pirson) is **this package**.
  It is fully compatible with Python **2 and 3**.

  It contains
  ``codeskulptor``, ``numeric``, ``simpleguics2pygame`` and ``simpleplot`` modules
  that reimplement
  ``codeskulptor``, ``numeric``, ``simplegui`` and ``simpleplot`` modules of CodeSkulptor.

  .. warning::
     SimpleGUICS2Pygame was **designed to mimic behavior of CodeSkulptor**.
     So `load_image()`_ and `load_sound()`_ methods can load medias only from URL, not local files.
     However SimpleGUICS2Pygame can save these medias to a specific local directory.
     See the `Download medias`_ tips.

     You can also use *specific* `_load_local_image()`_ and `_load_local_sound()`_ methods
     to load local files. But be careful, each specific method doesn't exist in CodeSkulptor.

     There exist some **little differences between SimpleGUICS2Pygame and SimpleGUI** of CodeSkulptor.
     See Compatibility_ notes.

     .. _`Download medias`: https://simpleguics2pygame.readthedocs.io/en/latest/Tips.html#download-medias
     .. _`load_image()`: https://simpleguics2pygame.readthedocs.io/en/latest/simpleguics2pygame/image.html#SimpleGUICS2Pygame.simpleguics2pygame.image.load_image
     .. _`_load_local_image()`: https://simpleguics2pygame.readthedocs.io/en/latest/simpleguics2pygame/image.html#SimpleGUICS2Pygame.simpleguics2pygame.image._load_local_image
     .. _`_load_local_sound()`: https://simpleguics2pygame.readthedocs.io/en/latest/simpleguics2pygame/sound.html#SimpleGUICS2Pygame.simpleguics2pygame.sound._load_local_sound
     .. _`load_sound()`: https://simpleguics2pygame.readthedocs.io/en/latest/simpleguics2pygame/sound.html#SimpleGUICS2Pygame.simpleguics2pygame.sound.load_sound

* SimpleGUITk_ (David Holm) is *another implementation* of SimpleGUI of CodeSkulptor, using Tkinter and some others packages. It is really less complete and not updated. However it works for some programs.

* simplequi_ (Arthur Gordon-Wright) is *another implementation* of SimpleGUI of CodeSkulptor, using Qt/PySide2. It is a partial implementation that I have not tested.

.. warning::
   * simplegui_ (Florian Berger) is a Python package which has the same name as SimpleGUI of CodeSkulptor, but it is *totally something else*.

   .. _`An Introduction to Interactive Programming in Python`: https://www.coursera.org/learn/interactive-python-1
   .. _simplegui: https://pypi.org/project/simplegui
   .. _`SimpleGUI of CodeSkulptor2`: https://py2.codeskulptor.org/docs.html#Frames
   .. _`SimpleGUI of CodeSkulptor3`: https://py3.codeskulptor.org/docs.html#Frames
   .. _SimpleGUITk: https://pypi.org/project/SimpleGUITk
   .. _simplequi: https://pypi.org/project/simplequi/

   * PySimpleGUI_ is also a Python package that is *totally something else*.

   .. _PySimpleGUI: https://pypi.org/project/PySimpleGUI/

|



Changes
=======
* 2.1.1 — May 4, 2021 (Work in progress)

  - Updated links to CodeSkulptor2_.

* 2.1.0 — November 29, 2020

  - Removed Pygame restriction to version 1.9.6.
  - Removed old special cases when Pygame was not installed.
  - Cleaned some warnings from mypy.
  - ``example/Nostalgic_Basic_Blitz.py``: corrected bug with negative position of bomb.

* 2.0.3 — October 2, 2020

  - Corrected reading permission of files in distribution files.
  - Added Arch Linux installation script (written by Danny Fajardo).

* 2.0.2 — May 23, 2020

  - Documentation:

    - Updated image and sound links.

  - Tests:

    - Completed missing type annotations in simpleguics2pygame/control.

* 2.0.1 — May 21, 2020

  - Documentation:

    - Added class diagram generated by Pyreverse.
    - Updated image and CodeSkulptor program links.

  - Program examples:

    - Adapted ``example/Memory.py`` with images moved to HTTPS.

  - Tests:

    - Added type annotations (in Python 2 mode) for each function.
    - Cleaned some type annotations instead ignore them.

* 2.0.0 — April 18, 2020

  - Converted from Mercurial version control system to Git.
  - Corrected files included in MANIFEST.in for distribution building. (Thanks to `7coil`.)
  - Improved installation. Now all **requirements are automatically installed**.

  - Modules:

    - **Splitted the big file ``simpleguics2pygame.py``.**
    - Added alpha possibility on background color.
    - Added dealing of **joypads**.
    - Added dealing of **MP3** sounds.
      Added ``draw_arc()`` in ``Canvas`` and ``test_arc``.
    - Added ``Frame.download_canvas_image()``, ``Frame._cursor_auto_hide`` and ``Frame._set_cursor_visible()``.
    - Added ``codeskulptor_version()`` in ``codeskulptor_lib``.
    - Added ``draw_text_multi()`` in ``simplegui_lib_draw``.
    - Added ``--frame-padding`` (thanks to `7coil`), ``--last``, ``--help``, ``--print-application-args``, ``--print-args`` and ``--version`` command line options.
    - Added ``randomize_iteration()`` in ``codeskulptor``.
    - Added ``transparent`` "color" name.
    - Added ``ValueError`` exception if ``draw_text()`` try to draw a text containing unprintable whitespace character.
    - Corrected ``keys`` parameter use in ``simplegui_lib_keys.Keys()``.
    - Improved dealing of input box.
    - Updated ``simpleplot`` module, to "run" same if matplotlib is not installed.

  - Documentation:

    - Corrected "Read the Docs" subpackage problem.
    - Added a developer's page.
    - Replaced ``_WEBSITE`` value by documentation link.
    - Updated. (Thanks to `John Gray` and `Tom Keller`.)
    - Splitted media links to image links and sound links.
    - Updated installation documentation.
    - Updated media and CodeSkulptor programs links.

  - Program examples:

    - Added ``example/presentation.py``.
    - Added ``example/stop_example.py``.
    - Moved from CodeSkulptor to CodeSkulptor3.

  - Scripts:

    - Added ``script/pygame_check.py`` to check Pygame installation alone.
    - Updated ``script/SimpleGUICS2Pygame_check.py``.

  - Tests:

    - Added static checking in ``Makefile``, and corrected a lot of style warnings.
    - Corrected and updated ``test/test_sound.py``.
    - Added ``test/test_command_line_options.py``.
    - Added ``test/test_input.py``.
    - Updated ``test/test_dir.py``.
    - Updated ``test/test_objects.py``.
    - Updated ``test/test_text.py``.

…

`Complete changelog`_

.. _`Complete changelog`: https://simpleguics2pygame.readthedocs.io/en/latest/ChangeLog.html
