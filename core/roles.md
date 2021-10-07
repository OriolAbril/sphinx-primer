# Roles

Roles are inline content and are generally used for formatting and
for cross-referencing. Roles require a type and an argument.
Optionally, when used for cross-referencing only, roles can also contain
a custom text for the hyperlink.
Also optionally, some formatting roles accept extra formatting options
in addition to the main argument, however, there is no general rule on that,
some use parenthesis, others semi colons or commas...

::::{tab-set}

:::{tab-item} Rendered content
* A formatting role for abbreviations: {abbr}`PPL (Probabilistic Programming Language)`
* A cross-referencing role:
  {doc}`markup`, {doc}`back to markup <markup>`, {func}`numpy.array`
:::

:::{tab-item} Raw MyST content
```
* A formatting role for abbreviations: {abbr}`PPL (Probabilistic Programming Language)`
* A cross-referencing role:
  {doc}`markup`, {doc}`back to markup <markup>`, {func}`numpy.array`
```
:::

:::{tab-item} Raw rST content
```
* A formatting role for abbreviations: :abbr:`PPL (Probabilistic Programming Language)`
* A cross-referencing role:
  :doc:`markup`, :doc:`back to markup <markup>`, :func:`numpy.array`
```
:::

::::

**Resources**
* [Sphinx docs on roles](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html)
* [readthedocs page on cross-referencing with sphinx](https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html)
