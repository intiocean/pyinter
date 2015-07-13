import pytest
from pyinter import interval as i
from pyinter import IntervalSet


def test_creation():
    one = i.open(3, 6)
    two = i.open(7, 10)
    expected_data = set([one, two])
    result = IntervalSet([one, two])
    assert result._data == expected_data


def test_equality_empty_interval_sets():
    one = IntervalSet()
    two = IntervalSet()
    assert one == two


def test_equality_of_two_equal_instances():
    one = IntervalSet([i.open(1, 10)])
    two = IntervalSet([i.open(1, 10)])
    assert one == two


def test_equality_of_not_equal():
    one = IntervalSet([i.open(1, 10)])
    two = IntervalSet([i.closed(1, 10)])
    assert one != two


def test_values_in():
    one = i.open(1, 5)
    two = i.closed(7, 10)
    ivset = IntervalSet((i.open(1, 5), i.closed(7, 10)))
    assert 1 not in ivset
    assert 1.00000001 in ivset
    assert 3 in ivset
    assert 7 in ivset
    assert 8 in ivset
    assert 10.0001 not in ivset
    assert one in ivset
    assert two in ivset


def test_intersection_of_disjoint_is_empty():
    first = IntervalSet((i.open(1, 5), i.closed(7, 10)))
    second = IntervalSet((i.open(20, 21), i.closed(22, 23)))
    expected = IntervalSet()
    result = first.intersection(second)
    assert result == expected


def test_intersection_of_overlapping():
    first = IntervalSet((i.open(1, 5), i.closed(7, 10)))
    second = IntervalSet((i.open(8, 21), i.closed(22, 23)))
    expected = IntervalSet((i.openclosed(8, 10), ))
    result = first.intersection(second)
    assert result == expected


def test_intersection_of_exactly_overlapping():
    first = IntervalSet((i.open(1, 5), i.closed(7, 10)))
    second = IntervalSet((i.open(1, 5), i.closed(7, 23)))
    expected = IntervalSet((i.open(1, 5), i.closed(7, 10)))
    result = first.intersection(second)
    assert result == expected


def test_intersection_of_almost_overlapping():
    first = IntervalSet((i.open(1, 5), i.closedopen(7, 10)))
    second = IntervalSet((i.open(1, 5), i.closed(7, 23)))
    expected = IntervalSet((i.open(1, 5), i.closedopen(7, 10)))
    result = first.intersection(second)
    assert result == expected


def test_intersection_of_equal():
    first = IntervalSet((i.open(1, 5), i.closed(7, 10)))
    result = first.intersection(first)
    assert result == first


def test_union_of_overlapping():
    first = IntervalSet((i.open(1, 5), i.closed(7, 10)))
    second = IntervalSet((i.open(8, 21), i.closed(22, 23)))
    expected = IntervalSet((i.open(1, 5), i.closedopen(7, 21), i.closed(22, 23)))
    result = first.union(second)
    assert result == expected


def test_union_of_disjoint():
    first = IntervalSet((i.open(1, 5), i.closed(7, 10)))
    second = IntervalSet((i.open(12, 21), i.closed(22, 23)))
    expected = IntervalSet((i.open(1, 5), i.closed(7, 10), i.open(12, 21), i.closed(22, 23)))
    result = first.union(second)
    assert result == expected


def test_union_of_equal():
    first = IntervalSet((i.open(1, 5), i.closed(7, 10)))
    result = first.union(first)
    assert result == first


def test_length_of_empty_is_zero():
    assert len(IntervalSet()) == 0


def test_len_works_as_expected():
    assert len(IntervalSet((i.open(1, 5), i.closed(7, 10)))) == 2


def test_length_of_unioned():
    first = IntervalSet((i.open(1, 5), i.closed(7, 10)))
    second = IntervalSet((i.open(8, 21), i.closed(22, 23)))
    # This is of length 3 as 2 of the intervals overlap and therefore join together
    assert len(first.union(second)) == 3


def test_initialising_with_generator_does_not_consume_generator_before_storing_items():
    generator = (el for el in (i.open(1, 5), i.closed(7, 10)))
    assert len(IntervalSet(generator)) == 2


def test_union_is_symmetric():  # check expected result and symmetric property
    expected = IntervalSet((i.open(1, 2), i.open(4, 7), i.open(12, 13)))
    first = IntervalSet((i.open(1, 2), i.open(4, 6)))
    second = IntervalSet((i.open(5, 7), i.open(12, 13)))
    assert first.union(second) == expected
    assert second.union(first) == expected


