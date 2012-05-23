class IntervalSet:
    '''A class to hold collections of intervals, otherwise known as discontinous ranges'''

    _data = set()

    def __init__(self, iterable=None):
        from .interval import Interval
        if iterable is None:
            self._data = set()
        elif all(isinstance(el, Interval) for el in iterable):
            self._data = set(iterable)
        else:
            raise TypeError('All elements must be Interval objects')

    def __repr__(self):
        return '{clazz}{elements}'.format(clazz=self.__class__.__name__, elements=tuple(sorted(self._data)))

    def __eq__(self, other):
        if hasattr(other, '_data'):
            return self._data == other._data
        else:
            raise NotImplementedError

    def __contains__(self, item):
        for interval in self._data:
            if item in interval:
                return True
        return False
    
    def __iter__():
        return self._data.__iter__()
    
    def _add(self, other):
        '''Add a interval to the underlying IntervalSet data store. This does not perform any tests as we assume that any requirements have already been checked and that this function is being called by an internal function such as union or intersection.'''
        if isinstance(other, IntervalSet):
            for interval in other:
                self._data.add(interval)
        else:
            self._data.add(interval)

    def intersection(self, other):
        '''Returns a new IntervalSet which represents the intersection of each of the intervals in this IntervalSet with each of the intervals in the other IntervalSet.
        
        Examples
        --------
        >>> abc
        '''
        result = IntervalSet()
        for other_inter in other:
            for interval in self:
                result._add(other_inter.intersect(interval))

    def union(self, other):
        '''Returns a new IntervalSet which represents the union of each of the intervals in this IntervalSet with each of the intervals in the other IntervalSet'''
        result = IntervalSet()
        for other_inter in other:
            for interval in self:
                result._add(other_inter.union(interval))