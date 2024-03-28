import pytest
from src.tests.test1.test1n1 import Product, Cart, Shop


@pytest.fixture
def sample_products():
    product1 = Product("Apple", 1.0, 4.5, 5)
    product2 = Product("Banana", 0.5, 4.0, 10)
    product3 = Product("Orange", 1.2, 4.2, 3)
    return product1, product2, product3


@pytest.fixture
def sample_cart(sample_products):
    cart = Cart()
    cart.add_product(sample_products[0])
    cart.add_product(sample_products[1])
    cart.add_product(sample_products[2])
    return cart


@pytest.fixture
def sample_shop(sample_cart):
    return Shop(sample_cart)


def test_add_product(sample_cart):
    product4 = Product("Apple", 1.0, 4.5, 3)
    sample_cart.add_product(product4)
    assert sample_cart.products[0].quantity == 8


def test_delete_product(sample_cart):
    product_to_delete = sample_cart.products[0]
    sample_cart.delete_product(product_to_delete)
    assert sample_cart.products[0].quantity == 0


def test_get_expensive(sample_shop):
    assert sample_shop.get_expensive().name == "Orange"


def test_get_cheap(sample_shop):
    assert sample_shop.get_cheap().name == "Banana"


def test_get_best(sample_shop):
    assert sample_shop.get_best().name == "Apple"


def test_get_worst(sample_shop):
    assert sample_shop.get_worst().name == "Banana"


def test_buy(sample_shop, sample_cart):
    sample_shop.buy(sample_cart)
    assert sample_shop.assortment.cost == 0.0
