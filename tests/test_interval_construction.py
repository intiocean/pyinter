from pyinter import interval as i


def test_open_interval_construction():
    expected_lower = i.Interval.OPEN
    expectedlower_value = 10
    expected_upper_value = 100
    expected_upper = i.Interval.OPEN
    result = i.Interval(i.Interval.OPEN, 10, 100, i.Interval.OPEN)
    assert result.lower == expected_lower
    assert result.lower_value == expectedlower_value
    assert result.upper_value == expected_upper_value
    assert result.upper == expected_upper


def test_closed_interval_construction():
    expected_lower = i.Interval.CLOSED
    expectedlower_value = 10
    expected_upper_value = 100
    expected_upper = i.Interval.CLOSED
    result = i.Interval(i.Interval.CLOSED, 10, 100, i.Interval.CLOSED)
    assert result.lower == expected_lower
    assert result.lower_value == expectedlower_value
    assert result.upper_value == expected_upper_value
    assert result.upper == expected_upper


def test_openclosed_interval_construction():
    expected_lower = i.Interval.OPEN
    expectedlower_value = 10
    expected_upper_value = 100
    expected_upper = i.Interval.CLOSED
    result = i.Interval(i.Interval.OPEN, 10, 100, i.Interval.CLOSED)
    assert result.lower == expected_lower
    assert result.lower_value == expectedlower_value
    assert result.upper_value == expected_upper_value
    assert result.upper == expected_upper


def test_closedopen_interval_construction():
    expected_lower = i.Interval.CLOSED
    expectedlower_value = 10
    expected_upper_value = 100
    expected_upper = i.Interval.OPEN
    result = i.Interval(i.Interval.CLOSED, 10, 100, i.Interval.OPEN)
    assert result.lower == expected_lower
    assert result.lower_value == expectedlower_value
    assert result.upper_value == expected_upper_value
    assert result.upper == expected_upper


def test_open_interval_construction_using_helper():
    expected_lower = i.Interval.OPEN
    expectedlower_value = 10
    expected_upper_value = 100
    expected_upper = i.Interval.OPEN
    result = i.open(10, 100)
    assert result.lower == expected_lower
    assert result.lower_value == expectedlower_value
    assert result.upper_value == expected_upper_value
    assert result.upper == expected_upper

    
def test_closed_interval_construction_using_helper():
    expected_lower = i.Interval.CLOSED
    expectedlower_value = 10
    expected_upper_value = 100
    expected_upper = i.Interval.CLOSED
    result = i.closed(10, 100)
    assert result.lower == expected_lower
    assert result.lower_value == expectedlower_value
    assert result.upper_value == expected_upper_value
    assert result.upper == expected_upper
    
def test_openclosed_interval_construction_using_helper():
    expected_lower = i.Interval.OPEN
    expectedlower_value = 10
    expected_upper_value = 100
    expected_upper = i.Interval.CLOSED
    result = i.openclosed(10, 100)
    assert result.lower == expected_lower
    assert result.lower_value == expectedlower_value
    assert result.upper_value == expected_upper_value
    assert result.upper == expected_upper


def test_closedopen_interval_construction_using_helper():
    expected_lower = i.Interval.CLOSED
    expectedlower_value = 10
    expected_upper_value = 100
    expected_upper = i.Interval.OPEN
    result = i.closedopen(10, 100)
    assert result.lower == expected_lower
    assert result.lower_value == expectedlower_value
    assert result.upper_value == expected_upper_value
    assert result.upper == expected_upper
