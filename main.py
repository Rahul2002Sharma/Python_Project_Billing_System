from inventory.inventory_manager import InventoryManager
from billing.billing_manager import BillingManager
from sales.sales_tracker import Sales
from inventory.product import Product
from utils.exceptions import InsufficientStockError


inventory = InventoryManager()
billing = BillingManager()
sales = Sales()

inventory.add_products(Product("101", "Laptop", 800, 10))
inventory.add_products(Product("102", "Smartphone", 500, 20))


while True:
    print("---------------------------------")
    print("Welcome to the Billing System")
    print("1. Generate Bill")
    print("2. Show Inventory")
    print("3. Show Daily Sales")
    print("4. Exit")
    choice = input("Enter your choice: ")

    try:
        if choice == '1':
            amount = billing.generate_bill(inventory)
            sales.add_sales(amount)
        elif choice == '2':
            inventory.show_inventory()
        elif choice == '3':
            sales.show_sales()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            print("------------------------------")
            print(":) :) :) :) :)  :) :) :) :) :) :) :) ")
            break
        else:
            print("Invalid choice. Please try again.")
    except InsufficientStockError as e:
        print(e)

