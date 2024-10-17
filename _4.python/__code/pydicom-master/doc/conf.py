from datetime import datetime
import os
import sys

import pydicom

try:
    import gen_rst
except ImportError:
    pass
sys.path.insert(0, os.path.abspath('../build_tools/sphinx'))  # noqa

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinx_gallery.gen_gallery',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',  # Numpy style docstrings
    'sphinx.ext.linkcode',
    'sphinx.ext.extlinks',
    # Custom
    'sphinx_copybutton',
]

autosummary_generate = True

autodoc_default_options = {
    'members': None,
    'no-inherited-members': None,
}

# copybutton conf
copybutton_prompt_text = r'>>> |\.\.\. '
copybutton_prompt_is_regexp = True

# Shortcuts for sphinx.ext.extlinks
extlinks = {
    # 'alias' : (url_prefix, caption)
    # Usage :dcm:`link text <part05/sect_6.2.html>`
    'dcm': (
        'http://dicom.nema.org/medical/dicom/current/output/chtml/%s',
        None
    ),
    'gh': (
        'https://github.com/pydicom/%s',
        None
    ),
    "issue": ("https://github.com/pydicom/pydicom/issues/%s", "#"),
    "pr": ("https://github.com/pydicom/pydicom/pull/%s", "#"),
}

# intersphinx configuration
intersphinx_mapping = {
    'python': ('https://docs.python.org/{.major}'.format(
        sys.version_info), None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference', None),
    'matplotlib': ('http://matplotlib.org', None),
}

sphinx_gallery_conf = {
    'default_thumb_file': 'assets/img/pydicom_flat_black_alpha.png',
    # path to your examples scripts
    'examples_dirs': '../examples',
    # path where to save gallery generated examples
    'gallery_dirs': 'auto_examples',
    'backreferences_dir': os.path.join('generated'),
    # to make references clickable
    'doc_module': 'pydicom',
    'reference_url': {
        'pydicom': None
    }
}

napoleon_google_docstring = False
napoleon_numpy_docstring = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'pydicom'
year = datetime.now().strftime('%Y')
copyright = f'2008-{year}, Darcy Mason and pydicom contributors'

version = pydicom.__version__
# The full version, including alpha/beta/rc tags.
release = pydicom.__version__

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Custom style
html_style = 'css/pydicom.css'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


html_logo = "assets/img/pydicom_flat_black.svg"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "assets/img/favicon.ico"


# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

latex_documents = [
  ('index', 'pydicom.tex', 'pydicom Documentation',
   'Darcy Mason and pydicom contributors', 'manual'),
]


def generate_example_rst(app, what, name, obj, options, lines):
    # generate empty examples files, so that we don't get
    # inclusion errors if there are no examples for a class / module
    examples_path = os.path.join(app.srcdir, "generated",
                                 "%s.examples" % name)
    if not os.path.exists(examples_path):
        # touch file
        open(examples_path, 'w').close()


def setup(app):
    app.connect('autodoc-process-docstring', generate_example_rst)
    app.add_css_file('css/pydicom.css')



import pydicom
import os, os.path
testfile_path = os.path.join(pydicom.__path__[0], '../tests/test_files')
save_dir = os.getcwd()
os.chdir(testfile_path)



