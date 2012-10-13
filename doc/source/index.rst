`Pyinter`
=========
.. automodule:: pyinter.__init__

`Interval` Class
----------------
.. class:: pyinter.Interval

   Instances of :class:`~pyinter.Interval` provide the following operations:

   .. describe:: Standard comparison operators: <=, <, ==, !=, >, >=

   Note: comparison is performed solely on the lower value of the :class:`~pyinter.Interval`.

   .. describe:: x in i

   Tests x to see if it is in the range specified by the :class:`~pyinter.Interval` i.

   .. describe:: interval | other

   Performs interval intersection just as :meth:`~Interval.intersect`

   .. automethod:: intersect

   .. describe:: interval & other

   Performs interval union just as :meth:`~Interval.union`

   .. automethod:: union


`Interval` Construction helpers
...............................
.. automodule:: pyinter.interval
   :members:
   :exclude-members: Interval

`IntervalSet` Class
-------------------
.. autoclass:: pyinter.IntervalSet
    :members:



Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
