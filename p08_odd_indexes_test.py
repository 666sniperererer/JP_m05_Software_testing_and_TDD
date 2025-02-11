from p08_odd_indexes import odd_indexes
import pytest

def test_odd_indexes():
    assert odd_indexes("řetězec") == "eěe"
    assert odd_indexes("elephant") == "lpat"
    assert odd_indexes("computer") == "optr"
    assert odd_indexes(456) == "5"
    assert odd_indexes(123456789) == "2468"
    assert odd_indexes(5) == ""
    assert odd_indexes(321.45) == "2.5"