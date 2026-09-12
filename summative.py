class Product:
    def __init__(self,product_id,name, category, price, quantity, size_value, size_unit, brand, supplier, entry_date, expiration_date):
        if price<=0:
            raise ValueError ("Price must be greater than 0")
        if quantity<0:
            raise ValueError ("Quantity cant be a negative number")
        if not isinstance (product_id, str):
            raise TypeError ("Product Id should be in text format")
        if product_id.strip()== "":
            raise ValueError ("Product Id cant be empty")
        if not isinstance (name, str):
            raise TypeError ("Product name should be in text format")
        if name.strip()== "":
            raise ValueError ("Product name cant be empty")
        if size_value<=0:
            raise ValueError ("Product size value should be a number greater than 0")
        self.product_id= product_id
        self.name= name
        self.category= category
        self.price= price
        self.quantity=quantity
        self.size_value= size_value
        self.size_unit= size_unit
        self.brand= brand
        self.supplier= supplier
        self.entry_date= entry_date
        self.expiration_date= expiration_date

    def increase_stock(self,amount):
        if amount<=0:
            raise ValueError ("Stock increase must be greater than 0")
        self.quantity+=amount
    def reduce_stock(self,amount):
        if amount<=0:
                raise ValueError ("Stock decrease must be greater than 0")
        if amount>self.quantity:
            raise ValueError ("Stock is insufficient")
        self.quantity-=amount

        
           
drink= Product("p001","cocacola","Food and beverage", 50, 50, 2, "L", "coca", "allan", "2/3/2026", "4/7/2026")
drink.increase_stock(50) 
drink.reduce_stock(23456) 
print(drink.name)
print(drink.price)
print(drink.category)
print(drink.entry_date)
print(drink.quantity)
