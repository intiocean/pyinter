from datetime import timedelta
from pyinter import Interval


def daterange(start, end, delta=timedelta(days=1), lower=Interval.CLOSED, upper=Interval.OPEN):
    """Returns a generator which creates the next value in the range on demand"""
    date_interval = Interval(lower=lower, lower_value=start, upper_value=end, upper=upper)
    current = start if start in date_interval else start + delta
    while current in date_interval:
        yield current
        current = current + delta

# TODO: extra functionality to add
# - specify the number of values instead of an end date?
