.. :changelog:

Release History
---------------
1.1.5 (2013-12-13)
++++++++++++++++++
- Fix the `__all__` list so that you can `from pyinter import *`.
- Change classes to new style classes (inheriting from object)
- Added an `add()` function to the `IntervalSet` class. This will add (union) an Interval inplace. (similarly to `set().add()`)
- The optional iterable of Interval objects passed when initialising an `IntervalSet` is now added Interval by Interval so that initialising with overlapping intervals works as expected.

0.1.4 (2013-11-16)
++++++++++++++++++
- Fix formatting in HISTORY.rst which was stopping the pypi page rendering it.

0.1.3 (2013-11-16)
++++++++++++++++++
- Removed \*.md from the MANIFEST file as it warns when installing that no files matching \*.md are found.
- Fix allowing an IntervalSet to be initialised with a generator.

0.1.2 (2013-10-12)
++++++++++++++++++
- Fixed the rendering of the README on pypi (hopefully!) by converting it from a .md file to a .rst file.

0.1.1 (2013-10-09)
++++++++++++++++++
- Adding Manifest file to fix the pypi release. This was broken because the README.md was not being included in the source distribution but setup.py had a reference to this file and therefore failed to run.

0.1.0 (2013-07-03)
++++++++++++++++++
- Initial release
