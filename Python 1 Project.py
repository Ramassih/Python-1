'''You are tasked with creating a simple inventory management system for
a market. The system should allow users to add, update, view, and remove
items from the inventory. Each item in the inventory will have a name,
price, quantity, and category. '''

# Initialize empty inventory list
inventory = []

def add_item():
    try:
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        category = input("Enter item category: ")

        # Check if item already exists
        for item in inventory:
            if item['name'].lower() == name.lower():
                print("Item already exists in inventory!")
                return

        # Add new item
        inventory.append({
            'name': name,
            'price': price,
            'quantity': quantity,
            'category': category
        })
        print(f"Item '{name}' added successfully!")

    except ValueError:
        print("Invalid input! Please enter valid price (number) and quantity (integer).")

def update_item():
    """Update an existing item in the inventory"""
    name = input("Enter name of item to update: ")

    for item in inventory:
        if item['name'].lower() == name.lower():
            try:
                print(f"Current details: {item}")
                item['price'] = float(input("Enter new price (leave blank to keep current): ") or item['price'])
                item['quantity'] = int(input("Enter new quantity (leave blank to keep current): ") or item['quantity'])
                item['category'] = input("Enter new category (leave blank to keep current): ") or item['category']
                print(f"Item '{name}' updated successfully!")
                return
            except ValueError:
                print("Invalid input! Price must be a number and quantity must be an integer.")
                return

    print(f"Item '{name}' not found in inventory!")

def view_inventory():
    """Display all items in the inventory"""
    if not inventory:
        print("Inventory is empty!")
        return

    print("\nCurrent Inventory:")
    print("-" * 50)
    print(f"{'Name':<20} {'Price':<10} {'Quantity':<10} {'Category':<15}")
    print("-" * 50)

    for item in inventory:
        print(f"{item['name']:<20} ${item['price']:<10.2f} {item['quantity']:<10} {item['category']:<15}")

def remove_item():
    """Remove an item from the inventory"""
    name = input("Enter name of item to remove: ")

    for i, item in enumerate(inventory):
        if item['name'].lower() == name.lower():
            del inventory[i]
            print(f"Item '{name}' removed successfully!")
            return

    print(f"Item '{name}' not found in inventory!")

def search_by_category():
    """Search for items by category"""
    category = input("Enter category to search: ")
    found_items = [item for item in inventory if item['category'].lower() == category.lower()]

    if not found_items:
        print(f"No items found in category '{category}'")
        return

    print(f"\nItems in category '{category}':")
    print("-" * 50)
    print(f"{'Name':<20} {'Price':<10} {'Quantity':<10} {'Category':<15}")
    print("-" * 50)

    for item in found_items:
        print(f"{item['name']:<20} ${item['price']:<10.2f} {item['quantity']:<10} {item['category']:<15}")

def main():
    """Main program loop"""
    while True:
        print("\nMarket Inventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            search_by_category()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()