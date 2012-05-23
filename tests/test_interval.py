from pyinter import interval as i
from pyinter import IntervalSet


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