class Category:
    _category_count = 0
    _products_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products or []
        Category._category_count += 1
        Category._products_count += len(self.products)

    def add_product(self, product):
        self.products.append(product)
        Category._products_count += 1


    @property
    def category_count(self):
        return Category._category_count

    @property
    def product_count(self):
        return Category._products_count
