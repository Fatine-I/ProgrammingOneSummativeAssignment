from decimal import Decimal, InvalidOperation
from datetime import datetime


class Product:
    DATE_FORMAT="%d/%m/%Y"
    def __init__(self, product_id, product_name, price, category="", brand="", size="", supplier="", entry_date=None, expiry_date=None):
        self.product_id=self._validate_id(product_id)
        self.product_name=self._validate_name(product_name, "Product name")
        self.category=category.strip() if category else ""
        self.brand=brand.strip() if brand else ""
        self.size=size.strip() if size else ""
        self.supplier=supplier.strip() if supplier else ""
        self.price=self._validate_price(price)
        self.entry_date=(self._validate_date(entry_date) if entry_date else datetime.now().strftime(self.DATE_FORMAT))
        self.expiry_date=self._validate_date(expiry_date) if expiry_date else None


    @staticmethod
    def _validate_id(product_id):
        if product_id is None or str(product_id).strip()=="":
            raise ValueError("Product ID cannot be empty.")
        return str(product_id).strip()

    @staticmethod
    def _validate_name(product_name, default_name):
        if product_name is None or str(product_name).strip()=="":
            raise ValueError(f"{default_name} cannot be empty.")
        return str(product_name).strip()

    @staticmethod
    def _validate_price(price):
        try:
            price=Decimal(str(price))
        except(InvalidOperation,ValueError,TypeError):
            raise ValueError("Price must be a valid number.")
        if price <=0:
            raise ValueError("Price must be greater than zero.")
        return price
    

    @classmethod
    def _validate_date(cls, date_str):
        try:
            datetime.strptime(date_str, cls.DATE_FORMAT)
        except (ValueError, TypeError):
            raise ValueError(f"Date must be in {cls.DATE_FORMAT} format.")
        return date_str
