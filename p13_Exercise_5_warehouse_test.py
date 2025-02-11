import pytest
from p13_Exercise_5_warehouse import Warehouse, Product

@pytest.fixture
def provide_test_products():
    print("\nPřipravuji testovací produkty")
    yield  [("maly_produkt", 11.81, 95.13-11.81),
            ("stredni_produkt", 25.95, 95.13-11.81-25.95),
            ("velky_produkt", 45.13, 95.13-11.81-25.95-45.13),
            ("posledni_produkt", 15.30, -1)
            ]
    print("\nHotovo, uklízím")

def test_product_placement(provide_test_products):
    warehouse = Warehouse("test_warehouse", 95.13)
    for name, volume, result in provide_test_products:
        product = Product(name, volume)
        assert warehouse.add(product) == result
