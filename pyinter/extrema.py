class _Indeterminate(object):

    # required for comparisons with dates, times, datetimes
    # https://docs.python.org/2/library/datetime.html#date-objects
    timetuple = tuple()

    def __eq__(self, other):
        return self is other

    def __hash__(self):
        return hash(repr(self))


class _NegativeInfinity(_Indeterminate):
    def __lt__(self, other):
        if self == other:
            return False
        return True

    def __le__(self, other):
        return True

    def __gt__(self, other):
        return False

    def __ge__(self, other):
        if self == other:
            return True
        return False

    def __repr__(self):
        return '-inf'


class _Infinity(_Indeterminate):
    def __lt__(self, other):
        return False

    def __le__(self, other):
        if self == other:
            return True
        return False

    def __gt__(self, other):
        if other == self:
            return False
        return True

    def __ge__(self, other):
        return True

    def __repr__(self):
        return 'inf'


INFINITY = _Infinity()
NEGATIVE_INFINITY = _NegativeInfinity()
