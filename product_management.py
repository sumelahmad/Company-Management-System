class Product:
    def __init__(self, product_id, name, category, price, stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

    def display_product_info(self):
        return f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock: {self.stock}"

class ProductManagement:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def update_product(self, product_id, name=None, category=None, price=None, stock=None):
        product = self.products.get(product_id)
        if product:
            if name:
                product.name = name
            if category:
                product.category = category
            if price:
                product.price = price
            if stock is not None:
                product.stock = stock

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def generate_inventory_report(self):
        for product in self.products.values():
            print(f"{product.name} - {product.stock} in stock")
