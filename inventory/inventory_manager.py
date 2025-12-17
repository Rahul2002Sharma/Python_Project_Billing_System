from inventory.product import Product
from utils.exceptions import InsufficientStockError

class InventoryManager:
    def __init__(self):
        self.products = {}

    def add_products(self,product):
        self.products[product.product_id] = product

    def get_product(self,product_id):
        return self.products.get(product_id)
    
    def update_stock(self,product_id,qty):
        product = self.get_product(product_id)
        if product.quantity < qty:
            raise InsufficientStockError(f"Insufficient stock for product ID {product_id}")
        product.quantity -= qty

    def show_inventory(self):
        for p in self.products.values():
            print(f"ID: {p.product_id}, Name: {p.name}, Price: {p.price}, Quantity: {p.quantity}")
