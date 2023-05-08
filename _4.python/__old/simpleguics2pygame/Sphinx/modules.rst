All modules of this package
===========================

.. toctree::
   codeskulptor
   codeskulptor_lib

   numeric

   simplegui_lib

   simpleguics2pygame

   simpleplot


.. warning::
   Be careful, the main module `simpleguics2pygame` is split in several files,
   but items from these files are available from the `simpleguics2pygame` module itself,
   like the `simplegui` module of CodeSkulptor.

   For example, the function `SimpleGUICS2Pygame.simpleguics2pygame.frame.create_frame()`
   must be used by `simplegui.create_frame()` in CodeSkulptor
   and also with SimpleGUICS2Pygame with
   `import SimpleGUICS2Pygame.simpleguics2pygame as simplegui`.


* :ref:`genindex`
* :ref:`modindex`
