import functools


class IntervalSet(object):
    """A class to hold collections of intervals, otherwise known as discontinuous ranges"""

    _data = set()

    def __init__(self, iterable=None):
        """Create an interval set.
        :param iterable: An optional iterable of Interval objects to initialise the IntervalSet with.
        """
        self._data = set()
        if iterable is not None:
            for el in iterable:
                self.add(el)

    def __repr__(self):
        return '{clazz}{elements}'.format(clazz=self.__class__.__name__, elements=tuple(sorted(self._data)))

    def __eq__(self, other):
        if hasattr(other, '_data'):
            return self._data == other._data
        else:
            raise NotImplementedError  # This will allow other a chance to check for equality

    def __contains__(self, item):
        for interval in self._data:
            if item in interval:
                return True
        return False

    def __iter__(self):
        return self._data.__iter__()

    def _add(self, other):
        """Add a interval to the underlying IntervalSet data store. This does not perform any tests as we assume that
        any requirements have already been checked and that this function is being called by an internal function such
        as union(), intersection() or add().
        :param other: An Interval to add to this one
        """
        if len([interval for interval in self if other in interval]) > 0:  # if other is already represented
            return
        # remove any intervals which are fully represented by the interval we are adding
        to_remove = [interval for interval in self if interval in other]
        self._data.difference_update(to_remove)
        self._data.add(other)

    def __len__(self):
        """Return the length of this object"""
        return self._data.__len__()

    def intersection(self, other):
        """Returns a new IntervalSet which represents the intersection of each of the intervals in this IntervalSet
        with each of the intervals in the other IntervalSet.
        :param other: An IntervalSet to intersect with this one.
        """
        # if self or other is empty the intersection will be empty
        result = IntervalSet()
        for other_inter in other:
            for interval in self:
                this_intervals_intersection = other_inter.intersect(interval)
                if this_intervals_intersection is not None:
                    result._add(this_intervals_intersection)
        return result

    __and__ = intersection

    def union(self, other):
        """Returns a new IntervalSet which represents the union of each of the intervals in this IntervalSet with each
        of the intervals in the other IntervalSet
        :param other: An IntervalSet to union with this one.
        """
        result = IntervalSet()
        for el in self:
            result.add(el)
        for el in other:
            result.add(el)
        return result

    __or__ = __add__ = union


    def add(self, other):
        """
        Add an Interval to the IntervalSet by taking the union of the given Interval object with the existing
        Interval objects in self.

        This has no effect if the Interval is already represented.
        :param other: an Interval to add to this IntervalSet.
        """
        if other.empty():
            return

        to_add = set()
        for inter in self:
            if inter.overlaps(other):  # if it overlaps with this interval then the union will be a single interval
                to_add.add(inter.union(other))
        if len(to_add) == 0:  # other must not overlap with any interval in self (self could be empty!)
            to_add.add(other)
        # Now add the intervals found to self
        if len(to_add) > 1:
            set_to_add = IntervalSet(to_add)  # creating an interval set unions any overlapping intervals
            for el in set_to_add:
                self._add(el)
        elif len(to_add) == 1:
            self._add(to_add.pop())
    
    def empty(self):
        return not self._data

    def difference(self, other):
        """
        Subtract an Interval or IntervalSet from the intervals in the set.
        """
        intervals = other if isinstance(other, IntervalSet) else IntervalSet((other,))
        result = IntervalSet()
        for left in self:
            for right in intervals:
                left = left - right
            if isinstance(left, IntervalSet):
                for interval in left:
                    result.add(interval)
            else:
                result.add(left)
        return result

    __sub__ = difference

    def complement(self):
        intersection = lambda a, b: a.intersection(b)
        return functools.reduce(intersection, [interval.complement() for interval in list(self)])
