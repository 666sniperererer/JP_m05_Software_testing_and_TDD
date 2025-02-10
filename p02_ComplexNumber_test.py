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
        print("START")

    def teardown_method(self):
        print("FINISH")

    def test_addition(self):
        complexnumber = ComplexNumber()
        result = basic_calculator.add(3, 5)
        assert result == 8