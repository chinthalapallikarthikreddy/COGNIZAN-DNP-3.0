# inventory_management.py

# Lists
product_names = []

def add_product(name):
    product_names.append(name)

def remove_product(name):
    if name in product_names:
        product_names.remove(name)

def update_product(old_name, new_name):
    if old_name in product_names:
        index = product_names.index(old_name)
        product_names[index] = new_name

# Dictionaries
product_details = {}

def add_product_detail(name, quantity, price):
    product_details[name] = (quantity, price)

def update_product_detail(name, quantity, price):
    if name in product_details:
        product_details[name] = (quantity, price)

def delete_product_detail(name):
    if name in product_details:
        del product_details[name]

# Tuples
def display_immutable_product(name):
    if name in product_details:
        product = product_details[name]
        immutable_product = (name, product[0], product[1])
        print(f"Product Tuple: {immutable_product}")

# Sets
product_categories = set()

def add_category(category):
    product_categories.add(category)

def remove_category(category):
    product_categories.discard(category)

# Combining Collections
def generate_sorted_report():
    sorted_products = sorted(product_details.items(), key=lambda item: item[1][1])
    for product in sorted_products:
        print(f"{product[0]}: Quantity={product[1][0]}, Price={product[1][1]}")

def find_products_in_price_range(min_price, max_price):
    matching_products = {name for name, (quantity, price) in product_details.items() if min_price <= price <= max_price}
    print(f"Products in price range ${min_price} - ${max_price}: {matching_products}")

def main():
    while True:
        print("\n1. Add Product")
        print("2. Remove Product")
        print("3. Update Product")
        print("4. Add Product Detail")
        print("5. Update Product Detail")
        print("6. Delete Product Detail")
        print("7. Display Immutable Product")
        print("8. Add Category")
        print("9. Remove Category")
        print("10. Generate Sorted Report")
        print("11. Find Products in Price Range")
        print("12. Quit")
        
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            name = input("Enter product name to add: ")
            add_product(name)
        elif choice == "2":
            name = input("Enter product name to remove: ")
            remove_product(name)
        elif choice == "3":
            old_name = input("Enter current product name: ")
            new_name = input("Enter new product name: ")
            update_product(old_name, new_name)
        elif choice == "4":
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            add_product_detail(name, quantity, price)
        elif choice == "5":
            name = input("Enter product name: ")
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            update_product_detail(name, quantity, price)
        elif choice == "6":
            name = input("Enter product name to delete: ")
            delete_product_detail(name)
        elif choice == "7":
            name = input("Enter product name to display as tuple: ")
            display_immutable_product(name)
        elif choice == "8":
            category = input("Enter category to add: ")
            add_category(category)
        elif choice == "9":
            category = input("Enter category to remove: ")
            remove_category(category)
        elif choice == "10":
            generate_sorted_report()
        elif choice == "11":
            min_price = float(input("Enter minimum price: "))
            max_price = float(input("Enter maximum price: "))
            find_products_in_price_range(min_price, max_price)
        elif choice == "12":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
