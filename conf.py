# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer

import json
import os

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'WP fail2ban Blocklist'
copyright = '2020-2026, Charles Lecklider'
author = 'Charles Lecklider'

_pkg = json.load(open(os.path.join(os.path.dirname(__file__), 'version.json')))
version = _pkg.get('version', '')
release = _pkg.get('version', '')
if _pkg.get('version_label'):
    release = '%s (%s)' % (version, _pkg['version_label'])


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv', 'venv']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# The master toctree document.
master_doc = 'index'

intersphinx_mapping = {
    'wp-fail2ban': (
        'https://docs.wp-fail2ban.com/en/latest/', (
            '../../../../plugin/sphinx/_build/html/objects.inv', None
        )
    ),
}

lexers['php'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)

