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

1. We start with a numbered list

   > Within the list we quote a section of some documentation
   >
   > :::{important}
   > The documentation has an info box with some code inside it:
   >
   > ```
   > print("Nested formatting yay!")
   > ```
   > :::

1. We continue the list and markdown knows that it's the same list and not a new one.

::::

::::{tab-item} Raw content

````
1. We start with a numbered list

   > Within the list we quote a section of some documentation
   >
   > :::{info}
   > The documentation has an info box with some code inside it:
   >
   > ```
   > print("Nested formatting yay!")
   > ```
   > :::

1. We continue the list and markdown knows that it's the same list and not a new one.
````

::::

:::::

| rST | MyST |
|---|---|
| [rST documentation in Sphinx docs](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) | [myst-parser docs](https://myst-parser.readthedocs.io/en/latest/index.html) |
| [rST documentation in Docutils docs](https://docutils.sourceforge.io/docs/user/rst/quickref.html) | [myst-nb docs](https://myst-nb.readthedocs.io/en/latest/) |
| [rST cheatsheet by Thomas Cokelaer](https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html) | [MyST cheatsheet in jupyterbook docs](https://jupyterbook.org/reference/cheatsheet.html) |

:::{toctree}
:hidden:

roles
directives
conf
:::
