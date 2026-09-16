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
* `Product`: Represents an individual item in the shop. It stores attributes such as the product ID, name, price, and current stock quantity.
* `Inventory`: Manages the collection of `Product` objects. It contains methods for adding, removing, updating, and searching for items in the stock.
* `SalesTracker`: Handles the checkout process. It records individual transactions, calculates total sales amounts, and updates the `Inventory` accordingly.

## Files Used
* `inventory.csv` (or `.txt`): Used to permanently store the current stock data (item names, IDs, prices, and quantities). The program reads from this file on startup and writes to it whenever stock changes.
* `sales_log.csv` (or `.txt`): Keeps a running historical record of all completed sales, including timestamps, items sold, and revenue generated.

## How to Run the Application
1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/oinusah/ProgrammingOneSummativeAssignment.git](https://github.com/oinusah/ProgrammingOneSummativeAssignment.git)

   ## Team Contributions
* **Allan Ojuka:** Designed and implemented the main user interface (UI) and managed the inventory tracking logic.
* **Debora Peter Hello:** Developed the finance module, handling revenue tracking, expense calculations, and financial reporting.
* **Osman Inusah:** Built the sales processing system, including customer transactions, sales logging, and receipt generation.
* **Fatine Icyimpaye:** Created the core `Product` class and managed product attributes, categorization, and item definitions.
