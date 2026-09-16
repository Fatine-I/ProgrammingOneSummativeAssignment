# Inventory & Sales Tracking System for a Small Shop

## Team Members
* Allan Ojuka
* Debora Peter Hello
* Osman Inusah
* Fatine Icyimpaye

## Project Description
The **Inventory & Sales Tracking System** is a Python-based application designed to help small shop owners easily manage their daily operations. The system allows users to keep track of available stock, process customer sales, and maintain accurate records of items sold. By automating these tasks, the application reduces manual errors, saves time, and provides clear insights into the shop's inventory levels and revenue. 

## Main Features
* **Inventory Management:** Add new products, update existing stock quantities, and remove discontinued items.
* **Sales Processing:** Record items sold, automatically calculate total costs, and deduct sold quantities from the active inventory.
* **Stock Tracking:** View a complete list of current inventory and receive alerts for items that are running low.
* **Data Persistence:** Automatically save and load all inventory and sales data so information is not lost when the application is closed.

## Classes Used
* **Product (product.py):** Stores details for a single item (ID, name, price, quantity, category, brand, size, supplier, entry date, and expiry date) and checks that all inputs are valid.

* **Inventory (inventory.py):** Manages the full product list. It allows adding, searching, updating, filtering, and removing products.

* **Sales (sales.py):** Handles the customer shopping cart, verifies stock availability, calculates sales totals, and logs past transactions.

* **Finance (finance.py):** Calculates exact money amounts, processes payments, calculates customer change, and logs overall income.

* **FileHandling (file_handling.py):** Reads and writes CSV data files using pandas to keep data safe.

* **ShopApplication (user_interface.py):** Controls the colorful user interface and displays menus and tables on screen.

* **UserInformation (user_information.py):** Holds details about the shop, such as shop name, owner name, location, and phone number.
## Files Used
All shop data is stored inside CSV files in the data/ folder:

`data/products.csv`: Stores the list of all products and their current quantities.

`data/sales.csv`: Stores a log of all items sold in every sale transaction.

`data/income.csv`: Stores the total money made from each completed sale along with the date and time.
## How to Run the Application
1.Install Required Libraries:

Open your terminal and install pandas and rich:

``pip install pandas rich``


2. Clone the Repository:

git clone https://github.com/oinusah/ProgrammingOneSummativeAssignment.git
cd ProgrammingOneSummativeAssignment

3.**Start the Program:**
Run the main.py file:

  ``python main.py``
## Team Contributions
* **Allan Ojuka:** Inventory logic (inventory.py) and designed the user interface menu (user_interface.py).
* **Debora Peter Hello:** Developed the finance module, handling revenue tracking, expense calculations, and financial reporting.
* **Osman Inusah:** Built the sales processing system, including customer transactions, sales logging, and receipt generation.
* **Fatine Icyimpaye:** Created the core `Product` class and managed product attributes, categorization, and item definitions.
