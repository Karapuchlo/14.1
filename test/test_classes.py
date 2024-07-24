import pytest
from product import Product
from category import Category

@pytest.fixture
def product():
    return Product("Test Product", "This is a test product", 9.99, 20)

@pytest.fixture
def category():
    return Category("Test Category", "This is a test category")

def test_product_initialization(product):
    assert product.name == "Test Product"
    assert product.description == "This is a test product"
    assert product.price == 9.99
    assert product.quantity == 20

def test_category_initialization(category):
    assert category.name == "Test Category"
    assert category.description == "This is a test category"
    assert category.products == []
    assert category.category_count == 1
    assert category.product_count == 0

def test_add_product_to_category(category, product):
    category.add_product(product)
    assert len(category.products) == 1
    assert category.product_count == 1
