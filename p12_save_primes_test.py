import pytest
from p12_save_primes import find_n_primes, save_primes

parameters = [
    (0, []),
    (1, [2]),
    (2, [2,3]),
    (3, [2,3,5]),
    (10,[2,3,5,7,11,13,17,19,23,29])
]

@pytest.mark.parametrize(
    "n, result",
    parameters
)
def test_find_n_primes(n, result):
    assert find_n_primes(n) == result

@pytest.fixture
def add_test_cases(tmp_path): #tmp_path je vestavěná fixtura pro vytvoření dočasné složky
    file_name = tmp_path / "test_primes.txt" #setup - tvorba souboru
    yield file_name
    if file_name.exists(): #teardown
        file_name.unlink() #smažeme soubor

def test_save_primes(add_test_cases):
    n = 5
    save_primes(n, add_test_cases)

    assert add_test_cases.exists()

    expected_primes = ["2\n", "3\n", "5\n", "7\n", "11\n",]
    with open(add_test_cases, "n") as f:
        pass
