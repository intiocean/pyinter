import operator
from pyinter.interval_set import IntervalSet
from .extrema import INFINITY, NEGATIVE_INFINITY


def open(lower_value, upper_value):
    """Helper function to construct an interval object with open lower and upper.

    For example:

    >>> open(100.2, 800.9)
    (100.2, 800.9)
    """
    return Interval(Interval.OPEN, lower_value, upper_value, Interval.OPEN)


def closed(lower_value, upper_value):
    """Helper function to construct an interval object with closed lower and upper.

    For example:

    >>> closed(100.2, 800.9)
    [100.2, 800.9]
    """
    return Interval(Interval.CLOSED, lower_value, upper_value, Interval.CLOSED)


def openclosed(lower_value, upper_value):
    """Helper function to construct an interval object with a open lower and closed upper.

    For example:

    >>> openclosed(100.2, 800.9)
    (100.2, 800.9]
    """
    return Interval(Interval.OPEN, lower_value, upper_value, Interval.CLOSED)


def closedopen(lower_value, upper_value):
    """Helper function to construct an interval object with a closed lower and open upper.

    For example:

    >>> closedopen(100.2, 800.9)
    [100.2, 800.9)
    """
    return Interval(Interval.CLOSED, lower_value, upper_value, Interval.OPEN)


