# Roles

Roles are for inline content, and are mostly used for formatting and
for cross-referencing. Roles require a type and an argument.
Optionally, when used for cross-referencing only, roles can also contain
a custom text for the hyperlink.
Also optionally, some formatting roles accept extra formatting options
in addition to the main argument, however, there is no general rule on that,
some use parenthesis, others semi colons or commas...

::::{tab-set}

:::{tab-item} Rendered content
* Formatting role for abbreviations and math:
  {abbr}`PPL (Probabilistic Programming Language)`, {math}`\exp{x}`
* Cross-referencing roles:
  {doc}`markup`, {doc}`back to markup <markup>`, {func}`numpy.array`
:::

:::{tab-item} Raw MyST content
```
* Formatting role for abbreviations and math:
  {abbr}`PPL (Probabilistic Programming Language)`, {math}`\exp{x}`
* Cross-referencing roles:
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

:::{tip}
Sphinx cross-references are much more powerful and friendly with people reading raw docs than
html links. You should probably not use html links unless you have a good reason to do so (i.e. a
single external link),
and you definitely should always use sphinx cross-references for internal links.

For more on sphinx cross-references go to {ref}`cross_referencing` page.
:::

**Resources**
* {doc}`Sphinx docs on roles <usage/restructuredtext/roles>`
* [readthedocs page on cross-referencing with sphinx](https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html)
