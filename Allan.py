import pandas as pd

class Product:
    def __init__(self,productid,productname,brand,suplier,date):
        self.productid = productid
        self.productname = productname
        self.brand = brand
        self.suplier = suplier
        self.date = date

        product1= Product(1,"omo","washing","Kamau","20-11-2020")



class Inventory:
    def __init__(self,product):
        self.product=product


    def add_product(self):        
        pass 
    def save_to_file(self)
        pass  
    def search_product(self):        
        pass   
    def updating(self):        
        pass   
    def show_inventory(self):        
        pass 
    def filter_inventory(self):
        pass  
    def check_stock(self):        
        pass   

    def reduce_stock(self):
        pass   

class Sales:
    pass
class Finance:
    pass
class File_handler:
    pass