# Inventory & Sales Tracking System for a Small Shop

## Team Members
* Allan Ojuka
* Debora Peter Hello
* Osman Inusah
* Fatine Icyimpaye

## Project Description
The **Inventory & Sales Tracking System** is a Python-based application designed to help small shop owners easily manage their daily operations. The system allows users to keep track of available stock, process customer sales, and maintain accurate records of items sold. By automating these tasks, the application reduces manual errors, saves time, and provides clear insights into the shop's inventory levels and revenue. 

## Main Features
* **Stock Management:** Add new items, update product details, change stock levels, and search for products by keyword or category.

* **Low Stock Alerts:** Easily see items that are running low or completely out of stock.

* **Sales & Checkout:** Add items to a customer sale, check if enough stock is available, and calculate cart totals.

* **Payment & Change Processing:** Compute exact monetary amounts, handle customer cash payments, and calculate change.

* **Save & Load Data:** Automatically load and save data in CSV files so your records stay safe.

* **Colorful Terminal Interface:** Uses the `rich` library to show clear tables and simple menus in the terminal.

## Classes Used
* **Product (product.py):** Stores details for a single item (ID, name, price, quantity, category, brand, size, supplier, entry date, and expiry date) and checks that all inputs are valid.

* **Inventory (`inventory.py`):** Manages the full product list. It allows adding, searching, updating, filtering, and removing products.

* **Sales (`sales.py`):** Handles the customer shopping cart, verifies stock availability, calculates sales totals, and logs past transactions.

* **Finance (`finance.py`):** Calculates exact money amounts, processes payments, calculates customer change, and logs overall income.

* **FileHandling (`file_handling.py`):** Reads and writes CSV data files using pandas to keep data safe.

* **ShopApplication (`user_interface.py`):** Controls the colorful user interface and displays menus and tables on screen.

* **UserInformation (`user_information.py`):** Holds details about the shop, such as shop name, owner name, location, and phone number.
## Files Used
All shop data is stored inside CSV files in the data/ folder:

`data/products.csv`: Stores the list of all products and their current quantities.

`data/sales.csv`: Stores a log of all items sold in every sale transaction.

`data/income.csv`: Stores the total money made from each completed sale along with the date and time.
## How to Run the Application
1.Install Required Libraries:

Open your terminal and install `pandas` and `rich`:

``pip install pandas rich``


2. Clone the Repository:

``git clone https://github.com/oinusah/ProgrammingOneSummativeAssignment.git
cd ProgrammingOneSummativeAssignment``

3.**Start the Program:**
Run the main.py file:

  ``python main.py``
## Team Contributions
* **Allan Ojuka:** Inventory logic (`inventory.py`) and designed the user interface menu (`user_interface.py`).
  
* **Debora Peter Hello:** Built the Finance module (`finance.py`) for handling exact money math, customer payments, change, and income records.

* **Osman Inusah:** Built the Sales module (`sales.py`) to handle shopping carts, stock checks during sales, and transaction logs.

* **Fatine Icyimpaye:** Designed the Product class (`product.py`) to store product details and check for correct data inputs.
