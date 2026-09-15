from file_handling import FileHandling
from finance import Finance
from inventory import Inventory
from product import Product
from sales import Sales

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
        if self._ask("Types yes to open, or exit to close", choices=["yes","exit"]) == "exit":
            return

        

    def _ask(self, label, **options):  # raw funtion that Propmts the user to return trimmed input.. to be use explitly in this codes
        return Prompt.ask(f" [{PRIMARY}] {escape(label)} [/{PRIMARY}]", console= self.console, show_default=False,**options).strip()

    def _table(self,title, headings, rows, show_header=True):
        table = Table( title=title, title_style=ACCENT,box=box.ROUNDED,
                      border_style=PRIMARY, header_style=PRIMARY, show_header=show_header)
        for heading in headings:
            table.add_column(heading)
        for row in rows:
            cells = []
            for value in row:
                cells.append(value if isinstance(value,Text) else Text(str(value)))
            table.add_row(*cells)
        if table.row_count:
            self.console.print(table)
        else:
            self.console.print("No record found.", style=WARNING)

    def _start_application(self): # loads csvs into inventory ,sales and finance
        
        pass

    def _save_changes(self):
        pass

    def _show_menu(self): # shows the user MENU
        self.console.print(Panel(
            f"[cyan]PRODUCT:[/] {len(self.inventory)}  "
            f"[yellow]Low stock:[/] {len(self.inventory.get_low_stock_products())}",
            title="shop Details", title_align="Left",border_style=PRIMARY, expand=False
,        ))
        rows = [(Text(key, style=PRIMARY), label) for key,label in self.MENU.item()]
        self._table("Main Menu", ["Option", "Action"], rows, show_header=False)

    def _add_product(self):
        pass

    def _update_product(self):
        pass

    def _print_products(self, products, title):
        rows = []
        for product in products:
            status = Text("ok", style=SUCCESS)
            if products.quantity <= self.inventory.low_stock_limit:
                status =Text("LOW", style=WARNING)
            if product.quantity == 0:
                status = Text("OUT", style=ERROR)
            rows.append((
                product.product_id,
                product.product_name,
                product.category or "-",
                product.brand or "-",
                f"{product.price:.2f}",
                product.quantity, status
            ))
        self._table(title, ["ID", "Product", "Category", "Brand", "Price", "Quantity", "Status"],rows)        
                
    def _record_sale(self):
        pass

        


