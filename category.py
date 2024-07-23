class Category:
    _total_categories = 0
    _total_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        Category._total_categories += 1

    def add_product(self, product):
        self.products.append(product)
        Category._total_products += 1

    @property
    def total_categories(self):
        return Category._total_categories

    @property
    def total_products(self):
        return Category._total_products
