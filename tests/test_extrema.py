import sys
from pyinter.extrema import INFINITY, NEGATIVE_INFINITY
import datetime


def test_inf_is_greater_than_one():
    assert INFINITY > 1
    assert 1 < INFINITY


def test_inf_is_greater_than_datetime_now():
    assert INFINITY > datetime.datetime.now()
    assert datetime.datetime.now() < INFINITY


def test_inf_is_greater_than_date_now():
    assert INFINITY > datetime.date.today()
    assert datetime.date.today() < INFINITY


def test_inf_is_greater_than_max_int():
    assert INFINITY > sys.maxint
    assert sys.maxint < INFINITY


def test_neg_inf_is_smaller_than_one():
    assert NEGATIVE_INFINITY < 1
    assert 1 > NEGATIVE_INFINITY


def test_neg_inf_is_smaller_than_datetime_now():
    assert NEGATIVE_INFINITY < datetime.datetime.now()
    assert datetime.datetime.now() > NEGATIVE_INFINITY


def test_neg_inf_is_smaller_than_date_now():
    assert NEGATIVE_INFINITY < datetime.date.today()
    assert datetime.date.today() > NEGATIVE_INFINITY


def test_neg_inf_is_smaller_than_max_int():
    assert NEGATIVE_INFINITY < sys.maxint
    assert sys.maxint > NEGATIVE_INFINITY
