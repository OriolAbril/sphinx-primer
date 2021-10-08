# Markup

The most common and simple formatting actions are supported natively in both rST
and MyST, and if you are reading this, chances are you already know which
syntax to use for things like titles, bullet lists or bold text.

More complex formatting can also be achieved with roles and directives, two
key concepts in sphinx that are covered in the following pages.
The resources below generally combine markup, roles and directives
(without distinguishing if their goal is formatting or not).

There is one very important aspect that is generally overlooked, but that is key
to both rST and MyST, which is that both support indefinite nesting of
markup and directives. See for yourselves:

:::::{tab-set}

::::{tab-item} Rendered content
:::{include} nesting_example.md
:start-line: 4
:::
::::

::::{tab-item} Raw content
:::{include} nesting_example.md
:code:
:start-line: 4
:::
::::

:::::

| rST | MyST |
|---|---|
| {ref}`rST documentation in Sphinx docs <sphinx:rst-primer>` | [MyST-Parser docs](https://myst-parser.readthedocs.io/en/latest/index.html) |
| [rST documentation in Docutils docs](https://docutils.sourceforge.io/docs/user/rst/quickref.html) | [MyST-NB docs](https://myst-nb.readthedocs.io/en/latest/) |
| [rST cheatsheet by Thomas Cokelaer](https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html) | [MyST cheatsheet in jupyterbook docs](https://jupyterbook.org/reference/cheatsheet.html) |

:::{toctree}
:hidden:

roles
directives
conf
:::
