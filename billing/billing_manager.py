from billing.bill import Bill
class BillingManager:
    def generate_bill(self,inventory):
        bill = Bill()

        while True:
            product_id = input("Enter Product ID: ")
            if product_id == "0":
                break
            qty = int(input("Enter Quantity: "))
            product = inventory.get_product(product_id)
            if product:
                inventory.update_stock(product_id, qty)
                bill.add_item(product, qty)
            else:
                print("Product not found in inventory.")

        total = bill.calculate_total()
        print("Total Amount:",total)
        return total
