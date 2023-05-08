# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'SimpleGUICS2Pygame'
copyright = '2013-2020, Olivier Pirson'
author = 'Olivier Pirson'

if os.environ.get('READTHEDOCS', None) != 'True':
    from SimpleGUICS2Pygame import _VERSION as SimpleGUICS2Pygame_VERSION

    version = SimpleGUICS2Pygame_VERSION


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo',
              'sphinx.ext.coverage', 'sphinx.ext.viewcode']

autodoc_mock_imports = ['audioread', 'matplotlib', 'pygame',
                        'simplegui',
                        'user305_SaT1YKoOikl4ax9']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
if os.environ.get('READTHEDOCS', None) != 'True':
    import sphinx_rtd_theme

    html_theme = 'sphinx_rtd_theme'

html_logo = '_static/img/SimpleGUICS2Pygame_64x64_t.png'
html_favicon = '_static/img/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
