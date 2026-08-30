import pandas as pd
import uuid
from datetime import datetime
from rich.console import Console

console = Console()

class Sales:
    def __init__(self, inventory, finance):
        # USES-A relationship setup
        self.inventory = inventory
        self.finance = finance
        self.sales_history = []

    def new_sale(self):
        current_sale = []
        
        while True:
            product_id = input("Enter Product ID (or 'done' to finish): ")
            if product_id.lower() == 'done':
                break
                
            # Ask Inventory if product exists
            product = self.inventory.find_product(product_id)
            if not product:
                console.print("[red]Product not found. Please try again.[/red]")
                continue
                
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    console.print("[red]Quantity must be greater than 0.[/red]")
                    continue
            except ValueError:
                console.print("[red]Invalid input. Please enter a number.[/red]")
                continue

            # Ask Inventory if stock is sufficient
            if not self.inventory.check_stock(product_id, quantity):
                console.print("[red]Insufficient stock available.[/red]")
                continue
                
            # Add valid item to cart
            current_sale.append({
                "product_id": product_id,
                "name": product.name,
                "quantity": quantity,
                "unit_price": product.price,
                "line_total": product.price * quantity
            })
            console.print("[green]Item added to cart![/green]")

        if not current_sale:
            return

        self._process_checkout(current_sale)

    def _process_checkout(self, current_sale):
        # Ask Finance to handle money logic
        total_due = self.finance.calculate_total(current_sale)
        payment_success = self.finance.process_payment(total_due)
        
        if payment_success:
            sale_id = str(uuid.uuid4())[:8]
            sale_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Record completed sale
            for item in current_sale:
                record = {
                    "Sale ID": sale_id,
                    "Date": sale_date,
                    **item
                }
                self.sales_history.append(record)
                # Tell Inventory to reduce stock ONLY after success
                self.inventory.reduce_stock(item["product_id"], item["quantity"])
                
            console.print(f"[green]Sale {sale_id} completed successfully![/green]")
        else:
            console.print("[red]Payment failed. Sale cancelled. Stock not reduced.[/red]")

    def display_history(self):
        if not self.sales_history:
            console.print("No sales history found.")
            return
            
        # Use Pandas for the reporting layer
        df = pd.DataFrame(self.sales_history)
        print(df.to_string(index=False))