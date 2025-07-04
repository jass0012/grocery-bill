import json
from datetime import datetime

def indian_grocery_calculator():
    print("\nINDIAN GROCERY CALCULATOR")
    print("----------------------------------")
    print("Track your grocery spending in Rs\n")

    categories = {
        'Vegetables': {'budget': 0, 'spent': 0},
        'Fruits': {'budget': 0, 'spent': 0},
        'Dairy': {'budget': 0, 'spent': 0},
        'Spices': {'budget': 0, 'spent': 0},
        'Grains & Pulses': {'budget': 0, 'spent': 0},
        'Oil & Ghee': {'budget': 0, 'spent': 0},
        'Snacks & Biscuits': {'budget': 0, 'spent': 0},
        'Beverages': {'budget': 0, 'spent': 0},
        'Household': {'budget': 0, 'spent': 0},
        'Personal Care': {'budget': 0, 'spent': 0},
        'Other': {'budget': 0, 'spent': 0}
    }

    items = {}  
    print("\nSET BUDGETS in Rs")
    for category in categories:
        while True:
            try:
                budget = float(input(f"Enter budget for {category} Rs: "))
                categories[category]['budget'] = budget
                break
            except ValueError:
                print("Please enter a valid amount.")

    while True:
        print("\nMAIN MENU")
        print("1. Add new item")
        print("2. Edit/Remove item")
        print("3. View current items")
        print("4. Check budget status")
        print("5. Generate bill and exit")
        choice = input("Choose an option 1-5: ")

        if choice == '1':
            print("\nAdd New Item")
            item_name = input("Item name: ").strip()
            
            print("\nAvailable Categories:")
            for i, cat in enumerate(categories.keys(), 1):
                print(f"{i}. {cat}")
            
            while True:
                try:
                    cat_choice = int(input("Select category number: "))
                    if 1 <= cat_choice <= len(categories):
                        category = list(categories.keys())[cat_choice - 1]
                        break
                    else:
                        print("Invalid choice. Try again.")
                except ValueError:
                    print("Enter a valid number.")

            while True:
                try:
                    quantity = float(input("Quantity kg/pcs/ltr: "))
                    price = float(input("Price per unit Rs: "))
                    break
                except ValueError:
                    print("Invalid input. Enter numbers only.")

            subtotal = quantity * price
            items[item_name] = {
                'category': category,
                'quantity': quantity,
                'price': price,
                'subtotal': subtotal
            }

            categories[category]['spent'] += subtotal
            print(f"\nAdded {quantity} {item_name} Rs{price}/unit Rs{subtotal}")

        elif choice == '2':
            if not items:
                print("No items to edit.")
                continue
            
            print("\nEdit/Remove Item")
            print("Current Items:")
            for idx, (item, details) in enumerate(items.items(), 1):
                print(f"{idx}. {item} {details['category']} {details['quantity']} x Rs{details['price']} Rs{details['subtotal']}")

            while True:
                try:
                    item_choice = int(input("Select item number to edit 0 to cancel: "))
                    if item_choice == 0:
                        break
                    elif 1 <= item_choice <= len(items):
                        selected_item = list(items.keys())[item_choice - 1]
                        old_data = items[selected_item]

                        print(f"\nEditing {selected_item}")
                        new_name = input(f"New name {selected_item}: ").strip() or selected_item
                        new_qty = input(f"New quantity {old_data['quantity']}: ")
                        new_price = input(f"New price Rs {old_data['price']}: ")

                        if new_qty:
                            items[selected_item]['quantity'] = float(new_qty)
                        if new_price:
                            items[selected_item]['price'] = float(new_price)
                        
                        items[selected_item]['subtotal'] = items[selected_item]['quantity'] * items[selected_item]['price']

                        categories[old_data['category']]['spent'] -= old_data['subtotal']
                        categories[items[selected_item]['category']]['spent'] += items[selected_item]['subtotal']

                        print("Updated successfully")
                        break
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Enter a valid number.")

        elif choice == '3':
            if not items:
                print("No items added yet.")
                continue
            
            print("\nYOUR GROCERY LIST")
            total = 0
            for category in categories:
                cat_items = {k: v for k, v in items.items() if v['category'] == category}
                if cat_items:
                    print(f"\n{category.upper()}")
                    for item, details in cat_items.items():
                        print(f"  {item} {details['quantity']} x Rs{details['price']} Rs{details['subtotal']}")
                    print(f"  Subtotal Rs{categories[category]['spent']}")
                    if categories[category]['budget'] > 0:
                        remaining = categories[category]['budget'] - categories[category]['spent']
                        print(f"  Budget Rs{categories[category]['budget']} Remaining Rs{remaining}")
                    total += categories[category]['spent']
            
            print(f"\nGRAND TOTAL Rs{total}")

        elif choice == '4':
            print("\nBUDGET STATUS")
            total_spent = 0
            total_budget = 0
            
            for category, data in categories.items():
                if data['budget'] > 0:
                    remaining = data['budget'] - data['spent']
                    status = "Under" if remaining >= 0 else "Over"
                    print(f"{category} Rs{data['spent']} Rs{data['budget']} {status} by Rs{abs(remaining)}")
                    total_spent += data['spent']
                    total_budget += data['budget']
            
            if total_budget > 0:
                total_remaining = total_budget - total_spent
                overall_status = "Under" if total_remaining >= 0 else "Over"
                print(f"\nTOTAL Rs{total_spent} Rs{total_budget} {overall_status} by Rs{abs(total_remaining)}")
            else:
                print("No budgets set yet.")

        elif choice == '5':
            if not items:
                print("No items to generate bill.")
                continue
            
            timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            filename = f"grocery_bill_{timestamp}.txt"
            
            total = sum(item['subtotal'] for item in items.values())
            
            with open(filename, 'w') as f:
                f.write("INDIAN GROCERY BILL\n")
                f.write(f"Date {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
                
                for category in categories:
                    cat_items = {k: v for k, v in items.items() if v['category'] == category}
                    if cat_items:
                        f.write(f"{category.upper()}\n")
                        for item, details in cat_items.items():
                            f.write(f"  {item} {details['quantity']} x Rs{details['price']} Rs{details['subtotal']}\n")
                        f.write(f"  Subtotal Rs{categories[category]['spent']}\n")
                        if categories[category]['budget'] > 0:
                            remaining = categories[category]['budget'] - categories[category]['spent']
                            f.write(f"  Budget Rs{categories[category]['budget']} Remaining Rs{remaining}\n")
                        f.write("\n")
                
                f.write(f"GRAND TOTAL Rs{total}\n")
            
            print(f"\nBill saved as {filename}")
            print("Thank you for shopping")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    indian_grocery_calculator()
