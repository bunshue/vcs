**simpleguics2pygame** — the main module, **replace the simplegui** module of CodeSkulptor
==========================================================================================

.. toctree::
   simpleguics2pygame/canvas
   simpleguics2pygame/control
   simpleguics2pygame/frame
   simpleguics2pygame/image
   simpleguics2pygame/keys
   simpleguics2pygame/sound
   simpleguics2pygame/timer


.. warning::
   Be careful, the main module `simpleguics2pygame` is split in several files,
   but items from these files are available from the `simpleguics2pygame` module itself,
   like the `simplegui` module of CodeSkulptor.

   For example, the function `SimpleGUICS2Pygame.simpleguics2pygame.frame.create_frame()`
   must be used by `simplegui.create_frame()` in CodeSkulptor
   and also with SimpleGUICS2Pygame with
   `import SimpleGUICS2Pygame.simpleguics2pygame as simplegui`.


.. automodule:: SimpleGUICS2Pygame.simpleguics2pygame
    :special-members:
    :private-members:
    :members:



* :ref:`genindex`
* :ref:`modindex`
