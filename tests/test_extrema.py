import sys
from pyinter.extrema import INFINITY, NEGATIVE_INFINITY
import datetime


def test_inf_is_greater_than_one():
    assert INFINITY > 1
    assert 1 < INFINITY


def test_inf_is_greater_or_equal_to_one():
    assert INFINITY >= 1
    assert 1 <= INFINITY


def test_inf_is_greater_than_datetime_now():
    assert INFINITY > datetime.datetime.now()
    assert datetime.datetime.now() < INFINITY


def test_inf_is_greater_than_date_now():
    assert INFINITY > datetime.date.today()
    assert datetime.date.today() < INFINITY


def test_inf_is_greater_than_a_large_number():
    assert INFINITY > sys.maxsize
    assert sys.maxsize < INFINITY


def test_inf_is_not_greater_than_itself():
    assert not INFINITY > INFINITY


def test_neg_inf_is_smaller_than_one():
    assert NEGATIVE_INFINITY < 1
    assert 1 > NEGATIVE_INFINITY


def test_neg_inf_is_smaller_than_or_eq_to_one():
    assert NEGATIVE_INFINITY <= 1
    assert 1 >= NEGATIVE_INFINITY


def test_neg_inf_is_smaller_than_datetime_now():
    assert NEGATIVE_INFINITY < datetime.datetime.now()
    assert datetime.datetime.now() > NEGATIVE_INFINITY


def test_neg_inf_is_smaller_than_date_now():
    assert NEGATIVE_INFINITY < datetime.date.today()
    assert datetime.date.today() > NEGATIVE_INFINITY


def test_neg_inf_is_smaller_than_a_large_negative_number():
    assert NEGATIVE_INFINITY < -sys.maxsize
    assert -sys.maxsize > NEGATIVE_INFINITY


def test_neg_inf_is_not_smaller_than_itself():
    assert not NEGATIVE_INFINITY < NEGATIVE_INFINITY


def test_equal_to_selves():
    assert INFINITY == INFINITY
    assert NEGATIVE_INFINITY == NEGATIVE_INFINITY
    assert INFINITY >= INFINITY
    assert NEGATIVE_INFINITY >= NEGATIVE_INFINITY
    assert INFINITY <= INFINITY
    assert NEGATIVE_INFINITY <= NEGATIVE_INFINITY


def test_inf_and_neg_inf_have_timetuple_attributes():
    assert hasattr(INFINITY, 'timetuple')
    assert hasattr(NEGATIVE_INFINITY, 'timetuple')
