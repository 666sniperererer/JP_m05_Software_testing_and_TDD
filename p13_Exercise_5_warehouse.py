class Warehouse:
    def __init__(self, name, capacity=float):
        self.name = name
        self.capacity = capacity

    def add(self, Product):
        volume = Product.volume
        if self.capacity >= volume:
            self.capacity -= volume
            return self.capacity
        else:
            return -1

class Product:
    def __init__(self, name, volume):
        self.volume = volume


if __name__ == '__main__':
    sklad = Warehouse("hlavni_sklad", 53.87)
    produkt = Product("test_product", 9.94)

    print(produkt.volume)
    print(sklad.capacity)

    print(sklad.add(produkt))

    print(sklad.capacity)