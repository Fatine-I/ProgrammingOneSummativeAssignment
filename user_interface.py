from file_handling import FileHandling
from finance import Finance
from inventory import Inventory
from product import Product
from sales1 import Sales

from time import sleep

from rich import box
from rich.console import Console
from rich.markup import escape
from rich.panel import Panel
from rich.progress import Progress
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text
from rich.theme import Theme

PRIMARY = "bold bright_blue"
ACCENT = "bold #ff69b4"
SUCCESS = "bold bright_green"
WARNING = "bold yellow"
ERROR = "bold red"


class ShopApplication:
    MENU = {
        "1":"Add product", "2": "Display all products", "3": "Search products",
        "4":"Update product information", "5": "Update product quantity",
        "6":"Record a sale", "7": "Display low-stock products",
        "8":"Display sales information", "0": "Save and exit",
    }
    FIELDS = {
        "product_name": "Product name", "price": "Price", "category": "Category",
        "brand": "Brand", "size": "Size", "supplier": "Supplier",
        "expiry_date": "Expiry date DD/MM/YYYY",
    }

    def __init__(self, data_directory= "data", low_stock_limit = 5):
        self.inventory = Inventory( low_stock_limit)
        self.files = FileHandling(data_directory)
        self.sales = self.finance = None
        self.console = Console(theme=Theme({"Prompt": PRIMARY}))
        self.pending_save = set()


    def run(self):
        pass

    def ask(self):
        pass

    def table(self):
        pass

    def start_application(self):
        pass

    def save_changes(self):
        pass

    def show_menu(self):
        pass

    def add_product(self):
        pass

    def update_product(self):
        pass

    def print_products(self):
        pass

    def record_sale(self):
        pass

        


