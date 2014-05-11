class _Indeterminate(object):
    def __eq__(self, other):
        return other is self

    def __hash__(self):
        return hash(repr(self))

    def timetuple(self):
        """
        In order to stop comparison from falling back to the default scheme of comparing object addresses,
        date comparison normally raises TypeError if the other comparand isn't also a date object. However,
        NotImplemented is returned instead if the other comparand has a timetuple() attribute.
        This hook gives other kinds of date objects a chance at implementing mixed-type comparison.
        """
        return tuple()


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
        return False

    def __repr__(self):
        return '-inf'


class _Infinity(_Indeterminate):
    def __lt__(self, other):
        return False

    def __le__(self, other):
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
