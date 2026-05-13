"""
Restaurant Order Management System
====================================
A Python program to manage restaurant orders using:
- Dictionaries for menu items
- Lists for customer orders
- String operations for order customization
- Tuples to return bill summary (total, item count)
"""

# ─────────────────────────────────────────────
# Menu stored as a dictionary: {item_name: price}
# ─────────────────────────────────────────────
menu = {
    "Burger":       5.99,
    "Pizza":        8.49,
    "Pasta":        6.75,
    "Salad":        4.50,
    "Fries":        2.99,
    "Soda":         1.50,
    "Water":        0.99,
    "Ice Cream":    3.25,
}


def display_menu():
    """Display all available menu items with their prices."""
    print("\n" + "=" * 40)
    print("       🍽️  RESTAURANT MENU  🍽️")
    print("=" * 40)
    for index, (item, price) in enumerate(menu.items(), start=1):
        # String formatting: title-case item name, right-aligned price
        print(f"  {index}. {item.title():<15} ${price:.2f}")
    print("=" * 40)


def add_item_to_menu(item_name, price):
    """
    Add a new item to the menu dictionary.

    Args:
        item_name (str): Name of the menu item.
        price (float): Price of the item.
    """
    # String strip + title to clean user input before storing
    cleaned_name = item_name.strip().title()
    menu[cleaned_name] = price
    print(f"✅ '{cleaned_name}' added to menu at ${price:.2f}")


def update_menu_price(item_name, new_price):
    """
    Update the price of an existing menu item.

    Args:
        item_name (str): Name of the item to update.
        new_price (float): The new price.
    """
    cleaned_name = item_name.strip().title()
    if cleaned_name in menu:
        menu[cleaned_name] = new_price
        print(f"✅ Price of '{cleaned_name}' updated to ${new_price:.2f}")
    else:
        print(f"❌ '{cleaned_name}' not found in menu.")


def delete_menu_item(item_name):
    """
    Remove an item from the menu.

    Args:
        item_name (str): Name of the item to remove.
    """
    cleaned_name = item_name.strip().title()
    if cleaned_name in menu:
        del menu[cleaned_name]
        print(f"🗑️  '{cleaned_name}' removed from menu.")
    else:
        print(f"❌ '{cleaned_name}' not found in menu.")


# ─────────────────────────────────────────────
# Customer orders stored as a list of dicts
# ─────────────────────────────────────────────
customer_order = []   # Each element: {"item": str, "note": str, "price": float}


def place_order(item_name, customization=""):
    """
    Add an item to the customer's order list.

    Args:
        item_name (str): Name of the menu item.
        customization (str): Special instructions (optional).
    """
    cleaned_name = item_name.strip().title()
    if cleaned_name not in menu:
        print(f"❌ '{cleaned_name}' is not on the menu.")
        return

    # String operations: replace common shortcuts, strip whitespace, join words
    note = customization.strip().replace("no ", "without ").replace("  ", " ")

    order_entry = {
        "item":  cleaned_name,
        "note":  note if note else "No special requests",
        "price": menu[cleaned_name],
    }
    customer_order.append(order_entry)
    print(f"✅ Added: {cleaned_name}  |  Note: {order_entry['note']}")


def remove_last_item():
    """Remove the most recently added item from the order."""
    if customer_order:
        removed = customer_order.pop()
        print(f"🗑️  Removed '{removed['item']}' from order.")
    else:
        print("⚠️  Order is already empty.")


def view_order():
    """Display the current order list."""
    if not customer_order:
        print("\n⚠️  No items in the order yet.")
        return
    print("\n" + "-" * 40)
    print("        📋  YOUR CURRENT ORDER")
    print("-" * 40)
    for idx, entry in enumerate(customer_order, start=1):
        print(f"  {idx}. {entry['item']:<15} ${entry['price']:.2f}")
        if entry["note"] != "No special requests":
            print(f"       📝 {entry['note']}")
    print("-" * 40)


def get_recent_orders(n=3):
    """
    Return a slice of the most recent n orders.

    Args:
        n (int): Number of recent items to retrieve.

    Returns:
        list: Slice of the last n order entries.
    """
    return customer_order[-n:]


def calculate_bill():
    """
    Calculate the total bill and return a summary as a tuple.

    Returns:
        tuple: (total_price (float), item_count (int))
    """
    if not customer_order:
        return (0.0, 0)

    total = sum(entry["price"] for entry in customer_order)
    item_count = len(customer_order)

    # Return bill summary as a tuple (total, count)
    return (round(total, 2), item_count)


def print_bill():
    """Print a formatted bill and show the tuple summary."""
    view_order()
    bill_summary = calculate_bill()          # tuple: (total, count)
    total, count = bill_summary              # tuple unpacking

    print("\n" + "=" * 40)
    print("           🧾  BILL SUMMARY")
    print("=" * 40)
    print(f"  Items ordered : {count}")
    print(f"  Total amount  : ${total:.2f}")
    print(f"  Bill tuple    : {bill_summary}")
    print("=" * 40)
    print("  Thank you for dining with us! 😊")
    print("=" * 40 + "\n")


# ─────────────────────────────────────────────
# Interactive menu-driven interface
# ─────────────────────────────────────────────
def main():
    """Main function to run the Restaurant Order Management System."""
    print("\n🍴 Welcome to the Restaurant Order Management System 🍴")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. View Menu")
        print("2. Place Order")
        print("3. View Current Order")
        print("4. Remove Last Item")
        print("5. View Recent Orders (last 3)")
        print("6. Print Bill")
        print("7. Add Item to Menu  (Admin)")
        print("8. Update Menu Price (Admin)")
        print("9. Delete Menu Item  (Admin)")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            display_menu()

        elif choice == "2":
            display_menu()
            item = input("Enter item name: ").strip()
            note = input("Any customization? (press Enter to skip): ").strip()
            place_order(item, note)

        elif choice == "3":
            view_order()

        elif choice == "4":
            remove_last_item()

        elif choice == "5":
            recent = get_recent_orders(3)
            if recent:
                print("\n📋 Last 3 ordered items:")
                for r in recent:
                    print(f"  - {r['item']} (${r['price']:.2f})  |  {r['note']}")
            else:
                print("⚠️  No orders yet.")

        elif choice == "6":
            print_bill()

        elif choice == "7":
            name  = input("New item name: ").strip()
            price = float(input("Price: $"))
            add_item_to_menu(name, price)

        elif choice == "8":
            name  = input("Item name to update: ").strip()
            price = float(input("New price: $"))
            update_menu_price(name, price)

        elif choice == "9":
            name = input("Item name to delete: ").strip()
            delete_menu_item(name)

        elif choice == "0":
            print("\n👋 Thank you! Goodbye!\n")
            break

        else:
            print("⚠️  Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
