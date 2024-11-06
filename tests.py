import pytest
from main import Category, Product
@pytest.fixture
def McDonald_category():
    return Category('Mcdonalds','Mcdonalds food', ["McFlurry", "French fries", "Hamburger"])

@pytest.fixture
def hamburger_product():
    return  Product('Hamburger','just burger', 23, 300)


def test_init_category(McDonald_category):
    assert McDonald_category.name == 'Mcdonalds'
    assert McDonald_category.description == 'Mcdonalds food'
    assert McDonald_category.products == ["McFlurry", "French fries", "Hamburger"]
    assert Category.total_categories == 1
    assert Category.total_unique_products == 3


def test_init_product(hamburger_product):

    assert hamburger_product.name == 'Hamburger'
    assert hamburger_product.description == 'just burger'
    assert hamburger_product.price == 23
    assert hamburger_product.amount_available == 300
