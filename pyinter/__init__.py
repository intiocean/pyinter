'''
Pyinter is a python interval library which deals with interval arithmetic and sets of intervals (discontinuous ranges).
'''

from pyinter.interval import Interval, open, closed, openclosed, closedopen
from pyinter.interval_set import IntervalSet
from pyinter import examples

__all__ = ['Interval', 'open', 'closed', 'openclosed', 'closedopen', 'IntervalSet', 'examples']
