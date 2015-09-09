from datetime import datetime
import pytest
from pyinter import interval as i
from pyinter import IntervalSet


def test_interval_copy():
    assert i.open(1, 4).copy() == i.open(1, 4)
    assert i.openclosed(1, 4).copy() == i.openclosed(1, 4)
    assert i.closedopen(1, 4).copy() == i.closedopen(1, 4)
    assert i.closed(1, 4).copy() == i.closed(1, 4)


def test_interval_copy_returns_a_new_instance():
    one = i.open(1, 4)
    assert one is one
    assert one is not one.copy()


def test_replace():
    assert i.open(1, 4).replace(upper_value=5) == i.open(1, 5)
    assert i.open(1, 4).replace(upper=i.Interval.CLOSED) == i.openclosed(1, 4)
    assert i.open(1, 4).replace(lower=i.Interval.CLOSED) == i.closedopen(1, 4)
    assert i.open(1, 4).replace(lower_value=0) == i.open(0, 4)


def test_overlaps():
    assert i.open(1, 4).overlaps(i.open(3, 6))
    assert i.open(3, 6).overlaps(i.open(1, 4))
    assert i.openclosed(1, 4).overlaps(i.open(3, 6))


def test_overlaps_touching():
    assert not i.openclosed(1, 4).overlaps(i.openclosed(4, 5))
    assert not i.closedopen(1, 4).overlaps(i.closedopen(4, 5))
    assert not i.open(1, 4).overlaps(i.open(4, 5))
    assert i.closed(1, 4).overlaps(i.closed(4, 5))


def test_overlaps_empty():
    assert not i.open(0, 0).overlaps(i.closed(1, 20))
    assert not i.open(1, 1).overlaps(i.closed(1, 20))
    assert not i.open(2, 2).overlaps(i.closed(1, 20))
    assert not i.closed(1, 20).overlaps(i.open(0, 0))
    assert not i.closed(1, 20).overlaps(i.open(1, 1))
    assert not i.closed(1, 20).overlaps(i.open(2, 2))


def test_overlaps_does_not_change_intervals():
    one = i.open(3, 6)
    two = i.open(1, 4)
    assert one.overlaps(two)
    assert one == i.open(3, 6)
    assert two == i.open(1, 4)
    assert two.overlaps(one)
    assert one == i.open(3, 6)
    assert two == i.open(1, 4)


def test_intersect_overlapping():
    one = i.open(3, 6)
    two = i.open(4, 10)
    expected = i.open(4, 6)
    assert one.intersect(two) == expected
    assert two.intersect(one) == expected


def test_intersect_non_overlapping():
    one = i.open(3, 6)
    two = i.open(8, 10)
    expected = None
    assert one.intersect(two) == expected
    assert two.intersect(one) == expected


def test_intersect_identical():
    one = i.open(3, 6)
    expected = one
    assert one.intersect(one) == expected


def test_intersection_via_overloaded_and():
    one = i.open(3, 6)
    two = i.open(4, 10)
    expected = i.open(4, 6)
    assert one & two == expected
    assert two & one == expected


def test_union_overlapping():
    one = i.open(3, 6)
    two = i.open(4, 10)
    expected = i.open(3, 10)
    assert one.union(two) == expected
    assert two.union(one) == expected


def test_union_non_overlapping():
    one = i.open(3, 6)
    two = i.open(8, 10)
    expected = IntervalSet([one, two])
    assert one.union(two) == expected
    assert two.union(one) == expected


def test_union_identical():
    one = i.open(3, 6)
    expected = one
    assert one.union(one) == expected


def test_union_via_overloaded_or():
    one = i.open(3, 6)
    two = i.open(4, 10)
    expected = i.open(3, 10)
    assert one | two == expected
    assert two | one == expected


def test_union_via_overloaded_add():
    one = i.open(3, 6)
    two = i.open(4, 10)
    expected = i.open(3, 10)
    assert one + two == expected
    assert two + one == expected


def test_subtract_non_overlapping():
    left = i.open(3, 6)
    right = i.open(8, 10)
    expected = i.open(3, 6)
    assert left - right == expected


def test_subtract_overlapping():
    left = i.open(3, 6)
    right = i.open(4, 8)
    expected = i.openclosed(3, 4)
    assert left - right == expected


def test_subtract_overlapping_start():
    left = i.open(1, 10)
    right = i.open(1, 5)
    expected = i.closedopen(5, 10)
    assert left - right == expected


def test_subtract_overlapping_end():
    left = i.open(1, 10)
    right = i.open(5, 10)
    expected = i.openclosed(1, 5)
    assert left - right == expected


def test_subtract_contained():
    left = i.open(3, 6)
    right = i.open(4, 5)
    expected = IntervalSet([i.openclosed(3, 4), i.closedopen(5, 6)])
    assert left - right == expected


def test_subtract_exact_overlap():
    left = i.closed(1, 2)
    right = i.closed(1, 2)
    assert (left - right).empty()


def test_subtract_empty_types():
    left = i.closed(datetime(2015, 1, 1), datetime(2020, 1, 1))
    right = i.closed(datetime(2010, 1, 1), datetime(2100, 1, 1))
    result = left - right
    assert result.empty()
    assert isinstance(result.lower_value, datetime)
    assert isinstance(result.upper_value, datetime)


def test_subtract_almost_complete_overlap():
    left = i.closed(1, 2)
    right = i.open(1, 5)
    expected = i.closed(1, 1)
    assert left - right == expected


def test_empty():
    assert i.open(1, 1).empty()
    assert i.open(3, 3).empty()
    assert i.openclosed(3, 3).empty()
    assert i.closedopen(3, 3).empty()
    assert not i.open(3, 4).empty()
    assert not i.openclosed(3, 4).empty()


def test_subtract_empty_from_empty_is_empty():
    assert i.open(0, 0) - i.open(0, 0) == i.open(0, 0)


def test_subtract_complete_overlap_returns_an_empty_interval():
    left = i.closed(1, 2)
    right = i.closed(1, 2)
    assert (left - right).empty()


def test_complement_open():
    unit = i.open(0, 1)
    complement = unit.complement()
    (lower_interval, upper_interval) = sorted(complement)  # an IntervalSet is not sorted
    assert lower_interval == i.openclosed(i.NEGATIVE_INFINITY, 0)
    assert upper_interval == i.closedopen(1, i.INFINITY)


def test_complement_closed():
    unit = i.closed(0, 1)
    complement = unit.complement()
    (lower_interval, upper_interval) = sorted(complement)  # an IntervalSet is not sorted
    assert lower_interval == i.open(i.NEGATIVE_INFINITY, 0)
    assert upper_interval == i.open(1, i.INFINITY)


def test_complement_empty():
    empty = i.open(0, 0)
    (interval,) = empty.complement()
    assert interval == i.open(i.NEGATIVE_INFINITY, i.INFINITY)


def test_complement_whole():
    whole = i.open(i.NEGATIVE_INFINITY, i.INFINITY)
    assert whole.complement().empty()


def test_repr():
    assert repr(i.open(1, 2)) == '(1, 2)'
    assert repr(i.openclosed(1, 2)) == '(1, 2]'
    assert repr(i.closed(1, 2)) == '[1, 2]'
    assert repr(i.closedopen(1, 2)) == '[1, 2)'


def test_raises_exception_if_lower_is_larger_than_upper_value():
    with pytest.raises(ValueError):
        i.open(2, 1)
