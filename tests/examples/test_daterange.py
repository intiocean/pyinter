from pyinter.examples import daterange
from datetime import datetime as dt, timedelta
from pyinter import Interval

def test_default_range():
    start, end = dt(2013, 1, 1), dt(2013, 1, 4)
    expected = [dt(2013, 1, 1), dt(2013, 1, 2), dt(2013, 1, 3)]
    result = list(daterange(start, end))
    assert result == expected


def test_closed_range():
    start, end = dt(2013, 1, 1), dt(2013, 1, 4)
    expected = [dt(2013, 1, 1), dt(2013, 1, 2), dt(2013, 1, 3), dt(2013, 1, 4)]
    result = list(daterange(start, end, lower=Interval.CLOSED, upper=Interval.CLOSED))
    assert result == expected


def test_every_hour():
    start, end = dt(2013, 1, 1), dt(2013, 1, 2)
    expected = [dt(2013, 1, 1, 0, 0),  dt(2013, 1, 1, 1, 0),  dt(2013, 1, 1, 2, 0),  dt(2013, 1, 1, 3, 0), 
                dt(2013, 1, 1, 4, 0),  dt(2013, 1, 1, 5, 0),  dt(2013, 1, 1, 6, 0),  dt(2013, 1, 1, 7, 0), 
                dt(2013, 1, 1, 8, 0),  dt(2013, 1, 1, 9, 0),  dt(2013, 1, 1, 10, 0),  dt(2013, 1, 1, 11, 0), 
                dt(2013, 1, 1, 12, 0),  dt(2013, 1, 1, 13, 0),  dt(2013, 1, 1, 14, 0),  dt(2013, 1, 1, 15, 0), 
                dt(2013, 1, 1, 16, 0),  dt(2013, 1, 1, 17, 0),  dt(2013, 1, 1, 18, 0),  dt(2013, 1, 1, 19, 0), 
                dt(2013, 1, 1, 20, 0),  dt(2013, 1, 1, 21, 0),  dt(2013, 1, 1, 22, 0),  dt(2013, 1, 1, 23, 0)]
    result = list(daterange(start, end, delta=timedelta(hours=1)))
    assert result == expected
