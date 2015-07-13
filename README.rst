=======
Pyinter
=======
..

    |latestversion| |downloads| |masterstatus| |mastercover| |issuecount|

..

Pyinter is a small and simple library written in Python for performing interval and discontinous range arithmetic.

.. code-block:: pycon

    >>> pyinter.openclosed(1.1, 12)
    (1.1, 12]
    >>> discontinous_range = pyinter.IntervalSet([pyinter.closedopen(5, 10), pyinter.closed(22, 23)])
    >>> discontinous_range
    IntervalSet([5, 10), [22, 23])
    >>> 7 in discontinous_range
    True
    >>> 10 in discontinous_range
    False  # This isn't in the range as it is an open interval which doesn't include its end points


Features
--------

-  interval objects which can be

   -  unioned
   -  intersected
   -  easily constructed using helper functions: *open, closed, openclosed and closedopen*

-  interval sets which can be

   -  unioned
   -  intersected


Installation
------------

To install Pyinter, simply:

.. code-block:: bash

    $ pip install pyinter

Or, if you absolutely must:

.. code-block:: bash

    $ easy_install pyinter

But I'm told you really shouldn't do that.


Documentation
-------------

Documentation is available at http://pyinter.readthedocs.org.


Contribute
----------
Contributions or suggestions for improvements are welcome.


.. |masterstatus| image:: http://img.shields.io/travis/intiocean/pyinter/master.svg?style=flat
    :target: https://travis-ci.org/intiocean/pyinter
    :alt: Release Build Status

.. |developstatus| image:: http://img.shields.io/travis/intiocean/pyinter/develop.svg?style=flat
    :target: https://travis-ci.org/intiocean/pyinter
    :alt: Development Build Status

.. |latestversion| image:: http://img.shields.io/pypi/v/pyinter.svg?style=flat
    :target: https://pypi.python.org/pypi/pyinter
    :alt: Latest Version

.. |downloads| image:: http://img.shields.io/pypi/dw/pyinter.svg?style=flat
    :target: https://pypi.python.org/pypi/pyinter
    :alt: Downloads per Week

.. |mastercover| image:: http://img.shields.io/coveralls/intiocean/pyinter/master.svg?style=flat
    :target: https://travis-ci.org/intiocean/pyinter
    :alt: Release Test Coverage

.. |developcover| image:: http://img.shields.io/coveralls/intiocean/pyinter/develop.svg?style=flat
    :target: https://travis-ci.org/intiocean/pyinter
    :alt: Development Test Coverage

.. |issuecount| image:: http://img.shields.io/github/issues/intiocean/pyinter.svg?style=flat
    :target: https://github.com/intiocean/pyinter/issues
    :alt: Github Issues