def test_intersection_is_symmetric():  # check expected result and symmetric property
    expected = IntervalSet((i.open(5, 6),))
    first = IntervalSet((i.open(1, 2), i.open(4, 6)))
    second = IntervalSet((i.open(5, 7), i.open(12, 13)))
    assert first.intersection(second) == expected
    assert second.intersection(first) == expected


def test_unioning_empty_interval_set_with_non_empty_has_the_correct_len():
    result = IntervalSet().union(IntervalSet((i.open(1, 2), i.open(3, 4))))
    assert len(result) == 2


def test_initialising_interval_with_overlapping_intervals_unions_them():
    expected = IntervalSet((i.open(1, 10),))
    result = IntervalSet([i.open(1, 7), i.closedopen(5, 10)])
    assert result == expected


def test_intersection_on_empty_set_works():
    expected = IntervalSet()
    result = IntervalSet().intersection(IntervalSet((i.open(1, 7),)))
    assert result == expected


def test_union_on_empty_set_works():
    expected = IntervalSet((i.open(1, 7),))
    result = IntervalSet().union(IntervalSet((i.open(1, 7),)))
    assert result == expected


def test_add_to_empty():
    expected = IntervalSet((i.open(1, 7),))
    result = IntervalSet()
    result.add(i.open(1, 7))
    assert result == expected


def test_add_overlapping_unions():
    expected = IntervalSet((i.open(1, 9),))
    result = IntervalSet((i.open(1, 7),))
    result.add(i.open(2, 9))
    assert result == expected


def test_add_overlapping_with_multiple():
    expected = IntervalSet((i.open(1, 20), i.open(30, 40)))
    result = IntervalSet((i.open(1, 7), i.open(10, 20), i.open(30, 40)))
    result.add(i.open(2, 15))
    assert result == expected


def test_add_non_overlapping_unions():
    expected = IntervalSet((i.open(1, 7), i.open(10, 20)))
    result = IntervalSet((i.open(1, 7),))
    result.add(i.open(10, 20))
    assert result == expected


def test_add_already_contained_has_no_effect():
    expected = IntervalSet((i.open(1, 7),))
    result = IntervalSet((i.open(1, 7),))
    result.add(i.open(2, 4))
    assert result == expected


def test_subtract_non_overlapping():
    left = IntervalSet((i.open(1, 4),))
    right = IntervalSet((i.open(8, 9),))
    expected = IntervalSet((i.open(1, 4),))
    assert left - right == expected


def test_subtract_overlapping():
    left = IntervalSet((i.open(1, 4), i.open(5, 10)))
    right = IntervalSet((i.open(0, 2), i.open(6, 8)))
    expected = IntervalSet((
        i.closedopen(2, 4),
        i.openclosed(5, 6),
        i.closedopen(8, 10),
    ))
    assert left - right == expected


def test_subtract_exactly_overlapping():
    left = IntervalSet((i.open(1, 4), i.open(5, 10)))
    right = IntervalSet((i.open(1, 4), i.open(5, 10)))
    expected = IntervalSet()
    assert left - right == expected


def test_subtract_a_contained_interval_from_interval_set():
    left = IntervalSet((i.open(1, 4), i.open(5, 10)))
    right = i.open(1, 4)
    expected = IntervalSet((i.open(5, 10),))
    assert left - right == expected


def test_subtract_interval_from_interval_set():
    left = IntervalSet((i.open(1, 4), i.open(5, 10)))
    right = i.open(8, 15)
    expected = IntervalSet((i.open(1, 4), i.openclosed(5, 8)))
    assert left - right == expected


def test_interval_set_with_empty_intervals_is_empty():
    res = IntervalSet((i.open(1, 1), i.open(15, 15),))
    assert res.empty()


def test_complement():
    one = i.open(3, 6)
    two = i.open(7, 10)
    intervals = IntervalSet([one, two])
    complement = intervals.complement()
    (lower, middle, upper) = sorted(complement)  # an IntervalSet is not sorted

    assert lower == i.openclosed(i.NEGATIVE_INFINITY, 3)
    assert middle == i.closed(6, 7)
    assert upper == i.closedopen(10, i.INFINITY)


def test_repr():
    interval_set = IntervalSet([i.open(3, 6), i.open(7, 10)])
    assert repr(interval_set) == 'IntervalSet((3, 6), (7, 10))'


def test_comparison_raises_not_implemented_error_if_it_cannot_compare():
    with pytest.raises(NotImplementedError):
        IntervalSet() == 1
