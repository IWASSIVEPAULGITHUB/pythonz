Ecommerce = {}

def add_product(product_name, price, quantity):
    product = {
        "name": product_name,
        "price": price,
        "quantity": quantity
    }
    Ecommerce[product_name] = product
    return product

def update_price(product_name, new_price):
    if product_name in Ecommerce:
        Ecommerce[product_name]["price"] = new_price
        return Ecommerce[product_name]
    else:
        print("Product not found!")
        return None

def update_quantity(product_name, quantity_change):
    if product_name in Ecommerce:
        Ecommerce[product_name]["quantity"] += quantity_change
        return Ecommerce[product_name]
    else:
        print("Product not found!")
        return None

while True:
    print("\nOptions:")
    print("1. Add product")
    print("2. Update price")
    print("3. Update quantity")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        product = input("Enter product name: ").strip()
        price = float(input("Enter the price of the product: "))
        qty = int(input("Enter the quantity of the product: "))
        add_product(product, price, qty)
        print(f"{product} added successfully.")
    elif choice == "2":
        product = input("Enter product name: ").strip()
        price = float(input("Enter the new price: "))
        update_price(product, price)
        print("Price updated successfully.")
    elif choice == "3":
        product = input("Enter product name: ").strip()
        qty_change = int(input("Enter the quantity change (+ for add, - for remove): "))
        update_quantity(product, qty_change)
        print("Quantity updated successfully.")
    elif choice == "4":
        print("Exit successful!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
