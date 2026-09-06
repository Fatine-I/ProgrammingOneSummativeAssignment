import pandas as pd

# products= []
# while True:
#     product = input("Enter Product 1")
#     if product == "":
#         break
    
#     products.append(product)

# print(products)
# p1= pd.Series(products)
# print(p1.describe)
import product_class as pc







class Inventory:
    def __init__(self):
        self.products= []


    def add_product(self):
        while True:
            product = input("Enter Product 1")
            if product == "":
                break
            product_sub_list = product.split(",")
            product_id, product_name, price = product_sub_list

            new_product =pc.Product(product_id,product_name,price)
            self.products.append(new_product)

    def show_product(self):
        print(f"{self.products}")


inventory = Inventory()
inventory.add_product()
inventory.show_product()


   
            