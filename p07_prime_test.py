from p07_prime import is_prime
import pytest

parameters = [(5, True),
             (0, False),
             (1, False),
             (2, True),
             (997, True)]

@pytest.mark.parametrize(
    "number, result", parameters)

def test_is_prime(number, result):
    assert is_prime(number) == result

    with pytest.raises(TypeError):
        assert is_prime("2") is True
        assert is_prime(5) == True #nedostupný řádek, předchozí vyhodil chybu (sem nedojde)
