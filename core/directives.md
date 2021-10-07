# Directives

Directives are block content with 4 content blocks/arguments:

:::::{tab-set}

::::{tab-item} MyST
````
```{directivename} main-argument
:kwarg1: value
:kwarg2: value

Main content of the directive, generally prose but not necessarly.
```
````
::::

::::{tab-item} MyST (colon fence)

````
:::{directivename} main-argument
:kwarg1: value
:kwarg2: value

Main content of the directive, generally prose but not necessarly.
:::
````

::::

::::{tab-item} rST

````
.. directivename:: main-argument
    :kwarg1: value
    :kwaarg2: value

    Main content of the directive, generally prose but not necessarly.
````

::::


:::::

Out of these 4 fields, only the directivename is always required,
however, most directives require the directive name and at least one
of main argument or main content.

As you can see, MyST allows two syntaxes to define directives.
Both work exactly the same, however, using the colon fence option
has the advantage of rendering the main content of the directive
as markdown which while only partially right, can already help get
an idea of formatting issues. After all, markup without roles and
directives in MyST is very similar to pure markdown.

Also note that in MyST, directives are defined with 3 or more backticks/colons,
in order to nest directives, you need to start with more backticks/colons to avoid
syntax errors due to anbiguity about which directive should be closed.

**Resources**
* [Sphinx docs on directives](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html)
* [MyST documentation on directives](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html#directives-a-block-level-extension-point)
