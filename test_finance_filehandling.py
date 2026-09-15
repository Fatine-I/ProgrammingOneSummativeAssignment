import unittest
import tempfile
from decimal import Decimal

import pandas as pd

from finance import Finance
from file_handling import FileHandling

class TestFinance(unittest.TestCase):
    def test_successful_payment_calculates_change(self):      #It tests that a valid customer  payment gives the correct change
        finance=Finance()                                     # creating an independent fresh finance object
        change= finance.process_payment("100.00", "150.00")   # example a customer pays 150 for 100 amount of a product

        # checking if the values returned are equal as stored by Finance
        self.assertEqual(change, Decimal("50.00"))
        self.assertEqual(finance.amount_received, Decimal("150.00"))
        self.assertEqual(finance.change, Decimal("50.00"))

    def test_insufficient_payment_raises_error(self):         #It checks whether finance rejects a payment that is below the amount to be paid
        finance= Finance()
        with self.assertRaises(ValueError):                   # if the payment is below it is rejected
            finance.process_payment("100.00", "60.00")


class TestFileHandling(unittest.TestCase):
    def test_missing_products_file_returns_empty_dictionary(self):  # This method tests that a missing products file does not crash the system
        with tempfile.TemporaryDirectory() as temp_directory:         #creating a temporary folder for the test CSV file
            file_handler= FileHandling(temp_directory)
            file_handler.prepare_directory()
            products= file_handler.load_products()
            self.assertEqual(products, {})            #It makes sure a new system with no products.csv is behaving like an empty inventory



    def test_save_and_load_income(self):      # this method tests that income data can be saved and loaded again correctly
            with tempfile.TemporaryDirectory() as temp_directory:    # it keeps test cvs files as separate from th real project data
                file_handler= FileHandling(temp_directory)
                file_handler.prepare_directory()
                       
                # An example of an income record using same columns as Finance
                income_data= pd.DataFrame([{"sale_id": "1", "amount": "100.00", "date": "2026-09-11"}])
                file_handler.save_income(income_data)
                loaded_income= file_handler.load_income()

                ## It confirms that the data read from the cvs matches the one saved
                self.assertEqual(len(loaded_income), 1)
                self.assertEqual(loaded_income.iloc[0]["sale_id"], "1")
                self.assertEqual(loaded_income.iloc[0]["amount"], "100.00")
                self.assertEqual(loaded_income.iloc[0]["date"], "2026-09-11")

if __name__=="__main__":   # runs the test
    unittest.main()            
