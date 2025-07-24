Restaurant Order Management System
--------------------------------------

Description:
This Python project allows users to:
•	View a restaurant-style food menu
•	Take orders with item names and quantities
•	Calculate the total bill with 5% GST
•	Automatically assign each order a unique number
•	Save the order details into a text file (`orders.txt`)

Files in this Project:
•	maincode.py            : Runs the main program loop
•	menu.py                   :Stores the menu items and prices
•	show_menu.py       : Displays the available menu to the user
•	take_order.py          : Handles order input and quantities
•	generate_bill.py     : Calculates subtotal, GST, and grand total
•	save_order.py          : Saves the order with order number and timestamp
•	orders.txt                  : Stores all previous orders
•	README.txt             :Explains how the project works

How to Run:
1. Open PyCharm and run ‘maincode.py’
2. Choose from the menu options:
   1 -> View Menu
   2 -> Take Order
   3 -> Exit the system

Sample Output (orders.txt):
Order #1 - new_order
pizza x 2 = Rs 500
coke x 1 = Rs 40
Grand Total = Rs 567.0
Order placed on 2025-07-23 22:48:12
------------------------------

Project highlights

This is one of my first full Python projects where I used:
•	Functions
•	Dictionaries
•	File handling
•	Modular coding with multiple `.py` files

 I also learned how to:
•	Write clean and structured code
•	Save data persistently using text files
•	Handle user input and format output properly
•	Count and generate unique order numbers using file content

-	I created this project as part of my learning journey for Python.
-	The project is designed to run in the terminal/console, and can be further improved with GUI or database integration in the future.

Tools & Concepts Used:
- Python 3
- File I/O (read/write)
- Dictionaries & loops
- Exception handling
- datetime module
- PyCharm IDE

Future Improvements:
- Add a feature to update/delete menu items
- Export orders as CSV or JSON
- Add login system (admin/staff)
- Build GUI using Tkinter


Built with love and learning by:
Shreya Nagpal
