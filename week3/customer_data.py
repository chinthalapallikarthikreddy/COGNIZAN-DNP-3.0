# customer_data.py

def update_purchase(customer_data, name, amount):
    if name in customer_data:
        customer_data[name] += amount
    else:
        customer_data[name] = amount

customer_data = {}
n = int(input("Enter the number of customers: "))

for _ in range(n):
    name = input("Enter the customer's name: ")
    amount = float(input(f"Enter the purchase amount for {name}: "))
    customer_data[name] = amount

name_to_update = input("Enter the name of the customer to update: ")
update_amount = float(input(f"Enter the amount to update for {name_to_update}: "))

update_purchase(customer_data, name_to_update, update_amount)

print("Updated customer data:")
for name, amount in customer_data.items():
    print(f"{name}: ${amount:.2f}")
