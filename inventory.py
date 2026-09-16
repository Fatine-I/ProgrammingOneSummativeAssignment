import product as pc

class Inventory:
   
    def __init__(self,low_stock_limit=5):
        self.products = {}
        self.low_stock_limit = pc.Product.validate_quantity(low_stock_limit) 

    def add_product(self,product):
        """ Adds one one product object to the inventory """
        if not isinstance(product, pc.Product):
            raise TypeError("Inventory can only store product objects.")
        if product.product_id in self.products:
            raise ValueError(f"Product ID {product.product_id} already exists.")
        self.products[product.product_id] = product
        return product     
    
    def find_product(self,product_id):
        """ return a product object if it exist or none if it not existing"""
        return self.products.get(str(product_id).strip().upper())

    def get_all_products(self):
        return sorted( self.products.values(), key= lambda product:product.product_id)

    def check_stock(self,product_id, quantity):
        """ returns a product object"""
        product = self.find_product(product_id)
        if product is None:
            return False
        try:
            quantity =pc.Product._validate_quantity(quantity)
        except (ValueError,TypeError):
            return False
        return quantity > 0 and product.quantity >= quantity

    def reduce_stock(self,product_id,quantity):
        product = self._require_product(product_id)
        if not self.check_stock(product_id,quantity):
            raise ValueError("insufficient stock available")
        product.quantity -= pc.Product._validate_quantity(quantity)
        return product
       
    def update_product(self,product_id, changes):
        product = self._require_product(product_id)
        allowed_fields = {
            "product_name",
            "price",
            "category",
            "brand",
            "size",
            "supplier",
            "expiry_date",
        }
        unknown_fields = set(changes) - allowed_fields
        if unknown_fields:
            raise ValueError(f"cannot update: {', '.join(sorted(unknown_fields))}")
        
        values = {
            "product_id": product.product_id,
            "product_name": product.product_name,
            "price": product.price,
            "quantity": product.quantity,
            "category": product.category,
            "brand": product.brand,
            "size": product.size,
            "supplier": product.supplier,
            "entry_date": product.entry_date,
            "expiry_date": product.expiry_date,
        }
        values.update(changes)
        update_product = pc.Product(**values)
        self.products[product.product_id] = update_product
        return update_product

    def update_quantity(self, product_id, new_quantity):
        product = self._require_product(product_id)
        product.quantity = pc.Product._validate_quantity(new_quantity) 
        return product
  
    def get_low_stock_products(self):
        return [
            product
            for product in self.get_all_products()
            if product.quantity <= self.low_stock_limit
        ]

    def filter_by_category(self,category):
        category =str(category).strip().lower()
        return [
            product
            for product in self.get_all_products()
            if product.category.lower() == category
        ]

    def search_products(self,search_word):
        search_word = str(search_word).strip().lower()
        if not search_word:
            return []  
              
        matches = [] 
        for product in self.products.values():
           searchable_values =(
               product.product_id,
               product.product_name,
               product.category,
               product.brand,
               product.supplier
           )
           if any(search_word in value.lower() for value in searchable_values):
               matches.append(product)
        return sorted(matches, key = lambda product: product.product_id)

    def delete_product(self,product_id):
        product = self._require_product(product_id)
        del self.products[product.product_id]        
        return product

    def _require_product(self,product_id):
        product = self.find_product(product_id)
        if product is None:
            raise ValueError( "Product not found")
        return product

    def __len__(self):
        return len(self.products)
    









        

              
        
