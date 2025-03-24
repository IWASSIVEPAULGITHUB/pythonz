# An invetory program when one can add,update,view items

inventory = {} # dictionary

# Function to add or update an item in the inventory
def add_item(item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity  
    else:
        inventory[item_name] = quantity  

# Function to retrieve item quantity
def get_item_quantity(item_name):
    return inventory.get(item_name, "Item not found in inventory")  

# Function to calculate total inventory quantity
def get_total_quantity():
    return sum(inventory.values())  


while True:
    print("\nOptions:")
    print("1. Add/Update Item")
    print("2. Retrieve Item Quantity")
    print("3. Display Total Inventory Quantity")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter item name: ").strip()
        qty = int(input("Enter quantity: "))
        add_item(item, qty)
        print(f"{qty} units of '{item}' added/updated.")

    elif choice == "2":
        item = input("Enter item name to check: ").strip()
        print(f"Quantity of '{item}': {get_item_quantity(item)}")

    elif choice == "3":
        print(f"Total quantity of all items: {get_total_quantity()}")

    elif choice == "4":
        print("Exit successful!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")


