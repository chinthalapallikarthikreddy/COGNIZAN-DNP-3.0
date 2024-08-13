# inventory_management.py

def check_inventory(inventory):
    for item, quantity in inventory:
        if quantity == 0:
            print(f"{item} is out of stock.")
        else:
            print(f"{item} has {quantity} in stock.")

inventory = []

n = int(input("Enter the number of items: "))

for _ in range(n):
    item = input("Enter the item name: ")
    quantity = int(input(f"Enter the quantity for {item}: "))
    inventory.append((item, quantity))

check_inventory(inventory)
