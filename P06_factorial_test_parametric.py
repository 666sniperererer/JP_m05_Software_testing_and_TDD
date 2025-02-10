from p06_factorial import fact, fact_r
import pytest

@pytest.mark.parametrize(
    "number, result",
    [(0, 1), (1, 1), (2, 2), (3, 6), (5, 120), (6, 720)]
)
def test_fact_p(number, result):
    assert fact(number) == result