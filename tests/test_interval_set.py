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
    second = IntervalSet((i.open(20,21), i.closed(22,23)))
    expected = IntervalSet()
    result = first.intersection(second)
    assert result == expected


def test_intersection_of_overlapping():
    first = IntervalSet((i.open(1, 5), i.closed(7, 10)))
    second = IntervalSet((i.open(8, 21), i.closed(22,23)))
    expected = IntervalSet((i.openclosed(8, 10), ))
    result = first.intersection(second)
    assert result == expected


def test_intersection_of_exactly_overlapping():
    first = IntervalSet((i.open(1, 5), i.closed(7, 10)))
    second = IntervalSet((i.open(1, 5), i.closed(7,23)))
    expected = IntervalSet((i.open(1, 5), i.closed(7, 10)))
    result = first.intersection(second)
    assert result == expected


def test_intersection_of_almost_overlapping():
    first = IntervalSet((i.open(1, 5), i.closedopen(7, 10)))
    second = IntervalSet((i.open(1, 5), i.closed(7,23)))
    expected = IntervalSet((i.open(1, 5), i.closedopen(7, 10)))
    result = first.intersection(second)
    assert result == expected


def test_intersection_of_equal():
    first = IntervalSet((i.open(1, 5), i.closed(7, 10)))
    result = first.intersection(first)
    assert result == first


def test_union_of_overlapping():
    first = IntervalSet((i.open(1, 5), i.closed(7, 10)))
    second = IntervalSet((i.open(8, 21), i.closed(22,23)))
    expected = IntervalSet((i.open(1, 5), i.closedopen(7, 21), i.closed(22, 23)))
    result = first.union(second)
    assert result == expected


def test_union_of_disjoint():
    first = IntervalSet((i.open(1, 5), i.closed(7, 10)))
    second = IntervalSet((i.open(12, 21), i.closed(22,23)))
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
    second = IntervalSet((i.open(8, 21), i.closed(22,23)))
    # This is of length 3 as 2 of the intervals overlap and therefore join together
    assert len(first.union(second)) == 3


def test_initialising_with_generator_does_not_consume_generator_before_storing_items():
    generator = (el for el in (i.open(1, 5), i.closed(7, 10)))
    assert len(IntervalSet(generator)) == 2