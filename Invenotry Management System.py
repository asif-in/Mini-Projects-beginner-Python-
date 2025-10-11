inventory = {}

def add_item(item, price, stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item] = {
            "price": float(price),
            "stock": int(stock),
        }
        print(f"Item '{item}' added successfully ✅")


def update_stock(item, quantity):
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")
    else:
        new_stock = inventory[item]["stock"] + quantity
        if new_stock < 0:
            print(f"Error: Insufficient stock for '{item}'.")
        else:
            inventory[item]["stock"] = new_stock
            print(f"Stock for '{item}' updated successfully ✅")


def sales_report(sales):
    total_revenue = 0.0

    for item, quantity_sold in sales.items():
        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
            continue

        if inventory[item]["stock"] < quantity_sold:
            print(f"Error: Insufficient stock for '{item}'.")
            continue

        price = inventory[item]["price"]
        total_revenue += price * quantity_sold
        inventory[item]["stock"] -= quantity_sold

    return f"Total revenue: ${total_revenue:.2f}"


# 🔹 MAIN MENU LOOP
while True:
    print("\n--- INVENTORY MENU ---")
    print("1. Add Item")
    print("2. Update Stock")
    print("3. Make a Sale (Generate Report)")
    print("4. View Inventory")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        item = input("Enter item name: ").capitalize()
        price = float(input("Enter item price: "))
        stock = int(input("Enter item stock: "))
        add_item(item, price, stock)

    elif choice == "2":
        item = input("Enter item name: ").capitalize()
        quantity = int(input("Enter quantity to add/remove (use - for remove): "))
        update_stock(item, quantity)

    elif choice == "3":
        sales = {}
        print("Enter items sold (type 'done' to finish):")
        while True:
            item = input("Item name: ").capitalize()
            if item.lower() == "done":
                break
            quantity = int(input("Quantity sold: "))
            sales[item] = quantity
        print(sales_report(sales))

    elif choice == "4":
        print("\nCurrent Inventory:")
        for item, details in inventory.items():
            print(f"{item} - Price: ${details['price']} | Stock: {details['stock']}")

    elif choice == "5":
        print("Exiting program. Goodbye ")
        break

    else:
        print("Invalid choice. Try again!")
