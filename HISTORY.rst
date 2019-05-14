.. :changelog:

Release History
---------------
0.2.0 (2019-05-14)
++++++++++++++++++
- Fix: The interval of 2 identical numbers equals the empty set if one of the boundaries is open #20
- Improvement: Add lower and upper properties and replace method which works similarly to date.replace #19

0.1.9 (2015-08-01)
++++++++++++++++++
- Fix empty interval types so that empty intervals could be compared with other intervals
- Add method `copy()` to create new `Interval` instances with the same bounds and values as the `Interval` being copied
- Fix method `overlaps` on `Interval` and add tests for it!

0.1.8 (2015-07-14)
++++++++++++++++++
- Fix formatting in README.rst as pypi isn't rendering it properly.

0.1.7 (2015-07-14)
++++++++++++++++++
- Fix `|` and `&` in the documentation.
- Implement subtraction of `Interval`'s and `IntervalSet`'s
- Add method `empty()` to detect empty `Interval` objects.
- Fix, each infinity should always equal itself.

0.1.6 (2014-05-11)
++++++++++++++++++
- Add a complement function
- Fix bug with using & and | for `union()` and `intersection()`
- Increase test coverage!

0.1.5 (2013-12-13)
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
