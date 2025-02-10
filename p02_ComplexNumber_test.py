'''
### Domácí úkol
Definujte třídu `ComplexNumber` reprezentující [komplexní číslo](https://cs.wikipedia.org/wiki/Komplexn%C3%AD_%C4%8D%C3%ADslo)
a definujte následující metody:
- [ ] `__init__` (konstruktor)
- [ ] `__eq__` (rovnost)
- [ ] `__lt__` (<)
- [ ] `__gt__` (>)
- [ ] `__repr__`
- [ ] `__str__`
- [ ] `properties` (gettery a settery)
- [ ] `add` (sčítání)
- [ ] `subtract` (odečítání)
- [ ] `multiply` (násobení)
- [ ] `divide` (dělení)
- [ ] `conjugate` (číslo komplexně sdružené)
- [ ] `absolute_value` (absolutní hodnota)
'''

import pytest
from p02_ComplexNumber import ComplexNumber


class Test:

    def setup_method(self):
        print("\nSTART\n")

    def teardown_method(self):
        print("FINISH\n")

    def test_eq(self):
        complexnumber1 = ComplexNumber(5, 3)
        complexnumber2 = ComplexNumber(7, 4)
        result = False
        assert result == (complexnumber1 == complexnumber2)

    def test_lt(self):
        pass

    def test_gt(self):
        pass

    def test_repr(self):
        pass

    def test_str(self):
        pass

    def test_add(self):
        pass

    def test_sub(self):
        pass

    def test_div(self):
        pass

    def test_con(self):
        pass

    def test_abs(self):
        pass