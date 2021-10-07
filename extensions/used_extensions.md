# Extensions in ArviZ and PyMC
## Built in extensions
Build in extensions are prefixed with `sphinx.ext.`
* `autodoc` and `autosummary` allow automating the process of including
  docstrings into the documentation.
* `viewcode` adds the `[source]` link to the API pages generated with
  `autosummary`
* `mathjax` invoques mathjax so that math is rendered correctly in html.
* `intersphinx` allows cross-referencing pages from other documentations.
* `napoleon` parses numpy style docstrings. I think it's the same as numpydoc and
  that we only need one of them.

## External extensions
* `numpydoc` same comment as `napoleon`
* `IPython` extensions add directives for code that is automatically executed when
  building the docs as well as highlighting for those code blocks.
* `matplotlib.sphinxext.plot_directive` and `bokeh.sphinxext.bokeh_plot`
  add directive that embed plots into the documentation.
* `myst` and `myst_nb` allow sphinx to parse `.md` and `.ipynb` files.
* `sphinx_design` adds multiple roles and directives for formatting options
  such as grids and cards based on bootstrap, octicon and font awesome icons...
* `sphinx_panels` deprecated and being replaced by `sphinx_design`
* `sphinx_copybutton` automatically adds a copy icon to all code blocks.
* `notfound.extension` support for a custom 404 error page.
* `ablog` adds a post directive to include tags, categories, date posted...
  to pages and automatically builds archives, tag word clouds...
* `sphinxcontrib.bibtex` adds roles and directive for latex-like citation
  capabilities and support for bibtex format references.


## "Homemade" extensions
* `gallery_generator` (ArviZ) runs all the files within the `examples/` folder
  and automatically builds the Example gallery page from them.
* `gallery_generator` (PyMC) generates some javascript code that creates cards
  for the Tutorials and Examples sections.
