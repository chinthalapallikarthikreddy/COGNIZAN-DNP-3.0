import threading
import time
import json

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
            else:
                raise ValueError("Not enough stock to remove")
        else:
            raise ValueError("Item not found in inventory")

    def check_stock(self, item_name):
        return self.items.get(item_name, 0)

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as f:
                json.dump(self.items, f)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                self.items = json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

    def restock_alert(self, threshold):
        while True:
            for item, quantity in self.items.items():
                if quantity < threshold:
                    print(f"Restock alert: {item} is low in stock!")
            time.sleep(5)

inventory = Inventory()

def inventory_operations():
    while True:
        action = input("Enter action (add, remove, check, save, load, quit): ").lower()
        if action == "add":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity to add: "))
            inventory.add_item(item_name, quantity)
        elif action == "remove":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            try:
                inventory.remove_item(item_name, quantity)
            except ValueError as e:
                print(e)
        elif action == "check":
            item_name = input("Enter item name: ")
            print(f"Stock for {item_name}: {inventory.check_stock(item_name)}")
        elif action == "save":
            filename = input("Enter filename to save: ")
            inventory.save_to_file(filename)
        elif action == "load":
            filename = input("Enter filename to load: ")
            inventory.load_from_file(filename)
        elif action == "quit":
            break
        else:
            print("Unknown action")

threshold = int(input("Enter restock threshold: "))
threading.Thread(target=inventory.restock_alert, args=(threshold,), daemon=True).start()
inventory_operations()
