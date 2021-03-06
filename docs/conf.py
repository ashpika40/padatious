#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Padatious documentation build configuration file
#

import os
import sys

sys.path.insert(0, os.path.abspath('../'))

# General Configuration

extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon']

autodoc_mock_imports = ['fann2.libfann', 'xxhash']

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# General Info
project = 'Padatious'
copyright = '2017, Mycroft AI'
author = 'Matthew Scholefield'

version = '0.1.0'
release = '0.1.0'  # Includes alpha/beta/rc tags.

language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Syntax Highlighting
pygments_style = 'sphinx'

todo_include_todos = False

import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    'navigation_depth': 4,
}

html_static_path = []
htmlhelp_basename = 'Padatiousdoc'

# Options for LaTeX output

latex_elements = {}
latex_documents = [
    (master_doc, 'Padatious.tex', 'Padatious Documentation',
     'Matthew Scholefield', 'manual'),
]


# Options for manual page output

man_pages = [
    (master_doc, 'padatious', 'Padatious Documentation',
     [author], 1)
]


# Options for Texinfo output

texinfo_documents = [
    (master_doc, 'Padatious', 'Padatious Documentation',
     author, 'Padatious', 'Neural Network Intent Parser.',
     'Miscellaneous'),
]

# Options for Napoleon

napoleon_google_docstring = True
napoleon_numpy_docstring = False


