SPHINXSOURCEDIR = .
SPHINXBUILDDIR = _build
LO = en

html:
	sphinx-build "$(SPHINXSOURCEDIR)" "$(SPHINXBUILDDIR)/html/$(LO)" -b html -D language="$(LO)"

gettext:
	sphinx-build "$(SPHINXSOURCEDIR)" "_gettext" -b gettext
