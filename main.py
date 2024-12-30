import json


class Category:
    name: str
    description: str
    __products: list
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.total_categories += 1
        Category.total_unique_products += len(self.__products)

    def add_product(self, product):
        self.__products.append(product)
        Category.total_categories += 1

    @property
    def products(self):
        for i in self.__products:
            return f"{i.name}, {i.price} руб. Остаток: {i.amount_available} шт."



class Product:
    name: str
    description: str
    price: float
    amount_available: int

    def __init__(self, name, description, price, amount_available):
        self.name = name
        self.description = description
        self.price = price
        self.amount_available = amount_available

    @classmethod
    def create_product(cls, name, description, price, amount_available, products_list):
        for product in products_list:
            if product.name == name:
                product.amount_available += amount_available
                product.price = max(product.price, price)
                return product
        return cls(name, description, price, amount_available)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена введена некорректно. Новая цена не установлена.")
        elif new_price < self._price:
            confirm = input("Цена понижается. Вы уверены? (y/n): ").lower()
            if confirm == "y":
                self._price = new_price
            else:
                print("Действие отменено.")
        else:
            self._price = new_price