class Interval(object):
    """An interval class with methods associated with mathematical intervals.
    This class can deal with any comparible objects.

    *Note: comparison is performed solely on the lower value*

    **Examples**
    An open interval:

    >>> Interval(Interval.OPEN, 100.2, 800.9, Interval.OPEN)
    (100.2, 800.9)

    A closed interval:

    >>> Interval(Interval.CLOSED, 100.2, 800.9, Interval.CLOSED)
    [100.2, 800.9]

    An open-closed interval:

    >>> Interval(Interval.OPEN, 100.2, 800.9, Interval.CLOSED)
    (100.2, 800.9]

    A closed-open interval:

    >>> Interval(Interval.CLOSED, 100.2, 800.9, Interval.OPEN)
    [100.2, 800.9)
    """
    OPEN = 0
    CLOSED = 1

    _lower = None
    _lower_value = None
    _upper_value = None
    _upper = None

    lower_value = property(fget=lambda self: self._lower_value, doc='This intervals lower value')
    upper_value = property(fget=lambda self: self._upper_value, doc='This intervals upper value')
    lower = property(fget=lambda self: self._lower, doc='Whether lower is Interval.OPEN or Interval.CLOSED')
    upper = property(fget=lambda self: self._upper, doc='Whether upper is Interval.OPEN or Interval.CLOSED')

    def __init__(self, lower, lower_value, upper_value, upper):
        """Create a new :class:`~pyinter.Interval` object, lower and upper should be one of
        :const:`~pyinter.Interval.OPEN` or :const:`~pyinter.Interval.CLOSED`"""
        if lower_value > upper_value:
            raise ValueError('lower_value({lower}) must be smaller than upper_value({upper})'.format(lower=lower_value,
                                                                                                     upper=upper_value))
        self._lower = lower
        self._lower_value = lower_value
        self._upper_value = upper_value
        self._upper = upper

    def copy(self):
        """Returns a new :class:`~pyinter.Interval` object with the same bounds and values."""
        return Interval(self._lower, self._lower_value, self._upper_value, self._upper)

    def replace(self, lower=None, lower_value=None, upper_value=None, upper=None):
        interval = self.copy()

        if lower is not None:
            interval._lower = lower
        if lower_value is not None:
            interval._lower_value = lower_value
        if upper_value is not None:
            interval._upper_value = upper_value
        if upper is not None:
            interval._upper = upper

        return interval

    def __repr__(self):
        lower_string = '(' if self._lower == self.OPEN else '['
        upper_string = ')' if self._upper == self.OPEN else ']'
        return '{l}{lv}, {uv}{u}'.format(l=lower_string, lv=self.lower_value, uv=self.upper_value, u=upper_string)

    def __lt__(self, other):
        if hasattr(other, 'lower_value'):
            return self.lower_value < other.lower_value
        else:
            raise NotImplementedError

    def __le__(self, other):
        if hasattr(other, 'lower_value'):
            return self.lower_value <= other.lower_value
        else:
            raise NotImplementedError

    def __eq__(self, other):
        if hasattr(other, '_lower') and hasattr(other, 'lower_value') \
                and hasattr(other, '_upper_value') and hasattr(other, '_upper'):
            return self._lower == other._lower and self.lower_value == other.lower_value \
                and self._upper_value == other._upper_value and self._upper == other._upper
        else:
            raise NotImplementedError

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if hasattr(other, 'lower_value'):
            return self.lower_value > other.lower_value
        else:
            raise NotImplementedError

    def __ge__(self, other):
        if hasattr(other, 'lower_value'):
            return self.lower_value >= other.lower_value
        else:
            raise NotImplementedError

    def __hash__(self):
        return hash(self.lower_value)

    def _contains_value(self, value):
        """Helper function for __contains__ to check a single value is contained within the interval"""
        g = operator.gt if self._lower is self.OPEN else operator.ge
        l = operator.lt if self._upper is self.OPEN else operator.le
        return g(value, self.lower_value) and l(value, self._upper_value)

    def __contains__(self, item):
        if isinstance(item, Interval):
            lower_in = False
            upper_in = False
            if self._contains_value(item._lower_value):
                lower_in = True
            elif self._lower == item._lower and self._lower_value == item._lower_value:
                lower_in = True
            if self._contains_value(item._upper_value):
                upper_in = True
            elif self._upper == item._upper and self._upper_value == item._upper_value:
                upper_in = True
            return lower_in and upper_in
        else:
            return self._contains_value(item)

    @classmethod
    def _opposite_boundary_type(cls, bound):
        return cls.CLOSED if bound == cls.OPEN else cls.OPEN

    def _get_new_lower_upper(self, other, operator):
        if operator == self.intersect:
            if self.lower_value == other.lower_value:
                new_lower = self._lower and other._lower
            elif self.lower_value < other.lower_value:
                new_lower = other._lower
            else:
                new_lower = self._lower

            if self._upper_value == other._upper_value:
                new_upper = self._upper and other._upper
            elif self._upper_value < other._upper_value:
                new_upper = self._upper
            else:
                new_upper = other._upper
        elif operator == self.union:
            if self.lower_value == other.lower_value:
                new_lower = self._lower or other._lower
            elif self.lower_value < other.lower_value:
                new_lower = self._lower
            else:
                new_lower = other._lower

            if self._upper_value == other._upper_value:
                new_upper = self._upper or other._upper
            elif self._upper_value < other._upper_value:
                new_upper = other._upper
            else:
                new_upper = self._upper
        return new_lower, new_upper

    def empty(self):
        return (self._lower_value >= self._upper_value and
               (self._lower == self.OPEN or self._upper == self.OPEN))

    def overlaps(self, other):
        """If self and other have any overlapping values returns True, otherwise returns False"""
        if self > other:
            smaller, larger = other, self
        else:
            smaller, larger = self, other
        if larger.empty():
            return False
        if smaller._upper_value == larger._lower_value:
            return smaller._upper == smaller.CLOSED and larger._lower == smaller.CLOSED
        return larger._lower_value < smaller._upper_value

    def intersect(self, other):
        """Returns a new :class:`~pyinter.Interval` representing the intersection of this :class:`~pyinter.Interval`
        with the other :class:`~pyinter.Interval`"""
        if self.overlaps(other):
            newlower_value = max(self.lower_value, other.lower_value)
            new_upper_value = min(self._upper_value, other._upper_value)
            new_lower, new_upper = self._get_new_lower_upper(other, self.intersect)
            return Interval(new_lower, newlower_value, new_upper_value, new_upper)
        else:
            return None

    __and__ = intersect

    def union(self, other):
        """Returns a new Interval or an :class:`~pyinter.IntervalSet` representing the union of this
        :class:`~pyinter.Interval` with the other :class:`~pyinter.Interval`.

        If the two intervals are overlaping then this will return an :class:`~pyinter.Interval`,
        otherwise this returns an :class:`~pyinter.IntervalSet`."""
        if self.overlaps(other):
            newlower_value = min(self.lower_value, other.lower_value)
            new_upper_value = max(self._upper_value, other._upper_value)
            new_lower, new_upper = self._get_new_lower_upper(other, self.union)
            return Interval(new_lower, newlower_value, new_upper_value, new_upper)
        else:
            return IntervalSet((self, other))

    __or__ = __add__ = union

    def difference(self, other):
        """Returns a new Interval or an :class:`~pyinter.IntervalSet` representing the subtraction of this
        :class:`~pyinter.Interval` with the other :class:`~pyinter.Interval`.

        The result will contain everything that is contained by the left interval but not contained
        by the second interval.

        If the `other` interval is enclosed in this one then this will return a
        :class:`~pyinter.IntervalSet`, otherwise this returns a :class:`~pyinter.Interval`.
        """
        if other.empty():
            return self
        if self in other:
            return open(self._lower_value, self._lower_value)
        if self._lower == other._lower and self._lower_value == other._lower_value:
            return Interval(self._opposite_boundary_type(other._upper), other._upper_value, self._upper_value, self._upper)
        if self._upper == other._upper and self._upper_value == other._upper_value:
            return Interval(self._lower, self._lower_value, other._lower_value, self._opposite_boundary_type(other._lower))
        if other in self:
            return IntervalSet([
                Interval(self._lower, self._lower_value, other.lower_value, self._opposite_boundary_type(other._lower)),
                Interval(self._opposite_boundary_type(other._upper), other._upper_value, self.upper_value, self._upper),
            ])
        if other.lower_value in self:
            return Interval(self._lower, self._lower_value, other._lower_value, self._opposite_boundary_type(other._lower))
        if other.upper_value in self:
            return Interval(self._opposite_boundary_type(other._upper), other._upper_value, self._upper_value, self._upper)
        return Interval(self._lower, self._lower_value, self._upper_value, self._upper)

    def complement(self):
        return IntervalSet([
            Interval(self.OPEN, NEGATIVE_INFINITY, self.lower_value, self._opposite_boundary_type(self._upper)),
            Interval(self._opposite_boundary_type(self._lower), self.upper_value, INFINITY, self.OPEN),
        ])

    __sub__ = difference
