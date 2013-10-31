Pyinter
=======

.. image:: https://badge.fury.io/py/pyinter.png
         :target: http://badge.fury.io/py/pyinter

.. image:: https://pypip.in/d/pyinter/badge.png
         :target: https://crate.io/packages/pyinter

.. image:: https://travis-ci.org/intiocean/pyinter.png?branch=master
         :target: https://travis-ci.org/intiocean/pyinter

.. image:: https://coveralls.io/repos/intiocean/pyinter/badge.png?branch=master
         :target: https://coveralls.io/r/intiocean/pyinter?branch=master

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
