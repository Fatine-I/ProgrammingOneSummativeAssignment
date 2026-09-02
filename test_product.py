import unittest
from decimal import Decimal
from product import Product


class TestProduct(unittest.TestCase):

    # ---- NORMAL / VALID CASES ----
    def test_valid_product_creation(self):
        p = Product("P001", "Coca-Cola 2L", "25.50", brand="Coca-Cola")
        self.assertEqual(p.product_id, "P001")
        self.assertEqual(p.price, Decimal("25.50"))


    def test_price_accepts_string_number_from_user_input(self):
        # Simulates input() always returning a string
        p = Product("P010", "Water", "1.00")
        self.assertEqual(p.price, Decimal("1.00"))

  
    def test_empty_id_rejected(self):
        with self.assertRaises(ValueError):
            Product("", "Bread", "5.00")

    def test_zero_price_rejected(self):
        with self.assertRaises(ValueError):
            Product("P002", "Bread", "0")

    def test_negative_price_rejected(self):
        with self.assertRaises(ValueError):
            Product("P003", "Bread", "-5.00")

    def test_non_numeric_price_rejected(self):
        with self.assertRaises(ValueError):
            Product("P011", "Bread", "cheap")


if __name__ == "__main__":
    unittest.main()
