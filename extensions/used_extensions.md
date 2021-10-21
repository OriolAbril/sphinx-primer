# Extensions in ArviZ and PyMC
## Built in extensions
{doc}`Built in extensions <sphinx:usage/extensions/index>` are prefixed with `sphinx.ext.`
* {mod}`~sphinx.ext.autodoc` and {mod}`~sphinx.ext.autosummary`
  allow automating the process of including docstrings into the documentation.
* {mod}`~sphinx.ext.viewcode` adds the `[source]` link to the API pages generated with
  `autosummary`
* {mod}`~sphinx.ext.mathjax` invoques mathjax so that math is rendered correctly in html.
* {mod}`~sphinx.ext.intersphinx` allows cross-referencing pages from other documentations.
* {mod}`~sphinx.ext.napoleon` parses numpy style docstrings. I think it's the same as numpydoc and
  that we only need one of them.

## External extensions
* [`numpydoc`](https://numpydoc.readthedocs.io/en/latest/) same comment as `napoleon`
* [`IPython`](https://ipython.readthedocs.io/en/stable/sphinxext.html) extensions add
  directives for code that is automatically executed when
  building the docs as well as highlighting for those code blocks.
* [`matplotlib.sphinxext.plot_directive`](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html)
  and [`bokeh.sphinxext.bokeh_plot`](https://docs.bokeh.org/en/latest/docs/reference/sphinxext.html#module-bokeh.sphinxext.bokeh_plot)
  add directive that embed plots into the documentation.
* [`myst`](https://myst-parser.readthedocs.io/en/latest/) and
  [`myst_nb`](https://myst-parser.readthedocs.io/en/latest/)
  allow sphinx to parse `.md` and `.ipynb` files.
* [`sphinx_design`](https://sphinx-design.readthedocs.io/en/sbt-theme/) adds
  multiple roles and directives for formatting options such as grids,
  tabs or cards based on bootstrap, octicon and font awesome icons...
* `sphinx_panels` deprecated and being replaced by `sphinx_design`
* [`sphinx_copybutton`](https://sphinx-copybutton.readthedocs.io/en/latest/)
  automatically adds a copy icon to all code blocks.
* [`sphinx_togglebutton`](https://sphinx-togglebutton.readthedocs.io/en/latest/) (pulled in under the hood by `myst_nb`) makes extra
  arguments and tags available for some directives and code cells in order
  to add "toggle buttons" and collapse content.
* [`notfound.extension`](https://sphinx-notfound-page.readthedocs.io/en/latest/)
  improves the support for a custom 404 error page, specially when hosting on
  GitHub pages or ReadTheDocs.
* [`ablog`](https://ablog.readthedocs.io/en/latest/) adds a post directive to include
  tags, categories, date posted... to pages and automatically builds archives, tag word clouds...
* [`sphinxcontrib.bibtex`](https://sphinxcontrib-bibtex.readthedocs.io/en/latest/) adds
  roles and directive for latex-like citation capabilities and support for bibtex format references.


## "Homemade" extensions
Even though these are part of the ArviZ/PyMC codebase, you should expect to work on
these extensions even less often than working on `conf.py`.
* [`gallery_generator`](https://github.com/arviz-devs/arviz/blob/main/doc/sphinxext/gallery_generator.py)
  (ArviZ) runs all the files within the `examples/` folder and automatically builds the
  [Example gallery](https://arviz-devs.github.io/arviz/examples/index.html) page from them.
* (soon to be removed) `gallery_generator` (PyMC) generates some javascript code that creates cards
  for the Tutorials and Examples sections.
