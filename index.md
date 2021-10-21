# Sphinx primer for ArviZ and PyMC contributors

:::{figure-md}

![sphinx logo](img/sphinx.png)

Sphinx is a documentation generator.
:::

Sphinx takes raw text content written with a markup language,
and it translates and renders it in an rich output format such as html or pdf.

The native markup language in Sphinx is rST, however, it is also possible
to use MyST, a superset of markdown thanks to the executablebooks project.

{numref}`sphinx-diagram` outlines the process by which sphinx generates documentation.
Don't worry if things don't make much sense yet. The key concept will be explained
as they are needed and references to further reading will also be provided in the
coming pages.

:::{graphviz}
:name: sphinx-diagram
:caption: Documentation generation process with Sphinx.
:alt: How Sphinx Render the Final HTML output from raw text
:align: center

digraph "sphinx-ext-graphviz" {
  size="6,4";
  rankdir="LR";
  graph [fontname="Verdana", fontsize="12"];
  node [fontname="Verdana", fontsize="12"];
  edge [fontname="Sans", fontsize="9"];

  sphinx [label="Sphinx", shape="component",
    href="https://www.sphinx-doc.org/"];
  ext [label="Extensions", shape="component"];
  rst [label="Docs (.rst)", shape="folder",
    href="https://docutils.sourceforge.io/docs/user/rst/quickref.html",
    fillcolor=green, style=filled];
  myst [label="Docs (.md or .ipynb)", shape="folder",
    href="https://docutils.sourceforge.io/docs/user/rst/quickref.html",
    fillcolor=orange, style=filled];
  conf [label="conf.py", shape="note",
    href="https://www.sphinx-doc.org/en/master/usage/configuration.html",
    color=blue, style=bold];
  html_files [label="HTML Files", shape="tab",
    href="https://docs.pymc.io/en/latest/",
    fillcolor=yellow, style=filled];

  rst -> sphinx [label=" parse "];
  myst -> sphinx [label=" parse (via MyST) "];
  conf -> sphinx [xlabel=" configure ", style=dashed];
  sphinx -> ext [label=" call ", style=dashed, arrowhead=none];
  sphinx -> html_files [label=" render "];
  ext -> html_files [style=dashed, label=" render "];
}
:::

ArviZ and PyMC use both rST and MyST, which can be combined without problem
within the same documentation, but the bulk of the content is written in MyST,
with rST being used nearly exclusively for docstrings.

Why MyST? MyST is a markdown superset, therefore pure markdown is also valid MyST.
Markdown is the most common markup language nowadays and both developers and users
of ArviZ and PyMC are familiar with it from sites like GitHub or Discourse.
Moreover, markdown is the markup language used in Jupyter notebooks.
Using MyST also allows us to work indistinctively in `.md` or `.ipynb` files.


:::{toctree}
:hidden:

goals
Sphinx core <core/markup>
extensions/index
themes
beyond/index
:::

