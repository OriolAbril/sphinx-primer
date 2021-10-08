# Doc generation configuration

Being Python based, the sphinx build is defined and configured by the
`conf.py` file. This file alone allows to configure the sphinx build
process by setting values to some preset variables.

It allows for example to add extensions to the build or to customize the
theme, the two concepts detailed in the upcoming pages.

As a contributor to ArviZ or PyMC, chances are you won't need
to worry about this `conf.py`.
They are already written and configure the build to suit our needs so far.
However, if you are working on theme layout or want to configure some
extensions, you'll need to edit this file.

**Resources**
* {ref}`Sphinx docs on configuration <build-config>`
