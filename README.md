Indian Grocery Calculator - README
Overview
The Indian Grocery Calculator is a Python-based tool designed to help users track their grocery spending in Indian Rupees (₹). It allows you to set budgets for different grocery categories, add items with quantities and prices, monitor spending against budgets, and generate detailed bills.

Features
Category-based Budgeting: Set budgets for 11 common Indian grocery categories

Vegetables, Fruits, Dairy, Spices, Grains & Pulses, Oil & Ghee

Snacks & Biscuits, Beverages, Household, Personal Care, Other

Item Management:

Add items with name, quantity, and price

Edit existing items (name, quantity, price)

View all items organized by category

Budget Tracking:

Real-time spending vs budget comparison

Category-wise and overall budget status

Visual indicators for over/under budget

Bill Generation:

Automatic generation of detailed grocery bills

Timestamped filenames for easy organization

Includes item details, subtotals, and grand total

How to Use
Set Budgets:

When you start the program, you'll be prompted to set budgets for each category

Enter amounts in Indian Rupees (₹)

Main Menu Options:

Add New Item: Enter item details and assign to a category

Edit/Remove Item: Modify existing items or their quantities

View Current Items: See all items organized by category with subtotals

Check Budget Status: Monitor spending against your budgets

Generate Bill: Create and save a detailed bill before exiting

Bill Generation:

Bills are automatically saved as text files with timestamps

Files are named like grocery_bill_DD-MM-YYYY_HH-MM-SS.txt
Requirements
Python 3.x

No additional libraries required (uses built-in modules only)

How to Run
Save the script as indian_grocery_calculator.py

Run from command line:

text
python indian_grocery_calculator.py
Sample Output Files
The program generates bills in this format:

text
INDIAN GROCERY BILL
Date: 04/07/2023 14:30:45

VEGETABLES
  Tomatoes 2.0 x ₹30 ₹60
  Onions 1.0 x ₹40 ₹40
  Subtotal: ₹100
  Budget: ₹500 Remaining: ₹400

DAIRY
  Milk 2.0 x ₹25 ₹50
  Subtotal: ₹50
  Budget: ₹200 Remaining: ₹150

GRAND TOTAL: ₹150
Notes
All monetary values are in Indian Rupees (₹)

Quantities can be entered in kg/pcs/ltr as appropriate

The program handles decimal values for precise calculations

Data is not saved between sessions (for persistent storage, consider adding database functionality)

Future Enhancements
Add monthly tracking and reporting

Implement data persistence (JSON/CSV/database)

Add graphical budget visualization

Include tax calculations

Support for multiple family members' shopping
