import json


class Category:
    name: str
    description: str
    products: list
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1
        Category.total_unique_products += len(self.products)




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


