# Sphinx primer

:::{figure-md}

![sphinx logo](sphinx.png)

Sphinx is a documentation generator.
:::

It takes raw text content written with a markup language,
and it translates and renders it in an rich output format such as html or pdf.

The native markup language in Sphinx is rST, however, it is also possible
to use MyST, a superset of markdown thanks to the executablebooks project.

ArviZ and PyMC use both rST and MyST, which can be combined without problem
within the same documentation, but the bulk of the content is written in MyST,
with rST being used nearly exclusively for docstrings.

:::{graphviz}
:name: sphinx.diagram
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
  rst [label="Docs (.rst)", shape="note",
    href="https://docutils.sourceforge.io/docs/user/rst/quickref.html",
    fillcolor=green, style=filled];
  myst [label="Docs (.md)", shape="note",
    href="https://docutils.sourceforge.io/docs/user/rst/quickref.html",
    fillcolor=orange, style=filled];
  html_files [label="HTML Files", shape="folder",
    href="https://pymc.readthedocs.io/en/latest/",
    fillcolor=yellow, style=filled];

  rst -> sphinx [label=" parse "];
  myst -> sphinx [label=" parse (via MyST) "];
  sphinx -> ext [label=" call ", style=dashed, arrowhead=none];
  sphinx -> html_files [label=" render "];
  ext -> html_files [style=dashed, label=" render "];
}
:::

Why MyST? MyST is a markdown superset, therefore pure markdown is also valid MyST.
Markdown is the most common markup language nowadays and both developers and users
of ArviZ and PyMC are familiar with it from sites like GitHub or Discourse.
Moreover, markdown is the markup language used in Jupyter notebooks.
Using MyST also allows us to work indistinctively in `.md` or `.ipynb` files.


:::{toctree}
:hidden:

goals
core/markup
extensions/index
themes
:::

