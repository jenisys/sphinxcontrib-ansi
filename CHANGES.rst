0.7.0 (UNRELEASED)
=====================

- Add more tests under "tests" directory.
- Add support for sphinx >= 2.0
- Add support for newer python3 versions.
- docs: Changed URLs to github repository.
- test: Fixed tests.
- test: Replace "mock" dependency with "unittest.mock".

sphinxcontrib.ansi:

- Replace "docutils.Node.traverse()" with "Nodes.findall()".
  REASON: "Nodes.travese()" is becoming deprecated.
- ANSI codes: Ignore unknown, unsupported ANSI codes.

FIXES:

- sphinxcontrib: Remove "__init__.py" for namespace support.
- sphinxcontrib.ansi: console.warn() -> console.warning()
- Issue #9: ANSI Codes in output (submitted by: robintibor)

DEVELOP:

- .envrc: Add "direnv" support to simplify workspace setup.

RELATED:

- OFFICIAL NEW REPO: https://github.com/sphinx-contrib/ansi
- https://pypi.org/project/sphinxcontrib-ansi/0.6.dev20201023/
  (tag missing; NOT REFLECTED on branch=master)

RELATED: Python packaging -- Namespace packages

* https://packaging.python.org/en/latest/guides/packaging-namespace-packages/

RELATED:

* https://direnv.net/

0.6 (Jul 8, 2011)
=================

- Added support for background colors (thanks to James Rowe)


0.5.1 (Jul 26, 2010)
====================

- Fixed wrong ordering with nested colors


0.5 (Jul 25, 2010)
==================

- Ignore colors in non-html output


0.4.1 (Jul 21, 2010)
====================

- Fixed #2:  Installation on Windows


0.4 (May 21, 2010)
==================

- Initial release
