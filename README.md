## A sphinx primer for ArviZ and PyMC contributors

This repo outlines the key uses and structure of sphinx within ArviZ and
PyMC documentation. Some parts will therefore be specific to these projects,
but the bulk of the content will be applicable to any MyST first project.

The content is written in `.md` MyST files and rendered with sphinx in
order to also showcase it's capabilities and serve as example.
It does have one peculiarity with respect to most sphinx sites however,
the content is structured in small pages so that when combined with
the left/right key navigation it has the feel of a presentation.

The website is published at https://sphinx-primer.readthedocs.io/en/latest/

#### Build the webpage locally
The content is written as a sphinx website, with the key navigation controls
activated so it can be read as a presentation too. To build the page you'll
need to install the `requirements-docs.txt` and run:

    sphinx-build . _build -b html

After that, open the `_build/index.html` file with your preferred browser.
