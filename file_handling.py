import pandas as pd
import os
from finance import Finance, parse_money



class Filehandling:
    """ This class uses pandas to save and load the system's csv files"""
    PRODUCT_COLUMNS = [
        "product_id", "product_name", "category","brand",  "size", "supplier",
        "price", "quantity","entry_date","expiry_date"
    ]

    def __init__(self,data_directory ="data"):
        #Relative paths always start  beside this program, not in the launch folder
        program_directory = os.path.dirname(os.path.abspath(__file__))
        self.data_directory = os.path.abspath(os.path.join(program_directory,data_directory))
        self.products_file = os.path.join(self.data_directory, "products.csv")
        self.sales_file =os.path.join(self.data_directory, "sales.csv")
        self.income_file = os.path.join(self.data_directory, "income.csv")

    def prepare_directory(self):   # called once at start ,when after, the user chooses to open the shop
        os.makedirs( self.data_directory, exist_ok=True)

    def save_changes(self,inventory, sales, finance, pending):
        #Remove a name only after that file saves succefully
        if "products" in pending:
            self.save_products(inventory.products)
            pending.remove( "products")
        if "sales" in pending:
            self.save_sales(sales.sales_df)
            pending.remove("sales")
        if "income" in pending:
            self.save_income(finance.income_df)
            pending.remove("income")

        

    def load_products(self):
        pass

    def save_products(self):
        pass


    def load_sales(self):        
        dataframe = self._read_csv(self.income_file,Finance.COLUMNS)

    def save_sales(self):
        pass

    def load_income(self):
        pass


    def save_income(self):
        pass

    @staticmethod
    def _read_csv(filename, required_columns):
        name = os.path.basename(filename)
        try:
            with open(filename, "r", encoding="utf-8-sig", newline="") as file:
                dataframe = pd.read_csv(file, dtype=str, keep_default_na=False) 
        except FileNotFoundError:
            return pd.DataFrame(columns=required_columns)

        except (pd.errors.EmptyDataError, pd.errors.ParserError, UnicodeError) as error:
            raise ValueError(f" cannot read {name}. check its csv contents; it was not changed") from error
        if set(dataframe.columns) != set(required_columns):
            raise ValueError(f"{name} must contain exactly these columns: {', '.join(required_columns)}")
        if not isinstance(dataframe.index, pd.RangeIndex) or dataframe.isna().any().any():
            raise ValueError(f"{name} contains an incomplete or incorrectly sized row.")
        return dataframe[required_columns]
        


    @staticmethod
    def _write_dataframe( filename, dataframe, columns):
        temporary = filename + ".tmp"

        with open(temporary, "w") as file :
            dataframe[columns].to_csv(file, index=False)
        os.replace(temporary,filename)



