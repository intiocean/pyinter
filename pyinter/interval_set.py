class IntervalSet:
    """A class to hold collections of intervals, otherwise known as discontinous ranges"""

    _data = set()

    def __init__(self, iterable=None):
        from .interval import Interval

        if iterable is None:
            self._data = set()
        else:
            self._data = set(iterable)

        if not all(isinstance(el, Interval) for el in self._data):
            raise TypeError('All elements must be Interval objects')

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
        as union or intersection."""
        if isinstance(other, IntervalSet):
            for interval in other:
                self._add(interval)
        else:

            if len([interval for interval in self if other in interval]) > 0:  # if other is already represented
                return
                # remove any intevals which are fully represented by the interval we are adding
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
        result = IntervalSet()
        for other_inter in other:
            for interval in self:
                this_intervals_intersection = other_inter.intersect(interval)
                if this_intervals_intersection is not None:
                    result._add(this_intervals_intersection)
        return result

    def union(self, other):
        """Returns a new IntervalSet which represents the union of each of the intervals in this IntervalSet with each
        of the intervals in the other IntervalSet
        :param other: An IntervalSet to union with this one.
        """
        result = IntervalSet()
        for other_inter in other:
            for interval in self:
                result._add(other_inter.union(interval))
        return result
