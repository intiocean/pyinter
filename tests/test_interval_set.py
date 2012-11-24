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


def test_intersection():
    pass


def test_union():
    pass