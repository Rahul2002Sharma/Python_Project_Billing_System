class Bill:
    tax = 0.05
    def __init__(self):
        self.items = []
    
    def add_item(self,product,qty):
        self.items.append((product,qty))
    
    def calculate_total(self):
        subtotal = sum(product.price * qty for product, qty in self.items)
        total_tax = subtotal * Bill.tax
        return subtotal + total_tax