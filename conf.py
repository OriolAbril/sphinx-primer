import os
import sys
from typing import Dict, Any

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.graphviz",
    "myst_nb",
    "sphinx_copybutton",
    "sphinx_design",
]

# ipython directive configuration
ipython_warning_is_error = False

# Generate API documentation when building
autosummary_generate = True
numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
#

# MyST related params
jupyter_execute_notebooks = "auto"
execution_excludepatterns = ["*.ipynb"]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "amsmath"
]

# The base toctree document.
master_doc = "index"

# General information about the project.
project = "Sphinx Primer"
copyright = "2021, Oriol Abril-Pla"
author = "Oriol Abril-Pla"

version = "0.1"
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".ipynb_checkpoints", "README.md"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/OriolAbril",
            "icon": "fab fa-github-square",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/OriolAbril",
            "icon": "fab fa-twitter-square",
        },
    ],
    "navbar_start": ["navbar-logo", "navbar-version"],
    "use_edit_page_button": True,
}
html_context = {
    "github_user": "OriolAbril",
    "github_repo": "sphinx-primer",
    "github_version": "main",
    "doc_path": ".",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_static_path = ["_static"]

# -- Options for HTMLHelp output ------------------------------------------

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/logo.png"


# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Example configuration for intersphinx
intersphinx_mapping = {
    "arviz": ("https://arviz-devs.github.io/arviz/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "pymc": ("https://docs.pymc.io/", None),
    "xarray": ("http://xarray.pydata.org/en/stable/", None),
}
