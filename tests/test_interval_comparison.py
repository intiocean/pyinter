from pytest import raises
from pyinter import interval as i


def get_intervals():
    small = i.open(1, 5)
    medium = i.open(3, 10)
    large = i.open(9, 18)
    xlarge = i.open(17, 100)
    return small, medium, large, xlarge


def test_less_than():
    small, medium, large, xlarge = get_intervals()
    assert small < medium
    assert small < large
    assert small < xlarge

    assert medium < large
    assert medium < xlarge

    assert large < xlarge


def test_less_than_or_equal_to():
    small, medium, large, xlarge = get_intervals()
    assert small <= small
    assert small <= medium
    assert small <= large
    assert small <= xlarge

    assert medium <= medium
    assert medium <= large
    assert medium <= xlarge

    assert large <= large
    assert large <= xlarge
    
    assert xlarge <= xlarge


def test_greater_than():
    small, medium, large, xlarge = get_intervals()
    assert medium > small
    assert large > small
    assert xlarge> small

    assert large > medium
    assert xlarge > medium

    assert xlarge > large


def test_greater_than_or_equal_to():
    small, medium, large, xlarge = get_intervals()
    assert small >= small
    assert medium >= small
    assert large >= small
    assert xlarge>= small

    assert medium >= medium
    assert large >= medium
    assert xlarge >= medium

    assert large >= large
    assert xlarge >= large
    
    assert xlarge >= xlarge


def test_equality():
    small = get_intervals()[0]
    assert small == small
    assert small == i.open(1,5)
    assert small == i.Interval(i.Interval.OPEN, 1, 5, i.Interval.OPEN)


def test_non_equality():
    small, medium = get_intervals()[:2]
    assert small != medium
    assert small != i.openclosed(1,5)
    assert small != i.closedopen(1,5)
    assert small != i.closed(1,5)
    assert small != i.Interval(i.Interval.OPEN, 1, 7, i.Interval.OPEN)
    assert small != i.open(100, 288)


def test_eq_raises():
    one = i.open(1, 10)
    with raises(NotImplementedError):
        one == None

def test_eq_raises_swapped():
    one = i.open(1, 10)
    with raises(NotImplementedError):
        None == one


def test_not_eq_raises():
    one = i.open(1, 10)
    with raises(NotImplementedError):
        one != None


def test_lt_raises():
    one = i.open(1, 10)
    with raises(NotImplementedError):
        one < None


def test_gt_raises():
    one = i.open(1, 10)
    with raises(NotImplementedError):
        one > None


def test_ge_raises():
    one = i.open(1, 10)
    with raises(NotImplementedError):
        one >= None


def test_le_raises():
    one = i.open(1, 10)
    with raises(NotImplementedError):
        one <= None


def test_contains():
    small = i.closed(1, 5)
    medium = i.closedopen(3, 10)
    assert small.lower_value in small
    assert small._upper_value in small
    assert medium.lower_value in medium
    assert medium._upper_value not in medium


def test_contains_fully_overlapping():
    small = i.closed(7, 10)
    medium = i.closedopen(7, 21)
    assert small in medium


def test_contains_self_closed():
    small = i.closed(3, 5)
    medium = i.closedopen(3, 10)
    assert small in small
    assert small in medium
    assert medium not in small


def test_contains_self_open():
    small = i.open(1, 5)
    medium = i.open(3, 10)
    assert small in small
    assert small not in medium
    assert medium not in small
    assert medium in medium


def test_contains_self_closed_open():
    small = i.closedopen(1, 5)
    medium = i.closed(7, 10)
    assert small in small
    assert small not in medium
    assert medium not in small


def test_contains_self_open_closed():
    small = i.openclosed(1, 5)
    medium = i.openclosed(1, 10)
    assert small in small
    assert medium not in small
    assert small in medium


def test_not_contains():
    small, medium = get_intervals()[:2]
    assert small.lower_value not in small
    assert small._upper_value not in small
    assert medium.lower_value not in medium
    assert medium._upper_value not in medium


def test_overlaps_open():
    one = i.open(1, 5)
    two = i.open(3, 10)
    assert one.overlaps(two)
    assert two.overlaps(one)
    assert one.overlaps(one)
    assert two.overlaps(two)


def test_overlaps_false():
    one = i.open(1, 5)
    two = i.open(7, 12)
    assert not one.overlaps(two)
    assert not two.overlaps(one)
    assert one.overlaps(one)
    assert two.overlaps(two)


def test_overlaps_corner_case_open():
    one = i.open(1, 5)
    two = i.open(5, 10)
    assert not one.overlaps(two)
    assert not two.overlaps(one)
    assert one.overlaps(one)
    assert two.overlaps(two)


def test_overlaps_corner_case_closed():
    one = i.closed(1, 5)
    two = i.closed(5, 10)
    assert one.overlaps(two)
    assert two.overlaps(one)
    assert one.overlaps(one)
    assert two.overlaps(two)
    