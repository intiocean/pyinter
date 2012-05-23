from pyinter import interval as i


def test_open_interval_construction():
    expected_lower = i.Interval.OPEN
    expected_lower_value = 10
    expected_upper_value = 100
    expected_upper = i.Interval.OPEN
    result = i.Interval(i.Interval.OPEN, 10, 100, i.Interval.OPEN)
    assert result._lower == expected_lower
    assert result._lower_value == expected_lower_value
    assert result._upper_value == expected_upper_value
    assert result._upper == expected_upper


def test_closed_interval_construction():
    expected_lower = i.Interval.CLOSED
    expected_lower_value = 10
    expected_upper_value = 100
    expected_upper = i.Interval.CLOSED
    result = i.Interval(i.Interval.CLOSED, 10, 100, i.Interval.CLOSED)
    assert result._lower == expected_lower
    assert result._lower_value == expected_lower_value
    assert result._upper_value == expected_upper_value
    assert result._upper == expected_upper


def test_openclosed_interval_construction():
    expected_lower = i.Interval.OPEN
    expected_lower_value = 10
    expected_upper_value = 100
    expected_upper = i.Interval.CLOSED
    result = i.Interval(i.Interval.OPEN, 10, 100, i.Interval.CLOSED)
    assert result._lower == expected_lower
    assert result._lower_value == expected_lower_value
    assert result._upper_value == expected_upper_value
    assert result._upper == expected_upper


def test_closedopen_interval_construction():
    expected_lower = i.Interval.CLOSED
    expected_lower_value = 10
    expected_upper_value = 100
    expected_upper = i.Interval.OPEN
    result = i.Interval(i.Interval.CLOSED, 10, 100, i.Interval.OPEN)
    assert result._lower == expected_lower
    assert result._lower_value == expected_lower_value
    assert result._upper_value == expected_upper_value
    assert result._upper == expected_upper


def test_open_interval_construction_using_helper():
    expected_lower = i.Interval.OPEN
    expected_lower_value = 10
    expected_upper_value = 100
    expected_upper = i.Interval.OPEN
    result = i.open(10, 100)
    assert result._lower == expected_lower
    assert result._lower_value == expected_lower_value
    assert result._upper_value == expected_upper_value
    assert result._upper == expected_upper

    
def test_closed_interval_construction_using_helper():
    expected_lower = i.Interval.CLOSED
    expected_lower_value = 10
    expected_upper_value = 100
    expected_upper = i.Interval.CLOSED
    result = i.closed(10, 100)
    assert result._lower == expected_lower
    assert result._lower_value == expected_lower_value
    assert result._upper_value == expected_upper_value
    assert result._upper == expected_upper
    
def test_openclosed_interval_construction_using_helper():
    expected_lower = i.Interval.OPEN
    expected_lower_value = 10
    expected_upper_value = 100
    expected_upper = i.Interval.CLOSED
    result = i.openclosed(10, 100)
    assert result._lower == expected_lower
    assert result._lower_value == expected_lower_value
    assert result._upper_value == expected_upper_value
    assert result._upper == expected_upper


def test_closedopen_interval_construction_using_helper():
    expected_lower = i.Interval.CLOSED
    expected_lower_value = 10
    expected_upper_value = 100
    expected_upper = i.Interval.OPEN
    result = i.closedopen(10, 100)
    assert result._lower == expected_lower
    assert result._lower_value == expected_lower_value
    assert result._upper_value == expected_upper_value
    assert result._upper == expected_upper
