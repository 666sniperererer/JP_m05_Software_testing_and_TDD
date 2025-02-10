from p06_factorial import fact, fact_r
import pytest

def test_fact():
    assert fact(5) == 120
    assert fact(4) == 24
    assert fact(2) == 2
    assert fact(3) == 6
    assert fact(0) == 1

    with pytest.raises(ValueError):
        assert fact(-5) == 1

    with pytest.raises(ValueError):
        assert fact(5.5) == 1

    with pytest.raises(ValueError):
        assert fact("str") == 1

def test_fact_r():
    assert fact_r(5) == 120
    assert fact_r(4) == 24
    assert fact_r(2) == 2
    assert fact_r(3) == 6
    assert fact_r(0) == 1

    with pytest.raises(ValueError):
        assert fact_r(-5) == 1

    with pytest.raises(ValueError):
        assert fact_r(5.5) == 1

    with pytest.raises(ValueError):
        assert fact_r("str") == 1