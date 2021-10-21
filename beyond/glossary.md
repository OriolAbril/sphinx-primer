# Glossary
Glossaries allow for a page with definitions for common terms
which can then be referenced and linked from anywhere
else on the documentation, or even from external docs!

The main references on glossary usage within sphinx are:
* [Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-glossary)
* [JupyterBook documentation](https://jupyterbook.org/content/content-blocks.html#glossaries)

However, there are several extra details that are not covered
in these two docs.

* Definitions can have multiple terms assigned to them. Thus, the
  syntax below can be used within the glossary:

  ```
  name1
  name2
    Shared definition between names 1 and 2
  ```

  In such cases, both `` {term}`name1` `` and `` {term}`name2` `` can be
  used to link to the same definition. Note that the name used as id
  will be the one shown as clickable link.

  Therefore, this feature can be used for acronyms but using
  `` {term}`MCMC` `` will show as `MCMC` even if
  `Markov Chain Monte Carlo` is also a name linked to that definition.
  To have the clickable link be `Markov Chain Monte Carlo` one of
  `` {term}`Markov Chain Monte Caro` `` or
  `` {term}`Markov Chain Monte Carlo <MCMC>` `` should be used.

* Term type ids are case insensitive. Thus, following the example
  above, `` {term}`mcmc` `` is as valid as `` {term}`MCMC` ``.
