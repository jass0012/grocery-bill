def indian_grocery_calculator():
    print("INDIAN GROCERY CALCULATOR")
    print("Enter items with quantities and prices in Rs. Type done when finished")

    items = {}
    total = 0.0

    common_units = {
        'rice': 'kg',
        'wheat': 'kg',
        'sugar': 'kg',
        'milk': 'litre',
        'oil': 'litre',
        'eggs': 'dozen',
        'tomato': 'kg',
        'onion': 'kg',
        'potato': 'kg'
    }

    while True:
        item_name = input("Enter item name or done to finish: ").strip().lower()
        if item_name == 'done':
            break

        unit = common_units.get(item_name, 'units')
        quantity_prompt = f"Enter quantity for {item_name} in {unit}: "
        price_prompt = f"Enter price per {unit} for {item_name}: Rs"

        try:
            quantity = float(input(quantity_prompt))
            price = float(input(price_prompt))
        except ValueError:
            print("Please enter valid numbers for quantity and price")
            continue

        subtotal = quantity * price
        items[item_name] = {
            'quantity': quantity,
            'unit': unit,
            'price': price,
            'subtotal': subtotal
        }
        total += subtotal

    print("\nBILL RECEIPT")
    print("Item            Qty    Price    Subtotal")
    for item, details in items.items():
        print(f"{item.title()}    {details['quantity']}{details['unit']}    Rs{details['price']:.2f}    Rs{details['subtotal']:.2f}")

    print(f"\nTOTAL: Rs{total:.2f}")
    print("Thank you for shopping with us")

if __name__ == "__main__":
    indian_grocery_calculator()