Tips
====

CodeSkulptor
------------
CodeSkulptor2_ is a Python implementation (in JavaScript) running in a browser.
It implements a subset of Python 2.

CodeSkulptor3_ is the same but it implements a subset of Python 3.

It is the environment used in the MOOC
`An Introduction to Interactive Programming in Python`_
(Rice University, Coursera).

.. _`An Introduction to Interactive Programming in Python`: https://www.coursera.org/learn/interactive-python-1
.. _CodeSkulptor2: https://py2.codeskulptor.org/
.. _CodeSkulptor3: https://py3.codeskulptor.org/


To use a program from CodeSkulptor in *standard Python* (with this package),
you need to change
``import simplegui``
by
``import SimpleGUICS2Pygame.simpleguics2pygame as simplegui``.

**The right way to do** is to write this

.. code-block:: python

    try:
        import simplegui
    except ImportError:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

and your program **runs both** in CodeSkulptor and *standard Python*.

So, if your program runs in CodeSkulptor, it imports ``simplegui``.
Else, an ``ImportError`` exception will be raised,
and then it will imports ``SimpleGUICS2Pygame.simpleguics2pygame``
and it renamed to ``simplegui``.


| In this package a little script_ ``cs2both.py`` can help to quickly make this changement on program downloaded from CodeSkulptor.
| Run ``python cs2both.py YOURPROGRAM.py``.
| The file ``YOURPROGRAM.py`` is copied to ``YOURPROGRAM.py.bak`` before changing.

.. _script: https://bitbucket.org/OPiMedia/simpleguics2pygame/src/master/SimpleGUICS2Pygame/script/

|
|

To use also the **other modules**,
you can write this.
But specify only those you use.

.. code-block:: python

    try:
        import simplegui

        import codeskulptor
        import numeric
        import simpleplot

        import user305_SXBsmszNiUxIeoV as codeskulptor_lib
        import user305_SZNWcbqQHXN4pow as simplegui_lib
    except ImportError:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

        import SimpleGUICS2Pygame.codeskulptor as codeskulptor
        import SimpleGUICS2Pygame.numeric as numeric
        import SimpleGUICS2Pygame.simpleplot as simpleplot

        import SimpleGUICS2Pygame.codeskulptor_lib as codeskulptor_lib
        import SimpleGUICS2Pygame.simplegui_lib as simplegui_lib

Note that import name like ``user305_SXBsmszNiUxIeoV`` in CodeSkulptor
is valid both for CodeSkulptor2 and CodeSkulptor3.
It corresponds to URLs
https://py2.codeskulptor.org/#user305_SXBsmszNiUxIeoV.py
and
https://py3.codeskulptor.org/#user305_SXBsmszNiUxIeoV.py .


Specific code
-------------
To run specific code on CodeSkulptor2_ or with SimpleGUICS2Pygame,
you can write this

.. code-block:: python

    try:
        import simplegui

        SIMPLEGUICS2PYGAME = False
    except ImportError:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

        SIMPLEGUICS2PYGAME = True

And then you can run specific code simply by testing value of ``SIMPLEGUICS2PYGAME``. For example:

.. code-block:: python

    # …

    def joypad_up(joypad, button):
        if joypad == 0:
            if button == 0:
                # …

    if SIMPLEGUICS2PYGAME:
        frame._set_joypadup_handler(joypad_up)


Joypads
-------
SimpleGUICS2Pygame adds the possibility to use joypads.
It is *not* available in CodeSkulptor.
You can make compatible program with the previous tip
to separate specific code.

Similarly to ``set_mouseclick_handler()`` and ``set_mousedrag_handler()`` functions,
the class `Frame`_ in SimpleGUICS2Pygame defines
``_set_joypaddown_handler()``,
``_set_joypadup_handler()``,
``_set_joypadaxe_handler()``
and ``_set_joypadhat_handler()``.

Two little examples using joypads
(but of course only when you run them with SimpleGUICS2Pygame directly on your computer):
`example/Pong.py`_
and `example/RiceRocks_Asteroids.py`_.

.. _`example/Pong.py`: https://py3.codeskulptor.org/#user305_X62vPplhMJxqOWu.py
.. _`example/RiceRocks_Asteroids.py`: https://py3.codeskulptor.org/#user305_XNvcqTxIBngtHPu.py
.. _`Frame`: simpleguics2pygame/frame.html#SimpleGUICS2Pygame.simpleguics2pygame.frame.Frame


Colors
------
The color parameter used by drawing functions must be in the following formats:

* ``'#rrggbb'`` with rr, gg, bb hexadecimal numbers on 2 figures
* ``'#rgb'`` with r, g, b  hexadecimal numbers on 1 figure
* ``'rbg(red,blue,green)'`` with red, blue, green 0 <= integer <= 255
* ``'rgba(red,blue,green,alpha)'`` with red, blue, green 0 <= integer <= 255 and alpha between 0 and 1
* a constant name in this list https://www.w3schools.com/colors/colors_names.asp .

See the official HTML colors:
http://www.opimedia.be/DS/mementos/colors.htm .


Command line arguments
----------------------
When you run a program you can use following arguments:
``python YOURPROGRAM.py [SimpleGUICS2Pygame arguments] [application arguments]``

