(cross_referencing)=
# Cross-referencing in sphinx
The [page from the readthedocs team](https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html)
is an amazing resource which also covers [intersphinx](https://docs.readthedocs.io/en/stable/guides/intersphinx.html).
However, it is focused on the `ref` and `doc` roles,
and omits all roles related to code referencing which are also key
for ArviZ and PyMC docs.

All objects and modules documented with `autodoc` and `autosummary`
can be referenced with [special cross referencing roles](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#cross-referencing-python-objects).

:::{note}
:class: dropdown

This is done because `autodoc` and `autosummary`
use special [python domain directives](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-python-domain)
under the hood to generate ids and populate the cross-referencing roles
specific to code objects.

As all this is automated you don't need to learn nor worry about that unless
you wanted to document some method of function manually. i.e. to include
a private object in the docs that would otherwise be ignored by autosummary.
:::

Therefore, the syntax for cross-referencing roles is:

:::::{tab-set}
::::{tab-item} MyST
:::{list-table}
:stub-columns: 1
:widths: 1 3

* - Default text
  - `` {(domain:)type_id}`(intersphinx_key:)reference_id` ``
* - Custom Text
  - `` {(domain:)type_id}`Custom text <(intersphinx_key:)reference_id>` ``
:::
::::
::::{tab-item} rST
:::{list-table}
:stub-columns: 1
:widths: 1 3

* - Default text
  - `` :(domain:)type_id:`(intersphinx_key:)reference_id` ``
* - Custom Text
  - `` :(domain:)type_id:`Custom text <(intersphinx_key:)reference_id>` ``
:::
::::
:::::

Where the parts `(domain:)` and `(intersphinx_key:)` are between parenthesis
to indicate they are optional, when used there should be no parenthesis.

Here are some extra notes related to cross-referencing.

* With code type references, `~` can be used before the id
  in order to show only the object name instead of the whole import path:

  :::{list-table}
  :header-rows: 1
  * - Source
    - Rendered link
  * - `` {mod}`sphinx.ext.autosummary` ``
    - {mod}`sphinx.ext.autosummary`
  * - `` {mod}`~sphinx.ext.autosummary` ``
    - {mod}`~sphinx.ext.autosummary`
  :::

* The complete type is not necessary unless there was ambiguity in the reference.
  Ambiguity in this context would mean a python and a c++ function with
  the same import path so that `` {func}`pymc.sample` `` could be either of
  them and so using `` {py:func}`pymc.sample` `` is necessary.

* If using intersphinx, all ids from all linked docs are
  available automatically. The intersphinx keys defined in the variable
  `intersphinx_mappings` in `conf.py` are again only necessary in
  the case of ambiguity. In practice this means that the intersphinx
  keys won't never be necessary for code references but are
  recommended for `ref` and `doc` type references, maybe `term`
  if multiple of the linked docs have a glossary available.

:::{tip}
Use [`sphobjinv`](https://sphobjinv.readthedocs.io/en/latest/) library to explore the available reference ids
and their types.

Note however that the types shown sometimes needs converting to the actual
role name which is generally an abbreviated version of the object type.
:::
