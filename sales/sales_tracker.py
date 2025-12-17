class Sales:
    def __init__(self):
        self.daily_sales = 0

    def add_sales(self,amount):
        self.daily_sales += amount
    
    def show_sales(self):
        print(f"Total Sales for the Day: {self.daily_sales}")