from pyinter import interval as i
from pyinter import IntervalSet

def test_complement_open():
  unit = i.open(0,1)
  complement = unit.complement()
  intervals = list(complement)
  (first_interval, second_interval) = intervals
  assert first_interval == i.openclosed(i.NEGATIVE_INFINITY, 0)
  assert second_interval == i.closedopen(1, i.INFINITY)

def test_complement_closed():
  unit = i.closed(0,1)
  complement = unit.complement()
  intervals = list(complement)
  (first_interval, second_interval) = intervals
  assert first_interval == i.open(i.NEGATIVE_INFINITY, 0)
  assert second_interval == i.open(1, i.INFINITY)

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
