
import product_class as pc

class Inventory:
   
    def __init__(self,low_stock_limit=5):
        self.products = {}
        self.low_stock_limit = low_stock_limit  

    def add_product(self,product):
        """ Adds one one product object to the inventory """

        if product.product_id in self.products:
            raise ValueError(f"A product with id  {product.product_id} already exist")

        self.products[product.product_id] = product
        return product

    def find_product(self,product_id):
        """ return a product object if it exist or none if it not existing"""

        return self.products.get(str(product_id).strip())

    def check_stock(self,product_id, quantity):
        """ returns a product object"""
        product = self.find_product(product_id)

        if product is None:
            return False

        try:
            quantity = int(quantity)
        except (ValueError,TypeError):
            return False

        return quantity > 0 and product.quantity >= quantity

    def reduce_stock(self,product_id,quantity_sold):  
        product = self.find_product(product_id)

        if product is None:
            raise ValueError("product not found!")

        if not self.check_stock(product_id,quantity_sold):
            raise ValueError("Insufficient stock available")

        product.quantity -=int(quantity_sold)

    def update_quantity(self, product_id, new_quantity):
        product = self.find_product(product_id)

        if product is None:
            raise ValueError("product not found!")

        try:
            new_quantity = int(new_quantity)

        except (ValueError,TypeError):
            raise ValueError("Quantity must be a whole number.")

        if new_quantity < 0 :
            raise ValueError("Quantity must be awhole number")

        product.quantity = new_quantity

    def get_low_stock_product(self):
        return [
            product
            for product in self.products.values()
            if product.quantity <= self.low_stock_limit
        ]

    def filter_by_category(self,category):
        category =str(category).strip().lower()

        return [
            product
            for product in self.products.values()
            if product.category.lower() == category
        ]

    def search_products(self,search_word):
        search_word = str(search_word).strip().lower()

        matches = []

        for product in self.products.values():
            if (
                search_word in str(product.product_id).lower()
                or search_word in product.product_name.lower()
                or search_word in product.category.lower()
                or search_word in product.brand.lower()
            ):
                matches.append(product)

        return matches

    def delete_product(self,product_id):
        product_id = str(product_id).strip()

        if product_id not in self.products:
            raise ValueError("product not found.")

        return self.products.pop(product_id)









        

              
        
