import unittest
import tempfile
import os
from decimal import Decimal

import pandas as pd

from finance import Finance  # type: ignore[reportMissingImports]
from file_handling import FileHandling  # type: ignore[reportMissingImports]

class TestFinance(unittest.TestCase):
    def test_successful_payment_calculates_change(self):      #It tests that a valid customer  payment gives the correct change
        finance=Finance()                                     # creating an independent fresh finance object
        change= finance.process_payment("100.00", "150.00")   # example a customer pays 150 for 100 amount of a product

        # checking if the values returned are equal as stored by Finance
        self.assertEqual(change, Decimal("50.00"))
        self.assertEqual(finance.amount_received, Decimal("150.00"))
        self.assertEqual(finance.change, Decimal("50.00"))

    def test_exact_payment_returns_zero_change(self):         #It tests whether the customer pays the exact amount due
        finance= Finance()
        change= finance.process_payment("250.00", "250.00")

        # Exact payment should succeed and there should be no change
        self.assertEqual(change, Decimal("0.00"))
        self.assertEqual(finance.amount_received, Decimal("250.00"))
        self.assertEqual(finance.change, Decimal("0.00"))


    def test_insufficient_payment_raises_error(self):         #It checks whether finance rejects a payment that is below the amount to be paid
        finance= Finance()
        with self.assertRaises(ValueError):                   # if the payment is below it is rejected
            finance.process_payment("100.00", "60.00")

    def test_money_with_more_than_two_decimal_places_raises_error(self):   #it test any invalid money format is rejected
        finance= Finance()
        with self.assertRaises(ValueError):                   # money format such as 10.157 should not be rounded
            finance.process_payment("10.157", "435.00")

    def test_invalid_test_money_raises_error(self):          #It tests that non numeric money input is rejected
        finance= Finance()                                   # when the amount input is text instead of monetary value
        with self.assertRaises(ValueError):               
            finance.process_payment("350.50", "hello")


class TestFileHandling(unittest.TestCase):
    def test_missing_products_file_returns_empty_dictionary(self):  # This method tests that a missing products file does not crash the system
        with tempfile.TemporaryDirectory() as temp_directory:       #creating a temporary folder for the test CSV file
            file_handler= FileHandling(temp_directory)
            file_handler.prepare_directory()
            products= file_handler.load_products()
            self.assertEqual(products, {})                   #It makes sure a new system with no products.csv is behaving like an empty inventory

    def test_save_and_load_income(self):                     # this method tests that income data can be saved and loaded again correctly
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

    def test_prepare_directory_creates_folder(self):    # it tests that FileHandling creates the data folder when it does not exist
        with tempfile.TemporaryDirectory() as temp_directory:
            new_folder= os.path.join(temp_directory, "shop_data")
            file_handler= FileHandling(new_folder)
            file_handler.prepare_directory()

            # the new folder should exist after prepare_directory() is called
            self.assertTrue(os.path.isdir(file_handler.data_directory))

    def test_empty_income_file_raises_error(self):           #it tests a completely empty csv is handled correctly
        with tempfile.TemporaryDirectory() as temp_directory:
            file_handler= FileHandling(temp_directory)
            file_handler.prepare_directory()

            # it creates an empty income.csv file
            with open(file_handler.income_file, "w", encoding= "utf-8"):
                pass

            # An empty csv has no usable columns or records
            with self.assertRaises(ValueError):
                file_handler.load_income()

    def test_income_file_with_wrong_columns_raises_error(self):    # it tests that an income csv with incorrect columns is rejected
        with tempfile.TemporaryDirectory() as temp_directory:
            file_handler= FileHandling(temp_directory)
            file_handler.prepare_directory()

            # an example of a wrong column
            wrong_data= pd.DataFrame([{"wrong_id": "1", "money": "100.00"}])
            wrong_data.to_csv(file_handler.income_file, index= False)

            with self.assertRaises(ValueError):      # fileHandling asshould reject an incorrectly strucutred csv
                file_handler.load_income()

    
if __name__=="__main__":   # runs the test
    unittest.main()            