* ``--default-font``: Use Pygame default font instead serif, monospace… (this is faster if you display a lot of text).
* ``--display-fps``: Display FPS average on the canvas.
* ``--fps N``: Set Frame Per Second (default: 60 FPS).
* ``--frame-padding N``: Set the padding in pixels found around the canvas (default: 2).
* ``--fullscreen``: Fullscreen mode.
* ``--help``: Print help message and quit.
* ``--keep-timers``: Keep running timers when close frame without asking (default: ask before close). See also ``--stop-timers``.
* ``--last``: Mark this argument as the last SimpleGUICS2Pygame's argument. (Do nothing else.)
* ``--no-border``: Window without border.
* ``--no-controlpanel``: Hide the control panel (and status boxes).
* ``--no-load-sound``: Don't load any sound.
* ``--no-status``: Hide two status boxes.
* ``--overwrite-downloaded-medias``: Download all images and sounds from Web and save in local directory even if they already exist.
* ``--print-application-args``: Print remaining arguments transmit to application.
* ``--print-args``: Print final configuration from SimpleGUICS2Pygame's argument.
* ``--print-load-medias``: Print URLs or local filenames loaded.
* ``--print-stats-cache``: After frame stopped, print some statistics of caches.
* ``--save-downloaded-medias``: Save images and sounds downloaded from Web that don't already exist in local directory.
* ``--stop-timers``: Stop all timers when ending program (default: running timers continue, as in CodeSkulptor). See also ``--keep-timers``.
* ``--version``: Print help message and quit.

If an argument is not in this list then it is ignored and all next arguments are ignored by SimpleGUICS2Pygame.

Arguments used by SimpleGUICS2Pygame is deleted to ``sys.argv``.
Remaining arguments can used by your application.

SimpleGUICS2Pygame arguments are automatically read
when the module ``simpleguics2pygame`` is imported.

Examples:
  * | ``python YOURPROGRAM.py --no-controlpanel --stop-timers --foo --fullscreen``
    | Run ``YOURPROGRAM.py`` with the control panel hidden and timers will stoped. But SimpleGUICS2Pygame ignore ``--foo`` and ``--fullscreen``.
    | ``YOURPROGRAM.py`` application receive ``--foo --fullscreen`` arguments.

  * | ``python YOURPROGRAM.py --no-controlpanel --last --stop-timers --foo --fps 30``
    | Run ``YOURPROGRAM.py`` with the control panel hidden. But SimpleGUICS2Pygame ignore ``--stop-timers``, ``--foo``, ``--fps`` and ``30``.
    | ``YOURPROGRAM.py`` application receive ``--stop-timers --foo --fps 30`` arguments.


Download medias
---------------
Run ``python YOURPROGRAM.py --save-downloaded-medias --print-load-medias`` once.
Images and sounds used (from URLs) will be saved in local directory (``_img/`` et ``_snd/`` by default).
Next simply run ``python YOURPROGRAM.py`` and the medias will be loaded from these local directories.

For example,
``load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png')``
save image to
``_img/commondatastorage.googleapis.com/codeskulptor_assets/lathrop/double_ship.png``.


SimpleGUICS2Pygame has two additional classes to load directly local files:
`_LocalImage()`_ and `_LocalSound()`_.
But be aware that these functions are *not* available in CodeSkulptor.

.. _`_LocalImage()`: simpleguics2pygame/image.html#SimpleGUICS2Pygame.simpleguics2pygame.image._LocalImage
.. _`_LocalSound()`: simpleguics2pygame/sound.html#SimpleGUICS2Pygame.simpleguics2pygame.sound._LocalSound



Helper functions
----------------
This package contains 5 additional modules with several helper functions that you can also import online in CodeSkulptor:

  * `codeskulptor_lib`_ — some miscellaneous functions
  * `simplegui_lib_draw`_ — draw functions
  * `simplegui_lib_fps`_ — class to calculate and display Frames Per Second
  * `simplegui_lib_keys`_ — class to manage keyboard handling
  * `simplegui_lib_loader`_ — class to load images and sounds

.. _`codeskulptor_lib`: codeskulptor_lib.html
.. _`simplegui_lib_draw`: simplegui_lib_draw.html
.. _`simplegui_lib_fps`: simplegui_lib_fps.html
.. _`simplegui_lib_keys`: simplegui_lib_keys.html
.. _`simplegui_lib_loader`: simplegui_lib_loader.html

For example, to draw multiline text you can use `draw_text_multi()`_ from the `simplegui_lib_draw`_ module by:

.. _`draw_text_multi()`: simplegui_lib_draw.html#SimpleGUICS2Pygame.simplegui_lib_draw.draw_text_multi

.. code-block:: python

    try:
        import simplegui

        import user305_SaT1YKoOikl4ax9 as simplegui_lib_draw
    except ImportError:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

        import SimpleGUICS2Pygame.simplegui_lib as simplegui_lib_draw

    def draw(canvas):
        # …
        draw_text_multi(canvas,
                        """line 1
    line 2
    line 3""", (x, y), size, 'white', 'serif')
        # …


Python assertions option
------------------------
Run
``python YOURPROGRAM.py``
then asserts is enabled and this package is (intentionnaly) very strict.
So maybe "correct" programs in CodeSkulptor fail!
(In fact CodeSkulptor is very permissive.
Some incorrect Python codes are accepted.)
It is a good point to develop and write *correct programs*.
But if you want just run a program
without annoying assertions
you can *disable* them with.
``python -O YOURPROGRAM.py``.

In some cases
run without assertions is **faster**.
See in the `Comparison of speeds`_ section,
an example where SimpleGUICS2Pygame functions are executed a lot of times.

.. _`Comparison of speeds`: Compatibility.html#comparison-of-speeds


Ressources: images, sounds and example programs
-----------------------------------------------
Online images_ & sounds_ links

.. _images: _static/links/img_links.html
.. _sounds: _static/links/snd_links.html

`Python programs running in CodeSkulptor`_

.. _`Python programs running in CodeSkulptor`: _static/links/prog_links.html
